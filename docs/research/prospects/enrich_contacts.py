"""Add each school's OFFICIAL email and phone, as published on the school's own website.

Reads launch-schools.private.csv, and for schools in the chosen launch areas visits the school's
website: the home page, then up to three linked pages whose link text or address mentions the
CBSE mandatory public disclosure or contact details (one linked PDF disclosure is read too).
It respects robots.txt, waits between requests to the same site, and stores where each contact
was found and when. Results are cached in contacts-cache.private.csv so the run can be resumed.

Usage:
  python -P -E enrich_contacts.py                 # all four launch areas
  python -P -E enrich_contacts.py --limit 20      # quick test
  python -P -E enrich_contacts.py --area Lucknow  # one area
Output: launch-schools-contacts.private.csv (the list plus email, phone, contact_url, contact_checked).
"""
import argparse, csv, datetime as dt, html, io, re, socket, ssl, threading, time, urllib.parse, urllib.request, urllib.robotparser
from concurrent.futures import ThreadPoolExecutor, as_completed
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
LIST = HERE / "launch-schools.private.csv"
CACHE = HERE / "contacts-cache.private.csv"
OUT = HERE / "launch-schools-contacts.private.csv"
UA = "Mozilla/5.0 (compatible; school-directory-check/1.0)"
TODAY = dt.date.today().isoformat()
TIMEOUT = 15
socket.setdefaulttimeout(TIMEOUT)
CTX = ssl.create_default_context()
LAX = ssl.create_default_context(); LAX.check_hostname = False; LAX.verify_mode = ssl.CERT_NONE  # many school sites have broken certificates

EMAIL = re.compile(r"[A-Za-z0-9._%+-]{2,64}@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,10}")
PHONE = re.compile(r"(?:\+?91[\s-]?|0)?(?:\d{2,4}[\s-]?\d{6,8}|[6-9]\d{4}[\s-]?\d{5})")
LINK_HINT = re.compile(r"disclosure|mandatory|appendix|contact|reach[- ]?us|cbse", re.I)
BAD_EMAIL = re.compile(r"(example|domain|yourmail|email\.com|sentry|wixpress|godaddy|\.png|\.jpg|\.gif|\.webp|\.svg|@2x)", re.I)
FIELDS = ["affiliation_no", "email", "phone", "contact_url", "contact_checked", "note"]


def fetch(url, want_pdf=False):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,application/pdf;q=0.9,*/*;q=0.5"})
    for ctx in (CTX, LAX):
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx) as r:
                ctype = r.headers.get("Content-Type", "")
                data = r.read(5_000_000 if want_pdf else 2_000_000)
                return r.geturl(), ctype, data
        except ssl.SSLError:
            continue
        except Exception:
            return None, "", b""
    return None, "", b""


_robots, _rlock = {}, threading.Lock()
def allowed(url):
    p = urllib.parse.urlparse(url); base = f"{p.scheme}://{p.netloc}"
    with _rlock:
        rp = _robots.get(base)
    if rp is None:
        rp = urllib.robotparser.RobotFileParser()
        _, _, data = fetch(base + "/robots.txt")
        try:
            rp.parse(data.decode("utf-8", "replace").splitlines())
        except Exception:
            rp.parse([])
        with _rlock:
            _robots[base] = rp
    return rp.can_fetch(UA, url)


def text_of(ctype, data):
    if "pdf" in ctype.lower() or data[:5] == b"%PDF-":
        try:
            import pypdf
            rd = pypdf.PdfReader(io.BytesIO(data))
            return " ".join((pg.extract_text() or "") for pg in rd.pages[:4])
        except Exception:
            return ""
    t = data.decode("utf-8", "replace")
    t = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", t)
    t = t.replace("&#64;", "@").replace("[at]", "@").replace("(at)", "@").replace(" at ", " at ")
    return html.unescape(re.sub(r"<[^>]+>", " ", t))


def mailtos(raw):
    return [urllib.parse.unquote(m) for m in re.findall(r"mailto:([^\"'?>\s]+)", raw, re.I)]


def tellinks(raw):
    return re.findall(r"tel:([+\d][\d\s-]{6,})", raw, re.I)


def clean_emails(found, site_host):
    out = []
    for e in found:
        e = e.strip(".,;:").lower()
        if BAD_EMAIL.search(e) or len(e) > 80 or e in out:
            continue
        out.append(e)
    # Prefer addresses on the school's own domain, then others the school publishes.
    host = site_host.lower().removeprefix("www.")
    out.sort(key=lambda e: (0 if host and e.split("@")[1].endswith(host.split(".", 1)[-1]) else 1))
    return out[:3]


def clean_phones(found):
    out = []
    for p in found:
        d = re.sub(r"\D", "", p)
        if d.startswith("91") and len(d) == 12: d = d[2:]
        if d.startswith("0"): d = d[1:]
        if len(d) != 10 or len(set(d)) < 4:
            continue
        if d not in out: out.append(d)
    return out[:3]


def norm_site(w):
    w = (w or "").strip().strip("/")
    if not w or w.lower() in ("na", "n/a", "nil", "-", "none"):
        return None
    if not re.match(r"https?://", w, re.I):
        w = "http://" + w
    p = urllib.parse.urlparse(w)
    return w if "." in p.netloc else None


def check(row):
    site = norm_site(row["website"])
    res = {"affiliation_no": row["affiliation_no"], "email": "", "phone": "", "contact_url": "", "contact_checked": TODAY, "note": ""}
    if not site:
        res["note"] = "no website"; return res
    if not allowed(site):
        res["note"] = "robots.txt disallows"; return res
    final, ctype, data = fetch(site)
    if not final:
        res["note"] = "site unreachable"; return res
    raw = data.decode("utf-8", "replace")
    host = urllib.parse.urlparse(final).netloc
    pages = [(final, raw, text_of(ctype, data))]
    links = []
    for href, label in re.findall(r"<a[^>]+href=[\"']([^\"'#]+)[\"'][^>]*>(.*?)</a>", raw, re.I | re.S):
        lab = re.sub(r"<[^>]+>", " ", label)
        if LINK_HINT.search(href) or LINK_HINT.search(lab):
            u = urllib.parse.urljoin(final, href)
            if urllib.parse.urlparse(u).netloc.endswith(host.removeprefix("www.")) or u.lower().endswith(".pdf"):
                if u not in links and u != final: links.append(u)
    links.sort(key=lambda u: (0 if re.search(r"disclosure|mandatory|appendix", u, re.I) else 1, u.lower().endswith(".pdf")))
    pdf_done = False
    for u in links[:4]:
        is_pdf = u.lower().endswith(".pdf")
        if is_pdf and pdf_done:
            continue
        if not allowed(u):
            continue
        time.sleep(1.0)  # be gentle with small school servers
        f2, c2, d2 = fetch(u, want_pdf=is_pdf)
        if f2:
            pages.append((f2, d2.decode("utf-8", "replace") if not is_pdf else "", text_of(c2, d2)))
            pdf_done = pdf_done or is_pdf
    # Prefer the disclosure page's contacts, then contact page, then home page.
    pages.sort(key=lambda p: (0 if re.search(r"disclosure|mandatory|appendix", p[0], re.I) else 1 if re.search(r"contact", p[0], re.I) else 2))
    for url, rawp, txt in pages:
        emails = clean_emails(mailtos(rawp) + EMAIL.findall(txt), host)
        phones = clean_phones(tellinks(rawp) + PHONE.findall(txt))
        if emails and not res["email"]:
            res["email"] = "; ".join(emails); res["contact_url"] = url
        if phones and not res["phone"]:
            res["phone"] = "; ".join(phones); res["contact_url"] = res["contact_url"] or url
        if res["email"] and res["phone"]:
            break
    if not (res["email"] or res["phone"]):
        res["note"] = "no contact found on home, contact or disclosure pages"
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--area", default="")
    ap.add_argument("--workers", type=int, default=8)
    a = ap.parse_args()
    rows = list(csv.DictReader(LIST.open(encoding="utf-8-sig")))
    target = [r for r in rows if r["launch_area"] and r["private"] in ("yes", "likely") and (not a.area or r["launch_area"] == a.area)]
    cache = {}
    if CACHE.exists():
        cache = {r["affiliation_no"]: r for r in csv.DictReader(CACHE.open(encoding="utf-8-sig"))}
    todo = [r for r in target if r["affiliation_no"] not in cache]
    if a.limit: todo = todo[:a.limit]
    print(f"{len(target)} launch-area private schools; {len(cache)} cached; checking {len(todo)} now", flush=True)
    new = not CACHE.exists()
    with CACHE.open("a", newline="", encoding="utf-8-sig") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS)
        if new: w.writeheader()
        done = 0
        with ThreadPoolExecutor(max_workers=a.workers) as ex:
            futs = {ex.submit(check, r): r for r in todo}
            for f in as_completed(futs):
                try:
                    res = f.result()
                except Exception as e:
                    res = {"affiliation_no": futs[f]["affiliation_no"], "contact_checked": TODAY, "note": f"error {type(e).__name__}"}
                w.writerow(res); fh.flush(); cache[res["affiliation_no"]] = res; done += 1
                if done % 100 == 0:
                    print(f"  {done}/{len(todo)} checked", flush=True)
    # Merge into the list for the launch areas.
    out_fields = list(rows[0].keys())
    for k in ("email", "phone"):
        if k not in out_fields: out_fields.append(k)
    out_fields += ["contact_url", "contact_checked", "contact_note"]
    merged = []
    for r in target:
        c = cache.get(r["affiliation_no"], {})
        r = dict(r)
        r["email"] = r.get("email") or c.get("email", "")
        r["phone"] = r.get("phone") or c.get("phone", "")
        r["contact_url"] = c.get("contact_url", "")
        r["contact_checked"] = c.get("contact_checked", "")
        r["contact_note"] = c.get("note", "")
        r["contact_source"] = "school website" if (c.get("email") or c.get("phone")) else r.get("contact_source", "")
        merged.append(r)
    with OUT.open("w", newline="", encoding="utf-8-sig") as fh:
        w = csv.DictWriter(fh, fieldnames=out_fields, extrasaction="ignore"); w.writeheader(); w.writerows(merged)
    em = sum(1 for r in merged if r["email"]); ph = sum(1 for r in merged if r["phone"])
    print(f"Wrote {OUT.name}: {len(merged)} schools; with email {em}; with phone {ph}; checked {sum(1 for r in merged if r['contact_checked'])}")


if __name__ == "__main__":
    main()
