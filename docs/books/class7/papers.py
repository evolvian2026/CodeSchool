"""Sample examination papers for 'Think Like a Coder - Class 7': half-yearly (term-1 chapters) and annual (whole year), plus
unplugged practical stations. Each question: s (section), q, m or parts [(text, marks)], ch, lv (R, U, Ap, An), answer, guide."""

AR = ["Both A and R are true, and R explains A.", "Both A and R are true, but R does not explain A.", "A is true, but R is false.",
      "A is false, but R is true."]


def Q(s, ch, lv, q, answer, guide="", m=None, **kw):
    if m is None and "parts" not in kw:
        m = {"A": 1, "B": 2, "C": 3, "D": 5}[s]
    return dict(s=s, ch=ch, lv=lv, q=q, m=m, answer=answer, guide=guide, **kw)


def ar(ch, lv, a, r, answer):
    return Q("A", ch, lv, f"<b>Assertion (A):</b> {a}<br/><b>Reason (R):</b> {r}", answer, opts=AR)


HALF = [
    Q("A", 1, "R", "10 lakh = ...", "a) 1 million", opts=["1 million", "10 million", "1 billion"]),
    Q("A", 1, "Ap", "6,48,512 rounded to the nearest lakh is ...", "a) 6,00,000", opts=["6,00,000", "6,50,000", "7,00,000"]),
    Q("A", 2, "Ap", "12 - 8 ÷ 4 = ...", "b) 10", opts=["1", "10", "2"]),
    Q("A", 3, "Ap", "The binary number 1101 is ... in decimal.", "b) 13", opts=["11", "13", "1101"]),
    Q("A", 3, "R", "In 0.06, the 6 is in the ... place.", "b) hundredths", opts=["tenths", "hundredths", "thousandths"]),
    Q("A", 4, "Ap", "If a = 3, then 2a + 5 = ...", "a) 11", opts=["11", "28", "10"]),
    Q("A", 9, "U", "Grouping customers with similar shopping habits, with no labels, is ...", "c) clustering",
      opts=["classification", "regression", "clustering"]),
    Q("A", 10, "U", "AI that picks the next practice question from a student's mistakes is used in ...", "a) education",
      opts=["education", "transport", "farming"]),
    ar(2, "U", "In 5 + 3 x 2, the multiplication is done first.", "Multiplication and division are done before addition and subtraction.",
       "a) Both A and R are true, and R explains A."),
    ar(9, "An", "A model should be tested on the same data it was trained on.", "Test data shows how well the model works on data it has not seen.",
       "d) A is false, but R is true."),
    Q("B", 1, "Ap", "Write 25,000,000 with Indian commas and in words.", "2,50,00,000; two crore fifty lakh", "1 mark for each"),
    Q("B", 2, "Ap", "Write one expression for 'add 4 and 6, then multiply by 3', and find its value.", "(4 + 6) x 3 = 30", "1 mark for the brackets, 1 mark for 30"),
    Q("B", 3, "Ap", "Write 0.75 as a fraction in simplest form, and 3/8 as a decimal.", "3/4; 0.375", "1 mark for each"),
    Q("B", 4, "Ap", "The perimeter of a rectangle is 2(l + b). Find it when l = 7 cm and b = 4.5 cm.", "2(7 + 4.5) = 23 cm", "1 mark for substituting, 1 mark for 23 cm"),
    Q("B", 10, "U", "Give one benefit and one risk of using AI in healthcare.", "For example: benefit, it spots illness early in X-rays; risk, it can be wrong, so a doctor must check",
      "1 mark for each"),
    Q("C", 2, "An", "Draw the expression tree for 3 x (8 - 2) + 10 ÷ 5 and work out its value.",
      "Top: +. Left branch: x joining 3 and (- joining 8 and 2). Right branch: ÷ joining 10 and 5. Value: 18 + 2 = 20.",
      "1 mark for + at the top, 1 mark for both branches, 1 mark for 20"),
    Q("C", 3, "Ap", "Write 5, 6, 7 and 8 as 4-bit binary numbers. How many bits are needed to write every number up to 100?",
      "0101, 0110, 0111, 1000. 7 bits (6 bits reach only 63; 7 bits reach 127).", "2 marks for the four numbers (1 mark for two), 1 mark for 7 bits"),
    Q("C", 4, "Ap", "Tables in a row seat 4n + 2 people, where n is the number of tables. How many people do 12 tables seat? How many tables are needed for 38 people?",
      "50 people; 9 tables (4 x 9 + 2 = 38)", "1 mark for 50, 2 marks for 9 tables (1 mark for the method)"),
    Q("C", 9, "U", "Classification, regression or clustering? (a) Predicting a house's price from its size. (b) Sorting X-rays into 'healthy' and 'not healthy'. "
      "(c) Grouping news stories by topic when there are no labels.", "(a) regression (b) classification (c) clustering", "1 mark for each"),
    Q("C", 1, "Ap", "Estimate 4,87,215 + 2,13,980 by rounding each number to the nearest thousand. Then find the exact answer and the difference.",
      "4,87,000 + 2,14,000 = 7,01,000; exact 7,01,195; difference 195", "1 mark for each"),
    Q("D", 9, "An", "A dataset has 500 photos of leaves, each labelled 'healthy' or 'diseased'.",
      "(a) Computer Vision (b) classification (c) for example 350 training, 75 validation, 75 test (d) It has learnt the training photos too closely; "
      "it needs more varied photos and must be judged on test data (e) for example, farmers can spot disease early and save their crop",
      "1 mark for each part",
      parts=[("Which AI domain is this?", 1), ("Is the task classification, regression or clustering?", 1), ("How would you split the 500 photos?", 1),
             ("The model is right 96% of the time on training photos but only 70% on test photos. What has gone wrong?", 1),
             ("Give one way this model could help farmers.", 1)]),
    Q("D", 4, "Ap", "Hexagons in a row are made from sticks: 1 hexagon uses 6 sticks, 2 use 11 and 3 use 16.",
      "(a) 5n + 1 (b) 201 (c) 12 hexagons (d) set sticks to 5 x n + 1", "(a) 2 marks (b) 1 mark (c) 1 mark (d) 1 mark",
      parts=[("Write a formula for the sticks needed for n hexagons.", 2), ("How many sticks do 40 hexagons need?", 1), ("How many hexagons can 61 sticks make?", 1),
             ("Write the formula as one line of a program.", 1)]),
    Q("E", 10, "An", "A route app compares two routes. Route A is 14 km and live traffic moves at 28 km/h. Route B is 10 km and live traffic moves at 15 km/h.",
      "(a) A: 30 minutes; B: 40 minutes (b) Route A, because it takes less time even though it is longer (c) how fast phones on each road are moving "
      "(d) for example, the app tracks where people go, so location data must be kept private",
      "(a) 2 marks (b) 1 mark (c) 1 mark (d) 1 mark",
      parts=[("How long does each route take?", 2), ("Which route does the app choose? Why?", 1), ("What live data does the app use?", 1),
             ("Give one privacy concern about route apps.", 1)]),
]

ANNUAL = [
    Q("A", 5, "Ap", "Two lines cross and one angle is 110°. The angle next to it on the straight line is ...", "a) 70°", opts=["70°", "110°", "250°"]),
    Q("A", 6, "Ap", "With 5 lights, each ON or OFF, how many cases are there?", "c) 32", opts=["10", "25", "32"]),
    Q("A", 7, "R", "A triangle with all three sides different is ...", "a) scalene", opts=["scalene", "isosceles", "equilateral"]),
    Q("A", 8, "Ap", "1/2 x 4/5 = ...", "a) 2/5", opts=["2/5", "5/10", "5/7"]),
    Q("A", 11, "U", "Parts of a whole are best shown with a ...", "a) pie chart", opts=["pie chart", "line graph"]),
    Q("A", 12, "R", "Data that repeats unfair decisions from the past shows ...", "b) historical bias", opts=["data bias", "historical bias", "measurement bias"]),
    Q("A", 3, "Ap", "The binary number 10000 is ... in decimal.", "a) 16", opts=["16", "32", "10"]),
    Q("A", 11, "Ap", "In a pie chart for 36 students, the slice for 9 students is ...", "b) 90°", opts=["36°", "90°", "9°"]),
    ar(7, "U", "3 cm, 4 cm and 9 cm can make a triangle.", "In a triangle, any two sides added together are longer than the third side.",
       "d) A is false, but R is true."),
    ar(5, "An", "Corresponding angles made by a transversal on two parallel lines are equal.", "Parallel lines never meet.",
       "b) Both A and R are true, but R does not explain A."),
    Q("B", 5, "Ap", "A transversal crosses two parallel lines, and one angle is 72°. Find the co-interior angle that pairs with it.", "108°",
      "1 mark for 180° - 72°, 1 mark for 108°"),
    Q("B", 6, "Ap", "Lights R, G and B. Clue 1: exactly one light is OFF. Clue 2: Red is OFF. Which lights are ON?", "Green and Blue", "2 marks"),
    Q("B", 7, "Ap", "An isosceles triangle has a top angle of 40°. Find the two equal base angles.", "70° each", "1 mark for 140° ÷ 2, 1 mark for 70°"),
    Q("B", 8, "Ap", "Half of a number, plus 7, is 19. Work backwards to find the number.", "19 - 7 = 12; 12 x 2 = 24", "1 mark for each step"),
    Q("B", 12, "U", "Name two kinds of bias in AI, with an example of each.",
      "For example: data bias, a face detector trained mostly on adults; historical bias, hiring data that repeats past unfairness", "1 mark for each"),
    Q("C", 6, "An", "Explain why the sum of any three consecutive numbers is a multiple of 3.", "n + (n + 1) + (n + 2) = 3n + 3 = 3(n + 1), which is a multiple of 3.",
      "1 mark for the three numbers, 1 mark for 3n + 3, 1 mark for 3(n + 1)"),
    Q("C", 7, "An", "Write a function classify(a, b, c) that names a triangle by its sides. Test it on (5, 5, 5), (5, 5, 8) and (4, 6, 7).",
      "If a = b and b = c: equilateral; else if a = b or b = c or a = c: isosceles; else: scalene. Results: equilateral, isosceles, scalene.",
      "1 mark for the function, 2 marks for all three results (1 mark for two)"),
    Q("C", 8, "Ap", "A tank is 3/4 full. 1/3 of the water in it is used, and 30 litres are left. What is the full capacity of the tank?",
      "30 L is 2/3 of the water, so the water was 45 L. 45 L is 3/4 of the tank, so the tank holds 60 L.", "1 mark for 45 L, 1 mark for the method, 1 mark for 60 L"),
    Q("C", 11, "Ap", "Of 120 students, 30 like cricket, 45 football, 15 hockey and 30 badminton. Find the angle of each slice in a pie chart, and check the total.",
      "90°, 135°, 45°, 90°; total 360°", "2 marks for the angles (1 mark for two), 1 mark for the check"),
    Q("C", 5, "An", "A turtle starts with heading 0°. Program: forward 40, turn right 50°, forward 30, turn right 130°, forward 40. Which two lines are parallel? Explain using headings.",
      "The headings are 0°, 50° and 180°. The first and third lines are parallel: 180° points the opposite way along the same direction.",
      "1 mark for the headings, 1 mark for the answer, 1 mark for the reason"),
    Q("D", 12, "An", "A bank trains a loan-approval model only on past decisions from one city branch.",
      "(a) data bias, and possibly historical bias (b) compare approval rates and accuracy for different groups and places (c) add records from other branches and groups "
      "(d) a person reviews important decisions and takes responsibility (e) tell people the main reasons for a decision",
      "1 mark for each part",
      parts=[("What kind of bias could this cause?", 1), ("How would you check whether the model is fair?", 1), ("How would you rebalance the data?", 1),
             ("What should humans do when the model is used?", 1), ("Give one way to make the model's decisions transparent.", 1)]),
    Q("D", 6, "Ap", "Three lights R, G and B are each ON or OFF.",
      "(a) OOO, OOU, OUO, OUU, UOO, UOU, UUO, UUU (U = ON, O = OFF) (b) R and G; R and B; G and B; all three (4 cases) (c) only Red and Green ON (d) 64",
      "(a) 2 marks, 1 mark for six or seven cases (b) 1 mark (c) 1 mark (d) 1 mark",
      parts=[("List all 8 cases.", 2), ("Clue 1: at least two lights are ON. Which cases are left?", 1), ("Clue 2: Blue is OFF. Which case is left?", 1),
             ("How many cases would there be with 6 lights?", 1)]),
    Q("E", 11, "Ap", "The temperature at noon on six days was 31°C, 33°C, 32°C, 35°C, 38°C and 35°C.",
      "(a) a line graph, because it shows change over time (b) 38°C; range 7°C (c) 34°C (d) mostly rising, with a dip on day 3 and on day 6 "
      "(e) It can be honest if the axis is clearly marked, but it makes small changes look large; starting at 0 or marking the break is fairer",
      "1 mark for each part",
      parts=[("Which chart would you use? Why?", 1), ("What is the highest temperature, and the range?", 1), ("What is the average temperature?", 1),
             ("Describe the trend.", 1), ("A chart's temperature axis starts at 30°C. Is that honest? Explain.", 1)]),
]

PAPERS = [dict(key="half", name="Half-yearly examination", scope="chapters 1-4 and AI 1-2 (term 1)", questions=HALF),
          dict(key="annual", name="Annual examination", scope="all chapters, mostly chapters 5-8 and AI 3-4 (term 2)", questions=ANNUAL)]

PRACTICAL = dict(stations=[
    ("1. Binary cards (chapter 3)", "Use five dot cards (16, 8, 4, 2, 1) to show three numbers the examiner chooses, then read two binary numbers back.",
     "Why does each card double? How many numbers can five cards show?"),
    ("2. Expression trees (chapter 2)", "Build an expression tree from cards for an expression, then evaluate it from the bottom up.",
     "Which operation is done last? How do brackets change the tree?"),
    ("3. Angle tracer (chapter 5)", "Trace a turtle program's heading after each turn and mark which lines are parallel.", "How do headings show parallel lines?"),
    ("4. Clue filter (chapter 6)", "Lay out all 8 light cards and remove cards clue by clue until one is left.", "Why start with every case? What does each clue remove?"),
    ("5. AI task sort (AI 1)", "Sort twelve problem cards into classification, regression and clustering.", "What does each kind of task give as its answer?"),
    ("6. Survey to pie chart (AI 3)", "Turn a small survey table into pie-chart angles and draw the chart.", "How do you find each angle? When is a bar chart better?"),
    ("7. The lopsided deck (AI 4)", "Find the bias in a training deck of cards and rebalance it.", "Which group is missing? How would you test the fix?"),
])
