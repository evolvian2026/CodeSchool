"""Content of 'Think Like a Coder - Class 6'. Original questions. CT chapters 1-10 follow the NCERT Class 6 maths textbook,
as CBSE's 2026-27 CT&AI Class 6 handbook does; AI chapters 1-4 follow the handbook's AI part; two 20-hour projects
cover the project hours (CBSE: 100 hours a year in Class 6 = 40 CT + 20 AI + 40 projects). Levels C1-C3."""
import figures_c6 as F

CH = []

# ------------------------------------------------------------------ Part 1: computational thinking (NCERT maths order)
CH.append(dict(
    n=1, title="Patterns in Mathematics", skill="Rules and functions: name a rule and reuse it", level="C1", color="#14A3A3",
    robo="A rule I use again and again gets a name: a function. square(n) means n x n. Give it 5 and it gives back 25!",
    learn=["A <b>sequence</b> is a list of numbers that follows a <b>rule</b>. Some rules say how to get the <b>next</b> term (add 3 each time). "
           "Others say how to get the term at any <b>position</b> (term = 3 x position + 2), which lets you jump straight to the 100th term.",
           "Coders give a useful rule a name and call it a <b>function</b>. A function takes an <b>input</b> and gives back an <b>output</b>: "
           "<i>square(4)</i> gives back 16, <i>triangle(4)</i> gives back 1 + 2 + 3 + 4 = 10."],
    words=[("sequence", "numbers that follow a rule"), ("term", "one number in a sequence"), ("function", "a named rule with an input"), ("output", "what the function gives back")],
    example=dict(title="Adding odd numbers makes squares",
                 steps=["1 = 1, 1 + 3 = 4, 1 + 3 + 5 = 9, 1 + 3 + 5 + 7 = 16. The answers are <b>square numbers</b>.",
                        "The picture shows why: each new odd number is an L-shaped layer that turns a square into the next square.",
                        "So the first <b>n</b> odd numbers add up to <b>n x n</b>. The first 10 odd numbers add up to 100."],
                 fig=lambda: F.odd_squares(4)),
    practice=[
        dict(q="Write the next two terms: 1, 4, 9, 16, 25, ...", boxes=2, answer="36 and 49"),
        dict(q="Triangular numbers: 1, 3, 6, 10, 15, ... What comes next?", boxes=1, answer="21 (add 6)"),
        dict(q="A sequence starts at 5 and adds 4 each time. What is its 10th term?", opts=["41", "45", "40", "37"], answer="a) 41 (5 + 9 x 4)"),
        dict(q="The function <b>f(n) = 3 x n - 1</b>. What is f(4)? Which input n gives the output 29?", boxes=2, answer="f(4) = 11; n = 10"),
        dict(q="In 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, ... each number appears one time fewer than its value. How many times does 7 appear?",
             opts=["5", "6", "7", "8"], answer="b) 6"),
    ],
    build=dict(intro="Write a function called <b>triangle(n)</b> that adds 1 + 2 + ... + n and gives back the total.",
               cards=[("Define triangle(n)", "step", "#14A3A3"), ("Set total to 0", "step", "#3B82F6"), ("Repeat for k = 1 to n", "loop", "#F5A524"),
                      ("change total by k", "step", "#3B82F6"), ("give back total", "step", "#14A3A3")],
               task="Run triangle(4) and triangle(6) by hand. What does each give back?", answer="triangle(4) = 10; triangle(6) = 21"),
    challenge=dict(q="Find the sum of the first 20 odd numbers without adding them one by one. Explain your shortcut.",
                   answer="400: the first n odd numbers add up to n x n, and 20 x 20 = 400"),
    ican=["describe a sequence with a rule", "use a function with an input", "spot square and triangular numbers"],
))

CH.append(dict(
    n=2, title="Lines and Angles", skill="Drawing programs: angles, turns and a square(size) function", level="C1", color="#F5A524",
    robo="I draw with two commands: forward and turn. Wrap them in a function called square(size) and I can draw any size of square!",
    learn=["An <b>angle</b> is an amount of turn, measured in <b>degrees</b>. A right angle is 90°, a straight angle 180° and a full turn 360°. "
           "Angles less than 90° are <b>acute</b>; between 90° and 180° are <b>obtuse</b>; more than 180° are <b>reflex</b>.",
           "A drawing robot uses <i>forward</i> and <i>turn</i>. To draw a closed shape with equal sides, it turns 360° in all, so each turn is "
           "360° ÷ number of sides. Put the steps in a <b>function</b> with an input, like <i>square(size)</i>, and reuse it."],
    words=[("angle", "an amount of turn"), ("acute", "less than 90°"), ("obtuse", "between 90° and 180°"), ("reflex", "more than 180°")],
    example=dict(title="Turning on the 8-point compass",
                 steps=["Neighbouring directions on an 8-point compass are <b>45°</b> apart (360° ÷ 8).",
                        "Face North and turn 135° clockwise: 135 ÷ 45 = 3 steps, through NE and E, to <b>SE</b>.",
                        "Face West and turn 90° anticlockwise: 2 steps, through SW, to <b>South</b>."],
                 fig=lambda: F.compass8(120)),
    practice=[
        dict(q="What type of angle is this?", fig=lambda: F.turn_angle(120, label=False), opts=["acute", "right", "obtuse", "reflex"], answer="c) obtuse (120°)"),
        dict(q="You face North-East and turn 90° anticlockwise. Which way do you face now?", opts=["North-West", "South-East", "North", "East"], answer="a) North-West"),
        dict(q="What angle do the hands of a clock make at 4 o'clock?", boxes=1, answer="120° (4 x 30°)"),
        dict(q="Fill the gap to draw a regular hexagon: <i>repeat 6 times: forward 40, turn right ___°</i>", boxes=1, answer="60"),
        dict(q="Eight children stand evenly around a circle, facing the centre. What angle at the centre is between two neighbours?",
             opts=["30°", "45°", "60°", "90°"], answer="b) 45°"),
    ],
    build=dict(intro="Write a <b>square(size)</b> function and use it twice.",
               cards=[("Define square(size)", "step", "#14A3A3"), ("Repeat 4 times", "loop", "#F5A524"), ("forward size", "step", "#3B82F6"),
                      ("turn right 90°", "step", "#3B82F6"), ("square(20)", "step", "#14A3A3"), ("square(40)", "step", "#14A3A3")],
               task="Now change it into <b>triangle(size)</b> for a triangle with equal sides. What goes in the repeat and the turn?",
               answer="Repeat 3 times: forward size, turn right 120° (3 x 120° = 360°)"),
    challenge=dict(q="Using square(30) and turns only, write a program that draws a windmill of 4 squares around one point.",
                   answer="Repeat 4 times: square(30), turn right 90° (each square starts at the centre)"),
    ican=["name and measure angles", "turn on an 8-point compass", "write and reuse a drawing function"],
))

CH.append(dict(
    n=3, title="Number Play", skill="Algorithms that repeat until something happens", level="C1", color="#8B5CF6",
    robo="Some loops don't know in advance how many times to run. They repeat UNTIL something happens, like reaching a palindrome!",
    learn=["An <b>algorithm</b> is a set of exact steps. Some algorithms <b>repeat until</b> a condition is true, so you cannot tell in advance how many steps they take.",
           "Number puzzles are full of them. <i>Reverse and add until you get a palindrome</i> (a number that reads the same both ways, like 363). "
           "To check an algorithm, <b>trace</b> it: write down every value as it changes."],
    words=[("algorithm", "exact steps to solve a problem"), ("repeat until", "loop that stops when something is true"),
           ("palindrome", "reads the same both ways"), ("trace", "follow steps and write each value")],
    example=dict(title="Reverse and add, starting with 57",
                 steps=["57 is not a palindrome, so add its reverse: 57 + 75 = 132.",
                        "132 is not a palindrome: 132 + 231 = 363.", "363 is a palindrome, so the loop <b>stops</b> after 2 steps."],
                 table=[["Step", "Number", "Reverse and add"], ["1", "57", "57 + 75 = 132"], ["2", "132", "132 + 231 = 363"], ["stop", "363", "palindrome"]]),
    practice=[
        dict(q="Which of these is a palindrome?", opts=["1231", "4554", "4545", "4500"], answer="b) 4554"),
        dict(q="Start with 39 and reverse-and-add until you get a palindrome. How many steps does it take, and what palindrome do you reach?", boxes=2,
             answer="2 steps: 39 + 93 = 132, 132 + 231 = 363"),
        dict(q="In the row 32, 47, 18, 59, 26, a number is a <b>supercell</b> if it is bigger than its neighbours on both sides "
               "(or its one neighbour, at an end). Which numbers are supercells?", boxes=2, answer="47 and 59"),
        dict(q="Rule: <i>if the number is even, halve it; if it is odd, multiply by 3 and add 1. Repeat until you reach 1.</i> "
               "Starting at 6, how many steps does it take?", boxes=1, answer="8 steps: 6, 3, 10, 5, 16, 8, 4, 2, 1"),
        dict(q="In a dice game the score is the total of all rolls, and the game ends when a 6 comes up for the second time. "
               "The final score is 20. What is the least number of rolls?", opts=["3", "4", "5", "6"],
             answer="b) 4: two 6s make 12; the other 8 needs at least 2 rolls with no 6 (such as 4 + 4)"),
    ],
    build=dict(intro="Kaprekar's routine for 3-digit numbers (digits not all the same).",
               cards=[("Input a 3-digit number", "event", "#E5484D"), ("Repeat until the number is 495", "loop", "#F5A524"),
                      ("make the biggest number from its digits", "step", "#3B82F6"), ("make the smallest number from its digits", "step", "#3B82F6"),
                      ("set number to biggest - smallest", "step", "#3B82F6"), ("change steps by 1", "step", "#3B82F6")],
               task="Trace it for 352. Write each subtraction. How many steps does it take?",
               answer="532 - 235 = 297, 972 - 279 = 693, 963 - 369 = 594, 954 - 459 = 495: 4 steps"),
    challenge=dict(q="Run Kaprekar's routine on 211. What happens? (Hint: keep three digits, so 99 is written 099.)",
                   answer="211 - 112 = 099, 990 - 099 = 891, 981 - 189 = 792, 972 - 279 = 693, 963 - 369 = 594, 954 - 459 = 495: it still reaches 495, in 6 steps"),
    ican=["follow and trace an algorithm", "use 'repeat until'", "explore number puzzles like palindromes"],
))

CH.append(dict(
    n=4, title="Data Handling and Presentation", skill="Lists: store, sort and find the biggest", level="C1", color="#2BB673",
    robo="I keep data in a list. Each item has a position: first, second, third... Then I can sort it, search it or draw it!",
    learn=["<b>Data</b> is a collection of facts, such as marks, temperatures or votes. Coders store data in a <b>list</b>: items in order, each at a numbered <b>position</b>.",
           "Data is easier to understand when organised in a <b>frequency table</b> and shown in a <b>pictograph</b> or <b>bar graph</b>. "
           "Every graph needs a title, labels and a <b>scale</b>, such as 1 square = 5 students."],
    words=[("data", "facts collected to answer a question"), ("list", "items in order, by position"), ("frequency", "how often something occurs"), ("scale", "what one unit stands for")],
    example=dict(title="Favourite sports of 30 students",
                 steps=["Survey results as a list: cricket 12, football 8, badminton 6, kabaddi 4. Check: 12 + 8 + 6 + 4 = 30.",
                        "In the bar graph, the height of each bar shows the number of students.",
                        "Sorted from most to least: cricket, football, badminton, kabaddi. Cricket is 3 times as popular as kabaddi."],
                 fig=lambda: F.bar_chart([12, 8, 6, 4], ["Cricket", "Football", "Badminton", "Kabaddi"], unit=8)),
    practice=[
        dict(q="Here is a list. What is in position 3? What is the largest value?", fig=lambda: F.list_boxes("temps", [31, 28, 33, 30, 35]), boxes=2,
             answer="33 and 35"),
        dict(q="Each symbol stands for 4 trees. How many more trees did Class 6 plant than Class 7?",
             fig=lambda: F.pictograph_rows([("Class 6", 4, F.GREEN), ("Class 7", 2.5, F.GREEN)], "= 4 trees"), boxes=1, answer="6 (16 - 10)"),
        dict(q="In a bar graph, 1 square stands for 5 students. A bar is 7 squares tall. How many students does it show?", boxes=1, answer="35"),
        dict(q="Sort 42, 17, 58, 23 from smallest to largest. Which number is in position 2?", opts=["17", "23", "42", "58"], answer="b) 23"),
        dict(q="In a pictograph each symbol stands for x litres, where x is a whole number. A shop has 6 symbols and sold less than 100 litres. What is the largest x can be?",
             opts=["15", "16", "17", "20"], answer="b) 16 (6 x 16 = 96; 6 x 17 = 102 is too many)"),
    ],
    build=dict(intro="An algorithm that finds the biggest item in a list.",
               cards=[("Set biggest to the first item", "step", "#3B82F6"), ("Repeat for each item in the list", "loop", "#F5A524"),
                      ("If item &gt; biggest", "if", "#8B5CF6"), ("set biggest to item", "step", "#3B82F6"), ("say biggest", "step", "#3B82F6")],
               task="Trace it on the list 12, 19, 7, 25, 14. Write the value of biggest after each item.", answer="12, 19, 19, 25, 25: it says 25"),
    challenge=dict(q="Heights in cm: 132, 140, 128, 145, 137. Change the program so it finds the shortest. Which cards change, and what is the answer?",
                   answer="Use 'smallest' instead of 'biggest' and 'If item &lt; smallest'; the shortest is 128 cm"),
    ican=["store data in a list", "read pictographs and bar graphs with a scale", "find the biggest item with an algorithm"],
))

CH.append(dict(
    n=5, title="Prime Time", skill="The sieve and a factor-finding algorithm", level="C2", color="#3B82F6",
    robo="A sieve keeps what you want and lets the rest fall through. My number sieve keeps only the primes!",
    learn=["A <b>factor</b> divides a number exactly; a <b>multiple</b> is in its times table. A <b>prime</b> has exactly two factors, 1 and itself. 1 is not prime.",
           "The <b>Sieve of Eratosthenes</b> is a 2,000-year-old algorithm: cross out 1; circle 2 and cross out its other multiples; "
           "circle the next number not crossed out (3) and cross out its multiples; repeat. The circled numbers are the primes."],
    words=[("factor", "divides a number exactly"), ("multiple", "a number in the times table"), ("prime", "exactly two factors"), ("sieve", "an algorithm that filters")],
    example=dict(title="The sieve for 1 to 30",
                 steps=["Cross out 1. Keep 2, cross out 4, 6, 8, ... Keep 3, cross out 9, 15, 21, 27 (6, 12, ... are already gone).",
                        "Keep 5 and cross out 25. The next prime, 7, has 7 x 7 = 49, which is past 30, so we can <b>stop</b>.",
                        "The primes up to 30 are 2, 3, 5, 7, 11, 13, 17, 19, 23 and 29."],
                 fig=lambda: F.number_grid(30)),
    practice=[
        dict(q="How many prime numbers are there from 1 to 30?", boxes=1, answer="10"),
        dict(q="Which of these is a prime number?", opts=["21", "27", "29", "33"], answer="c) 29"),
        dict(q="12 points are equally spaced on a circle. Start at 2 and join every 2nd point: 2, 4, 6, ... How many lines are drawn before you get back to 2?",
             fig=lambda: F.circle_points(12, 2, size=120), opts=["3", "4", "5", "6"], answer="d) 6"),
        dict(q="On the same circle, start at 5 and join every 5th point: 5, 10, 3, ... How many lines are drawn before you get back to 5?",
             opts=["4", "5", "6", "12"], answer="d) 12 (5 and 12 share no factor except 1, so every point is visited)"),
        dict(q="How many factors does 36 have?", boxes=1, answer="9: 1, 2, 3, 4, 6, 9, 12, 18, 36"),
    ],
    build=dict(intro="An algorithm that lists the factors of n and checks if n is prime.",
               cards=[("Input n", "event", "#E5484D"), ("Repeat for k = 1 to n", "loop", "#F5A524"), ("If n ÷ k leaves no remainder", "if", "#8B5CF6"),
                      ("add k to the list factors", "step", "#3B82F6"), ("If factors has exactly 2 items", "if", "#8B5CF6"), ("say 'prime'", "step", "#3B82F6")],
               task="Run it for n = 15 and n = 13. What is in the list each time, and does it say 'prime'?",
               answer="15: [1, 3, 5, 15], not prime; 13: [1, 13], prime"),
    challenge=dict(q="On the 12-point circle, which jumps from 1 to 11 visit every point? What do these numbers have in common with 12?",
                   answer="1, 5, 7 and 11: they share no factor with 12 except 1"),
    ican=["find factors and multiples", "use the sieve to find primes", "explain a factor-finding algorithm"],
))

CH.append(dict(
    n=6, title="Perimeter and Area", skill="Functions with two inputs; breaking shapes apart", level="C2", color="#E5484D",
    robo="area(l, w) has two inputs. I break a tricky shape into rectangles, call area() for each part and add the answers!",
    learn=["<b>Perimeter</b> is the distance around a shape; <b>area</b> is the space inside it. For a rectangle: perimeter = 2 x (l + w) and area = l x w.",
           "A function can have more than one input: <i>area(l, w)</i>. To find the area of an L-shape, <b>decompose</b> it into rectangles, "
           "find each area and add. This is the same skill coders use to break a big problem into smaller ones."],
    words=[("perimeter", "the distance around"), ("area", "the space inside"), ("decompose", "break into smaller parts"), ("input", "a value given to a function")],
    example=dict(title="The area and perimeter of an L-shaped garden",
                 steps=["Split the L into rectangle A (8 m by 3 m) and rectangle B (3 m by 4 m).",
                        "area(8, 3) = 24 and area(3, 4) = 12, so the garden is 24 + 12 = <b>36 m²</b>.",
                        "Perimeter: add the six sides: 8 + 3 + 5 + 4 + 3 + 7 = <b>30 m</b>. (The top step is 8 - 3 = 5 m.)"],
                 fig=lambda: F.lshape(8, 3, 3, 4)),
    practice=[
        dict(q="What are area(7, 5) and the perimeter of a 7 cm by 5 cm rectangle?", boxes=2, answer="35 cm² and 24 cm"),
        dict(q="A square has a perimeter of 20 cm. What is its area?", opts=["20 cm²", "25 cm²", "16 cm²", "100 cm²"], answer="b) 25 cm² (side 5 cm)"),
        dict(q="Two rectangles both have an area of 24 cm²: 6 cm by 4 cm, and 12 cm by 2 cm. Which has the longer perimeter?",
             opts=["6 by 4", "12 by 2", "the same"], answer="b) 12 by 2 (28 cm, against 20 cm)"),
        dict(q="Find the area of this shape by breaking it into two rectangles.", fig=lambda: F.lshape(10, 2, 4, 5, unit=11, split=False),
             boxes=1, answer="40 m² (10 x 2 + 4 x 5)"),
        dict(q="A square of perimeter 16 cm is cut along a diagonal into two triangles. Which statement is <b>false</b>?",
             opts=["Two sides of each triangle meet at a right angle", "Each triangle has a side of 4 cm",
                   "Together the triangles have an area of 16 cm²", "Each triangle has an area of 16 cm²"],
             answer="d) each triangle has an area of 8 cm², not 16"),
    ],
    build=dict(intro="Use one function inside another.",
               cards=[("Define area(l, w)", "step", "#14A3A3"), ("give back l x w", "step", "#14A3A3"), ("Define floor_cost(l, w, rate)", "step", "#14A3A3"),
                      ("give back area(l, w) x rate", "step", "#14A3A3"), ("say floor_cost(5, 4, 60)", "step", "#3B82F6")],
               task="A classroom is 5 m by 4 m and tiles cost Rs 60 per square metre. What does the program say?", answer="area(5, 4) = 20; 20 x 60 = Rs 1,200"),
    challenge=dict(q="Draw two shapes, each made of 12 unit squares joined edge to edge: one with the shortest perimeter you can find, one with the longest.",
                   answer="Shortest: a 3 x 4 rectangle (14 units). Longest: a 1 x 12 strip, or any shape whose squares never form a 2 x 2 block (26 units)"),
    ican=["find perimeter and area", "use a function with two inputs", "break a shape into rectangles"],
))

CH.append(dict(
    n=7, title="Fractions", skill="Compare, simplify and sort fractions", level="C2", color="#EC4899",
    robo="To sort fractions, I compare two neighbours and swap them if they are in the wrong order. Then I do it again!",
    learn=["<b>Equivalent fractions</b> name the same amount: 1/2 = 2/4 = 3/6. A fraction is in <b>simplest form</b> when no number above 1 divides both top and bottom.",
           "To <b>compare</b> fractions, write them with the same bottom number (or as marks out of 100). "
           "To <b>sort</b> a list, a computer can compare neighbours and swap them when they are in the wrong order, going along the list again and again (<b>bubble sort</b>)."],
    words=[("equivalent", "the same amount"), ("simplest form", "cannot be simplified more"), ("compare", "find which is bigger"), ("bubble sort", "swap neighbours until sorted")],
    example=dict(title="Which subject did Riya do best in?",
                 steps=["Riya's marks: Art 18/20, Maths 42/50, Science 88/100. Different totals make them hard to compare.",
                        "Make them all out of 100: 18/20 = 90/100, 42/50 = 84/100, 88/100 stays 88/100.",
                        "Sorted from best: <b>Art, Science, Maths</b>."],
                 table=[["Subject", "Marks", "Out of 100"], ["Art", "18/20", "90"], ["Maths", "42/50", "84"], ["Science", "88/100", "88"]]),
    practice=[
        dict(q="What is 18/24 in simplest form?", opts=["9/12", "3/4", "6/8", "2/3"], answer="b) 3/4"),
        dict(q="Which is bigger: 5/8 or 3/5?", opts=["5/8", "3/5", "equal"], answer="a) 5/8 (25/40 against 24/40)"),
        dict(q="Put 2/3, 3/8 and 1/2 in order from smallest. Which one is in the middle?", opts=["2/3", "3/8", "1/2"], answer="c) 1/2 (3/8, 1/2, 2/3)"),
        dict(q="One pass of bubble sort on [3/4, 1/4, 1/2]: compare each pair of neighbours from the left and swap if the left one is bigger. What is the list after one pass?",
             opts=["[1/4, 1/2, 3/4]", "[1/4, 3/4, 1/2]", "[3/4, 1/2, 1/4]"], answer="a) [1/4, 1/2, 3/4]"),
        dict(q="Asha eats 1/3 of a pizza and Ben eats 1/4. What fraction is left?", boxes=1, answer="5/12 (1 - 4/12 - 3/12)"),
    ],
    build=dict(intro="An algorithm that puts a fraction in simplest form.",
               cards=[("Input top and bottom", "event", "#E5484D"), ("Repeat until no number above 1 divides both", "loop", "#F5A524"),
                      ("find a number that divides both", "step", "#3B82F6"), ("divide top and bottom by it", "step", "#3B82F6"), ("say top / bottom", "step", "#3B82F6")],
               task="Trace it for 24/36. Write each division you make.", answer="For example ÷2: 12/18, ÷2: 6/9, ÷3: 2/3 (or ÷12 in one step)"),
    challenge=dict(q="Put 7/8, 5/6 and 11/12 in order without drawing. What pattern helps?",
                   answer="5/6, 7/8, 11/12: each is 1 minus a piece (1/6, 1/8, 1/12); the smaller the missing piece, the bigger the fraction"),
    ican=["simplify fractions", "compare and order fractions", "trace a sorting pass"],
))

CH.append(dict(
    n=8, title="Playing with Constructions", skill="Construction scripts: exact steps and debugging", level="C2", color="#14A3A3",
    robo="A construction is a program for your compass and ruler. If one step is missing, the drawing has a bug!",
    learn=["A <b>construction</b> uses only a ruler and a compass, following exact steps. It is an algorithm: anyone who follows the same steps gets the same drawing.",
           "All points the same distance from a centre make a <b>circle</b>. Where two circles cross, a point is that distance from <i>both</i> centres. "
           "If a script gives the wrong shape, <b>debug</b> it: follow it step by step and find the step that is missing or wrong."],
    words=[("construct", "draw exactly with ruler and compass"), ("arc", "part of a circle"), ("perpendicular", "at right angles"), ("debug", "find and fix a mistake")],
    example=dict(title="A script for the perpendicular bisector of AB",
                 steps=["Draw AB = 6 cm.", "With the compass at A and a radius more than 3 cm, draw arcs above and below AB.",
                        "With the same radius and the compass at B, draw arcs that cross the first ones at P and Q.",
                        "Join P and Q. PQ cuts AB at its middle point M, at a right angle."],
                 fig=lambda: F.construction(300)),
    practice=[
        dict(q="Two circles of radius 5 cm have centres 6 cm apart. At how many points do they cross?", opts=["0", "1", "2", "3"], answer="c) 2"),
        dict(q="Two circles of radius 3 cm have centres 8 cm apart. At how many points do they cross?", opts=["0", "1", "2", "3"], answer="a) 0 (3 + 3 is less than 8)"),
        dict(q="Debug this script for a 4 cm square: <i>Draw AB = 4 cm. At B draw a right angle and mark BC = 4 cm. Join A to C.</i> What goes wrong?",
             opts=["It draws a triangle, not a square", "Nothing is wrong", "The sides are too long"],
             answer="a) it draws a triangle; it needs: at C draw a right angle, mark CD = 4 cm, join D to A"),
        dict(q="All the points that are exactly 3 cm from a point O make a ...", opts=["line", "circle", "square", "triangle"], answer="b) circle"),
        dict(q="A 2 by 2 grid is made of 4 small squares. How many squares can you see in it altogether?", boxes=1, answer="5 (4 small and 1 big)"),
    ],
    build=dict(intro="Follow this script with a ruler and set square to draw a rectangle 5 cm by 3 cm.",
               cards=[("Draw AB = 5 cm", "step", "#3B82F6"), ("At A and B, draw right angles", "step", "#3B82F6"), ("Mark AD = 3 cm and BC = 3 cm", "step", "#3B82F6"),
                      ("Join D to C", "step", "#3B82F6"), ("Check: ___", "if", "#8B5CF6")],
               task="Draw it in the space. Then write a check step that would catch a mistake.", drawspace=True,
               answer="For example: check DC = 5 cm and that the two diagonals are equal (about 5.8 cm)"),
    challenge=dict(q="Write a script that uses only a ruler and compass to draw a triangle with all three sides 5 cm.",
                   answer="Draw AB = 5 cm; draw an arc of radius 5 cm with centre A; draw an arc of radius 5 cm with centre B; they cross at C; join AC and BC"),
    ican=["write exact construction steps", "use circles to find points", "debug a script that goes wrong"],
))

CH.append(dict(
    n=9, title="Symmetry", skill="Reflect and rotate: functions that change shapes", level="C2", color="#F5A524",
    robo="reflect() is a function too: give it a square on one side of the mirror, and it gives back the square on the other side!",
    learn=["A shape has a <b>line of symmetry</b> if folding along the line makes both halves match. It has <b>rotational symmetry</b> if it looks the same after "
           "less than a full turn; the number of times it matches in one full turn is its <b>order</b>.",
           "Drawing programs flip shapes with a <b>reflect</b> function. On a grid with a mirror line, each square moves to the same distance on the other side of the line."],
    words=[("line of symmetry", "fold line where halves match"), ("reflection", "a mirror image"), ("rotational symmetry", "matches itself when turned"), ("order", "how many times it matches")],
    example=dict(title="Reflecting a shape on a grid",
                 steps=["The red line is the mirror. A square 1 column left of the line goes to 1 column right of it.",
                        "A square 3 columns left goes 3 columns right. The row does not change.",
                        "Reflect every shaded square and the whole shape is mirrored."],
                 fig=lambda: F.mirror_grid({(0, 2), (1, 1), (1, 2), (2, 0), (3, 2)}, show_mirror=True)),
    practice=[
        dict(q="How many lines of symmetry does a square have?", boxes=1, answer="4"),
        dict(q="Which letter has <b>no</b> line of symmetry?", opts=["A", "H", "F", "O"], answer="c) F"),
        dict(q="What is the order of rotational symmetry of an equilateral triangle?", opts=["1", "2", "3", "6"], answer="c) 3"),
        dict(q="Shade the mirror image on the other side of the red line. How many squares will be shaded in all?",
             fig=lambda: F.mirror_grid({(0, 0), (0, 1), (1, 1), (2, 2), (3, 1)}), boxes=1, answer="10"),
        dict(q="A square sheet is folded in half. A triangle is cut out with one side along the fold. What do you see when it is unfolded?",
             opts=["a triangle-shaped hole", "a diamond-shaped hole", "two separate triangle holes", "no hole"], answer="b) a diamond-shaped hole"),
    ],
    build=dict(intro="Columns on a grid are numbered 1 to 6, and the mirror line is between columns 3 and 4.",
               cards=[("Define reflect(column)", "step", "#14A3A3"), ("give back 7 - column", "step", "#14A3A3"), ("Repeat for each shaded square", "loop", "#F5A524"),
                      ("shade column reflect(column) in the same row", "step", "#3B82F6")],
               task="A shape covers columns 1, 2 and 3 of a row. Which columns does its reflection cover? Check that reflect(3) is 4.",
               answer="Columns 6, 5 and 4 (7 - 1, 7 - 2 and 7 - 3)"),
    challenge=dict(q="Design a pattern with exactly 2 lines of symmetry and rotational symmetry of order 2. Draw it and mark the lines.",
                   answer="Open answer, for example a rectangle or the letter H"),
    ican=["find lines of symmetry", "find the order of rotational symmetry", "use a reflect function on a grid"],
))

CH.append(dict(
    n=10, title="The Other Side of Zero", skill="Integers in data: lowest, highest and range", level="C2", color="#3B82F6",
    robo="Below zero is not 'nothing'. -8 °C is colder than -3 °C. I track the lowest and highest values, even when they are negative!",
    learn=["<b>Integers</b> are the whole numbers with their negatives: ..., -3, -2, -1, 0, 1, 2, 3, .... On a number line, numbers to the left are smaller, so -7 is less than -3.",
           "Integers appear in real data: winter temperatures in Leh, floors below the ground in a lift, or a bank balance. "
           "The <b>range</b> of data is highest minus lowest; with negatives, subtracting a negative means adding: 4 - (-8) = 12."],
    words=[("integer", "a whole number or its negative"), ("negative", "less than zero"), ("range", "highest minus lowest"), ("minimum", "the lowest value")],
    example=dict(title="Tracing a lift",
                 steps=["The lift starts at the ground floor, 0. It goes up 4 floors: 0 + 4 = <b>4</b>.",
                        "It goes down 6 floors: 4 - 6 = <b>-2</b> (the second basement).",
                        "It goes up 1 floor: -2 + 1 = <b>-1</b>."],
                 fig=lambda: F.number_line(-5, 5, 1)),
    practice=[
        dict(q="Which is smaller?", opts=["-7", "-3"], answer="a) -7"),
        dict(q="At night it is 3 °C. The temperature falls by 8 degrees. What is it now?", boxes=1, answer="-5 °C"),
        dict(q="P50, Q42, R34, S26, ... Which letter is the first to have a negative number?", opts=["U", "V", "W", "X"],
             answer="c) W (T18, U10, V2, W-6)"),
        dict(q="A lift starts at floor 2. It goes down 5, up 1, then down 3. Which floor is it on?", boxes=1, answer="-5"),
        dict(q="Work out (-4) + 9 + (-6).", boxes=1, answer="-1"),
    ],
    build=dict(intro="A temperature log for one week in Leh in winter (°C).",
               fig=lambda: F.bar_neg([-3, -7, 2, -1, -8, 0, 4], ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], w=380),
               cards=[("Set lowest and highest to the first value", "step", "#3B82F6"), ("Repeat for each temperature", "loop", "#F5A524"),
                      ("If temp &lt; lowest, set lowest to temp", "if", "#8B5CF6"), ("If temp &gt; highest, set highest to temp", "if", "#8B5CF6"),
                      ("say highest - lowest", "step", "#3B82F6")],
               task="Run it on the week: -3, -7, 2, -1, -8, 0, 4. What are the lowest, the highest and the range?",
               answer="Lowest -8, highest 4, range 4 - (-8) = 12 degrees"),
    challenge=dict(q="A submarine is at -120 m. It rises 45 m, dives 30 m, then rises 60 m. Where is it now? Above or below sea level?",
                   answer="-45 m (-120 + 45 - 30 + 60), which is 45 m below sea level"),
    ican=["compare and order integers", "add and subtract with negatives", "find the range of data with negatives"],
))

# ------------------------------------------------------------------ Part 2: artificial intelligence (CBSE handbook AI chapters)
AI = dict(level="C3", skill_prefix="AI skill: ")


def ai(k, **kw):
    d = dict(AI, n=10 + k, badge=f"AI{k}", kicker=f"AI CHAPTER {k}", short=f"AI {k}",
             source=f"Goes with the AI part of CBSE's Class 6 CT&AI handbook, chapter {k}")
    d.update(kw)
    d["toc"] = f"AI {k}. {d['title']}"
    d["header"] = f"AI chapter {k}  ·  {d['title']}"
    return d


CH.append(ai(
    1, title="Introduction to AI", skill="Tell AI from automation; how machines learn", color="#8B5CF6",
    robo="A timer that always does the same thing is automation. A machine that learns from examples and gets better is AI!",
    learn=["<b>Intelligence</b> is the ability to learn, think, solve problems and adapt. <b>Artificial Intelligence (AI)</b> makes machines do tasks that "
           "usually need human intelligence, such as recognising faces or understanding speech, by finding patterns in <b>data</b>.",
           "<b>Automation</b> follows fixed instructions and does the same thing every time, like a washing machine timer. AI <b>learns</b>: "
           "from labelled examples (<b>supervised</b> learning), by finding groups on its own (<b>unsupervised</b>), or by trial, reward and penalty (<b>reinforcement</b>)."],
    words=[("AI", "machines that learn and decide"), ("automation", "fixed steps, same result"), ("labelled data", "examples with the right answer"), ("model", "what an AI learns")],
    example=dict(title="AI or automation?",
                 steps=["A traffic light that changes every 60 seconds follows a fixed rule: <b>automation</b>.",
                        "Face unlock on a phone learnt your face from pictures and still works with glasses on: <b>AI</b>.",
                        "Ask: does it <b>learn from data</b> and improve, or always do the same thing?"],
                 table=[["Machine", "Learns from data?", "AI or automation"], ["Microwave timer", "No", "Automation"], ["Spam filter", "Yes", "AI"],
                        ["Voice assistant", "Yes", "AI"], ["Fixed-time signal", "No", "Automation"]], widths=[130, 130, 130]),
    practice=[
        dict(q="Which of these is <b>not</b> AI?", opts=["a voice assistant", "face recognition", "a fixed-time traffic signal", "a chatbot"], answer="c) a fixed-time traffic signal"),
        dict(q="A teacher gives a computer 500 photos, each tagged 'cat' or 'dog'. This is ...", opts=["labelled data", "unlabelled data", "not data"], answer="a) labelled data"),
        dict(q="A game program gets +1 for a win and -1 for a loss, and plays thousands of games to get better. This is ...",
             opts=["supervised learning", "unsupervised learning", "reinforcement learning"], answer="c) reinforcement learning"),
        dict(q="A shop's computer puts customers into groups by what they buy, without being told what the groups are. This is ...",
             opts=["supervised learning", "unsupervised learning", "reinforcement learning"], answer="b) unsupervised learning"),
        dict(q="The first research project to use the name 'Artificial Intelligence' was held in ...", opts=["1906", "1956", "1996", "2016"], answer="b) 1956, at Dartmouth College"),
    ],
    build=dict(intro="Write a sorting rule for 'AI or automation?' as code cards.",
               cards=[("Look at the machine", "step", "#3B82F6"), ("If it learns from data or examples", "if", "#8B5CF6"), ("put it in the AI box", "step", "#3B82F6"),
                      ("else", "if", "#8B5CF6"), ("put it in the automation box", "step", "#3B82F6")],
               task="Use your rule on: a calculator, a spam filter, an alarm clock, a photo app that finds faces, a music app that suggests songs, street lights on a timer.",
               answer="AI: spam filter, face-finding photo app, song suggestions. Automation: calculator, alarm clock, timer street lights"),
    challenge=dict(q="Pick a machine at home that follows fixed instructions. How could AI make it more helpful? What data would it need?",
                   answer="Open answer, for example a fan that learns when the family is usually home, using data about times and temperatures"),
    ican=["explain what AI is", "tell AI from automation", "name three ways machines learn"],
))

CH.append(ai(
    2, title="Basic Data Concepts", skill="Types of data; collect, organise and show it", color="#2BB673",
    robo="AI is only as good as its data. So first we learn to collect it carefully, organise it neatly and show it clearly!",
    learn=["<b>Data</b> is raw facts: numbers, words, pictures, sounds or videos. When it is organised to answer a question it becomes <b>information</b>.",
           "We <b>collect</b> data by asking (surveys), watching (observation), measuring, or from records. We <b>organise</b> it by grouping similar items (classifying), "
           "putting it in tables, labelling it clearly and storing it safely. We <b>show</b> it with tables, bar charts and pictograms."],
    words=[("data", "raw facts"), ("information", "data organised to be useful"), ("survey", "asking people questions"), ("classify", "group similar items")],
    example=dict(title="The eco club's tree-planting drive",
                 steps=["Data collected: Class 6 planted 30 trees, Class 7 20, Class 8 35 and Class 9 15.",
                        "Key: one tree symbol = 10 trees, so 35 trees is 3 and a half symbols.",
                        "Information: Class 8 planted the most, 20 more than Class 9."],
                 fig=lambda: F.pictograph_rows([("Class 6", 3, F.GREEN), ("Class 7", 2, F.GREEN), ("Class 8", 3.5, F.GREEN), ("Class 9", 1.5, F.GREEN)], "= 10 trees")),
    practice=[
        dict(q="A recording of the school bell is which type of data?", opts=["number", "text", "image", "sound"], answer="d) sound"),
        dict(q="Measuring a plant's height every week collects which type of data?", opts=["number", "text", "image", "sound"], answer="a) number"),
        dict(q="In a pictogram, one symbol = 10 trees. Class 8 has 3½ symbols and Class 9 has 1½. How many more trees did Class 8 plant?", boxes=1, answer="20 (35 - 15)"),
        dict(q="Putting similar data into groups is called ...", opts=["labelling", "classifying", "storing", "deleting"], answer="b) classifying"),
        dict(q="A teacher wants to compare five students' marks at a glance. What is best?", opts=["a bar chart", "a long paragraph", "a sound recording"], answer="a) a bar chart"),
    ],
    build=dict(intro="Plan and run a small survey: <i>How do you come to school?</i>",
               cards=[("Ask one clear question", "step", "#3B82F6"), ("Collect answers with tally marks", "step", "#3B82F6"), ("Organise into a frequency table", "step", "#3B82F6"),
                      ("Draw a bar chart with a scale", "step", "#3B82F6"), ("Write one conclusion", "step", "#3B82F6")],
               task="Ask 10 classmates. Draw your tally table and bar chart in the space, then write your conclusion.", drawspace=True,
               answer="Open answer; check that the tallies add up to 10 and that the chart has a title, labels and a scale"),
    challenge=dict(q="A survey asked 5 players from the cricket team, 'Which sport is best?' All said cricket. Can we say the whole school likes cricket best? Why?",
                   answer="No: 5 people is a small sample, and they all play cricket, so the data is biased"),
    ican=["name types of data", "collect and organise data", "choose a table or chart to show data"],
))

CH.append(ai(
    3, title="Patterns and Decisions", skill="Learn a rule from labelled examples, then decide", color="#F5A524",
    robo="I learn like this: look at examples with the right answers, find the pattern, make a rule, then test it on new examples!",
    learn=["A <b>pattern</b> is something that repeats or can be predicted. AI finds patterns in <b>labelled examples</b> and uses them to <b>predict</b> labels for new things. "
           "This is how a spam filter learns which emails are spam.",
           "An <b>observation</b> says what the data shows (it was warmer at 2 pm on 5 days). A <b>conclusion</b> says what it means (afternoons are usually warmer). "
           "A conclusion from a little data may be wrong, so we test it, and use more and fairer data."],
    words=[("pattern", "something that repeats"), ("observation", "what the data shows"), ("conclusion", "what the data means"), ("prediction", "a best guess for a new case")],
    example=dict(title="Learning when a mango is ripe",
                 steps=["Look at the labelled examples. Colour does not decide it: mango 4 is yellow but not ripe, and mango 5 is green but ripe.",
                        "Every ripe mango is soft and every unripe one is hard. Rule: <b>if soft, then ripe</b>.",
                        "Test it on new mangoes whose labels we know. If it is right on most of them, we can use it to decide."],
                 table=[["Mango", "Colour and feel", "Label"], ["1", "yellow, soft", "ripe"], ["2", "green, hard", "not ripe"], ["3", "yellow, soft", "ripe"],
                        ["4", "yellow, hard", "not ripe"], ["5", "green, soft", "ripe"]]),
    practice=[
        dict(q="'On 5 days it was warmer at 2 pm than at 8 am.' This is ...", opts=["an observation", "a conclusion"], answer="a) an observation"),
        dict(q="'So afternoons are usually warmer than mornings.' This is ...", opts=["an observation", "a conclusion"], answer="b) a conclusion"),
        dict(q="Labelled emails: <i>Win a prize now!</i> spam; <i>Class test on Monday</i> not spam; <i>Free gift, click here</i> spam; "
               "<i>PTM at 10 am</i> not spam. What would a filter trained on these predict for <i>Click now to win free coins</i>?",
             opts=["spam", "not spam"], answer="a) spam (it has the words 'win', 'free' and 'click')"),
        dict(q="An AI learnt 'cat' only from photos of white cats. It is shown a black cat. What might go wrong?",
             opts=["It may not recognise it as a cat", "It will always be right", "It will turn the photo white"], answer="a) it may not recognise it: its training data was not varied enough"),
        dict(q="Riya scored 18, 19 and 20 in weeks when she practised daily, and 12 and 11 in weeks when she did not. What is the best decision?",
             opts=["practise daily", "stop practising", "nothing can be decided"], answer="a) practise daily"),
    ],
    build=dict(intro="Be the classifier. Find the rule that tells a <b>Zib</b> from a <b>Zob</b>.",
               fig=lambda: F.creature_sets([("stripes", F.ORANGE, "Zib"), ("spots", F.BLUE, "Zob"), ("stripes", F.GREEN, "Zib"),
                                            ("spots", F.ORANGE, "Zob"), ("stripes", F.BLUE, "Zib"), ("spots", F.GREEN, "Zob")],
                                           [("stripes", F.PINK, "?"), ("spots", F.PINK, "?"), ("stripes", F.ORANGE, "?")]),
               cards=[("Look at the new creature", "step", "#3B82F6"), ("If it has ___", "if", "#8B5CF6"), ("predict Zib", "step", "#3B82F6"),
                      ("else", "if", "#8B5CF6"), ("predict Zob", "step", "#3B82F6")],
               task="Fill in the rule, then label the three new creatures. Does colour matter?",
               answer="If it has stripes, predict Zib, else Zob. New creatures: Zib, Zob, Zib. Colour does not matter: each colour appears in both groups"),
    challenge=dict(q="A new creature has both stripes and spots. What should the classifier say? How could we make it better?",
                   answer="It cannot be sure, because it never saw one like this; it should say 'not sure', and we should add labelled examples like it to the training data"),
    ican=["tell an observation from a conclusion", "find a rule from labelled examples", "explain why more and fairer data helps"],
))

CH.append(ai(
    4, title="Ethics and Digital Responsibility", skill="Strong passwords, privacy and digital footprints", color="#E5484D",
    robo="Online, think before you click, share or copy. Be safe, be kind and be honest, just like in the classroom!",
    learn=["<b>Digital responsibility</b> means being careful, respectful and honest when using technology. Copying someone's work as your own is <b>plagiarism</b>; "
           "copying paid software without permission is <b>piracy</b>; tricking people into giving passwords is <b>phishing</b>.",
           "Everything you do online leaves a <b>digital footprint</b>. <b>Active</b> footprints are things you choose to share, like posts and forms. "
           "<b>Passive</b> ones are collected without you noticing, like location data and cookies. Protect your <b>privacy</b>, use strong passwords, and tell a trusted adult if something feels wrong."],
    words=[("digital footprint", "the trail you leave online"), ("phishing", "tricking people to get secrets"), ("plagiarism", "copying work as your own"), ("privacy", "control of your personal data")],
    example=dict(title="Make a strong password you can remember",
                 steps=["Pick three random words that do not belong together: <i>mango, kite, river</i>.",
                        "Join them with a symbol and add a number: <b>Mango!Kite7River</b>. It is long and mixes capitals, small letters, a number and a symbol.",
                        "Never use your name or birthday, never reuse it everywhere, and never share it, not even with friends."],
                 fig=lambda: F.password_meter(4)),
    practice=[
        dict(q="Which password is strongest?", opts=["riya2014", "password", "Kite!Mango7River", "123456"], answer="c) Kite!Mango7River"),
        dict(q="An email says: <i>Your account is locked. Reply with your password to unlock it.</i> This is ...", opts=["phishing", "a prize", "a software update"], answer="a) phishing"),
        dict(q="Posting a photo of your science project online leaves which kind of footprint?", opts=["active", "passive"], answer="a) active"),
        dict(q="An app records where you are without you posting anything. This is which kind of footprint?", opts=["active", "passive"], answer="b) passive"),
        dict(q="Arjun copies an essay from a website and hands it in as his own. This is ...", opts=["plagiarism", "research", "hacking", "piracy"], answer="a) plagiarism"),
    ],
    build=dict(intro="A safety rule for messages, written as code cards.",
               cards=[("When a message asks for personal information", "event", "#E5484D"), ("If you do not know the sender", "if", "#8B5CF6"),
                      ("do not reply or click; tell an adult", "step", "#3B82F6"), ("else", "if", "#8B5CF6"), ("check with an adult before sharing", "step", "#3B82F6")],
               task="Write your own rule for this: a stranger in a game chat asks for the name of your school.",
               answer="For example: if a stranger asks where I live or study, I do not answer, I block or report them, and I tell a trusted adult"),
    challenge=dict(q="List 5 things that are part of your digital footprint. Mark each one active or passive.",
                   answer="Open answer, for example active: posts, comments, online forms; passive: location history, cookies, suggestions based on your likes"),
    ican=["make and protect a strong password", "spot phishing", "explain active and passive footprints"],
))

# ------------------------------------------------------------------ Projects (2 x 20 hours)
PROJECTS = []


def project(k, **kw):
    d = dict(n=100 + k, badge=f"P{k}", kicker=f"PROJECT {k}  ·  20 HOURS", short=f"Project {k}", level="C3", skill_prefix="Project skill: ",
             source="CBSE: 40 project hours a year in Class 6, as two projects of 20 hours")
    d.update(kw)
    d["toc"] = f"Project {k}. {d['title']}"
    d["header"] = f"Project {k}  ·  {d['title']}"
    return d


PROJECTS.append(project(
    1, title="Weather Across India", skill="Collect, organise and present real data", color="#14A3A3",
    question="How different is the weather in five Indian cities, and what patterns can we find?",
    brief=["Your team picks five cities in different parts of India, for example Leh, Shimla, Jaipur, Kolkata and Chennai. For two weeks, record each city's highest and "
           "lowest temperature and whether it rained, from the newspaper or an official source such as the India Meteorological Department (IMD).",
           "Then organise the data, find the highest, lowest and range for each city, draw charts, look for patterns and present what you found. "
           "This project uses lists, integers, min and max, charts, patterns and conclusions."],
    words=[("dataset", "all the data you collected"), ("source", "where the data came from"), ("range", "highest minus lowest"), ("trend", "a change over time")],
    robo="A project is like a big program: plan it, break it into parts, test it and fix it. One stage at a time!",
    plan=[("1", "Define", "Agree the question, choose five cities and decide what to record each day."),
          ("2-3", "Collect", "Record the highest and lowest temperature and rain for each city every day for two weeks. Write the source."),
          ("4", "Organise", "Put the data in one table per city. Look for missing or odd values and check them."),
          ("5", "Calculate", "For each city find the highest, the lowest and the range. Count the rainy days."),
          ("6", "Show", "Draw a bar chart of the ranges, and a bar chart of one city's daily highs."),
          ("7", "Find patterns", "Write three observations and one conclusion. Is two weeks of data enough to be sure?"),
          ("8", "Predict and test", "Predict tomorrow's highest temperature for one city, then check the real value."),
          ("9", "Present", "Make a poster or a 3-minute talk: question, data, charts, findings and limits."),
          ("10", "Reflect", "Score your work with the rubric and write what you would improve.")],
    example=dict(title="From raw data to a finding: Leh, one week in January (practice data)",
                 steps=["Daily highest temperatures: -2, 0, -4, 1, -3, -1, 2 °C.",
                        "Highest 2, lowest -4, so the range is 2 - (-4) = <b>6 degrees</b>.",
                        "Observation: the highest temperature was below 0 °C on 4 of the 7 days.",
                        "Conclusion, with its limit: Leh's January days are often below freezing, but one week of data is not enough to be sure."],
                 fig=lambda: F.bar_neg([-2, 0, -4, 1, -3, -1, 2], ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], w=360, unit=9, step=2)),
    sheet=dict(title="My data sheet", intro="One row per day for one city. Write where each value came from.",
               header=["Date", "City", "High °C", "Low °C", "Rain? (Y/N)", "Source"], widths=[68, 92, 62, 62, 72, 159], blank=8, row_h=19),
    draw=[dict(title="Draw your chart", text="Draw a bar chart of the temperature range of each city. Choose a scale, then label both axes and give the chart a title.", h=130)],
    rubric=[("Question", "Clear, and can be answered with the data collected."),
            ("Data", "Complete, from a named source, with odd values checked."),
            ("Thinking", "Highest, lowest and range are right; patterns are spotted."),
            ("Charts and talk", "Charts have titles, scales and labels; the talk is clear."),
            ("Honesty and limits", "Says what the data cannot show; nothing copied without credit."),
            ("Teamwork", "Everyone has a job and the work is shared fairly.")],
    ethics=["I wrote down where every piece of data came from.", "I did not change any data to make a better story.",
            "I said what my data cannot tell us (only two weeks, only five cities).", "I used only official or trusted websites, with an adult's help."],
    reflect=["What surprised you most in your data?", "If you did this project again, what would you change?"],
    answer="Open project: assess with the rubric. Check that each range is highest minus lowest, for example 2 - (-4) = 6.",
))

PROJECTS.append(project(
    2, title="A Smarter School Routine", skill="Design, test and improve an algorithm", color="#8B5CF6",
    question="Can we design a better routine for a real problem at school, and prove it works?",
    brief=["Pick a real problem at school: a long queue at the water cooler, books returned to the wrong shelf, or a slow start to assembly. "
           "Observe it and collect data, such as how many minutes the queue takes.",
           "Design a new routine as an algorithm and draw it as a flowchart with a start, steps, decisions and an end. "
           "Try it for a week, collect the same data again and compare. Did your algorithm make things better?"],
    words=[("flowchart", "a picture of an algorithm"), ("decision", "a yes or no question in a flowchart"), ("test", "try it and measure"), ("improve", "change it to work better")],
    robo="Coders don't guess. They measure, change one thing, and measure again!",
    plan=[("1", "Define", "Choose one problem. Write who it affects and how you will measure it."),
          ("2", "Observe", "Collect 'before' data: for example, time five lunch breaks at the water cooler."),
          ("3-4", "Design", "Break the problem down. Write your new routine as steps, then draw it as a flowchart."),
          ("5", "Check", "Trace the flowchart with a friend. Fix any step that is unclear or missing."),
          ("6-7", "Try it", "With your teacher's permission, use the routine for a week and collect 'after' data."),
          ("8", "Compare", "Put the before and after data in a table and a bar chart."),
          ("9", "Present", "Show the problem, the flowchart, the data and the result to your class."),
          ("10", "Reflect", "Score your work with the rubric. Was the routine fair to everyone?")],
    example=dict(title="A flowchart for the water cooler",
                 steps=["Ovals show <b>start</b> and <b>end</b>, boxes show <b>steps</b> and diamonds show <b>decisions</b>, with a 'yes' and a 'no' arrow.",
                        "The 'no' arrows make loops: wait until the cooler is free; keep filling until the bottle is full.",
                        "Test result (practice data): 20 children took 9 minutes before and 6 minutes after, which is 3 minutes faster."],
                 fig=lambda: F.flowchart()),
    sheet=dict(title="Before and after data", intro="Measure the same thing in the same way, on five days before and five days after the new routine.",
               header=["Day", "What we measured", "Before", "After", "Difference"], widths=[60, 185, 90, 90, 90],
               rows=[["Example", "Minutes for 20 children to fill bottles", "9", "6", "3"]], blank=5, row_h=19),
    draw=[dict(title="Draw your flowchart", text="Use ovals for start and end, boxes for steps and diamonds for decisions. Label both arrows from every diamond. "
                                                   "Trace it with a friend before you try it for real.", h=590)],
    rubric=[("Problem", "A real, specific problem with a clear way to measure it."),
            ("Algorithm", "Steps are exact, in order, and cover what to do when something goes wrong."),
            ("Flowchart", "Correct shapes; every decision has a 'yes' and a 'no' path."),
            ("Testing", "Before and after data are collected the same way and compared."),
            ("Fairness", "The routine works for everyone, including younger children."),
            ("Talk and teamwork", "A clear talk with the flowchart and chart; the work is shared fairly.")],
    ethics=["We asked permission before trying the routine.", "We collected no names or personal details, only counts and times.",
            "We listened to people who did not like the new routine.", "We reported the real result, even if things did not improve."],
    reflect=["Which step of your algorithm needed the most fixing, and why?", "Who else in school could use your routine?"],
    answer="Open project: assess with the rubric. A good flowchart has one start, one end, and a 'yes' and a 'no' arrow from every decision.",
))

FACTS = {
    1: "Spreadsheet formulas work like functions: write the rule once and it fills thousands of rows.",
    2: "Ships and aircraft steer by headings in degrees: 90 means due East and 180 means due South.",
    3: "The Indian mathematician D. R. Kaprekar found that any 4-digit number with at least two different digits reaches 6174 with his routine.",
    4: "Cricket apps store every ball of a match as data, which is how they draw run-rate charts.",
    5: "Very large prime numbers help keep online banking and messages secret.",
    6: "Architects' software finds the area of a floor plan by breaking it into rectangles and triangles.",
    7: "Music uses fractions: a half note lasts half as long as a whole note.",
    8: "Computer-aided design (CAD) programs draw with exact steps, just like a construction script.",
    9: "Photo apps flip pictures with a reflect function: every pixel moves to the other side of a mirror line.",
    10: "Lifts in tall buildings show basement floors as B1 and B2, or as -1 and -2.",
    11: "The name 'Artificial Intelligence' was coined for a 1956 summer research project at Dartmouth College, USA.",
    12: "Weather apps combine data from satellites, radars and thousands of weather stations.",
    13: "Email services learn to filter spam from the messages people mark as spam.",
    14: "In India, cyber fraud can be reported on the helpline 1930 or at cybercrime.gov.in.",
}


# ------------------------------------------------------------------ specimen: classroom kit illustration (Classes 6-8)
def _kit_items():
    from reportlab.platypus import Table, TableStyle, Paragraph, Spacer
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib import colors
    from reportlab.graphics.shapes import Drawing, Group
    sm = ParagraphStyle("kitsm", fontName="Kid", fontSize=9, leading=12, textColor=F.SOFT)
    q = ParagraphStyle("kitq", fontName="Kid", fontSize=10, leading=13.5, textColor=F.INK)
    qb = ParagraphStyle("kitqb", parent=q, fontName="KidB")
    cards = Drawing(240, 110)
    for i, (lab, col) in enumerate([("Define area(l, w)", F.TEAL), ("give back l x w", F.TEAL), ("Repeat for each item", F.ORANGE), ("If item > biggest", F.PURPLE)]):
        d = F.code_card(lab, "step", w=116, h=30, color=col)
        x, y = (i % 2) * 122, 70 - (i // 2) * 40
        for el in d.contents:
            cards.add(Group(el, transform=(1, 0, 0, 1, x, y)))
    creatures = F.creature_row([("stripes", F.ORANGE, "Zib"), ("spots", F.BLUE, "Zob"), ("stripes", F.GREEN, "Zib"), ("spots", F.PINK, "?")], size=40)
    items = Table([[creatures, cards],
                   [Paragraph("<b>AI picture cards</b> for classifying and testing (60)", sm), Paragraph("<b>Function and loop cards</b> (4 decks)", sm)],
                   [F.flow_shapes(), F.number_grid(30, cell=17, show=True)],
                   [Paragraph("<b>Flowchart stencil cards</b> for projects (30)", sm), Paragraph("<b>Sieve and data boards</b>, write-on, wipe-off (10)", sm)]],
                  colWidths=[515.27 / 2, 515.27 / 2])
    items.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("ALIGN", (0, 0), (-1, -1), "CENTER"), ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                               ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F7F9FC")), ("ROUNDEDCORNERS", [10, 10, 10, 10])]))
    rows = [["Item", "Quantity per kit"], ["AI picture cards (classify, train and test)", "60"], ["Function, loop and decision card decks", "4 decks of 54"],
            ["Flowchart stencil cards", "30"], ["Project data sheet pads (A4)", "2 pads of 50"], ["Write-on sieve and data boards", "10"],
            ["Project posters: plan, rubric, safe online", "3"], ["Teacher quick-guide card", "1"], ["Sturdy box", "1"]]
    head = ParagraphStyle("kith", parent=qb, textColor=colors.white)
    data = [[Paragraph(c, head if i == 0 else q) for c in r] for i, r in enumerate(rows)]
    t = Table(data, colWidths=[515.27 - 140, 140])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#14A3A3")), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("TOPPADDING", (0, 0), (-1, -1), 4),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 5), ("LINEBELOW", (0, 1), (-1, -1), 0.5, colors.HexColor("#D6DEEA")), ("ROUNDEDCORNERS", [8, 8, 8, 8]),
                           ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F3F6FB")])]))
    return [items, Spacer(1, 10), t, Spacer(1, 6), Paragraph("Illustrations show the design. Final materials will be confirmed after the pilot.", sm)]


META = dict(
    textbook_short="NCERT maths, Class 6",
    textbook_long="the NCERT Class 6 maths textbook",
    cover_follows="Follows NCERT Class 6 maths, CBSE's four AI chapters and two projects",
    cover_tag="Computational thinking and AI for Class 6",
    cover_line="Theory, worked examples, practice, coding on paper, AI and projects",
    cover_cards=(("Define area(l, w)", "step", F.TEAL), ("Repeat for each", "step", F.ORANGE), ("If soft: ripe", "step", F.PURPLE)),
    welcome="Hello again! I am <b>Robo</b>. This year we go further: we will write functions, work with lists and data, find out how AI learns "
            "from examples, and run two real projects. All you need is a pencil and a curious mind.",
    projects_note="Two 20-hour team projects: plan, collect real data, build, test, present and score your work with a rubric.",
    front_cards=[("Step: do this", "step", "#3B82F6"), ("Repeat: a loop", "loop", "#F5A524"), ("If: a decision", "if", "#8B5CF6"),
                 ("Define: a function", "step", "#14A3A3"), ("When: an event", "event", "#E5484D")],
    chapters_note="Chapters 1-10 go with the same chapters of the NCERT Class 6 maths textbook, so they can be used in maths periods. "
                  "AI chapters 1-4 follow the AI part of CBSE's Class 6 handbook, and the two projects run across the year. ",
    hours_note="CBSE sets 100 hours a year in Class 6: about 40 for computational thinking, 20 for AI and 40 for two projects. "
               "The coding here needs no computer: students write, trace and debug programs on paper, which prepares them for block and text coding. ",
    levels_note="Levels: C1 rules, functions and lists; C2 algorithms with inputs, sorting and debugging; C3 AI ideas, data and projects.",
    cutout_cards=[("Define ___", "step"), ("give back ___", "step"), ("Repeat ___ times", "loop"), ("Repeat for each item", "loop"), ("Repeat until ___", "loop"),
                  ("If ___", "if"), ("else", "if"), ("When ___ happens", "event"), ("Input ___", "event"), ("Set ___ to ___", "step"), ("change ___ by ___", "step"), ("say ___", "step")],
    sample=[1, 13],  # CT chapter 1 (functions, C1) and AI chapter 3 (learning from labelled examples, C3)
    sample_projects=[101],  # Project 1: Weather Across India
    band=dict(
        about_title="A complete CT&amp;AI programme for Classes 6-8",
        about_intro="From 2026-27, CBSE asks schools to teach Computational Thinking and AI in Classes 3-8. In Classes 6-8 it is <b>100 hours a year</b>; "
                    "in Class 6 that is about 40 hours of computational thinking, 20 hours of AI and two projects of 20 hours each. CBSE's free handbook gives "
                    "puzzles for each maths chapter and four AI chapters. CodeSchool turns it into a full course any teacher can run, with no computer lab needed.",
        compare=[["What schools need", "CBSE's free handbook", "CodeSchool Projects and AI Pack"],
                 ["CT for each maths chapter", "Puzzles", "Theory, worked examples, practice in levels and coding on paper"],
                 ["AI chapters", "Four chapters with exercises", "The same four topics, with unplugged activities and 'build it' tasks"],
                 ["Coding", "No", "Functions, lists, loops and flowcharts on paper, ready for block or text coding"],
                 ["Projects (40 hours)", "Hours set aside", "Two complete 20-hour projects with plans, data sheets and rubrics"],
                 ["Teacher lesson plans", "Answer keys", "A period-by-period teacher script book"],
                 ["Assessment", "No format given", "Project rubrics, observation journal and term summary"],
                 ["Teacher training", "CBSE workshops", "School orientation, termly workshops and support"]],
        why=["Chapters 1-10 follow NCERT Class 6 maths in order, so the CT work fits the maths period.",
             "The four AI chapters match the AI part of CBSE's handbook and are taught with hands-on, unplugged activities.",
             "Two ready-made projects fill the 40 project hours, with plans, data sheets and rubrics.",
             "Works in any classroom: paper, cards and posters. A projector or computer lab helps but is optional."],
        receives=[["For", "What they get", "Classes"],
                  ["Each student", "Projects and AI Pack: workbook with CT chapters, AI chapters, two project units and cut-out cards", "6, 7, 8"],
                  ["Each class section", "Classroom kit: AI picture cards, function and flowchart cards, data sheet pads, project posters, box", "6, 7, 8"],
                  ["Each teacher", "Teacher script book, answer keys, project rubrics, observation journal, short how-to videos", "6, 7, 8"],
                  ["The school", "Orientation at school, a workshop every term, a support line and a term summary format", "All"]],
        series=[["Book", "Levels", "Coder skills"],
                ["Classes 3-5 Practice Packs", "B1-B7", "Steps, loops, if-else, variables, search and a game designed on paper (separate samples)"],
                ["Class 6 Projects and AI Pack (this sample)", "C1-C3", "Functions, lists, sieve and sorting, debugging, four AI chapters and two projects"],
                ["Class 7 Projects and AI Pack", "C4-C5", "In development, following CBSE's Class 7 handbook"],
                ["Class 8 Projects and AI Pack", "C6-C8", "In development, following CBSE's Class 8 handbook"]],
        price="<b>Indicative price:</b> Rs 599 per student per year (MRP) for the Classes 6-8 Projects and AI Pack, through the school's book list. "
              "It can replace an existing computer book, so the cost to parents stays about the same. Kits, teacher books and training come with the packs. "
              "Prices are indicative until confirmed in writing.",
        contents_intro="The complete book has 10 CT chapters that follow the NCERT Class 6 maths textbook, 4 AI chapters that follow CBSE's handbook and two 20-hour "
                       "projects, plus answers, a glossary and cut-out code cards. This sample includes CT chapter 1, AI chapter 3 and Project 1 in full.",
        kit_intro="One kit per class section, used all year. Everything is printed, laminated and reusable.",
        kit_items=_kit_items,
        assess=[["Skill", "Beginning", "Developing", "Secure", "Extending"],
                ["Algorithms and functions", "Follows given steps", "Writes steps with loops", "Writes and reuses a function", "Designs and tests functions with inputs"],
                ["Data", "Reads a table", "Organises data in a table or list", "Charts data; finds lowest, highest, range", "Draws fair conclusions and states limits"],
                ["AI ideas", "Names AI examples", "Tells AI from automation", "Explains learning from labelled data", "Explains bias and how better data helps"],
                ["Projects", "Takes part with help", "Completes stages with help", "Plans, tests and presents with the team", "Improves the work using evidence"]],
        summary=[["Area", "Level", "Teacher comment"],
                 ["Computational thinking (overall)", "Secure", "Writes functions with inputs and traces lists confidently."],
                 ["AI and digital responsibility", "Developing", "Tells AI from automation; next step: explaining why data can be biased."],
                 ["Project 1: Weather Across India", "Rubric 19 of 24", "Careful data collection with sources; charts need clearer scales."]],
        parents_1="This year your child will learn <b>computational thinking and AI</b>, following CBSE's new curriculum for Classes 3-8. In Class 6 that is about "
                  "100 hours over the year: problem solving linked to maths, four short AI chapters and two group projects.",
        parents_2="Your child will use the <i>Think Like a Coder</i> workbook. Most of the work is on paper: writing exact step-by-step instructions, working with real data, "
                  "learning how AI finds patterns, and learning to use technology safely and honestly.",
        home_tips=["Ask your child to explain a project to you: the question, the data and what they found.",
                   "Talk about AI you use at home, such as voice assistants and video suggestions. What data might they use?",
                   "Agree family rules for passwords, sharing photos and talking to strangers online.",
                   "Praise careful thinking and honest results, even when a project does not go to plan."],
        take_home=("Write down the highest temperature in your town every day for a week, from the newspaper or the weather report. What were the highest, the lowest and the range?",
                   "answers vary; the range is the highest minus the lowest."),
        cover_tag="Computational thinking and AI for Classes 6-8",
        cover_lines=("A sample for schools: a CT chapter, an AI chapter, a full project,", "a teacher script, the classroom kit and how assessment works"),
        cover_info="Class 6 sample  ·  NCERT maths chapters, CBSE AI chapters and projects  ·  No lab needed",
        cover_price="Projects and AI Pack Rs 599 per student (indicative)  ·  Free pilot, January-March 2027",
        back_line="Computational thinking and AI for Classes 6-8, for CBSE schools",
    ),
    teacher=dict(
        title="Train the classifier",
        source="From the teacher book, Class 6, AI chapter 3 (<i>Patterns and Decisions</i>). One 40-minute period. Level C3.",
        need=[["Kit", "AI picture cards: 12 Zib and Zob creature cards (8 labelled for training, 4 unlabelled for testing), scoring slips"],
              ["Book", "AI chapter 3 pages, 'Try it' questions 3 and 4"],
              ["Goal", "Students find a rule from labelled examples, test it on new examples, count how many it gets right, and explain why varied data helps"]],
        steps=[["1. Predict and run (8 min)", "Show the 8 labelled training cards. Ask: 'What makes a Zib a Zib?'",
                "Groups list features (colour, stripes, spots) and predict a rule."],
               ["2. Investigate (8 min)", "Ask: 'Does colour matter? How do you know?'", "Groups check every card against their rule and drop features that do not fit."],
               ["3. Modify (8 min)", "Hand out the 4 unlabelled test cards.", "Groups classify them with their rule; the teacher reveals the labels and groups count how many were right."],
               ["4. Put in order (8 min)", "Give out jumbled step cards: collect examples, find the pattern, make a rule, test, improve.",
                "Order the steps of training an AI model and match them to what they just did."],
               ["5. Make (8 min)", "Show a creature with both stripes and spots.", "Decide what the classifier should say, and write one way to improve the training data."]],
        setup_fig=lambda: F.creature_row([("stripes", F.ORANGE, "Zib"), ("spots", F.BLUE, "Zob"), ("stripes", F.GREEN, "Zib"), ("spots", F.ORANGE, "Zob")], size=40),
        setup_w=230,
        setup_text="<b>Set-up:</b> lay the labelled cards out as the 'training' set. Colours are mixed on purpose, so the only real pattern is stripes (Zib) or spots (Zob).",
        mistakes=["<b>A rule from one card.</b> 'Orange ones are Zibs' fits one card but not the others. Check the rule against every card.",
                  "<b>Using the test cards to make the rule.</b> Then the score is not a fair test of what was learnt.",
                  "<b>Thinking AI is always right.</b> A rule learnt from a few examples can fail on something new, like a creature with both patterns."],
        paces="<b>Support:</b> start with 4 training cards that differ only in pattern.<br/><b>Stretch:</b> add a creature with a new feature (horns) and ask whether the rule "
              "must change; write the score as a fraction, such as 3/4 right.",
        check=["Two quick questions at the end of the period:",
               "1. Why do we test on cards the classifier has not seen? (to check it learnt the pattern, not the answers)&nbsp;&nbsp; "
               "2. A classifier got 9 of 12 test cards right. What fraction is that in simplest form? (3/4)",
               "Note in the observation journal: <b>Beginning</b> (sorts by one card), <b>Developing</b> (finds a rule with help), "
               "<b>Secure</b> (finds and tests a rule and counts the score), <b>Extending</b> (explains the limits of the data and suggests better examples)."],
        link="CBSE's Class 6 handbook introduces labelled data, supervised learning, observations and conclusions in its AI chapters. "
             "In this lesson students do by hand what a supervised learning model does, before they meet AI tools.",
    ),
)
