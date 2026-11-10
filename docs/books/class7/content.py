"""Content of 'Think Like a Coder - Class 7'. Original questions. CT chapters 1-8 follow the NCERT Class 7 maths textbook,
as CBSE's 2026-27 CT&AI Class 7 handbook does; AI chapters 1-4 follow the handbook's AI part; two 20-hour projects
cover the project hours (CBSE: 100 hours a year in Class 7 = 40 CT + 20 AI + 40 projects). Levels C4-C5."""
import figures_c7 as F

CH = []

# ------------------------------------------------------------------ Part 1: computational thinking (NCERT maths order)
CH.append(dict(
    n=1, title="Large Numbers Around Us", skill="Compare, round and estimate big numbers step by step", level="C4", color="#14A3A3",
    robo="To compare two big numbers I follow an algorithm: count the digits first, then compare from the left until two digits differ.",
    learn=["In the <b>Indian system</b> we group digits as lakhs and crores: 1 lakh = 1,00,000 and 1 crore = 1,00,00,000 = 100 lakh. "
           "In the <b>international system</b> we use thousands, millions and billions: 1 million = 10 lakh and 1 billion = 100 crore.",
           "Computers compare numbers with a fixed set of steps: the number with <b>more digits</b> is bigger; if they have the same number of digits, "
           "compare <b>from the left</b> until two digits differ. To <b>estimate</b>, round to a convenient place first."],
    words=[("lakh", "1,00,000"), ("crore", "1,00,00,000"), ("million", "10,00,000 (10 lakh)"), ("estimate", "a close, easy answer")],
    example=dict(title="Which is bigger: 4,56,78,912 or 45,678,921?",
                 steps=["Remove the commas: 45678912 and 45678921. Both have <b>8 digits</b>, so we compare from the left.",
                        "4 = 4, 5 = 5, 6 = 6, 7 = 7, 8 = 8, 9 = 9. The first difference is in the tens place: 1 against 2.",
                        "So <b>45,678,921</b> is bigger. Commas only help us read; Indian and international grouping show the same value."]),
    practice=[
        dict(q="How many lakhs make 1 crore?", boxes=1, answer="100"),
        dict(q="1 million is the same as ...", opts=["1 lakh", "10 lakh", "1 crore", "10 crore"], answer="b) 10 lakh"),
        dict(q="Using the digits 7, 0 and 3, each exactly twice, write the largest and the smallest 6-digit numbers.", boxes=2,
             answer="7,73,300 and 3,00,377 (a number cannot start with 0)"),
        dict(q="Round 4,86,72,315 to the nearest lakh.", boxes=1, answer="4,87,00,000"),
        dict(q="What is the product of all the digits on a phone keypad, 0 to 9?", opts=["362880", "3628800", "0", "45"],
             answer="c) 0: anything multiplied by 0 is 0"),
    ],
    build=dict(intro="An algorithm that compares two big numbers.",
               cards=[("Input numbers A and B", "event", "#E5484D"), ("If one has more digits", "if", "#8B5CF6"), ("say that one is bigger", "step", "#3B82F6"),
                      ("Repeat for each place from the left", "loop", "#F5A524"), ("If the digits differ, the bigger digit wins; stop", "if", "#8B5CF6")],
               task="Trace it for 9,87,654 and 10,02,003. Then for 45,67,890 and 45,69,001. In which place is the first difference?",
               answer="10,02,003 has 7 digits against 6, so it is bigger. 45,69,001 is bigger: the first difference is in the thousands place (7 against 9)"),
    challenge=dict(q="India's population is about 140 crore. Write this in digits, and in the international system.",
                   answer="1,40,00,00,000 = 1,400,000,000, which is 1.4 billion"),
    ican=["read lakhs, crores and millions", "compare big numbers step by step", "round and estimate"],
))

CH.append(dict(
    n=2, title="Arithmetic Expressions", skill="Order of operations and expression trees", level="C4", color="#F5A524",
    robo="A computer reads 8 + 6 x 3 as 8 + 18, not 14 x 3. Brackets first, then x and ÷, then + and -. I draw it as a tree!",
    learn=["An <b>expression</b> is a mix of numbers and operations, like 8 + 6 x (5 - 2). To get one answer everyone must use the same <b>order</b>: "
           "<b>brackets</b> first, then <b>x and ÷</b> from left to right, then <b>+ and -</b> from left to right.",
           "Computers store an expression as a <b>tree</b>: each operation joins two parts. They work it out from the bottom of the tree up, "
           "so the operation at the top is done last."],
    words=[("expression", "numbers joined by operations"), ("term", "a part added or subtracted"), ("brackets", "do this part first"), ("precedence", "which operation goes first")],
    example=dict(title="Work out 8 + 6 x (5 - 2)",
                 steps=["Brackets first: 5 - 2 = 3.", "Then multiply: 6 x 3 = 18.", "Then add: 8 + 18 = <b>26</b>. In the tree, the bottom operation (-) is done first and the top one (+) last."],
                 fig=lambda: F.expr_tree(("+", 8, ("×", 6, ("−", 5, 2))), w=260)),
    practice=[
        dict(q="Work out 20 - 4 x 3 and (20 - 4) x 3.", boxes=2, answer="8 and 48"),
        dict(q="Which operation in the box makes this true? 6 [ ? ] 4 + 10 = 34", opts=["+", "-", "x", "÷"], answer="c) x (6 x 4 + 10 = 34)"),
        dict(q="A bus has 40 seats and 23 passengers. At stop 1, 5 get off and 8 get on. At stop 2, 6 get off and 12 get on. How many seats are empty now?",
             boxes=1, answer="8 (23 - 5 + 8 - 6 + 12 = 32 passengers)"),
        dict(q="Where do brackets go to make 2 + 3 x 4 equal 20?", opts=["(2 + 3) x 4", "2 + (3 x 4)", "no brackets are needed"], answer="a) (2 + 3) x 4"),
        dict(q="What is the value of this expression tree?", fig=lambda: F.expr_tree(("×", ("+", 3, 5), ("−", 9, 4)), w=240), boxes=1, answer="40: (3 + 5) x (9 - 4)"),
    ],
    build=dict(intro="A program that adds up a shopping bill.",
               cards=[("Set total to 0", "step", "#3B82F6"), ("change total by 3 x 45", "step", "#3B82F6"), ("change total by 2 x 120", "step", "#3B82F6"),
                      ("change total by -50 (discount)", "step", "#3B82F6"), ("say total", "step", "#3B82F6")],
               task="What does it say? Write the whole bill as one expression.", answer="3 x 45 + 2 x 120 - 50 = 135 + 240 - 50 = 325"),
    challenge=dict(q="Use 2, 3, 4 and 5, each once, with any operations and brackets, to make 24.", answer="For example 4 x (5 + 3 - 2) = 24 or 2 x (3 + 4 + 5) = 24; accept any correct expression"),
    ican=["follow the order of operations", "use brackets to change the order", "read an expression tree"],
))

CH.append(dict(
    n=3, title="A Peek Beyond the Point", skill="Decimals, binary numbers and punched-card sorting", level="C4", color="#8B5CF6",
    robo="Our numbers use bundles of ten. Computers use bundles of two: 1, 2, 4, 8, 16. That is binary, written with only 0 and 1!",
    learn=["In our <b>decimal</b> system each place is worth 10 times the place to its right: ..., 100, 10, 1, and after the point 1/10, 1/100, .... "
           "So 3.47 means 3 ones, 4 tenths and 7 hundredths.",
           "Computers use the <b>binary</b> system, where place values are 1, 2, 4, 8, 16, .... Each <b>bit</b> is 0 or 1. "
           "23 = 16 + 4 + 2 + 1, so 23 is <b>10111</b> in binary. Five bits give 32 patterns, enough to give each of the 26 letters its own punched card."],
    words=[("decimal", "place values in tens"), ("binary", "place values in twos"), ("bit", "a binary digit, 0 or 1"), ("place value", "what a digit's position is worth")],
    example=dict(title="Writing 23 in binary with dot cards",
                 steps=["Start from the biggest card that fits: 16. That leaves 7.", "8 is too big, so the 8 card is face down: 0. Then 4 (leaves 3), 2 (leaves 1) and 1.",
                        "Face-up cards are 1s and face-down cards are 0s: 23 = <b>10111</b>."],
                 fig=lambda: F.binary_cards(23)),
    practice=[
        dict(q="What is 13 in binary?", opts=["1011", "1101", "1110", "1001"], answer="b) 1101 (8 + 4 + 1)"),
        dict(q="What is the binary number 10010 in decimal?", boxes=1, answer="18 (16 + 2)"),
        dict(q="Every student in a class of 40 needs a different binary number. How many bits are needed?", opts=["5", "6", "7", "8"],
             answer="b) 6: 5 bits give only 32 numbers, 6 bits give 64"),
        dict(q="Which is the smallest?", opts=["0.5", "0.45", "0.405"], answer="c) 0.405"),
        dict(q="Find the next term: 1.2, 2.4, 2.6, 5.2, 5.4, 10.8, ?", opts=["11.0", "21.6", "10.10", "11.8"], answer="a) 11.0 (alternately x 2 and + 0.2)"),
    ],
    build=dict(intro="An algorithm that turns a decimal number into binary by halving.",
               cards=[("Input n", "event", "#E5484D"), ("Repeat until n is 0", "loop", "#F5A524"), ("write down the remainder of n ÷ 2", "step", "#3B82F6"),
                      ("set n to n ÷ 2, dropping the remainder", "step", "#3B82F6"), ("read the remainders from last to first", "step", "#3B82F6")],
               task="Trace it for 14. Write each value of n and each remainder. What binary number do you get?",
               answer="14: remainder 0, n = 7; remainder 1, n = 3; remainder 1, n = 1; remainder 1, n = 0. Read backwards: 1110"),
    challenge=dict(q="Letters are numbered A = 1 to Z = 26 and written in 5-bit binary (J = 10 = 01010). Which letter is 10011? Write the 5 bits for R.",
                   answer="10011 = 19 = S; R = 18 = 10010"),
    ican=["read decimal place values", "change numbers between binary and decimal", "explain how 5 bits can label 26 letters"],
))

CH.append(dict(
    n=4, title="Expressions using Letter-Numbers", skill="Variables and formulas for growing patterns", level="C4", color="#2BB673",
    robo="A letter-number is a variable: a name for a number that can change. Write the rule once, then put in any number!",
    learn=["A <b>letter-number</b> (a variable) stands for a number. A <b>formula</b> uses letters to give a rule that works every time: "
           "the perimeter of a square with side s is <b>4s</b>.",
           "To use a formula, <b>substitute</b>: put the number in place of the letter. Programs do the same: <i>set sticks to 3 x n + 1</i> works for any n. "
           "Terms with the same letter are <b>like terms</b> and can be added: 3x + 2x = 5x."],
    words=[("variable", "a letter that stands for a number"), ("formula", "a rule written with letters"), ("substitute", "put a number in place of a letter"), ("like terms", "terms with the same letter")],
    example=dict(title="Matchstick squares in a row",
                 steps=["1 square needs 4 sticks, 2 squares need 7 and 3 squares need 10. Each new square adds <b>3</b> sticks.",
                        "So n squares need <b>3n + 1</b> sticks: 3 for each square, plus 1 for the very first side.",
                        "Substitute n = 20: 3 x 20 + 1 = <b>61</b> sticks, without drawing them."],
                 fig=lambda: F.matchstick_row((1, 2, 3))),
    practice=[
        dict(q="If a = 4 and b = 3, what is 5a - 2b?", boxes=1, answer="14 (20 - 6)"),
        dict(q="Simplify 3x + 5 + 2x - 1.", opts=["5x + 4", "6x + 4", "5x + 6", "10x"], answer="a) 5x + 4"),
        dict(q="A + B = Z, where B = 3 x A, B is more than 6 and Z is less than 13. All are whole numbers. What is A?", opts=["1", "2", "3", "4"],
             answer="c) 3 (B = 9, Z = 12)"),
        dict(q="Each block is the sum of the two blocks below it. What is P?", fig=lambda: F.pyramid([["23"], ["", ""], ["3", "P", "4"]]), boxes=1,
             answer="8: the middle row is 3 + P and P + 4, so 2P + 7 = 23"),
        dict(q="A pen costs Rs p and a notebook costs 3 times as much. Riya buys 2 pens and 4 notebooks. Which expression gives the total?",
             opts=["14p", "6p", "9p", "2p + 4"], answer="a) 14p (2p + 12p)"),
    ],
    build=dict(intro="A program that uses the matchstick formula.",
               cards=[("Input n (number of squares)", "event", "#E5484D"), ("set sticks to 3 x n + 1", "step", "#3B82F6"), ("If sticks &gt; 50", "if", "#8B5CF6"),
                      ("say 'Buy another box'", "step", "#3B82F6"), ("say sticks", "step", "#3B82F6")],
               task="Run it for n = 10 and for n = 17. What does it say each time?", answer="n = 10: 31 sticks. n = 17: 52 sticks, and it says 'Buy another box'"),
    challenge=dict(q="Triangles in a row: 1 triangle needs 3 sticks, 2 need 5, 3 need 7. Write the formula. How many sticks for 25 triangles?",
                   answer="2n + 1; 51 sticks"),
    ican=["use letters for numbers", "substitute values into a formula", "write a formula for a growing pattern"],
))

CH.append(dict(
    n=5, title="Parallel and Intersecting Lines", skill="Angle rules and tracing drawing programs", level="C5", color="#3B82F6",
    robo="Two lines drawn with the same heading never meet: they are parallel. When lines cross, I use angle rules instead of measuring!",
    learn=["<b>Parallel</b> lines never meet. When two lines <b>intersect</b>, <b>vertically opposite</b> angles are equal, and angles next to each other "
           "on a straight line add up to <b>180°</b>.",
           "A line that crosses two parallel lines is a <b>transversal</b>: it makes 8 angles, and they come in just two sizes that add up to 180°. "
           "In a drawing program, lines drawn with the same heading are parallel, so you can check a program by tracing the heading after each turn."],
    words=[("parallel", "never meet"), ("intersect", "cross at a point"), ("vertically opposite", "equal angles across a crossing"), ("transversal", "a line crossing two lines")],
    example=dict(title="Two lines cross, and one angle is 65°",
                 steps=["The angle next to it on the straight line is 180° - 65° = <b>115°</b>.",
                        "Vertically opposite angles are equal, so the other two angles are <b>65°</b> and <b>115°</b>.",
                        "Check: 65 + 115 + 65 + 115 = 360°, a full turn."],
                 fig=lambda: F.cross_angles(65)),
    practice=[
        dict(q="Two angles on a straight line: one is 72°. What is the other?", boxes=1, answer="108°"),
        dict(q="Vertically opposite angles are (3x + 10)° and (5x - 30)°. Find x and the size of each angle.", boxes=2, answer="x = 20; each angle is 70°"),
        dict(q="At which times is the minute hand on 12 and the hour hand perpendicular to it?", opts=["3:00 and 9:00", "6:00 only", "12:00 and 6:00", "3:00 only"],
             answer="a) 3:00 and 9:00"),
        dict(q="A turtle program: <i>forward 50, turn right 90°, forward 30, turn right 90°, forward 50.</i> How are the first and last lines related?",
             opts=["parallel", "perpendicular", "they meet"], answer="a) parallel (the heading has turned 180°)"),
        dict(q="Each side of a square is divided into 4 equal parts, and lines parallel to the sides join the marks. How many squares of all sizes are there?",
             opts=["16", "25", "30", "32"], answer="c) 30 (16 + 9 + 4 + 1)"),
    ],
    build=dict(intro="Trace this drawing program on dotted paper.",
               cards=[("Repeat 3 times", "loop", "#F5A524"), ("forward 60", "step", "#3B82F6"), ("turn right 120°", "step", "#3B82F6")],
               task="What shape does it draw? Then write a program for a rhombus with sides of 60 whose opposite sides are parallel.", drawspace=True,
               answer="An equilateral triangle. Rhombus: repeat 2 times: forward 60, turn right 60°, forward 60, turn right 120°"),
    challenge=dict(q="A transversal crosses two parallel lines. One of the 8 angles is 50°. How many angles are 50°, and what are the others?",
                   answer="4 angles are 50° and the other 4 are 130°"),
    ican=["use vertically opposite and straight-line angles", "spot parallel lines in a drawing program", "find angles made by a transversal"],
))

CH.append(dict(
    n=6, title="Number Play", skill="True or false: list every case and filter with clues", level="C5", color="#E5484D",
    robo="With 3 lights there are only 8 ON/OFF cards. Each clue throws away the cards that break it, until one card is left. That's how computers reason!",
    learn=["Each light is either ON or OFF: <b>true</b> or <b>false</b>. With 3 lights there are 2 x 2 x 2 = <b>8</b> possible cards; with 5 lights, 32. "
           "On a punched card a notch means ON and a hole means OFF.",
           "To solve a logic puzzle, start with <b>every case</b>, then <b>filter</b>: each clue removes the cards that break it. A computer does exactly this, very fast. "
           "Some number facts are true for <b>every</b> case, and we can explain why, like 'a 2-digit number minus its reverse is always a multiple of 9'."],
    words=[("true or false", "the two values in logic"), ("case", "one possible combination"), ("filter", "remove cases that break a rule"), ("truth table", "a list of every case")],
    example=dict(title="Three lights R, G and B: which are ON?",
                 steps=["Clue 1: <i>Red is ON.</i> Keep the 4 cards that start with U.", "Clue 2: <i>Blue is OFF.</i> Keep UOO and UUO.",
                        "Clue 3: <i>Exactly two lights are ON.</i> Only <b>UUO</b> is left: Red and Green are ON, Blue is OFF."],
                 fig=lambda: F.punch_cards(["OOO", "OOU", "OUO", "OUU", "UOO", "UOU", "UUO", "UUU"], keep=["UUO"], w=56)),
    practice=[
        dict(q="How many ON/OFF combinations are there for 4 lights?", boxes=1, answer="16"),
        dict(q="With the 8 cards for R, G and B, the clue is <i>Green is OFF</i>. How many cards are left?", opts=["2", "4", "6", "8"], answer="b) 4"),
        dict(q="Clues: <i>Red is ON</i> and <i>all lights are the same</i>. Which card is left?", opts=["all ON", "all OFF", "only Red ON"], answer="a) all ON (UUU)"),
        dict(q="A 2-digit number with different digits minus its reverse is always a multiple of ...", opts=["2", "5", "9", "10"],
             answer="c) 9, because (10a + b) - (10b + a) = 9(a - b)"),
        dict(q="A 4-digit number has two even and two odd digits. Can its digit sum be odd?", opts=["yes", "no, it is always even"],
             answer="b) no: two odd digits make an even sum, and even digits keep it even"),
    ],
    build=dict(intro="A computer can solve a number puzzle by checking every case.",
               cards=[("Repeat for every number from 10 to 99", "loop", "#F5A524"), ("If its digits add up to 11", "if", "#8B5CF6"),
                      ("If it is 27 more than its reverse", "if", "#8B5CF6"), ("say the number", "step", "#3B82F6")],
               task="Which numbers does the program say? Find them without checking all 90 numbers.",
               answer="Only 74: 9 x (a - b) = 27 means a - b = 3, and a + b = 11, so a = 7 and b = 4 (74 - 47 = 27)"),
    challenge=dict(q="With 5 lights (Y, P, R, G, B), how many cards are in the full deck? Clues: Y is ON, P is OFF, exactly 3 lights are ON. How many cards are left?",
                   answer="32 cards; 3 are left (Y on, P off, and two of R, G and B on)"),
    ican=["list all true/false combinations", "use clues to filter cases", "explain why a rule is always true"],
))

CH.append(dict(
    n=7, title="A Tale of Three Intersecting Lines", skill="Triangle rules as checks; debugging a function", level="C5", color="#EC4899",
    robo="Not any three sticks make a triangle! My is_triangle() check has to test all three sides, or it has a bug.",
    learn=["Three lengths make a triangle only if <b>each side is shorter than the other two added together</b> (the <b>triangle inequality</b>). "
           "The three angles of a triangle always add up to <b>180°</b>.",
           "Triangles are named by sides (<b>equilateral</b>: 3 equal, <b>isosceles</b>: 2 equal, <b>scalene</b>: none equal) and by angles (acute, right, obtuse). "
           "A program that checks inputs must test <b>every</b> condition; testing only one is a common bug."],
    words=[("triangle inequality", "each side &lt; sum of the other two"), ("equilateral", "all sides equal"), ("isosceles", "two sides equal"), ("scalene", "no sides equal")],
    example=dict(title="Can these lengths make a triangle?",
                 steps=["3 cm, 4 cm, 8 cm: 3 + 4 = 7, which is less than 8, so the two short sides cannot meet. <b>No triangle.</b>",
                        "5 cm, 6 cm, 8 cm: 5 + 6 = 11 &gt; 8, 5 + 8 &gt; 6 and 6 + 8 &gt; 5. <b>A scalene triangle.</b>",
                        "Shortcut: if the two shortest sides add up to more than the longest, it works."]),
    practice=[
        dict(q="Which set of lengths can form a triangle?", opts=["2, 3, 6", "4, 4, 9", "5, 7, 10", "1, 2, 3"], answer="c) 5, 7, 10"),
        dict(q="Two angles of a triangle are 48° and 67°. What is the third?", boxes=1, answer="65°"),
        dict(q="A triangle has angles of 30°, 60° and 90°. What kind is it?", opts=["acute", "right-angled", "obtuse"], answer="b) right-angled"),
        dict(q="An isosceles triangle has a perimeter of 20 cm, whole-number sides, and its two equal sides are even numbers. How many such triangles are there?",
             opts=["1", "2", "3", "4"], answer="b) 2: 6, 6, 8 and 8, 8, 4 (4, 4, 12 and 2, 2, 16 break the triangle inequality)"),
        dict(q="An equilateral triangle and a square both have sides of 4 cm. Which has the bigger area?", opts=["the square", "the triangle", "the same"],
             answer="a) the square (16 cm², the triangle is about 6.9 cm²)"),
    ],
    build=dict(intro="This function is meant to check whether three lengths make a triangle.",
               cards=[("Define is_triangle(a, b, c)", "step", "#14A3A3"), ("If a + b &gt; c", "if", "#8B5CF6"), ("give back 'yes'", "step", "#14A3A3"),
                      ("else", "if", "#8B5CF6"), ("give back 'no'", "step", "#14A3A3")],
               task="Test it with 2, 10, 3. What does it give back, and what is the right answer? Fix the bug.",
               answer="It says 'yes' (2 + 10 &gt; 3), but 2 + 3 &lt; 10, so it is not a triangle. Fix: If a + b &gt; c AND b + c &gt; a AND a + c &gt; b"),
    challenge=dict(q="How many different triangles with whole-number sides have a perimeter of 12 cm?", answer="3: (2, 5, 5), (3, 4, 5) and (4, 4, 4)"),
    ican=["test the triangle inequality", "use the angle sum of 180°", "debug a checking function"],
))

CH.append(dict(
    n=8, title="Working with Fractions", skill="Fraction operations and working backwards", level="C4", color="#14A3A3",
    robo="To undo a program, I do the opposite steps in the opposite order. 'Take away a third' is undone by 'divide by 2/3'!",
    learn=["'Of' means multiply: 3/4 of 48 = 3/4 x 48 = 36. To multiply fractions, multiply tops and bottoms. To divide by a fraction, "
           "multiply by its <b>reciprocal</b>: 6 ÷ 3/4 = 6 x 4/3 = 8.",
           "Many puzzles give the end and ask for the start. <b>Work backwards</b>: undo each step with its <b>inverse</b> (add undoes subtract, "
           "÷ undoes x), starting from the last step."],
    words=[("of", "means multiply"), ("reciprocal", "the fraction turned upside down"), ("inverse", "the step that undoes another"), ("work backwards", "start from the end")],
    example=dict(title="Meera's sweets",
                 steps=["Meera keeps 1/3 of her sweets, gives 1/4 of the rest to her sister, and gives the remaining 18 to her brother. How many did she have?",
                        "The brother got 3/4 of the rest, so the rest was 18 ÷ 3/4 = <b>24</b>.",
                        "The rest was 2/3 of the total, so the total was 24 ÷ 2/3 = <b>36</b>. Check: she keeps 12, her sister gets 6 and her brother 18."]),
    practice=[
        dict(q="What is 3/4 of 48?", boxes=1, answer="36"),
        dict(q="Work out 2/3 x 9/10.", opts=["3/5", "11/13", "18/13", "2/5"], answer="a) 3/5 (18/30)"),
        dict(q="On a bus, 1/4 of the passengers get off at stop A, then 20 get on. At stop B, half get off. 40 are left. How many were on the bus at the start?",
             boxes=1, answer="80: before B there were 80; before the 20 got on, 60; that is 3/4 of the start"),
        dict(q="Work out 6 ÷ 3/4.", opts=["8", "4.5", "2", "18"], answer="a) 8"),
        dict(q="Half of a field grows wheat. 2/5 of the wheat part is watered today. What fraction of the whole field is watered?", boxes=1, answer="1/5"),
    ],
    build=dict(intro="A fraction function used inside a program.",
               cards=[("Define of(f, n)", "step", "#14A3A3"), ("give back f x n", "step", "#14A3A3"), ("Set money to 600", "step", "#3B82F6"),
                      ("change money by - of(1/3, money)", "step", "#3B82F6"), ("change money by - of(1/4, money)", "step", "#3B82F6"), ("say money", "step", "#3B82F6")],
               task="Trace it. What is money after each step, and what does the program say?", answer="600, then 600 - 200 = 400, then 400 - 100 = 300: it says 300"),
    challenge=dict(q="Write the 'undo' program: start from 300 and get back to 600.",
                   answer="Set money to 300; divide money by 3/4 (400); divide money by 2/3 (600). Undo the last step first"),
    ican=["find a fraction of a quantity", "multiply and divide fractions", "work backwards to find a start value"],
))

# ------------------------------------------------------------------ Part 2: artificial intelligence (CBSE handbook AI chapters)
AI = dict(level="C5", skill_prefix="AI skill: ")


def ai(k, **kw):
    d = dict(AI, n=8 + k, badge=f"AI{k}", kicker=f"AI CHAPTER {k}", short=f"AI {k}",
             source=f"Goes with the AI part of CBSE's Class 7 CT&AI handbook, chapter {k}")
    d.update(kw)
    d["toc"] = f"AI {k}. {d['title']}"
    d["header"] = f"AI chapter {k}  ·  {d['title']}"
    return d


CH.append(ai(
    1, title="AI Domains and Applications", skill="Classify, predict a number, or find groups", color="#8B5CF6",
    robo="AI has three big areas: numbers and tables, pictures, and language. And three ways to predict: classify, regress and cluster!",
    learn=["AI works in three main <b>domains</b>: <b>Data Science</b> (numbers and tables), <b>Computer Vision</b> (images and video) and "
           "<b>Natural Language Processing</b> (text and speech). Each learns patterns from a <b>dataset</b>.",
           "<b>Classification</b> puts things into labelled groups (spam or not spam). <b>Regression</b> predicts a number (tomorrow's temperature). "
           "<b>Clustering</b> finds groups in data that has no labels. A dataset is split into <b>training</b>, <b>validation</b> and <b>test</b> parts, "
           "so the model is checked on data it has never seen."],
    words=[("classification", "sort into labelled groups"), ("regression", "predict a number"), ("clustering", "find groups without labels"), ("dataset", "the data a model learns from")],
    example=dict(title="Predicting a number from a small dataset (regression)",
                 steps=["Hours of practice and test marks for one student: 1 hour: 52, 2 hours: 58, 3 hours: 64, 4 hours: 70.",
                        "The pattern: each extra hour adds about <b>6</b> marks.", "Prediction for 5 hours: about 70 + 6 = <b>76</b>. It is a prediction, not a promise: real data is rarely this neat."],
                 table=[["Hours", "Marks", "Change"], ["1", "52", ""], ["2", "58", "+6"], ["3", "64", "+6"], ["4", "70", "+6"], ["5", "?", "predict 76"]]),
    practice=[
        dict(q="Which technique predicts a number, like tomorrow's temperature?", opts=["classification", "regression", "clustering"], answer="b) regression"),
        dict(q="A photo app groups pictures of the same face without being told any names. This is ...", opts=["classification", "regression", "clustering"], answer="c) clustering"),
        dict(q="An app reads car number plates from camera pictures. Which domain is this?", opts=["Data Science", "Computer Vision", "NLP"], answer="b) Computer Vision"),
        dict(q="500 images are split into 70% training, 15% validation and 15% test. How many test images are there?", boxes=1, answer="75"),
        dict(q="A chatbot answers questions typed in Hindi. Which domain is this?", opts=["Data Science", "Computer Vision", "NLP"], answer="c) NLP"),
    ],
    build=dict(intro="Be a clustering algorithm. Each dot is a fruit, placed by its size and sweetness. There are no labels.",
               fig=lambda: F.scatter([(1.5, 9), (2, 8.5), (1, 9.5), (2.5, 8), (1.8, 8.8), (8, 5), (9, 4.5), (7, 6), (9.5, 5.5)],
                                     "size (cm)", "sweetness (1-10)", w=320, h=160, xmax=10, ymax=10),
               cards=[("Look for points that sit close together", "step", "#3B82F6"), ("Repeat until every point is in a group", "loop", "#F5A524"),
                      ("put the point with its nearest group", "step", "#3B82F6"), ("Name each group by what its points share", "step", "#3B82F6")],
               task="Circle the groups you find. How many are there, and what could each group be?",
               answer="Two groups: small, very sweet fruit (like grapes or berries) and big, less sweet fruit (like apples or guavas). Clustering finds them without labels"),
    challenge=dict(q="Give one example from your school of classification, one of regression and one of clustering.",
                   answer="Open answer, for example: sorting library books by subject (classification); predicting lunch numbers (regression); grouping students by favourite clubs (clustering)"),
    ican=["name three AI domains", "tell classification, regression and clustering apart", "explain training, validation and test data"],
))

CH.append(ai(
    2, title="AI in Industries", skill="AI in health, education, transport and communication", color="#2BB673",
    robo="AI helps doctors, teachers, drivers and translators. But it helps people decide; it doesn't take the blame or the responsibility!",
    learn=["In <b>healthcare</b>, AI helps read X-rays and scans and spot illness early. In <b>education</b>, it gives personalised practice and instant feedback. "
           "In <b>transport</b>, it times traffic lights and finds faster routes. In <b>communication</b>, it translates, cleans up noisy audio and blocks spam.",
           "AI is useful because it handles huge amounts of data quickly. But it can make mistakes, so people stay <b>responsible</b>: "
           "a doctor checks a diagnosis, and personal data must be kept safe."],
    words=[("diagnosis", "finding out what illness it is"), ("personalised", "made for one person"), ("route planning", "choosing the best way"), ("translation", "changing one language to another")],
    example=dict(title="How a route app chooses",
                 steps=["It collects live data: how fast phones on each road are moving.", "It predicts the travel time for each route, not just the distance.",
                        "It picks the shortest <b>time</b>, Route B here, and re-plans if there is an accident."],
                 table=[["Route", "Distance", "Predicted time"], ["A", "12 km", "35 min"], ["B", "15 km", "28 min"], ["C", "10 km", "40 min"]]),
    practice=[
        dict(q="Analysing MRI scans helps which field?", opts=["healthcare", "education", "transport", "communication"], answer="a) healthcare"),
        dict(q="Giving instant feedback on a quiz is AI in ...", opts=["healthcare", "education", "transport", "communication"], answer="b) education"),
        dict(q="Changing traffic-light timing using camera counts of cars is AI in ...", opts=["healthcare", "education", "transport", "communication"], answer="c) transport"),
        dict(q="Using the route table in the example, which route would the app choose if it wanted the shortest <b>distance</b>?", opts=["A", "B", "C"], answer="c) C (10 km), even though it is the slowest"),
        dict(q="Why should a doctor check an AI's diagnosis?", opts=["AI can make mistakes and the doctor is responsible", "AI is always wrong", "to make it slower"],
             answer="a) AI can make mistakes, and the doctor is responsible for the patient"),
    ],
    build=dict(intro="Rules for a smart traffic light at a crossing of two roads.",
               cards=[("Count the cars waiting on each road", "step", "#3B82F6"), ("If one road has more than 20 cars waiting", "if", "#8B5CF6"),
                      ("give that road a longer green light", "step", "#3B82F6"), ("else", "if", "#8B5CF6"), ("use the normal timing", "step", "#3B82F6"),
                      ("If an ambulance is detected", "if", "#8B5CF6"), ("turn its road green at once", "step", "#3B82F6")],
               task="Road 1 has 25 cars and road 2 has 8. What happens? Then an ambulance arrives on road 2. What happens now?",
               answer="Road 1 gets a longer green light; when the ambulance is detected, road 2 turns green at once"),
    challenge=dict(q="Which check should come first in the program: the ambulance or the car count? Why?",
                   answer="The ambulance check, because an emergency must win over any queue; checked last, the car rule could delay it"),
    ican=["give examples of AI in four industries", "explain how a route app decides", "say why humans stay responsible"],
))

CH.append(ai(
    3, title="Data Visualisation and Analysis", skill="Choose bar, line or pie charts and read them honestly", color="#F5A524",
    robo="A bar chart compares, a line graph shows change over time, and a pie chart shows parts of a whole. Pick the right one!",
    learn=["<b>Structured data</b> fits in rows and columns, like a marks table; <b>unstructured data</b> does not, like photos or voice messages. "
           "We collect data by observation, surveys, measurement and digital devices, and store it in databases, spreadsheets or CSV files.",
           "Charts make patterns easy to see: <b>bar charts</b> compare groups, <b>line graphs</b> show change over time, and <b>pie charts</b> show parts of a whole "
           "(each slice's angle = its share of 360°). Good data is <b>accurate</b> (close to the true value) and <b>precise</b> (exact), and an honest chart does not exaggerate."],
    words=[("structured data", "data in rows and columns"), ("line graph", "shows change over time"), ("pie chart", "shows parts of a whole"), ("accuracy", "closeness to the true value")],
    example=dict(title="How 40 students travel to school",
                 steps=["Bus 20, walk 10, car 6, cycle 4. Total 40.", "Each slice's angle = count ÷ 40 x 360°: bus 20 ÷ 40 x 360 = <b>180°</b>, walk 90°, car 54° and cycle 36°.",
                        "Check: 180 + 90 + 54 + 36 = 360°. Half the class comes by bus."],
                 fig=lambda: F.pie_chart([20, 10, 6, 4], ["Bus", "Walk", "Car", "Cycle"], size=130)),
    practice=[
        dict(q="Which chart is best for showing a student's marks over six months?", opts=["pie chart", "line graph", "bar chart"], answer="b) line graph"),
        dict(q="Which chart is best for showing how a day's 24 hours are spent?", opts=["pie chart", "line graph", "scatter plot"], answer="a) pie chart"),
        dict(q="In a pie chart of 60 students, 15 chose cricket. What angle is the cricket slice?", boxes=1, answer="90° (15/60 x 360)"),
        dict(q="A scale always shows 50.12 kg for a bag that really weighs 48 kg. The scale is ...",
             opts=["precise but not accurate", "accurate but not precise", "both", "neither"], answer="a) precise but not accurate"),
        dict(q="Which of these is structured data?", opts=["a table of marks", "a video", "a voice message", "a photo"], answer="a) a table of marks"),
    ],
    build=dict(intro="A shop's ice-cream sales from Monday to Sunday: 12, 15, 14, 20, 26, 40, 38.",
               cards=[("Choose the chart type", "step", "#3B82F6"), ("Draw the axes and choose a scale", "step", "#3B82F6"), ("Plot each value", "step", "#3B82F6"),
                      ("Join the points", "step", "#3B82F6"), ("Write the trend in one sentence", "step", "#3B82F6")],
               task="Draw the chart in the space and write the trend.", drawspace=True,
               answer="A line graph. Sales rise through the week and are highest at the weekend (40 on Saturday)"),
    challenge=dict(q="A bar chart's axis starts at 90 instead of 0, so a score of 92 looks twice as tall as 91. Why is this misleading, and how would you fix it?",
                   answer="The bar heights no longer show the real values; start the axis at 0, or clearly mark the break in the axis"),
    ican=["choose the right chart", "work out pie chart angles", "read a trend and check that a chart is honest"],
))

CH.append(ai(
    4, title="Ethics and AI Bias Awareness", skill="Spot bias in data and keep humans in charge", color="#E5484D",
    robo="I learn only from the examples people give me. If the examples are lopsided, my answers will be lopsided too!",
    learn=["<b>AI ethics</b> means making sure AI is fair, open about how it decides, safe and respectful of privacy. <b>Bias</b> is an unfair preference "
           "for or against someone. Machines do not invent bias: it usually comes from the <b>data</b>.",
           "<b>Data bias</b>: some groups are missing or rare in the training data. <b>Historical bias</b>: the data repeats past unfair decisions. "
           "<b>Measurement bias</b>: the wrong thing is measured. For important decisions, a <b>human in the loop</b> must check and take responsibility."],
    words=[("bias", "an unfair preference"), ("fairness", "works equally well for everyone"), ("transparency", "being open about how it decides"), ("human in the loop", "a person checks the decision")],
    example=dict(title="The lopsided deck",
                 steps=["A classifier learns 'fruit or vegetable' from 18 fruit cards and only 2 vegetable cards.",
                        "It learns that almost everything is a fruit. On a test of 50 fruits and 10 vegetables it gets 45 fruits but only 3 vegetables right.",
                        "Overall it is 48 of 60 = 80% right, which looks good, but it is only <b>30%</b> right for vegetables. Fix: add vegetable examples and check each group."],
                 table=[["Group", "Training cards", "Right in the test"], ["Fruit", "18", "45 of 50 (90%)"], ["Vegetable", "2", "3 of 10 (30%)"]], widths=[110, 120, 170]),
    practice=[
        dict(q="A hiring system learnt from past decisions in which mostly men were hired, and now prefers men. This is ...", opts=["data bias", "historical bias", "measurement bias"], answer="b) historical bias"),
        dict(q="A face recogniser trained mostly on one group of people often fails for others. This is ...", opts=["data bias", "historical bias", "measurement bias"], answer="a) data bias"),
        dict(q="A health AI judges how ill people are from how much money they spent on treatment. This is ...", opts=["data bias", "historical bias", "measurement bias"],
             answer="c) measurement bias: spending is not the same as illness"),
        dict(q="An AI rejects a loan application. What should happen next?", opts=["a person should review the decision", "nothing: the AI is always right", "the applicant should never apply again"],
             answer="a) a person should review it, because important decisions need a human in the loop"),
        dict(q="Before sharing a shocking news post about a classmate, you should ...", opts=["check it with a trusted source, and not share hurtful posts", "share it quickly", "add your own comments"],
             answer="a) check it, and never share posts that hurt someone"),
    ],
    build=dict(intro="A fairness check you can run on any classifier.",
               cards=[("Count each group in the training data", "step", "#3B82F6"), ("If one group is much smaller", "if", "#8B5CF6"),
                      ("add more examples of that group", "step", "#3B82F6"), ("Test on a balanced test set", "step", "#3B82F6"), ("Compare accuracy for each group", "step", "#3B82F6")],
               task="After adding 16 vegetable cards, the classifier gets 46 of 50 fruits and 9 of 10 vegetables right. Work out the accuracy for each group and overall. Is it fairer?",
               answer="Fruit 92%, vegetable 90%, overall 55 of 60 (about 92%). Yes: both groups are now about equally accurate"),
    challenge=dict(q="Write two rules a school should follow before using AI to help choose students for a competition.",
                   answer="Open answer, for example: a teacher makes the final decision; check that the AI works equally well for every group; explain to students how it was used"),
    ican=["explain three kinds of bias", "check accuracy for each group", "say why humans must review important decisions"],
))

# ------------------------------------------------------------------ Projects (2 x 20 hours)
PROJECTS = []


def project(k, **kw):
    d = dict(n=100 + k, badge=f"P{k}", kicker=f"PROJECT {k}  ·  20 HOURS", short=f"Project {k}", level="C5", skill_prefix="Project skill: ",
             source="CBSE: 40 project hours a year in Class 7, as two projects of 20 hours")
    d.update(kw)
    d["toc"] = f"Project {k}. {d['title']}"
    d["header"] = f"Project {k}  ·  {d['title']}"
    return d


PROJECTS.append(project(
    1, title="Nutri-Quest Food Planner", skill="Use data and rules to plan a balanced week", color="#2BB673",
    question="Can we use nutrition data and simple rules to plan a balanced, affordable week of school lunches?",
    brief=["Your team collects data for 12 common foods: food group, protein, energy and cost per serving, from food packets or the Indian Food Composition "
           "Tables of ICMR-NIN, with your teacher's help.",
           "Then write rules, for example: <i>every lunch has a grain, a protein food and a vegetable; no dish more than twice a week; each lunch costs at most Rs 40.</i> "
           "Plan Monday to Friday, check every day against every rule, fix what breaks, improve the plan and present it with charts."],
    words=[("nutrient", "what food gives the body"), ("constraint", "a rule a plan must follow"), ("budget", "the most you can spend"), ("balanced", "has every food group")],
    robo="A planner is an algorithm with rules. Check every rule for every day, and fix the plan until nothing breaks!",
    plan=[("1", "Define", "Agree the question and the food groups. Decide what data to collect for each food."),
          ("2", "Collect", "Record food group, protein, energy and cost per serving for 12 foods. Write each source."),
          ("3", "Organise", "Make one table of all the foods. Check for missing or odd values."),
          ("4", "Write rules", "Write 3 to 5 rules as 'every lunch must ...' or 'if ... then ...'."),
          ("5", "Build", "Make a first plan for Monday to Friday."),
          ("6", "Check", "Check each day against each rule in a table. Fix every broken rule."),
          ("7", "Improve", "Make version 2: cheaper, more protein or more variety. Compare the two versions."),
          ("8", "Show", "Draw a bar chart of protein per day and a pie chart of cost by food group."),
          ("9", "Present", "Present the rules, the plan, the checks and the charts in 3 minutes."),
          ("10", "Reflect", "Score your work with the rubric and write what you would change.")],
    example=dict(title="Checking a plan against the rules (practice data)",
                 steps=["Rules: R1 grain + protein + vegetable every day; R2 no dish more than twice a week; R3 at most Rs 40 a lunch.",
                        "Wednesday breaks R3 (Rs 46): swap paneer for chana (Rs 36). Friday breaks R2 (dal a third time): swap dal for chana, its second time.",
                        "Check again: every day now passes every rule. A computer checks plans the same way, rule by rule."],
                 table=[["Day", "Lunch", "Rules broken"], ["Mon", "roti, dal, bhindi (Rs 32)", "none"], ["Tue", "rice, rajma, salad (Rs 38)", "none"],
                        ["Wed", "roti, paneer, peas (Rs 46)", "R3"], ["Thu", "rice, dal, cabbage (Rs 30)", "none"], ["Fri", "roti, dal, spinach (Rs 30)", "R2"]],
                 widths=[50, 250, 110]),
    sheet=dict(title="Food data sheet", intro="One row per food. Write values per serving and where each value came from.",
               header=["Food", "Food group", "Protein (g)", "Energy (kcal)", "Cost (Rs)", "Source"], widths=[92, 88, 70, 75, 60, 130], blank=9, row_h=19),
    draw=[dict(title="My 5-day plan and rule check", text="Draw a table with a row for each day (Monday to Friday) and columns for the lunch, its cost and each rule. "
                                                         "Tick each rule the day passes; mark any rule it breaks, fix the day and check again.", h=580)],
    rubric=[("Question and rules", "Clear rules that make a lunch balanced and affordable."),
            ("Data", "Nutrition and cost data for every food, each with a source."),
            ("Plan", "Every day follows every rule, and the checks are shown."),
            ("Improvement", "Version 2 is better in a way that can be measured."),
            ("Charts and talk", "The right chart for each job; a clear, short talk."),
            ("Teamwork", "Everyone has a job and the work is shared fairly.")],
    ethics=["We wrote down where every value came from.", "We respected food choices for religion, health and allergies.",
            "We did not collect anyone's weight or health details.", "We said our plan is a school project, not medical advice."],
    reflect=["Which rule was the hardest to keep, and why?", "How would your plan change for a classmate with a food allergy?"],
    answer="Open project: assess with the rubric. Check that every day of the final plan passes every rule.",
))

PROJECTS.append(project(
    2, title="Sort It with AI", skill="Build a waste classifier and measure its accuracy", color="#8B5CF6",
    question="Can we teach a classifier to put school waste in the right bin, and measure how often it is right?",
    brief=["Waste is easier to recycle when it goes in the right bin: <b>wet</b> (food and garden waste), <b>dry</b> (paper, plastic, metal, glass) "
           "or <b>hazardous</b> (batteries, bulbs, medicines). Your team makes 60 picture cards of waste items and labels each one.",
           "Use 40 cards to find rules (training) and keep 20 for testing. Write the rules as a decision tree, test it, measure the accuracy, study the mistakes, "
           "improve, and test again. Schools with computers can also train a no-code model on photos and compare."],
    words=[("label", "the right answer for an example"), ("feature", "something you can observe"), ("accuracy", "correct ÷ total"), ("test set", "examples kept back for checking")],
    robo="A classifier is only as good as its examples. Test it on cards it has never seen, count the mistakes, and improve!",
    plan=[("1", "Define", "Agree the question and the three bins. Decide how you will measure success."),
          ("2", "Collect", "Make 60 picture cards of waste items, about 20 for each bin, and label each one."),
          ("3", "Check labels", "Check unclear labels with your teacher. Shuffle and split: 40 training, 20 test."),
          ("4", "Find features", "Study the training cards: what can you observe that separates the bins?"),
          ("5", "Build", "Write your rules as a decision tree with yes/no questions."),
          ("6", "Test", "Run the tree on the 20 test cards. Record each prediction and the true label."),
          ("7", "Measure", "Work out the accuracy. Make a table of which bins were mixed up."),
          ("8", "Improve", "Fix a rule or add training cards, then test on new cards you have not used."),
          ("9", "Present", "Show the tree, the results before and after, and what you learnt."),
          ("10", "Reflect", "Score your work with the rubric. Which mistakes matter most?")],
    example=dict(title="Testing a decision tree (practice data)",
                 steps=["The tree asks: <i>Is it food or a plant?</i> If yes: wet. If no: <i>Is it a battery, bulb or medicine?</i> If yes: hazardous; if no: dry.",
                        "On 20 test cards it got 17 right: accuracy = 17 ÷ 20 = <b>85%</b>.",
                        "The 3 mistakes show what to fix: a used tissue with food, a broken thermometer and a paint tin had no question that fitted them."],
                 fig=lambda: F.decision_tree("Food or plant?", "Wet", "Battery, bulb or medicine?", "Hazardous", "Dry", w=400)),
    sheet=dict(title="Test results", intro="One row per test card. Write the true label, your tree's prediction, and whether it was right.",
               header=["Card", "Item", "True bin", "Predicted bin", "Right? (Y/N)"], widths=[50, 175, 100, 100, 90], blank=9, row_h=19),
    rubric=[("Data", "60 clearly labelled cards; labels checked; test cards kept apart."),
            ("Rules", "A clear decision tree that uses features anyone can observe."),
            ("Testing", "Accuracy worked out correctly on unseen cards; mistakes listed."),
            ("Improvement", "A rule or the data is improved, and accuracy is measured again."),
            ("Fairness and honesty", "Real results reported, and accuracy checked for each bin."),
            ("Talk and teamwork", "A clear presentation; the work is shared fairly.")],
    ethics=["We kept the test cards apart until the end.", "We reported our real accuracy, even when it was low.",
            "We checked unclear labels with our teacher instead of guessing.", "We asked which mistakes could cause harm, like a battery in the wet bin."],
    reflect=["Which items were hardest to classify, and why?", "How could a wrong prediction cause harm in real life?"],
    answer="Open project: assess with the rubric. Accuracy = correct test cards ÷ all test cards, for example 17 ÷ 20 = 85%.",
))

FACTS = {
    1: "Indian newspapers often give big numbers in lakhs and crores, while international ones use millions and billions.",
    2: "Spreadsheets and scientific calculators follow the same order of operations you do: brackets first, then x and ÷, then + and -.",
    3: "Acharya Pingala used patterns of short and long syllables, much like binary, to study poetry metres about 2,000 years ago.",
    4: "In games, variables like score and lives are letter-numbers: names for values that change as you play.",
    5: "Railway lines are parallel: the two rails must stay exactly the same distance apart.",
    6: "Inside a computer, every decision comes down to tiny switches that are either on or off: true or false.",
    7: "Bridges and towers use triangles because a triangle cannot change shape unless a side changes length.",
    8: "Recipes are scaled with fractions: half a recipe means half of every ingredient.",
    9: "Phone cameras use computer vision to find faces and focus on them.",
    10: "Navigation apps use live data from many phones to estimate traffic and travel times.",
    11: "In the 1850s, Florence Nightingale used a chart to show that more soldiers were dying of disease than of wounds.",
    12: "India's Digital Personal Data Protection Act, 2023 sets rules for how organisations may use people's personal data.",
}


# ------------------------------------------------------------------ specimen: classroom kit illustration (Classes 6-8)
def _kit_items():
    from reportlab.platypus import Table, TableStyle, Paragraph, Spacer
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib import colors
    sm = ParagraphStyle("kitsm", fontName="Kid", fontSize=9, leading=12, textColor=F.SOFT)
    q = ParagraphStyle("kitq", fontName="Kid", fontSize=10, leading=13.5, textColor=F.INK)
    head = ParagraphStyle("kith", parent=q, fontName="KidB", textColor=colors.white)
    cards = F.punch_cards(["UOU", "UUO", "OUU"], w=56)
    items = Table([[cards, F.binary_cards(13, w=38, h=52)],
                   [Paragraph("<b>Punched-card logic deck</b> with sorting sticks (32 cards)", sm), Paragraph("<b>Binary dot cards</b> 16, 8, 4, 2, 1 (20 sets)", sm)],
                   [F.item_cards([("banana peel", "wet", F.GREEN), ("old battery", "hazardous", F.RED), ("newspaper", "dry", F.BLUE)], w=72, h=44),
                    F.pie_chart([20, 10, 6, 4], ["Bus", "Walk", "Car", "Cycle"], size=70)],
                   [Paragraph("<b>AI picture cards</b>: waste, fruit and vegetable sets (120)", sm), Paragraph("<b>Chart and data boards</b>, write-on, wipe-off (10)", sm)]],
                  colWidths=[515.27 / 2, 515.27 / 2])
    items.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("ALIGN", (0, 0), (-1, -1), "CENTER"), ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                               ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F7F9FC")), ("ROUNDEDCORNERS", [10, 10, 10, 10])]))
    rows = [["Item", "Quantity per kit"], ["Punched-card logic deck with sticks", "32 cards, 6 sticks"], ["Binary dot cards", "20 sets of 5"],
            ["AI picture cards (waste, fruit, vegetable)", "120"], ["Function, loop and decision card decks", "4 decks of 54"],
            ["Project data sheet pads (A4)", "2 pads of 50"], ["Project posters: plan, rubric, fair AI", "3"], ["Teacher quick-guide card", "1"], ["Sturdy box", "1"]]
    data = [[Paragraph(c, head if i == 0 else q) for c in r] for i, r in enumerate(rows)]
    t = Table(data, colWidths=[515.27 - 140, 140])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#14A3A3")), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("TOPPADDING", (0, 0), (-1, -1), 4),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 5), ("LINEBELOW", (0, 1), (-1, -1), 0.5, colors.HexColor("#D6DEEA")), ("ROUNDEDCORNERS", [8, 8, 8, 8]),
                           ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F3F6FB")])]))
    return [items, Spacer(1, 10), t, Spacer(1, 6), Paragraph("Illustrations show the design. Final materials will be confirmed after the pilot.", sm)]


META = dict(
    textbook_short="NCERT maths, Class 7",
    textbook_long="the NCERT Class 7 maths textbook",
    cover_follows="Follows NCERT Class 7 maths, CBSE's four AI chapters and two projects",
    cover_tag="Computational thinking and AI for Class 7",
    cover_line="Theory, worked examples, practice, coding on paper, AI and projects",
    cover_cards=(("sticks = 3n + 1", "step", F.TEAL), ("Repeat until n is 0", "step", F.ORANGE), ("If a + b > c", "step", F.PURPLE)),
    welcome="Welcome back! I am <b>Robo</b>. In Class 7 we count in binary like a computer, write formulas with variables, solve logic puzzles by filtering cases, "
            "find out how AI predicts and why it can be unfair, and run two real projects.",
    projects_note="Two 20-hour team projects: plan, collect real data, build, test, present and score your work with a rubric.",
    front_cards=[("Step: do this", "step", "#3B82F6"), ("Repeat: a loop", "loop", "#F5A524"), ("If: a decision", "if", "#8B5CF6"),
                 ("Define: a function", "step", "#14A3A3"), ("When: an event", "event", "#E5484D")],
    chapters_note="Chapters 1-8 go with the same chapters of the NCERT Class 7 maths textbook, so they can be used in maths periods. "
                  "AI chapters 1-4 follow the AI part of CBSE's Class 7 handbook, and the two projects run across the year. ",
    hours_note="CBSE sets 100 hours a year in Class 7: about 40 for computational thinking, 20 for AI and 40 for two projects. "
               "The coding here needs no computer: students write, trace and debug programs on paper, which prepares them for block and text coding. ",
    levels_note="Levels: C4 big numbers, expressions, binary, variables and fractions; C5 logic, angle and triangle rules, AI, data and projects.",
    cutout_cards=[("Define ___", "step"), ("give back ___", "step"), ("Repeat until ___", "loop"), ("Repeat for each ___", "loop"), ("If ___", "if"), ("else", "if"),
                  ("AND", "if"), ("OR", "if"), ("Input ___", "event"), ("Set ___ to ___", "step"), ("change ___ by ___", "step"), ("say ___", "step")],
    sample=[3, 12],  # CT chapter 3 (binary and punched cards, C4) and AI chapter 4 (bias, C5)
    sample_projects=[102],  # Project 2: Sort It with AI
    band=dict(
        about_title="A complete CT&amp;AI programme for Classes 6-8",
        about_intro="From 2026-27, CBSE asks schools to teach Computational Thinking and AI in Classes 3-8. In Classes 6-8 it is <b>100 hours a year</b>; "
                    "in Class 7 that is about 40 hours of computational thinking, 20 hours of AI and two projects of 20 hours each. CBSE's free handbook gives "
                    "puzzles for each maths chapter and four AI chapters. CodeSchool turns it into a full course any teacher can run, with no computer lab needed.",
        compare=[["What schools need", "CBSE's free handbook", "CodeSchool Projects and AI Pack"],
                 ["CT for each maths chapter", "Puzzles", "Theory, worked examples, practice in levels and coding on paper"],
                 ["AI chapters", "Four chapters with exercises", "The same four topics, with unplugged activities and 'build it' tasks"],
                 ["Coding", "No", "Formulas, binary, logic filters, checks and debugging on paper, ready for block or text coding"],
                 ["Projects (40 hours)", "Hours set aside", "Two complete 20-hour projects with plans, data sheets and rubrics"],
                 ["Teacher lesson plans", "Answer keys", "A period-by-period teacher script book"],
                 ["Assessment", "No format given", "Project rubrics, observation journal and term summary"],
                 ["Teacher training", "CBSE workshops", "School orientation, termly workshops and support"]],
        why=["Chapters 1-8 follow NCERT Class 7 maths in order, so the CT work fits the maths period.",
             "The four AI chapters match the AI part of CBSE's handbook and are taught with hands-on, unplugged activities.",
             "Two ready-made projects fill the 40 project hours, with plans, data sheets and rubrics.",
             "Works in any classroom: paper, cards and posters. A projector or computer lab helps but is optional."],
        receives=[["For", "What they get", "Classes"],
                  ["Each student", "Projects and AI Pack: workbook with CT chapters, AI chapters, two project units and cut-out cards", "6, 7, 8"],
                  ["Each class section", "Classroom kit: punched-card logic deck, binary cards, AI picture cards, data sheet pads, project posters, box", "6, 7, 8"],
                  ["Each teacher", "Teacher script book, answer keys, project rubrics, observation journal, short how-to videos", "6, 7, 8"],
                  ["The school", "Orientation at school, a workshop every term, a support line and a term summary format", "All"]],
        series=[["Book", "Levels", "Coder skills"],
                ["Classes 3-5 Practice Packs", "B1-B7", "Steps, loops, if-else, variables, search and a game designed on paper (separate samples)"],
                ["Class 6 Projects and AI Pack", "C1-C3", "Functions, lists, sieve and sorting, debugging, four AI chapters and two projects (separate sample)"],
                ["Class 7 Projects and AI Pack (this sample)", "C4-C5", "Binary, expressions, formulas, logic filters, triangle checks, four AI chapters and two projects"],
                ["Class 8 Projects and AI Pack", "C6-C8", "In development, following CBSE's Class 8 handbook"]],
        price="<b>Indicative price:</b> Rs 599 per student per year (MRP) for the Classes 6-8 Projects and AI Pack, through the school's book list. "
              "It can replace an existing computer book, so the cost to parents stays about the same. Kits, teacher books and training come with the packs. "
              "Prices are indicative until confirmed in writing.",
        contents_intro="The complete book has 8 CT chapters that follow the NCERT Class 7 maths textbook, 4 AI chapters that follow CBSE's handbook and two 20-hour "
                       "projects, plus answers, a glossary and cut-out code cards. This sample includes CT chapter 3, AI chapter 4 and Project 2 in full.",
        kit_intro="One kit per class section, used all year. Everything is printed, laminated and reusable.",
        kit_items=_kit_items,
        assess=[["Skill", "Beginning", "Developing", "Secure", "Extending"],
                ["Algorithms and formulas", "Follows given steps", "Evaluates expressions in the right order", "Writes formulas and traces programs", "Designs and debugs checks"],
                ["Logic", "Uses one clue", "Filters cases with two clues", "Lists every case and filters them", "Explains why a rule always holds"],
                ["AI ideas", "Names AI domains", "Tells classification, regression, clustering apart", "Measures accuracy on test data", "Finds and explains bias in data"],
                ["Projects", "Takes part with help", "Completes stages with help", "Plans, tests and presents with the team", "Improves the work using evidence"]],
        summary=[["Area", "Level", "Teacher comment"],
                 ["Computational thinking (overall)", "Secure", "Converts to binary confidently and writes formulas for growing patterns."],
                 ["AI and ethics", "Developing", "Spots data bias; next step: checking accuracy for each group."],
                 ["Project 2: Sort It with AI", "Rubric 20 of 24", "Careful testing on unseen cards; the decision tree needs a rule for unclear items."]],
        parents_1="This year your child will learn <b>computational thinking and AI</b>, following CBSE's new curriculum for Classes 3-8. In Class 7 that is about "
                  "100 hours over the year: problem solving linked to maths, four AI chapters and two group projects.",
        parents_2="Your child will use the <i>Think Like a Coder</i> workbook. Most of the work is on paper: writing exact steps, using binary and formulas, "
                  "solving logic puzzles, learning how AI predicts and why it can be unfair, and using technology responsibly.",
        home_tips=["Ask your child to show you how to write your age in binary.",
                   "Talk about AI you see, such as route apps, video suggestions and translation. What data might they use? Could they be unfair to anyone?",
                   "Before sharing news online, check it together with a trusted source.",
                   "Praise careful thinking and honest results, even when a project does not go to plan."],
        take_home=("Write your age and your house number in binary. Which one has more 1s?", "answers vary; check by adding the place values (16, 8, 4, 2, 1)."),
        cover_tag="Computational thinking and AI for Classes 6-8",
        cover_lines=("A sample for schools: a CT chapter, an AI chapter, a full project,", "a teacher script, the classroom kit and how assessment works"),
        cover_info="Class 7 sample  ·  NCERT maths chapters, CBSE AI chapters and projects  ·  No lab needed",
        cover_price="Projects and AI Pack Rs 599 per student (indicative)  ·  Free pilot, January-March 2027",
        back_line="Computational thinking and AI for Classes 6-8, for CBSE schools",
    ),
    teacher=dict(
        title="The lopsided deck",
        source="From the teacher book, Class 7, AI chapter 4 (<i>Ethics and AI Bias Awareness</i>). One 40-minute period. Level C5.",
        need=[["Kit", "AI picture cards: a lopsided training deck (18 fruit, 2 vegetable cards), a test deck (10 fruit, 10 vegetable), 8 extra vegetable cards, scoring slips"],
              ["Book", "AI chapter 4 pages, 'Try it' questions 1-3"],
              ["Goal", "Students see how unbalanced training data makes a classifier unfair, measure accuracy for each group, and fix the data"]],
        steps=[["1. Predict and run (8 min)", "Groups look only at the lopsided training deck and write a rule for 'fruit or vegetable'.",
                "Predict how many test cards their rule will get right."],
               ["2. Investigate (8 min)", "Hand out the test deck. Ask: 'Which group does your rule get wrong most often?'",
                "Count right answers for fruits and vegetables separately."],
               ["3. Modify (8 min)", "Give out the 8 extra vegetable cards.", "Rewrite the rule using the more balanced training deck, then test again."],
               ["4. Put in order (8 min)", "Give out jumbled step cards: count groups, find the gap, add examples, test, compare.", "Order the steps of a fairness check."],
               ["5. Make (8 min)", "Ask: 'Where could this happen in real life?'", "Write one real example (faces, voices, languages) and how to check it."]],
        setup_fig=lambda: F.bar_chart([18, 2], ["Fruit", "Vegetable"], w=200, unit=4),
        setup_w=220,
        setup_text="<b>Set-up:</b> keep the decks apart. The training deck has 18 fruit cards but only 2 vegetable cards; the test deck has 10 of each.",
        mistakes=["<b>Trusting the overall score.</b> A good overall score can hide a group that is mostly wrong. Always check each group.",
                  "<b>Blaming the machine.</b> A classifier copies its examples; the bias came from the data people chose.",
                  "<b>Fixing by removing.</b> Taking the hard cards out of the test deck hides the problem instead of solving it."],
        paces="<b>Support:</b> give groups a ready-made rule and ask them only to test it and count.<br/><b>Stretch:</b> write accuracy for each group as a percentage, "
              "before and after adding vegetable cards, and draw a bar chart of both.",
        check=["Two quick questions at the end of the period:",
               "1. A classifier gets 45 of 50 fruits and 3 of 10 vegetables right. What is its overall accuracy? (48 of 60 = 80%)&nbsp;&nbsp; "
               "2. Why is 80% misleading here? (vegetables are only 30% right)",
               "Note in the observation journal: <b>Beginning</b> (says the rule is wrong), <b>Developing</b> (counts errors with help), "
               "<b>Secure</b> (measures accuracy for each group), <b>Extending</b> (links the errors to missing data and proposes a fix)."],
        link="CBSE's Class 7 handbook explains data, historical and measurement bias and why humans must stay in the loop. "
             "In this lesson students create bias, measure it and fix it with their own hands.",
    ),
)
