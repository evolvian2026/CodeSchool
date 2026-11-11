"""Sample examination papers for 'Think Like a Coder - Class 6': half-yearly (term-1 chapters) and annual (whole year), plus
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
    Q("A", 1, "Ap", "What is the next term? 2, 6, 10, 14, ...", "b) 18", opts=["16", "18", "20"]),
    Q("A", 1, "R", "A function takes an input and gives back ...", "a) an output", opts=["an output", "an error", "a loop"]),
    Q("A", 2, "R", "An angle between 90° and 180° is ...", "b) obtuse", opts=["acute", "obtuse", "reflex"]),
    Q("A", 3, "U", "Which number is a palindrome?", "a) 1221", opts=["1221", "1212", "1122"]),
    Q("A", 4, "Ap", "In the list [7, 3, 9, 5], the biggest item is at position ...", "b) 3", opts=["1", "3", "4"]),
    Q("A", 5, "R", "Which number is neither prime nor composite?", "a) 1", opts=["1", "2", "9"]),
    Q("A", 11, "U", "A washing machine that runs the same fixed cycle every time is an example of ...", "b) automation", opts=["AI", "automation"]),
    Q("A", 12, "R", "Data that has been organised to answer a question is called ...", "a) information", opts=["information", "noise", "a password"]),
    ar(5, "U", "51 is not a prime number.", "51 = 3 x 17, so it has more than two factors.", "a) Both A and R are true, and R explains A."),
    ar(11, "An", "A spam filter is an example of AI.", "A spam filter follows the same fixed rule every time and never changes.",
       "c) A is true, but R is false. (Spam filters learn from labelled examples.)"),
    Q("B", 1, "Ap", "triangle(n) = 1 + 2 + ... + n. Find triangle(6) and triangle(10).", "21 and 55", "1 mark for each"),
    Q("B", 2, "Ap", "A robot faces East on an 8-point compass. It turns 135° anticlockwise. Which way does it face now?", "North-West",
      "2 marks; 1 mark for counting 3 steps of 45°"),
    Q("B", 3, "Ap", "Reverse and add until you get a palindrome, starting with 39. Show each step.", "39 + 93 = 132; 132 + 231 = 363", "1 mark for each step"),
    Q("B", 5, "Ap", "List the common factors of 18 and 24. Which is the highest?", "1, 2, 3, 6; the highest is 6", "1 mark for the list, 1 mark for 6"),
    Q("B", 12, "U", "Name two ways of collecting data, with an example of each.", "For example: a survey (asking classmates their favourite sport); "
      "observation (counting vehicles at the gate); measuring (students' heights)", "1 mark for each way with an example"),
    Q("C", 2, "An", "Write a function rectangle(l, w) that draws a rectangle with turns. Write the call that draws a rectangle 60 long and 30 wide. What do its turns add up to?",
      "define rectangle(l, w): repeat 2 times: forward l, turn right 90°, forward w, turn right 90°. Call: rectangle(60, 30). The turns add up to 360°.",
      "1 mark for the function, 1 mark for the call, 1 mark for 360°"),
    Q("C", 4, "An", "Write an algorithm to find the smallest item in a list. Trace it on 12, 7, 15, 4, 9.",
      "Set smallest to the first item; for each item, if item < smallest then smallest = item. Trace: 12, 7, 7, 4, 4. Smallest is 4.",
      "1 mark for the algorithm, 1 mark for the trace, 1 mark for 4"),
    Q("C", 5, "Ap", "List the prime numbers between 30 and 50. Say which multiples you cross out to find them.",
      "31, 37, 41, 43, 47. Cross out multiples of 2, 3, 5 and 7 (35 and 49 are the multiples of 7 left).",
      "2 marks for the list (1 mark with one missing or extra), 1 mark for the explanation"),
    Q("C", 3, "Ap", "Repeat until n = 1: if n is even, n = n ÷ 2, else n = 3n + 1. Start with n = 7. Write every value and count the steps.",
      "7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1: 16 steps", "2 marks for the values (1 mark with one slip), 1 mark for 16"),
    Q("C", 11, "U", "Explain supervised, unsupervised and reinforcement learning, with one example of each.",
      "Supervised: learns from labelled examples, such as photos labelled cat or dog. Unsupervised: finds groups with no labels, such as grouping customers. "
      "Reinforcement: learns by trial, reward and penalty, such as a game-playing robot.", "1 mark for each"),
    Q("D", 1, "Ap", "A row of houses is made with sticks: 1 house uses 5 sticks, 2 houses use 9 and 3 houses use 13.",
      "(a) add 4 (b) sticks = 4n + 1 (c) 101 (d) 20 houses", "(a) 1 mark (b) 2 marks (c) 1 mark (d) 1 mark",
      parts=[("Write a 'next term' rule.", 1), ("Write a 'position' rule for n houses.", 2), ("How many sticks do 25 houses need?", 1),
             ("How many houses can be made with 81 sticks?", 1)]),
    Q("D", 12, "An", "Plan a survey to answer: 'How much water do students in our school drink in a day?'",
      "Open answer, for example: (a) 'How many glasses of water did you drink yesterday?' with options 0-2, 3-5, 6-8, more than 8 (b) ask 10 students from each class "
      "(c) a frequency table of options and counts (d) a bar chart, because it compares groups (e) do not write names; store the sheets safely",
      "1 mark for each part",
      parts=[("Write your survey question and its answer options.", 1), ("Say whom you will ask and how.", 1), ("Draw the table you will use to organise the answers.", 1),
             ("Which chart will you use to show the results? Why?", 1), ("Give one way to keep the data private and safe.", 1)]),
    Q("E", 4, "Ap", "Rainfall (in mm) for one week is stored as a list: Mon 12, Tue 0, Wed 25, Thu 8, Fri 30, Sat 5, Sun 0.",
      "(a) 30 (b) highest: Friday, 30 mm; lowest: Tuesday and Sunday, 0 mm (c) 80 mm (d) 5 symbols (e) Monday, Wednesday and Friday",
      "1 mark for each part",
      parts=[("What is at position 5 of the list?", 1), ("Which day had the most rain and which had the least?", 1), ("What was the total rainfall?", 1),
             ("In a pictograph, 1 symbol = 5 mm. How many symbols show Wednesday?", 1), ("On which days was there more than 10 mm of rain?", 1)]),
]

ANNUAL = [
    Q("A", 6, "Ap", "area(9, 4) = ...", "c) 36", opts=["13", "26", "36"]),
    Q("A", 7, "Ap", "Which fraction is in its simplest form?", "b) 5/8", opts=["6/9", "5/8", "4/10"]),
    Q("A", 8, "R", "In a construction, the compass is used to ...", "a) draw arcs and circles", opts=["draw arcs and circles", "measure angles", "colour shapes"]),
    Q("A", 9, "Ap", "What is the order of rotational symmetry of a regular pentagon?", "b) 5", opts=["1", "5", "10"]),
    Q("A", 10, "Ap", "-3 - 4 = ...", "a) -7", opts=["-7", "-1", "7"]),
    Q("A", 13, "U", "A rule learnt from labelled examples is used to ...", "a) predict labels for new examples",
      opts=["predict labels for new examples", "delete data", "draw charts"]),
    Q("A", 14, "R", "Copying someone's essay and calling it your own is ...", "b) plagiarism", opts=["phishing", "plagiarism", "piracy"]),
    Q("A", 2, "Ap", "A robot draws a regular hexagon. Each turn is ...", "b) 60°", opts=["45°", "60°", "120°"]),
    ar(10, "U", "-8 is smaller than -2.", "On a number line, -8 is to the left of -2.", "a) Both A and R are true, and R explains A."),
    ar(14, "An", "The password 'Rohan2014' is strong.", "Strong passwords are long and mix words, numbers and symbols that are hard to guess.",
       "d) A is false, but R is true. (A name and a year are easy to guess.)"),
    Q("B", 6, "Ap", "Find the perimeter and the area of a rectangle 12 m long and 5 m wide.", "34 m; 60 m²", "1 mark for each"),
    Q("B", 7, "Ap", "Write three fractions equal to 2/5.", "For example 4/10, 6/15, 8/20", "2 marks for three; 1 mark for two"),
    Q("B", 9, "Ap", "Columns are numbered 1 to 10, with a mirror line between 5 and 6. Where do squares in column 2 and column 5 go when reflected?",
      "column 9 and column 6", "1 mark for each"),
    Q("B", 10, "Ap", "Temperatures were -6°C, 4°C, -1°C and 9°C. Find the range.", "9 - (-6) = 15°C", "1 mark for the method, 1 mark for 15"),
    Q("B", 13, "U", "Observation or conclusion? (a) 18 of the 20 apples in this basket are red. (b) Apples are usually red.", "(a) observation (b) conclusion",
      "1 mark for each"),
    Q("C", 6, "Ap", "A plot is a 10 m by 8 m rectangle with a 4 m by 3 m rectangle cut out of one corner. Find its area and its perimeter.",
      "Area: 80 - 12 = 68 m². Perimeter: 36 m (cutting a corner out does not change the distance around).",
      "1 mark for the method, 1 mark for 68 m², 1 mark for 36 m"),
    Q("C", 7, "Ap", "Sort 2/3, 1/2, 3/4 and 5/12 from smallest to biggest with bubble sort. First write them in twelfths; then show each pass.",
      "Twelfths: 8, 6, 9, 5. Pass 1: 6, 8, 5, 9. Pass 2: 6, 5, 8, 9. Pass 3: 5, 6, 8, 9. So 5/12, 1/2, 2/3, 3/4.",
      "1 mark for twelfths, 1 mark for the passes, 1 mark for the final order"),
    Q("C", 8, "An", "A script to find the midpoint of AB = 8 cm says: 1. Draw AB. 2. With the compass at A and radius 3 cm, draw arcs above and below AB. "
      "3. With the compass at B and radius 5 cm, draw arcs. 4. Join the points where the arcs cross. Find two bugs and fix the script.",
      "Bug 1: 3 cm is not more than half of AB (4 cm), so the arcs may not meet. Bug 2: the radius must be the same from A and from B. Fix: use 5 cm from both A and B.",
      "1 mark for each bug, 1 mark for the fix"),
    Q("C", 14, "U", "A message says: 'Congratulations! You have won a phone. Send your parent's bank OTP within 10 minutes to claim it.' Give three signs that this is phishing.",
      "It is too good to be true; it asks for an OTP (secret bank information); it rushes you; it comes from an unknown sender.", "1 mark for each sign, up to 3"),
    Q("C", 13, "An", "Labelled examples for 'Does it float?': wooden block, floats; iron nail, sinks; plastic ball, floats; steel spoon, sinks; cork, floats. "
      "Find a rule. Use it to predict a glass marble. Is the prediction right?",
      "Rule: if it is made of metal, it sinks; else it floats. Prediction: the marble floats. Wrong: a glass marble sinks, so the rule needs more varied examples.",
      "1 mark for the rule, 1 mark for the prediction, 1 mark for spotting the error"),
    Q("D", 10, "Ap", "A lift serves floors -3 to 10. It starts at floor 0 and makes these moves: +5, -7, +2, -1, +6.",
      "(a) 5, -2, 0, -1, 5 (b) -2 (c) 21 floors (d) If floor + move < -3 then show 'Not allowed', else move.",
      "(a) 2 marks, 1 mark with one slip (b) 1 mark (c) 1 mark (d) 1 mark",
      parts=[("Trace the floor after each move.", 2), ("What is the lowest floor reached?", 1), ("How many floors does the lift travel in all?", 1),
             ("Write a rule that stops the lift going below floor -3.", 1)]),
    Q("D", 9, "An", "Symmetry in letters and shapes.", "(a) M, A, T and H (b) N, O and S (c) for example a rectangle (d) new column = 9 - column "
      "(e) Line symmetry: folding makes the halves match. Rotational symmetry: turning by less than a full turn looks the same.", "1 mark for each part",
      parts=[("Which letters of the word MATH have a line of symmetry going straight down?", 1), ("Which letters of the word NOSE have rotational symmetry of order 2?", 1),
             ("Name a shape with exactly 2 lines of symmetry and rotational symmetry of order 2.", 1),
             ("Columns are numbered 1 to 8, with a mirror between 4 and 5. Write a rule for the new column after reflecting.", 1),
             ("Explain the difference between line symmetry and rotational symmetry.", 1)]),
    Q("E", 13, "An", "A school wants an AI app that predicts which students may need extra help in maths, using last year's marks and attendance.",
      "(a) Last year's students' marks and attendance, each labelled 'needed help' or 'did not' (b) to check it works on data it has not seen "
      "(c) for example, students' marks could be seen by others or shared without permission (d) the teacher, because people are responsible for decisions "
      "(e) for example, if the data came only from one section, it may be unfair to others", "1 mark for each part",
      parts=[("What labelled examples would it learn from?", 1), ("Why should it be tested on new students' data before it is used?", 1), ("Give one privacy risk.", 1),
             ("Who should make the final decision about extra help? Why?", 1), ("Give one way bias could get into the app.", 1)]),
]

PAPERS = [dict(key="half", name="Half-yearly examination", scope="chapters 1-5 and AI 1-2 (term 1)", questions=HALF),
          dict(key="annual", name="Annual examination", scope="all chapters, mostly chapters 6-10 and AI 3-4 (term 2)", questions=ANNUAL)]

PRACTICAL = dict(stations=[
    ("1. Function machine (chapter 1)", "Find the hidden rule from four input-output cards, then predict the output for a new input.",
     "How did you find the rule? How can you check it?"),
    ("2. Drawing robot (chapter 2)", "Write forward-and-turn steps for a partner to draw a regular hexagon on grid paper.",
     "Why is each turn 60°? What do the turns add up to?"),
    ("3. The sieve (chapter 5)", "Use the 1-50 sieve card to find all the primes.", "Why can you stop after crossing out multiples of 7? Is 1 prime?"),
    ("4. Bubble sort (chapter 7)", "Sort six fraction cards from smallest to biggest by swapping neighbours; count the swaps.",
     "How do you compare two fractions? How do you know the list is sorted?"),
    ("5. AI sorter (AI 3)", "Learn a rule from eight labelled picture cards, then label four new cards.", "Which feature decides the label? What would make the rule better?"),
    ("6. Stay safe online (AI 4)", "Rate five passwords as weak or strong, and sort three messages into safe and phishing.",
     "What makes a password strong? What would you do with the phishing message?"),
])
