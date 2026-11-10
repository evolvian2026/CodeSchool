"""Build the 24-page school specimen booklet for the Classes 3-5 programme, from the Class 3 book.

Usage: python -P -E docs/books/class3/build_specimen.py [out.pdf]
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import build_book as B
import figures as F
from content import CH
from reportlab.lib import colors
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Spacer, Table, TableStyle, PageBreak, NextPageTemplate, KeepTogether)
from reportlab.graphics.shapes import Drawing, Rect, Circle, Line, String, PolyLine
from reportlab.pdfbase import pdfmetrics

P, S, box, icon, C, tint, CW, LM, PW, PH = B.P, B.S, B.box, B.icon, B.C, B.tint, B.CW, B.LM, B.PW, B.PH
OUT = sys.argv[1] if len(sys.argv) > 1 else str(pathlib.Path(__file__).resolve().parents[1] / "CodeSchool-Classes3-5-Specimen-Booklet.pdf")
TEAL = "#14A3A3"
SAMPLE = [1, 11, 14]  # chapters shown in full: steps (B1), if-then (B3), robot routes


def table(rows, widths, head_color=TEAL, font=10.5, zebra=True, bold_first=True):
    data = []
    for i, r in enumerate(rows):
        data.append([P(str(c), "q", fontSize=font, leading=font + 3.5, fontName="KidB" if (i == 0 or (bold_first and j == 0)) else "Kid",
                       textColor=colors.white if i == 0 else B.INK) for j, c in enumerate(r)])
    t = Table(data, colWidths=widths, repeatRows=1)
    st = [("BACKGROUND", (0, 0), (-1, 0), C(head_color)), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("TOPPADDING", (0, 0), (-1, -1), 4),
          ("BOTTOMPADDING", (0, 0), (-1, -1), 5), ("LINEBELOW", (0, 1), (-1, -1), 0.5, C("#D6DEEA")), ("ROUNDEDCORNERS", [8, 8, 8, 8])]
    if zebra:
        st.append(("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, C("#F3F6FB")]))
    t.setStyle(TableStyle(st))
    return t


def heading(text, size=22):
    return P(text, "h", fontSize=size, leading=size + 5)


def checklist(items, color=TEAL):
    rows = []
    for it in items:
        rows.append([icon("check", color, 16), P(it, "body", spaceAfter=0)])
    t = Table(rows, colWidths=[24, CW - 24 - 28])  # fits inside a box (20pt padding + cell padding)
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("TOPPADDING", (0, 0), (-1, -1), 2), ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]))
    return t


# ------------------------------------------------------------------ school-facing pages
def about_pages():
    s = [NextPageTemplate("body"), PageBreak(), B.SetChapter(None), heading("A complete CT&amp;AI programme for Classes 3-5"),
         P("From 2026-27, CBSE asks schools to teach Computational Thinking and AI in Classes 3-8: <b>50 hours a year in Classes 3-5</b>, "
           "built into Mathematics and The World Around Us periods. CBSE's free handbooks give puzzles for each maths chapter. "
           "CodeSchool adds everything a teacher needs to teach it well, with no computers needed."), Spacer(1, 8)]
    s += [table([["What schools need", "CBSE's free handbook", "CodeSchool Practice Pack"],
                 ["Puzzles for each maths chapter", "Yes", "Yes, in levels from easy to challenge"],
                 ["Theory in simple words", "Short introduction", "A Learn page and Robo's tip in every chapter"],
                 ["Worked examples", "No", "One per chapter, step by step"],
                 ["Coding", "No (follow steps only)", "'Now you build it': coding on paper with code cards"],
                 ["Hands-on activities", "One or two a year", "A classroom kit used all year"],
                 ["Teacher lesson plans", "Answer keys", "A period-by-period teacher script book"],
                 ["Assessment and report card", "No format given", "Self-check, observation journal and term summary"],
                 ["Teacher training", "CBSE workshops", "School orientation, termly workshops and support"]],
                [150, 150, CW - 300]), Spacer(1, 10)]
    s += [box([checklist(["Follows the NCERT <i>Maths Mela</i> chapters in the same order, so it fits the maths period.",
                          "Built around the CT skills in CBSE's curriculum: steps, patterns, abstraction, decomposition, logic and data.",
                          "Works in any classroom: paper, cards and a floor mat. A projector helps but is optional.",
                          "Ready for a maths or EVS teacher, not only a computer specialist."])],
              TEAL, "Why schools choose it", icon("star"))]
    s += [NextPageTemplate("body"), PageBreak(), heading("What each school receives")]
    s += [table([["For", "What they get", "Classes"],
                 ["Each child", "Practice Pack: level workbook with coding cut-outs and take-home challenges", "3, 4, 5"],
                 ["Each class section", "Classroom kit: code cards, floor grid mat, cipher wheels, sorting cards, box", "3, 4, 5"],
                 ["Each teacher", "Teacher script book, answer keys, observation journal, short how-to videos", "3, 4, 5"],
                 ["The school", "Orientation at school, a workshop every term, a support line and a term summary format", "All"]],
                [100, CW - 170, 70]), Spacer(1, 10)]
    s += [heading("The series", 16)]
    s += [table([["Book", "Levels", "Coder skills"],
                 ["Class 3 Practice Pack (this sample)", "B1-B3", "Steps and codes, views, loops, decomposition, patterns, events, data, logic, sorting, if-then, variables, grids"],
                 ["Class 4 Practice Pack", "B3-B5", "If-else choices, nested loops, sorting machines, variables and inputs"],
                 ["Class 5 Practice Pack", "B5-B7", "Variables, search strategies, debugging and a game designed on paper"],
                 ["Classes 6-8 Projects and AI Pack", "C1-C8", "Functions, data, the AI chapters and two 20-hour projects a year (separate sample)"]],
                [170, 50, CW - 220]), Spacer(1, 10)]
    s += [box([P("<b>Indicative price:</b> Rs 449 per child per year (MRP) for the Classes 3-5 Practice Pack, through the school's book list. "
                 "It can replace an existing computer book, so the cost to parents stays about the same. Kits, teacher books and training come with the packs. "
                 "Prices are indicative until confirmed in writing.", "body")], "#F5A524", "Price and ordering", icon("pencil")), Spacer(1, 10)]
    s += [box([P("A <b>free pilot</b> in two or three sections from January to March 2027: materials, a teacher orientation, weekly support and a short "
                 "report against success measures agreed in advance. No obligation to continue.", "body")], "#2BB673", "Try it first", icon("blocks"))]
    return s


def how_lesson_runs():
    s = [NextPageTemplate("body"), PageBreak(), heading("How a lesson runs"),
         P("Every lesson fits one 40-minute period and follows the same five steps, based on the PRIMM approach used in computing classrooms "
           "(predict, run, investigate, modify, make). Children learn the routine once and then focus on the thinking."), Spacer(1, 10)]
    steps = [("1", "Predict and run", "8 min", "Children predict what a set of steps will do, then act it out.", "#14A3A3"),
             ("2", "Investigate", "8 min", "Pairs answer 'why' questions about how it worked.", "#3B82F6"),
             ("3", "Modify", "8 min", "Children change the steps to do something new.", "#8B5CF6"),
             ("4", "Put in order", "8 min", "Jumbled code cards go back in the right order.", "#F5A524"),
             ("5", "Make", "8 min", "Pairs write their own program and swap with another pair.", "#2BB673")]
    rows = []
    for n, name, mins, what, col in steps:
        badge = Drawing(40, 40); badge.add(Circle(20, 20, 18, fillColor=C(col), strokeColor=None))
        badge.add(String(20, 13, n, fontName="KidBl", fontSize=18, fillColor=colors.white, textAnchor="middle"))
        rows.append([badge, P(f"<font color='{col}'><b>{name}</b></font>&nbsp;&nbsp;<font size='9' color='#5B6577'>{mins}</font><br/>{what}", "body", spaceAfter=0)])
    t = Table(rows, colWidths=[52, CW - 52])
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("BOTTOMPADDING", (0, 0), (-1, -1), 8), ("LEFTPADDING", (0, 0), (-1, -1), 0)]))
    s += [t, Spacer(1, 8)]
    s += [box([P("CBSE asks schools to assess CT&amp;AI through written puzzles, group activities and a <b>Teacher Observation Journal</b>. "
                 "Each step gives the teacher something to observe: predictions show reasoning, modifications show understanding, and the 'make' step shows "
                 "whether a child can build an algorithm of their own. The journal format and a term summary for the report card come with the teacher book.")],
              "#5B6577", "How it supports CBSE's assessment"), Spacer(1, 8)]
    s += [box([checklist(["Children who finish early move to the challenge level; children who need help use a hint card.",
                          "Most activities are done in pairs, so children who find reading hard can still take part by talking and acting out.",
                          "Teacher preparation is about 5-10 minutes per lesson using the script."], "#8B5CF6")], "#8B5CF6", "Every child can take part")]
    return s


def kids_view_page():
    fm = B.front_matter()
    toc_i = next(k for k, f in enumerate(fm) if isinstance(f, B.TableOfContents))
    cut = max(k for k in range(toc_i) if isinstance(fm[k], PageBreak))
    return fm[:cut - 1]  # Robo's welcome and 'How this book works' page


def parents_page():
    s = [NextPageTemplate("body"), PageBreak(), B.SetChapter(None), heading("A note for parents"),
         P("Schools can send this page home at the start of the year.", "small"), Spacer(1, 6)]
    s += [P("Dear parents,"),
          P("This year your child will learn <b>computational thinking</b> as part of maths, following CBSE's new curriculum for Classes 3-8. "
            "Computational thinking means solving problems the way a programmer does: breaking a big job into steps, spotting patterns, "
            "keeping what matters and following clear rules. These skills help in maths, reading and everyday life, and they are the base for coding and AI later."),
          P("Your child will use the <i>Think Like a Coder</i> workbook in class. There are no screens: children solve puzzles, crack secret codes, "
            "guide a robot around a grid and write programs with paper code cards."), Spacer(1, 6)]
    s += [box([checklist(["Ask your child to explain a puzzle to you. Explaining is part of the learning.",
                          "Play 'robot' at home: your child gives you step-by-step instructions to make a sandwich, and you follow them exactly.",
                          "Spot patterns together: on clothes, tiles, calendars and number plates.",
                          "Praise effort and good thinking, not just right answers."], "#2BB673")], "#2BB673", "How you can help at home", icon("star")), Spacer(1, 8)]
    s += [box([P("Write the numbers 1 to 20. Colour every 3rd number. What pattern do you see? Which number would be the 10th coloured one?", "body"),
               P("<font size='9' color='#5B6577'>Answer: 3, 6, 9, ... the 10th is 30.</font>", "body")], "#8B5CF6", "Take-home challenge", icon("blocks")), Spacer(1, 8)]
    s += [P("No child's personal data is collected by the workbook. Thank you for your support."), P("<b>Class teacher</b> ____________________&nbsp;&nbsp;&nbsp; <b>School</b> ____________________")]
    return s


def contents_page():
    s = [NextPageTemplate("body"), PageBreak(), heading("Inside the full Class 3 book"),
         P(f"The complete book has 14 chapters, one for each NCERT <i>Maths Mela</i> chapter, plus answers, a glossary and cut-out code cards. "
           f"This sample includes chapters {', '.join(str(n) for n in SAMPLE)} in full.", "body"), Spacer(1, 6)]
    rows = [["Ch", "Chapter", "Coder skill", "Level", "In this sample"]]
    for ch in CH:
        rows.append([str(ch["n"]), ch["title"], ch["skill"], ch["level"], "Yes" if ch["n"] in SAMPLE else ""])
    s += [table(rows, [30, 150, CW - 290, 50, 60], font=10)]
    return s


def teacher_pages():
    ch = next(c for c in CH if c["n"] == 14)
    s = [NextPageTemplate("body"), PageBreak(), B.SetChapter(None), heading("Sample teacher script: Robot routes"),
         P("From the teacher book, Class 3, chapter 14 (<i>The Surajkund Fair</i>). One 40-minute period. Level B1-B2.", "small"), Spacer(1, 6)]
    s += [table([["You need", ""], ["Kit", "Floor grid mat (or a 4 x 5 grid drawn on the floor or board), arrow cards, two stall cards"],
                 ["Book", "Chapter 14 pages, 'Try it' questions 1-3"], ["Goal", "Children follow and write a program of arrows, and find a bug in a route"]],
                [70, CW - 70], head_color="#E5484D", zebra=False), Spacer(1, 8)]
    s += [table([["Step and time", "Teacher does", "Children do"],
                 ["1. Predict and run (8 min)", "Put 'Robo' (a child) on A1 and a stall card on C3. Hold up: up, up, right, right.",
                  "Predict where Robo will stop. One child walks the program while the class reads the arrows aloud."],
                 ["2. Investigate (8 min)", "Ask: 'Would right, right, up, up reach the same stall? Does the order matter?'",
                  "Discuss in pairs. Try it on the mat. (Here both work; with a wall, order can matter.)"],
                 ["3. Modify (8 min)", "Put a 'wall' card on B3. Ask children to change one arrow so Robo avoids it.",
                  "Change the program and test it on the mat."],
                 ["4. Put in order (8 min)", "Give each pair jumbled arrow cards for a new stall.",
                  "Order the cards so Robo reaches the stall, then do 'Try it' question 1."],
                 ["5. Make (8 min)", "Ask pairs to plan a trip to two stalls.",
                  "Write the route with arrow cards, swap with another pair and test their route."]],
                [110, (CW - 110) / 2, (CW - 110) / 2], head_color="#E5484D", font=9.5), Spacer(1, 8)]
    setup = Table([[F.grid(4, 5, robot=(0, 0), items={(2, 2): ("T", F.PURPLE)}, walls=[(2, 1)], cell=26),
                    P("<b>Set-up:</b> Robo starts on A1, the toy stall (T) is on C3. In step 3, put the wall card on B3 (grey). "
                      "Children then change one arrow so Robo still reaches the stall.", "body")]], colWidths=[170, CW - 190])
    setup.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("LEFTPADDING", (0, 0), (-1, -1), 0)]))
    s += [box([setup], "#3B82F6", "Lesson set-up"), Spacer(1, 8),
          box([checklist(["<b>Counting the start square as a step.</b> Ask: 'Did Robo move yet?'",
                          "<b>Mixing up left and right.</b> In this level, arrows are map directions (up means towards the top of the grid), not turns.",
                          "<b>Skipping a square when walking the route.</b> Have the class count each move aloud."], "#E5484D")],
              "#E5484D", "Common mistakes to watch for"), Spacer(1, 8),
          box([P("<b>Support:</b> use a 3 x 3 grid and only up and right arrows.<br/><b>Stretch:</b> shorten a route with 'repeat' (for example, repeat 3 times: right). "
                 "Ask which route is shortest and how they know.", "body")], "#8B5CF6", "Different paces"), Spacer(1, 8),
          box([P("Two quick questions at the end of the period:", "body"),
               P("1. Robo is on A1. Write the arrows to reach C2.&nbsp;&nbsp; 2. With a wall on B2, the program <i>up, right, right</i> fails. Which arrow is the bug? (the 2nd)", "body"),
               P("Note in the observation journal: <b>Beginning</b> (needs help following arrows), <b>Developing</b> (follows, cannot yet write), "
                 "<b>Secure</b> (writes a working route), <b>Extending</b> (finds the shortest route or uses repeat).", "body")],
              "#14A3A3", "Check for understanding"), Spacer(1, 8),
          box([P("Grids and robot routes connect to CBSE's Class 3 handbook chapter on <i>The Surajkund Fair</i> (paths, grids and pathway tiles), "
                 "and build the idea of a program as exact instructions: the base for block coding in later classes.", "body")], "#5B6577", "Curriculum link"),
          B.IfFits(Table([[Spacer(1, 14)], [heading("Teacher notes", 15)], [B.lines(9, CW)]], colWidths=[CW],
                         style=[("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0)]))]
    return s


def kit_page():
    s = [NextPageTemplate("body"), PageBreak(), heading("The classroom kit"),
         P("One kit per class section, used all year. Everything is printed, laminated and reusable.", "body"), Spacer(1, 6)]
    # drawn kit items
    g = F.grid(4, 5, robot=(0, 0), items={(2, 2): ("T", F.PURPLE), (3, 4): ("K", F.GREEN)}, cell=24)
    cards = Drawing(230, 110)
    for i, (lab, k, col) in enumerate([("up", "up", F.BLUE), ("right", "right", F.BLUE), ("Repeat 3 times", "step", F.ORANGE), ("If dry", "step", F.PURPLE)]):
        d = F.code_card(lab, k, w=108, h=30, color=col)
        x, y = (i % 2) * 116, 70 - (i // 2) * 40
        for el in d.contents:
            from reportlab.graphics.shapes import Group
            cards.add(Group(el, transform=(1, 0, 0, 1, x, y)))
    wheel = F.cipher_wheel(150)
    shapes = F.shape_row(["triangle", "circle", "square", "star", "diamond"], r=13)
    items = Table([[g, cards], [P("<b>Floor grid mat</b> (6 x 6 ft) for robot routes", "small"), P("<b>Code cards</b>: arrows, repeat, if, when (4 decks)", "small")],
                   [wheel, shapes], [P("<b>Cipher wheels</b> for secret codes (20)", "small"), P("<b>Picture and shape cards</b> for patterns and sorting (120)", "small")]],
                  colWidths=[CW / 2, CW / 2])
    items.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("ALIGN", (0, 0), (-1, -1), "CENTER"), ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                               ("BACKGROUND", (0, 0), (-1, -1), C("#F7F9FC")), ("ROUNDEDCORNERS", [10, 10, 10, 10])]))
    s += [items, Spacer(1, 10)]
    s += [table([["Item", "Quantity per kit"], ["Code card decks (playing-card size, laminated)", "4 decks of 54"], ["Cut-out coding blocks (die-cut sheets)", "20 sheets"],
                 ["Floor grid mat, washable", "1"], ["Cipher wheels", "20"], ["Picture and shape cards", "120"], ["Robot direction tokens", "30"],
                 ["Teacher quick-guide card", "1"], ["Sturdy box", "1"]], [CW - 140, 140], font=10)]
    s += [Spacer(1, 6), P("Illustrations show the design. Final materials will be confirmed after the pilot.", "small")]
    return s


def assessment_page():
    s = [NextPageTemplate("body"), PageBreak(), heading("Assessment and the report card"),
         P("CBSE asks for continuous, competency-based assessment in CT&amp;AI. The teacher book includes an observation journal using four levels, "
           "and a term summary that fits on the report card.", "body"), Spacer(1, 6)]
    s += [table([["Skill", "Beginning", "Developing", "Secure", "Extending"],
                 ["Following steps", "Follows short steps with help", "Follows and fixes simple steps", "Writes steps with loops", "Designs and improves own steps"],
                 ["Patterns", "Spots simple repeats", "Continues a pattern", "Finds the core and rule", "Makes new patterns and explains them"],
                 ["Breaking problems down", "Needs help to start", "Breaks familiar jobs into steps", "Breaks new problems into steps", "Plans steps and their order alone"],
                 ["Logic and rules", "Uses one clue", "Uses two clues or an if-then rule", "Uses several clues and if-else", "Spots extra clues and explains"]],
                [100] + [(CW - 100) / 4] * 4, font=9), Spacer(1, 12)]
    s += [heading("Sample term summary", 15),
          table([["Area", "Level", "Teacher comment"],
                 ["Computational thinking (overall)", "Secure", "Breaks problems into steps and writes loops confidently."],
                 ["Coding on paper", "12 of 14 'build it' tasks", "Ready for if-else rules with more than two choices."],
                 ["Self-check ('How did I do?')", "Mostly green", "Finds codes easy and clues harder; we practised clue puzzles together."]],
                [150, 100, CW - 250], font=10), Spacer(1, 10)]
    s += [box([P("Each chapter ends with <b>'How did I do?'</b>, where children colour a face for each 'I can' statement. "
                 "Teachers can compare this with what they observed, which helps children learn to judge their own progress.", "body")], TEAL, "Children check themselves too")]
    return s


def answers_page():
    s = [NextPageTemplate("twocol"), PageBreak(), B.SetChapter(None), heading("Answers for the sample chapters")]
    for ch in CH:
        if ch["n"] not in SAMPLE:
            continue
        items = [P(f"<font color='{ch['color']}'>{ch['n']}. {ch['title']}</font>", "ansh")]
        items += [P(f"<b>{i}.</b> {q['answer']}", "ans") for i, q in enumerate(ch["practice"], 1)]
        items += [P(f"<b>Build it:</b> {ch['build']['answer']}", "ans"), P(f"<b>Challenge:</b> {ch['challenge']['answer']}", "ans")]
        s.append(KeepTogether(items))
    s += [NextPageTemplate("body")]
    return s


def next_steps_page():
    s = [NextPageTemplate("body"), PageBreak(), heading("Next steps for your school"), Spacer(1, 4)]
    steps = [("Look through this sample", "Try a chapter with a class or ask a teacher to review it."),
             ("Talk to us", "A short meeting with the principal and coordinator to answer questions."),
             ("Start a free pilot", "Two or three sections, January to March 2027, with an orientation and weekly support."),
             ("Add it to the 2027-28 book list", "Most schools finalise their list by the end of January.")]
    rows = []
    for i, (a, b) in enumerate(steps, 1):
        rows.append([B.number_badge(i, TEAL), P(f"<b>{a}</b><br/>{b}", "body", spaceAfter=0)])
    t = Table(rows, colWidths=[34, CW - 34])
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("BOTTOMPADDING", (0, 0), (-1, -1), 10), ("LEFTPADDING", (0, 0), (-1, -1), 0)]))
    s += [t, Spacer(1, 10)]
    s += [box([P("<b>Anoop Dobhal</b>, CodeSchool, Bullseye Knowledge System Limited<br/>Phone / WhatsApp: [Phone]&nbsp;&nbsp;·&nbsp;&nbsp;Email: [Email]", "body")],
              TEAL, "Contact"), Spacer(1, 12)]
    s += [heading("Notes", 15), B.lines(9, CW)]
    return s


# ------------------------------------------------------------------ covers
def on_spec_cover(c, doc):
    c.saveState()
    c.setFillColor(C("#14A3A3")); c.rect(0, 0, PW, PH, stroke=0, fill=1)
    c.setFillColor(C("#0E7C7C")); c.rect(0, 0, PW, PH * 0.32, stroke=0, fill=1)
    for x, y, r, col in ((470, 700, 30, "#FFD23F"), (530, 800, 22, "#EC4899"), (548, 590, 46, "#F5A524"), (70, 470, 26, "#8B5CF6"), (540, 380, 28, "#2BB673")):
        c.setFillColor(C(col)); c.circle(x, y, r, stroke=0, fill=1)
    c.setFillColor(C("#FFD23F")); c.roundRect(LM + 10, PH - 84, 150, 26, 13, stroke=0, fill=1)
    c.setFillColor(B.INK); c.setFont("KidB", 11); c.drawCentredString(LM + 85, PH - 75, "SPECIMEN BOOKLET")
    c.setFillColor(colors.white); c.setFont("KidBl", 48); c.drawString(LM + 10, PH - 150, "Think Like")
    c.drawString(LM + 10, PH - 202, "a Coder")
    c.setFillColor(C("#FFD23F")); c.setFont("Fun", 20); c.drawString(LM + 14, PH - 238, "Computational thinking for Classes 3-5")
    c.setFillColor(colors.white); c.setFont("Kid", 12.5)
    c.drawString(LM + 14, PH - 264, "A sample for schools: three full chapters, a teacher script,")
    c.drawString(LM + 14, PH - 281, "the classroom kit and how assessment works")
    F.robo(220, color=F.YELLOW, wave=True).drawOn(c, PW - 290, 270)
    c.setFillColor(colors.white); c.setFont("KidB", 12.5)
    c.drawString(LM + 10, 205, "For CBSE's Computational Thinking and AI curriculum, 2026-27")
    c.setFont("Kid", 11)
    c.drawString(LM + 10, 186, "Follows the NCERT Maths Mela chapters  ·  No computers needed")
    c.drawString(LM + 10, 168, "Practice Pack Rs 449 per child (indicative)  ·  Free pilot, January-March 2027")
    c.setFont("Kid", 8.5)
    c.drawString(LM + 10, 52, "© 2026 Bullseye Knowledge System Limited. All rights reserved. Not for sale.")
    c.drawString(LM + 10, 40, "CodeSchool is a working name. Not an official CBSE or NCERT publication.")
    c.restoreState()


def on_back_cover(c, doc):
    c.saveState()
    c.setFillColor(C("#0E7C7C")); c.rect(0, 0, PW, PH, stroke=0, fill=1)
    c.setFillColor(C("#14A3A3")); c.circle(PW / 2, PH * 0.62, 190, stroke=0, fill=1)
    F.robo(170, color=F.YELLOW, wave=True).drawOn(c, PW / 2 - 85, PH * 0.50)
    c.setFillColor(colors.white); c.setFont("KidBl", 30); c.drawCentredString(PW / 2, PH * 0.36, "Think Like a Coder")
    c.setFont("Kid", 13); c.drawCentredString(PW / 2, PH * 0.36 - 26, "Computational thinking for Classes 3-5, for CBSE schools")
    c.setFillColor(C("#FFD23F")); c.roundRect(PW / 2 - 150, PH * 0.24, 300, 34, 17, stroke=0, fill=1)
    c.setFillColor(B.INK); c.setFont("KidB", 13); c.drawCentredString(PW / 2, PH * 0.24 + 11, "Ask us about a free pilot")
    c.setFillColor(colors.white); c.setFont("Kid", 11.5)
    c.drawCentredString(PW / 2, PH * 0.24 - 26, "Phone / WhatsApp: [Phone]   ·   Email: [Email]")
    c.setFont("Kid", 8.5)
    c.drawCentredString(PW / 2, 52, "© 2026 Bullseye Knowledge System Limited. All rights reserved. Specimen copy, not for sale.")
    c.drawCentredString(PW / 2, 40, "CodeSchool is a working name. Not an official CBSE or NCERT publication.")
    c.restoreState()


class SpecDoc(BaseDocTemplate):
    def __init__(self, fn):
        super().__init__(fn, pagesize=B.A4, leftMargin=B.LM, rightMargin=B.RM, topMargin=B.TM, bottomMargin=B.BM,
                         title="Think Like a Coder - Classes 3-5 specimen booklet", author="CodeSchool, Bullseye Knowledge System Limited",
                         subject="Specimen booklet for schools")
        fr = Frame(B.LM, B.BM, CW, PH - B.TM - B.BM, id="f", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        gap = 18
        left = Frame(B.LM, B.BM, (CW - gap) / 2, PH - B.TM - B.BM, id="l", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        right = Frame(B.LM + (CW + gap) / 2, B.BM, (CW - gap) / 2, PH - B.TM - B.BM, id="r", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates([PageTemplate("cover", [fr], onPage=on_spec_cover), PageTemplate("body", [fr], onPageEnd=B.on_body),
                               PageTemplate("twocol", [left, right], onPageEnd=B.on_body), PageTemplate("back", [fr], onPage=on_back_cover)])
        self.chapter = None
        self.default_header = "Specimen booklet  ·  Classes 3-5"
        self.footer_note = "Specimen copy · not for sale"


def build():
    story = [Spacer(1, 1)]
    story += about_pages()
    story += kids_view_page()
    story += how_lesson_runs()
    story += contents_page()
    for ch in CH:
        if ch["n"] in SAMPLE:
            story += B.chapter_story(ch)
    story += teacher_pages()
    story += kit_page()
    story += assessment_page()
    story += answers_page()
    cut = B.back_matter()
    i = next(k for k, f in enumerate(cut) if isinstance(f, B.TocMark) and f.key == "cards")
    story += [NextPageTemplate("body"), PageBreak(), B.SetChapter(None)] + cut[i:]
    story += parents_page()
    story += next_steps_page()
    story += [NextPageTemplate("back"), PageBreak(), Spacer(1, 1)]
    doc = SpecDoc(OUT)
    doc.multiBuild(story)
    print("built", OUT)


if __name__ == "__main__":
    build()
