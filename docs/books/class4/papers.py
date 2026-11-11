"""Sample examination papers for 'Think Like a Coder - Class 4': half-yearly (term-1 chapters) and annual (whole year).
Each question: s (section), q (text), m (marks) or parts [(text, marks)], ch (chapter), lv (R, U, Ap, An), answer, guide."""
import figures_c4 as F


def Q(s, ch, lv, q, answer, guide="", m=None, **kw):
    if m is None and "parts" not in kw:
        m = {"A": 1, "B": 2, "C": 3, "D": 4}[s]
    return dict(s=s, ch=ch, lv=lv, q=q, m=m, answer=answer, guide=guide, **kw)


def mirror3():
    return F.mirror_grid({(0, 1), (2, 0), (3, 2)}, cell=20)


def travel_chart():
    return F.bar_chart([6, 10, 4, 8], ["Bus", "Walk", "Cycle", "Car"], w=300, unit=9)


def vehicle_tree():
    return F.decision_tree("Does it have wheels?", "bicycle", "Does it float?", "boat", "kite", w=380)


HALF = [
    Q("A", 1, "R", "How many edges does a cube have?", "c) 12", opts=["6", "8", "12"]),
    Q("A", 2, "U", "Rule: if it is sunny then wear a hat, else carry an umbrella. What do you do on a rainy day?", "b) carry an umbrella",
      opts=["wear a hat", "carry an umbrella"]),
    Q("A", 3, "Ap", "Which number is even?", "c) 58", opts=["35", "47", "58"]),
    Q("A", 3, "U", "Even + odd is always ...", "b) odd", opts=["even", "odd"]),
    Q("A", 4, "Ap", "6,000 + 400 + 9 = ...", "a) 6,409", opts=["6,409", "6,490", "64,009"]),
    Q("A", 5, "Ap", "One quarter of 16 is ...", "b) 4", opts=["2", "4", "8"]),
    Q("A", 6, "Ap", "250 cm = ...", "b) 2 m 50 cm", opts=["2 m 5 cm", "2 m 50 cm", "25 m"]),
    Q("A", 7, "R", "A fan can be ON or OFF. This is the fan's ...", "a) state", opts=["state", "shape", "size"]),
    Q("B", 1, "U", "How many faces, edges and corners does a matchbox (a cuboid) have?", "6 faces, 12 edges, 8 corners",
      "2 marks for all three; 1 mark for two"),
    Q("B", 2, "Ap", "Rule: if the number is even then add 10, else add 1. What comes out for 6, and for 9?", "16 and 10", "1 mark for each"),
    Q("B", 4, "Ap", "Using 3, 0, 7 and 5 once each, write the biggest and the smallest 4-digit numbers.", "7,530 and 3,057",
      "1 mark for each (0 cannot come first)"),
    Q("B", 5, "U", "A roti is cut into 4 pieces of different sizes. Is each piece a quarter? Why?", "No, because quarters must be 4 equal parts",
      "1 mark for no, 1 mark for the reason"),
    Q("B", 6, "Ap", "Robo faces right. It turns left, then turns left again. Which way does it face now?", "left", "2 marks; 1 mark for 'up' after the first turn"),
    Q("B", 7, "Ap", "A toggle light starts ON. You press it 5 times. Is it ON or OFF? Why?", "OFF, because an odd number of presses flips it",
      "1 mark for OFF, 1 mark for the reason"),
    Q("C", 3, "Ap", "Add one check coin to the end of each row so that every row has an even number of black coins. Row 1: black, white, black. "
      "Row 2: white, white, black. Row 3: black, black, black. Write the colour of each check coin.", "Row 1: white. Row 2: black. Row 3: black.",
      "1 mark for each row"),
    Q("C", 4, "Ap", "Sort 8, 3 and 5 with the sorting network (top two wires, then bottom two, then top two). Write the order after each comparator.",
      "After 1: 3, 8, 5. After 2: 3, 5, 8. After 3: 3, 5, 8.", "1 mark for each comparator"),
    Q("C", 6, "Ap", "Write a loop with turns that draws a square with sides of 5 steps. How many steps does Robo walk in all?",
      "Repeat 4 times: forward 5, turn right. 20 steps.", "2 marks for the loop, 1 mark for 20"),
    Q("C", 1, "An", "Write exact steps to draw a square with sides of 3 cm and both of its diagonals.",
      "1. Draw a line AB 3 cm long. 2. At A and at B draw lines 3 cm long, straight up. 3. Join the tops to finish the square. 4. Join each corner to the opposite corner.",
      "1 mark for exact lengths, 1 mark for the square, 1 mark for the diagonals"),
    Q("D", 2, "An", "A robot sorts things on a belt: if the thing is round then say 'R' and put it in basket R, else say 'L' and put it in basket L. "
      "The things are a ball, a pencil, a coin and a ruler.", "(a) basket R (b) the pencil and the ruler (c) R, L, R, L",
      "(a) 1 mark (b) 1 mark (c) 2 marks, 1 mark with one slip",
      parts=[("Where does the ball go?", 1), ("Which things go into basket L?", 1),
             ("The robot runs: repeat 4 times: pick the next thing, then use the rule. The things come in this order: coin, ruler, ball, pencil. What does it say?", 2)]),
    Q("D", 7, "An", "A school gate has a light. Green means open, red means closed. Button G makes it green, button R makes it red, and button T switches it "
      "to the other colour. The light starts red.", "(a) green (b) green (c) R: red; T: green; T: red; T: green. The gate ends open.",
      "(a) 1 mark (b) 1 mark (c) 2 marks for a full trace, 1 mark for two correct rows",
      parts=[("Press T. What colour is the light?", 1), ("Start again from red. Press T, T, G. What colour is it now?", 1),
             ("Start again from red. Make a trace table for R, T, T, T. Is the gate open or closed at the end?", 2)]),
]

ANNUAL = [
    Q("A", 8, "R", "Which unit measures how heavy a bag is?", "a) kilogram", opts=["kilogram", "litre", "metre"]),
    Q("A", 9, "Ap", "Outer loop: repeat 3 times. Inner loop: repeat 6 times: clap. How many claps?", "b) 18", opts=["9", "18", "36"]),
    Q("A", 10, "R", "In a clue table, a tick means ...", "a) it is true", opts=["it is true", "it is not possible", "not sure"]),
    Q("A", 11, "U", "Which shape has exactly one line of symmetry?", "a) a heart shape", opts=["a heart shape", "a circle", "a square"]),
    Q("A", 12, "Ap", "Start at 5:00. Repeat until the clock shows 7:00: add 30 minutes. How many times does the loop run?", "b) 4", opts=["2", "4", "6"]),
    Q("A", 13, "R", "In a decision tree, each answer takes you along a ...", "a) branch", opts=["branch", "loop", "clock"]),
    Q("A", 14, "Ap", "Two groups of five tally marks and three more marks show ...", "b) 13", opts=["8", "13", "23"]),
    Q("A", 6, "Ap", "1 m 5 cm = ... cm", "b) 105", opts=["15", "105", "150"]),
    Q("B", 8, "Ap", "Fill in: 2 kg 300 g = ___ g, and 3 L 50 mL = ___ mL.", "2,300 g; 3,050 mL", "1 mark for each"),
    Q("B", 9, "Ap", "Write a nested loop to plant 4 rows of 5 trees. How many trees are planted?", "Repeat 4 times: (repeat 5 times: plant a tree). 20 trees.",
      "1 mark for the nested loop, 1 mark for 20"),
    Q("B", 11, "Ap", "Write three capital letters that have a line of symmetry going straight down.",
      "For example A, H, M (also I, O, T, U, V, W, X, Y)", "2 marks for three correct letters; 1 mark for two"),
    Q("B", 12, "An", "Today is Saturday. What day was it 9 days ago?", "Thursday", "2 marks; 1 mark for seeing that 7 days ago was Saturday"),
    Q("B", 13, "Ap", "Write one yes/no question that separates a cow from a hen.", "For example: Does it have four legs?",
      "1 mark for a yes/no question, 1 mark if it separates them"),
    Q("B", 3, "Ap", "Is 47 + 38 odd or even? Explain without adding.", "Odd, because odd + even is always odd",
      "1 mark for odd, 1 mark for the reason"),
    Q("C", 10, "An", "Tara, Uday and Vani sit in seats 1, 2 and 3. Tara is not in seat 1. Uday is in seat 3. Who sits where?",
      "Vani: seat 1. Tara: seat 2. Uday: seat 3.", "1 mark for each person"),
    Q("C", 8, "An", "You have a 5 litre jug and a 2 litre jug. Write the steps to get exactly 1 litre.",
      "Fill the 5 L jug. Pour from it to fill the 2 L jug (3 L left). Empty the 2 L jug. Pour again from the 5 L jug to fill the 2 L jug. 1 L is left in the 5 L jug.",
      "3 marks for steps that work; 2 marks if one step is missing; 1 mark for a sensible start"),
    Q("C", 12, "Ap", "Write a repeat-until loop for saving ₹10 every week until you have ₹60. How many weeks does it take?",
      "Set savings to 0. Repeat until savings = 60: add 10. It takes 6 weeks.", "1 mark for the loop, 1 mark for the condition, 1 mark for 6"),
    Q("C", 11, "Ap", "The red dashed line is a mirror. Shaded squares are in columns A, B and C. In which column is the mirror partner of each one?",
      "A goes to F, B goes to E, C goes to D (each stays in its own row)", "1 mark for each", fig=mirror3, lines=2),
    Q("D", 14, "Ap", "The bar graph shows how the children of Class 4 come to school.", "(a) walking (b) 2 more (c) 28 (d) four tally marks: ||||",
      "1 mark for each part", fig=travel_chart,
      parts=[("Which way is the most common?", 1), ("How many more children walk than come by car?", 1), ("How many children are there in all?", 1),
             ("Draw the tally marks for the children who cycle.", 1)]),
    Q("D", 13, "An", "Look at this decision tree.", "(a) bicycle (b) The tree has only one leaf for things with wheels, so a car is called a bicycle. "
      "Add the question 'Does it have an engine?' after 'yes': yes, car; no, bicycle. (c) kite",
      "(a) 1 mark (b) 2 marks: 1 mark for the reason, 1 mark for a question that fixes it (c) 1 mark", fig=vehicle_tree,
      parts=[("Where does a car end up?", 1), ("Why is that wrong? What question would you add to fix the tree?", 2), ("Where does a kite end up?", 1)]),
]

PAPERS = [dict(key="half", name="Half-yearly examination", scope="chapters 1-7 (term 1)", questions=HALF),
          dict(key="annual", name="Annual examination", scope="all chapters, mostly chapters 8-14 (term 2)", questions=ANNUAL)]
