"""Sample examination papers for 'Think Like a Coder - Class 5': half-yearly (term-1 chapters) and annual (whole year).
Each question: s (section), q (text), m (marks) or parts [(text, marks)], ch (chapter), lv (R, U, Ap, An), answer, guide."""
import figures_c5 as F


def Q(s, ch, lv, q, answer, guide="", m=None, **kw):
    if m is None and "parts" not in kw:
        m = {"A": 1, "B": 2, "C": 3, "D": 4}[s]
    return dict(s=s, ch=ch, lv=lv, q=q, m=m, answer=answer, guide=guide, **kw)


def map_x():
    return F.treasure_map(rows=5, cols=6, start=(0, 0), items={(4, 3): ("X", F.RED)}, walls=[(1, 0), (1, 1)], cell=24)


HALF = [
    Q("A", 1, "U", "'The sky is blue OR grass is purple.' This statement is ...", "a) true", opts=["true", "false", "can't tell"]),
    Q("A", 1, "Ap", "A number is even AND more than 10. Which number fits?", "b) 12", opts=["8", "12", "15"]),
    Q("A", 2, "Ap", "Set cake to 12 slices. Eat one third of them. Now cake is ...", "b) 8", opts=["4", "8", "9"]),
    Q("A", 3, "R", "A right angle is ...", "b) 90°", opts=["45°", "90°", "180°"]),
    Q("A", 3, "Ap", "A turtle draws a triangle with equal sides. Each turn is ...", "c) 120°", opts=["60°", "90°", "120°"]),
    Q("A", 4, "R", "A program asks 'How many km?' The number you type in is the program's ...", "a) input", opts=["input", "output", "loop"]),
    Q("A", 6, "Ap", "A running total starts at 0. Add 4, then 6, then 5. The total is ...", "b) 15", opts=["10", "15", "16"]),
    Q("A", 8, "U", "Which search is usually faster on a long list in order?", "b) halving search", opts=["one-by-one search", "halving search"]),
    Q("B", 2, "Ap", "Find 3/4 of 24, and 2/5 of 20.", "18 and 8", "1 mark for each"),
    Q("B", 3, "Ap", "The turtle faces North and turns 270° clockwise. Which way does it face now?", "West", "2 marks; 1 mark for a correct method"),
    Q("B", 5, "Ap", "Write >, < or =: (a) 2 km ___ 1,999 m (b) 4,000 m ___ 4 km", "(a) > (b) =", "1 mark for each"),
    Q("B", 6, "Ap", "In a picture graph one jug means 4 litres. How many litres do 3½ jugs show? How many jugs show 10 litres?", "14 litres; 2½ jugs",
      "1 mark for each"),
    Q("B", 7, "Ap", "The rule is dots = 4 x step - 1. How many dots are there in step 1, and in step 10?", "3 and 39", "1 mark for each"),
    Q("B", 4, "An", "A program says: set fuel to 30; fuel = fuel + 12; fuel = fuel - 20. What is fuel at the end? Which line is the refill?",
      "22; fuel = fuel + 12", "1 mark for each"),
    Q("C", 1, "An", "A 2-digit number has digits that add up to 5. Is each statement true, false or can't tell? (a) It is less than 60. (b) It is odd. (c) It has a 9 in it.",
      "The numbers can be 14, 23, 32, 41 or 50. (a) true (b) can't tell (c) false", "1 mark for each"),
    Q("C", 8, "An", "A secret number is from 1 to 100. It is 70. Write the first three guesses of a halving search, and which numbers are left after each.",
      "50: 51 to 100 left. 75: 51 to 74 left. 62: 63 to 74 left. (Other middles, such as 63, are fine.)", "1 mark for each guess with the numbers left"),
    Q("C", 7, "Ap", "Step 1 has 1 tile, step 2 has 4 tiles and step 3 has 9 tiles (squares of tiles). Write the rule. How many tiles in step 8? Which step has 100 tiles?",
      "tiles = step x step; 64; step 10", "1 mark for each"),
    Q("C", 5, "An", "Set nearest to 1,000 m. Check four shops: 450 m, 1 km 200 m, 380 m and 600 m. If a shop is nearer, update nearest. Write nearest after each check. Which shop is nearest?",
      "450, 450, 380, 380. The shop 380 m away.", "2 marks for the values (1 mark with one slip), 1 mark for the answer"),
    Q("D", 6, "Ap", "Five cows give 9, 11, 8, 12 and 10 litres of milk. A program keeps a running total and a counter.", "(a) 9, 20, 28, 40, 50 (b) 5 (c) 5 cups",
      "(a) 2 marks, 1 mark with one slip (b) 1 mark (c) 1 mark",
      parts=[("Write the running total after each cow.", 2), ("What does the counter show at the end?", 1),
             ("In a picture graph one cup = 10 litres. How many cups show the total?", 1)]),
    Q("D", 4, "Ap", "A school bus program uses a variable called children. It starts at 0. At stop 1, 12 children get on. At stop 2, 8 get on and 3 get off. At school, everyone gets off.",
      "(a) 12 (b) 17 (c) 0 (d) If children = 40 then say 'Bus full', else open the door.", "1 mark for each part",
      parts=[("What is children after stop 1?", 1), ("What is children after stop 2?", 1), ("What is children after school?", 1),
             ("The bus has 40 seats. Write an if-else rule the program could use at each stop.", 1)]),
]

ANNUAL = [
    Q("A", 9, "Ap", "A machine's rule is + 7. Input 15 gives ...", "b) 22", opts=["8", "22", "105"]),
    Q("A", 10, "Ap", "A design with 8 petals turns by how much after each petal?", "b) 45°", opts=["40°", "45°", "60°"]),
    Q("A", 11, "R", "Covering a floor with one repeating tile and no gaps is called ...", "a) tiling", opts=["tiling", "sorting", "timing"]),
    Q("A", 12, "R", "How many seconds are there in 2 minutes?", "c) 120", opts=["60", "100", "120"]),
    Q("A", 13, "Ap", "A frog starts at 0 and jumps 6 each time. Which spot does it land on?", "b) 30", opts=["16", "30", "40"]),
    Q("A", 14, "U", "A map scale says 1 square = 50 m. How far are 4 squares?", "b) 200 m", opts=["54 m", "200 m", "450 m"]),
    Q("A", 15, "R", "Which graph uses small pictures to show data?", "a) a picture graph", opts=["a picture graph", "a bar graph", "a number line"]),
    Q("A", 3, "Ap", "The turtle turns right 90° four times. Now it is ...", "a) facing the same way as at the start",
      opts=["facing the same way as at the start", "facing the opposite way"]),
    Q("B", 9, "An", "A machine turns 4 into 13 and 6 into 19. Find the rule.", "x 3, then + 1", "2 marks; 1 mark for a rule that fits one pair"),
    Q("B", 10, "U", "What is the order of rotational symmetry of a square? Of a triangle with equal sides?", "4 and 3", "1 mark for each"),
    Q("B", 11, "Ap", "A shape covers 9 whole squares and 6 half squares. What is its area?", "12 square units", "2 marks; 1 mark for 6 halves = 3"),
    Q("B", 12, "Ap", "Race times: Neha 1 minute 5 seconds, Om 58 seconds, Pia 62 seconds. Write all the times in seconds. Who won?", "65, 58, 62; Om won",
      "1 mark for the seconds, 1 mark for Om"),
    Q("B", 13, "Ap", "A 2-jumper and a 5-jumper start at 0. Where do they first land on the same spot? Where is the next one?", "10 and 20", "1 mark for each"),
    Q("B", 14, "Ap", "Start at C2. Go North 2, then East 3. Where are you now?", "F4", "2 marks; 1 mark for C4 after going North"),
    Q("C", 9, "An", "Machine A doubles a number (x 2). Machine B takes away 3 (- 3). (a) Put 10 through A, then B. (b) Put 10 through B, then A. (c) Does the order matter?",
      "(a) 17 (b) 14 (c) Yes, the outputs are different", "1 mark for each"),
    Q("C", 12, "An", "Set timer to 10. Repeat until timer = 0: say timer, then timer = timer - 3. Trace it. What is the bug? Fix it.",
      "It says 10, 7, 4, 1, -2, ... and never reaches exactly 0, so it never stops. Fix: repeat until timer < 1 (or take away 2, or start at 9).",
      "1 mark for the trace, 1 mark for the bug, 1 mark for a fix"),
    Q("C", 13, "An", "Set position to 0. Repeat until position > 40: position = position + 3; if position is a multiple of 5 then say 'Meet!'. At which positions does it say 'Meet!'?",
      "15 and 30", "1 mark for listing the landings, 1 mark for 15, 1 mark for 30"),
    Q("C", 11, "Ap", "A floor 6 squares long and 4 squares wide is covered with 2 x 2 tiles. Each tile has 1 red square and 3 white squares. How many tiles, red squares and white squares?",
      "6 tiles; 6 red; 18 white", "1 mark for each"),
    Q("D", 14, "Ap", "Robo starts on A1. The grey squares are walls.", "(a) D5 (b) For example East 3, North 4 (7 moves); any 7-move route that avoids A2 and B2 (c) 700 m",
      "(a) 1 mark (b) 2 marks: 1 for directions, 1 for avoiding the walls (c) 1 mark", fig=map_x,
      parts=[("Where is the treasure X?", 1), ("Write a shortest route from A1 to X with compass directions, avoiding the walls.", 2),
             ("1 square = 100 m. How far is your route?", 1)]),
    Q("D", 15, "An", "A treasure game scores: +10 for the treasure, +2 for each coin, -3 for each wall bump. Ana found the treasure, 3 coins and bumped 2 walls. "
      "Bo found the treasure and 1 coin, with no bumps.", "(a) 10 (b) 12 (c) Bo (d) Open answer, for example: a bump should cost less than a coin, "
      "or the winner is the fastest player.", "1 mark for each part",
      parts=[("What is Ana's score?", 1), ("What is Bo's score?", 1), ("Who wins?", 1), ("Suggest one change to make the scoring fairer, and say why.", 1)]),
]

PAPERS = [dict(key="half", name="Half-yearly examination", scope="chapters 1-8 (term 1)", questions=HALF),
          dict(key="annual", name="Annual examination", scope="all chapters, mostly chapters 9-15 (term 2)", questions=ANNUAL)]
