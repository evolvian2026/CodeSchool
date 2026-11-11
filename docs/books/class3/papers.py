"""Sample examination papers for 'Think Like a Coder - Class 3': half-yearly (term-1 chapters) and annual (whole year).
Each question: s (section), q (text), m (marks) or parts [(text, marks)], ch (chapter), lv (R, U, Ap, An), answer, guide."""
import figures as F


def Q(s, ch, lv, q, answer, guide="", m=None, **kw):
    if m is None and "parts" not in kw:
        m = {"A": 1, "B": 2, "C": 3, "D": 4}[s]
    return dict(s=s, ch=ch, lv=lv, q=q, m=m, answer=answer, guide=guide, **kw)


def star_grid():
    return F.grid(4, 4, robot=(0, 0), items={(2, 3): ("S", F.PURPLE)}, walls=[(0, 1), (1, 1)], cell=24)


HALF = [
    Q("A", 1, "R", "Writing each letter as a different letter, using a rule, makes a ...", "a) secret code", opts=["secret code", "number line", "pattern block"]),
    Q("A", 1, "Ap", "With key +1, the code for SUN is ...", "a) TVO", opts=["TVO", "RTM", "TUN"]),
    Q("A", 2, "R", "Looking at a cup from the top, you see a ...", "a) circle", opts=["circle", "triangle", "square"]),
    Q("A", 3, "Ap", "Start at 60. Add 20 three times. Where do you end?", "c) 120", opts=["80", "100", "120"]),
    Q("A", 4, "U", "Which step comes first when you plant a seed?", "b) dig a small hole", opts=["water the soil", "dig a small hole", "watch it grow"]),
    Q("A", 5, "Ap", "What comes next? triangle, circle, circle, triangle, circle, circle, ...", "b) triangle", opts=["circle", "triangle", "square"]),
    Q("A", 6, "U", "In 'when the whistle blows, start running', the event is ...", "a) the whistle blows",
      opts=["the whistle blows", "start running", "the race ends"]),
    Q("A", 7, "Ap", "5 packets have 4 bangles each. How many bangles in all?", "b) 20", opts=["9", "20", "45"]),
    Q("B", 1, "Ap", "Code the word BAT with key +2.", "DCV", "2 marks; 1 mark if two letters are right"),
    Q("B", 2, "U", "You draw a map to the park for a friend. Write one thing that matters and one thing that does not.",
      "For example, matters: the roads and where to turn; does not matter: the colour of the houses", "1 mark for each"),
    Q("B", 3, "Ap", "Write the next two numbers: 150, 175, 200, ___, ___", "225, 250", "1 mark for each"),
    Q("B", 4, "An", "Find the bug: 1. Put on your shoes. 2. Put on your socks. 3. Tie the laces. Write the correct order.", "2, 1, 3",
      "2 marks; 1 mark for spotting that socks come before shoes"),
    Q("B", 6, "Ap", "Write one 'when ... do ...' rule for the school bell.", "For example: when the bell rings, line up",
      "1 mark for the event, 1 mark for the action"),
    Q("B", 7, "U", "21 laddoos are put in packets of 3. How many packets are there?", "7", "2 marks; 1 mark for a drawing or a correct method"),
    Q("C", 3, "An", "Write a loop that starts at 0 and reaches 100 by adding 20 each time. How many times does it repeat? Write the numbers it reaches.",
      "Repeat 5 times: add 20. It reaches 20, 40, 60, 80, 100.", "1 mark for the loop, 1 mark for 5 times, 1 mark for the numbers"),
    Q("C", 5, "Ap", "The core of a bead pattern is red, blue, blue.", "(a) red, blue, blue, red, blue, blue, red, blue, blue (b) red (c) 6",
      "1 mark for each part", parts=[("Write the first 9 beads.", 1), ("What colour is the 10th bead?", 1), ("How many blue beads are in the first 9?", 1)]),
    Q("C", 4, "Ap", "Break 'making a sandwich' into at least 5 small steps, in order.",
      "For example: take two slices of bread; spread butter; add the vegetables; put the second slice on top; cut it in half.",
      "1 mark for 5 steps, 1 mark for a sensible order, 1 mark if each step is one small action"),
    Q("C", 1, "An", "Riya coded a word with key +1 and got IBU. Decode it, and say how you decoded it.", "HAT. Move each letter back by 1.",
      "2 marks for HAT (1 mark for two letters), 1 mark for the method"),
    Q("D", 7, "Ap", "Meena's stall sold rakhis on four days: Monday 12, Tuesday 18, Wednesday 9, Thursday 15.",
      "(a) Tuesday (b) Wednesday, Monday, Thursday, Tuesday (c) 54 (d) 6", "1 mark for each part",
      parts=[("Which day sold the most rakhis?", 1), ("Sort the days from fewest rakhis to most.", 1), ("How many rakhis were sold in all?", 1),
             ("Tuesday's rakhis were packed in packets of 3. How many packets?", 1)]),
    Q("D", 6, "An", "A counter machine has three buttons: +1, +10 and +100. It now shows 245.",
      "(a) 345 (b) 10 presses: +10 five times and +1 five times (c) When the counter shows 999, say 'Full!'",
      "(a) 1 mark; (b) 2 marks, 1 mark for 55 more; (c) 1 mark",
      parts=[("Press +100 once. What does it show?", 1), ("Start again at 245. Which presses reach 300 with the fewest presses? How many presses?", 2),
             ("The machine says 'Full!' at 999. Write this as a 'when ... do ...' rule.", 1)]),
]

ANNUAL = [
    Q("A", 8, "U", "Rule: if the ball is red, put it in box A, else put it in box B. Where does a green ball go?", "b) box B", opts=["box A", "box B"]),
    Q("A", 9, "Ap", "I have 4 hundreds, 0 tens and 6 ones. I am ...", "b) 406", opts=["46", "406", "460"]),
    Q("A", 10, "Ap", "Sort 9, 3 and 6 from smallest to biggest.", "a) 3, 6, 9", opts=["3, 6, 9", "9, 6, 3", "3, 9, 6"]),
    Q("A", 11, "U", "On a balance, the left pan goes up. So the left side is ...", "b) lighter", opts=["heavier", "lighter", "the same"]),
    Q("A", 12, "Ap", "Set coins to 10. Add 5. Take away 3. Now coins is ...", "a) 12", opts=["12", "18", "8"]),
    Q("A", 13, "R", "How many days are there in a week?", "b) 7", opts=["5", "7", "12"]),
    Q("A", 14, "Ap", "Robo is on B2 and moves up once. Where is it now?", "a) B3", opts=["B3", "C2", "B1"]),
    Q("A", 2, "R", "Keeping only the details that matter is called ...", "a) abstraction", opts=["abstraction", "addition", "a pattern"]),
    Q("B", 8, "Ap", "Share 14 pencils fairly among 3 children. How many does each child get, and how many are left?", "4 each, 2 left",
      "1 mark for each"),
    Q("B", 9, "An", "I am a 3-digit number between 500 and 600. My tens digit is 0 and my ones digit is 7. Who am I?", "507",
      "2 marks; 1 mark for the hundreds digit 5"),
    Q("B", 10, "Ap", "Sort 6, 2, 5 by swapping neighbours. Write the list after each swap.", "2, 6, 5; then 2, 5, 6",
      "1 mark for each swap"),
    Q("B", 12, "Ap", "Set water to 20 litres. Use 6 litres. Add 10 litres. Write water after each step.", "14, then 24", "1 mark for each"),
    Q("B", 13, "Ap", "Today is Thursday. What day will it be after 4 days?", "Monday", "2 marks; 1 mark for counting on with one slip"),
    Q("B", 3, "Ap", "Fill the gap: start at 0, repeat 4 times: add ___, to reach 200.", "50", "2 marks"),
    Q("C", 14, "Ap", "Write the shortest list of arrows that takes Robo from A1 to the star S on D3 without going through the walls. How many arrows?",
      "up, up, right, right, right: 5 arrows. Any 5-arrow route that avoids the walls is correct.",
      "2 marks for a correct route, 1 mark for 5", fig=star_grid, lines=2),
    Q("C", 11, "An", "Write an if-then-else rule for a water tank's pump. What does your rule do when the tank is half full?",
      "If the tank is full then switch the pump off, else keep the pump on. Half full: the pump stays on.",
      "1 mark for the condition, 1 mark for both actions, 1 mark for the half-full case"),
    Q("C", 9, "An", "Write 3 clues so that only the number 352 fits all of them.",
      "For example: I am between 300 and 400. My tens digit is 5. My ones digit is 2.", "1 mark for each clue that helps narrow it to 352"),
    Q("C", 13, "Ap", "A loop says: each day from Monday to Saturday, read 2 pages. How many pages is that? If you also read 4 pages on Sunday, how many pages in the week?",
      "12 pages; 16 pages", "1 mark for 6 days, 1 mark for 12, 1 mark for 16"),
    Q("D", 12, "Ap", "Asha plays a shop game. The variable money starts at ₹50.", "(a) ₹38 (b) ₹58 (c) ₹28 (d) money stores how many rupees Asha has",
      "1 mark for each part",
      parts=[("She buys a pen for ₹12. What is money now?", 1), ("Her aunt gives her ₹20. What is money now?", 1),
             ("She buys 2 notebooks for ₹15 each. What is money now?", 1), ("What does the variable money store?", 1)]),
    Q("D", 10, "An", "For the class party, children voted for snacks: samosa 8, idli 5, pakora 8, fruit 6.",
      "(a) samosa and pakora (8), fruit (6), idli (5) (b) samosa and pakora (c) For example: vote again between only those two, or toss a coin",
      "(a) 1 mark (b) 1 mark (c) 2 marks for a fair rule, 1 mark for a rule that is not clearly fair",
      parts=[("Sort the snacks from most votes to fewest.", 1), ("Which two snacks are tied?", 1), ("Write a fair rule to choose between them.", 2)]),
]

PAPERS = [dict(key="half", name="Half-yearly examination", scope="chapters 1-7 (term 1)", questions=HALF),
          dict(key="annual", name="Annual examination", scope="all chapters, mostly chapters 8-14 (term 2)", questions=ANNUAL)]
