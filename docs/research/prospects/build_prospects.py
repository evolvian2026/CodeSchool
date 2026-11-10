"""Build the private launch-school list from hand-downloaded CBSE SARAS files.

Reads every saras-*.private.(xlsx|csv|xls|html) file in this folder, matches columns by
their headings, merges duplicates by affiliation number, classifies management type,
flags launch areas, and writes launch-schools.private.csv and a summary. Principal
names are deliberately not copied. Needs only openpyxl (for .xlsx).
"""
import csv, datetime as dt, html.parser, pathlib, re, sys
from collections import Counter

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "launch-schools.private.csv"
SUMMARY = HERE / "launch-schools-summary.private.txt"
TODAY = dt.date.today().isoformat()

# Heading keywords -> output field. First match wins; matching ignores case and punctuation.
COLUMNS = [
    ("affiliation_no", ["affiliation no", "aff no", "affiliationno", "affno", "affiliation number", "aff code"]),
    ("status", ["school status", "status of school", "category", "school type", "type of school", "management", "status"]),
    ("school_name", ["school name", "name of school", "name of the school", "schoolname", "school"]),
    ("address", ["address", "postal address", "school address"]),
    ("district", ["district"]),
    ("state", ["state", "state ut", "state/ut"]),
    ("pin", ["pin", "pincode", "pin code"]),
    ("level", ["affiliation type", "level", "class", "affiliated upto", "affiliation upto"]),
    ("website", ["website", "web site", "url"]),
    ("email", ["email", "e mail", "e-mail", "email id"]),
    ("phone", ["phone", "telephone", "contact no", "mobile", "phone no", "contact"]),
]
SKIP = ["principal", "head", "trust", "society", "qualification", "fax"]  # never copied

# Launch areas: (label, state keyword, district keywords). Matching is case-insensitive.
LAUNCH = [
    ("Delhi NCR", "delhi", []),
    ("Delhi NCR", "haryana", ["gurugram", "gurgaon", "faridabad"]),
    ("Delhi NCR", "uttar pradesh", ["gautam buddha nagar", "gautam budh nagar", "noida", "ghaziabad"]),
    ("Chandigarh tricity", "chandigarh", []),
    ("Chandigarh tricity", "punjab", ["mohali", "s.a.s nagar", "sas nagar", "sahibzada ajit singh nagar"]),
    ("Chandigarh tricity", "haryana", ["panchkula"]),
    ("Lucknow", "uttar pradesh", ["lucknow"]),
    ("Jaipur", "rajasthan", ["jaipur"]),
]

MGMT = [  # (management type, is_private, patterns on status text or school name)
    ("Kendriya Vidyalaya", False, [r"\bkvs\b", r"kendriya vidyalaya"]),
    ("Navodaya Vidyalaya", False, [r"\bjnv\b", r"navodaya"]),
    ("Sainik / military", False, [r"sainik school", r"military school"]),
    ("Army / defence society", False, [r"army public school", r"\bawes\b", r"air force school", r"navy children", r"naval public"]),
    ("Central Tibetan", False, [r"\bctsa\b", r"tibetan"]),
    ("Atomic Energy", False, [r"atomic energy"]),
    ("Eklavya (EMRS)", False, [r"eklavya", r"\bemrs\b"]),
    ("Government", False, [r"\bgovt\b", r"government", r"\bgsss\b", r"\bgmss\b", r"rajkiya", r"pm shri", r"sarvodaya", r"\bsoe\b", r"school of excellence"]),
    ("Government-aided", False, [r"\baided\b"]),
    ("Private (independent)", True, [r"independent", r"private", r"unaided"]),
]


def norm(s):
    return re.sub(r"[^a-z0-9/ ]+", " ", str(s or "").lower()).strip()


class _TableParser(html.parser.HTMLParser):
    """Reads <table> rows from HTML saved as .xls/.html (common for 'Excel' exports)."""
    def __init__(self):
        super().__init__(); self.rows, self.row, self.cell, self.in_cell = [], None, [], False
    def handle_starttag(self, tag, attrs):
        if tag == "tr": self.row = []
        elif tag in ("td", "th"): self.in_cell, self.cell = True, []
    def handle_endtag(self, tag):
        if tag in ("td", "th") and self.row is not None:
            self.row.append(" ".join("".join(self.cell).split())); self.in_cell = False
        elif tag == "tr" and self.row is not None:
            if any(c for c in self.row): self.rows.append(self.row)
            self.row = None
    def handle_data(self, data):
        if self.in_cell: self.cell.append(data)


def read_rows(path):
    suf = path.suffix.lower()
    if suf == ".xlsx":
        import openpyxl
        wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
        rows = []
        for ws in wb.worksheets:
            rows += [["" if v is None else str(v).strip() for v in r] for r in ws.iter_rows(values_only=True)]
        return rows
    raw = path.read_bytes()
    text = raw.decode("utf-8-sig", errors="replace")
    if "<table" in text.lower():
        p = _TableParser(); p.feed(text); return p.rows
    if suf == ".xls":
        sys.exit(f"{path.name}: a binary .xls file. Open it in Excel and 'Save as' .xlsx, then re-run.")
    dialect = csv.Sniffer().sniff(text[:4096], delimiters=",;\t") if text.strip() else csv.excel
    return [r for r in csv.reader(text.splitlines(), dialect)]


def map_header(rows):
    """Find the header row (the first row matching at least 3 known headings) and map columns."""
    for i, row in enumerate(rows[:30]):
        m = {}
        for j, cell in enumerate(row):
            h = norm(cell)
            if not h or any(k in h for k in SKIP) and "school" not in h:
                continue
            for field, keys in COLUMNS:
                if field not in m and any(h == k or h.startswith(k) or k in h for k in keys):
                    m[field] = j; break
        if len(m) >= 3 and "school_name" in m:
            return i, m
    return None, None


def classify(status, name):
    text = f"{norm(status)} | {norm(name)}"
    for label, private, pats in MGMT:
        if any(re.search(p, text) for p in pats):
            return label, private
    return "Unclassified", None


def launch_area(state, district, address):
    s, d, a = norm(state), norm(district), norm(address)
    for label, st, dists in LAUNCH:
        if st in s and (not dists or any(k in d or k in a for k in dists)):
            return label
    return ""


def main():
    files = sorted(p for p in HERE.glob("saras-*.private.*") if p.suffix.lower() in (".xlsx", ".csv", ".xls", ".html", ".htm"))
    if not files:
        sys.exit("No saras-*.private.* files found in " + str(HERE))
    schools, problems = {}, []
    for f in files:
        rows = read_rows(f)
        hi, m = map_header(rows)
        if m is None:
            problems.append(f"{f.name}: no header row with 'school name' and two other known columns"); continue
        n = 0
        for r in rows[hi + 1:]:
            get = lambda k: (r[m[k]].strip() if k in m and m[k] < len(r) else "")
            name = get("school_name")
            if not name or norm(name) in ("school name", "name of school"):
                continue
            aff = re.sub(r"\D", "", get("affiliation_no")) or f"noaff:{norm(name)}|{norm(get('district'))}"
            rec = {k: get(k) for k, _ in COLUMNS}
            for k in ("state", "district"):  # 'JAIPUR' and 'Jaipur' are the same place
                if rec[k].isupper() or rec[k].islower(): rec[k] = rec[k].title()
            rec["affiliation_no"] = aff if not aff.startswith("noaff:") else ""
            prev = schools.get(aff)
            if prev:  # merge: keep the first non-empty value of each field
                for k, v in rec.items():
                    if not prev.get(k) and v: prev[k] = v
                prev["source_file"] += f"; {f.name}"
                if (prev["email"] or prev["phone"]) and not prev["contact_source"]: prev["contact_source"] = "SARAS download"
                continue
            mg, private = classify(rec["status"], name)
            rec.update(management=mg, private={True: "yes", False: "no", None: "check"}[private],
                       launch_area=launch_area(rec["state"], rec["district"], rec["address"]),
                       contact_source="SARAS download" if (rec["email"] or rec["phone"]) else "",
                       source_file=f.name, captured=TODAY)
            schools[aff] = rec; n += 1
        print(f"{f.name}: {n} schools")
    fields = ["affiliation_no", "school_name", "address", "district", "state", "pin", "status", "level", "management",
              "private", "launch_area", "website", "email", "phone", "contact_source", "source_file", "captured"]
    data = sorted(schools.values(), key=lambda r: (r["launch_area"] == "", r["state"], r["district"], r["school_name"]))
    with OUT.open("w", newline="", encoding="utf-8-sig") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore"); w.writeheader(); w.writerows(data)

    def block(title, counter):
        return [title] + [f"  {k or '(blank)'}: {v}" for k, v in counter.most_common()] + [""]
    lines = [f"Launch-school list built {TODAY} from {len(files)} file(s); {len(data)} unique schools.", ""]
    lines += block("By management type:", Counter(r["management"] for r in data))
    lines += block("Private (yes / no / check):", Counter(r["private"] for r in data))
    lines += block("Launch area (private schools only):", Counter(r["launch_area"] for r in data if r["private"] == "yes"))
    lines += block("By state:", Counter(r["state"] for r in data))
    lines += block("Top districts (private schools):", Counter(f"{r['district']}, {r['state']}" for r in data if r["private"] == "yes"))
    lines += [f"With a website: {sum(1 for r in data if r['website'])}",
              f"With an email or phone from SARAS: {sum(1 for r in data if r['email'] or r['phone'])}"]
    if problems:
        lines += ["", "Problems:"] + [f"  {p}" for p in problems]
    SUMMARY.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines[:1] + [f"Wrote {OUT.name} and {SUMMARY.name}"] + (["Problems: " + "; ".join(problems)] if problems else [])))


if __name__ == "__main__":
    main()
