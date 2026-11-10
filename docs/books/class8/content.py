"""Content of 'Think Like a Coder - Class 8'. Original questions. CT chapters 1-7 follow the NCERT Class 8 maths textbook,
as CBSE's 2026-27 CT&AI Class 8 handbook does; AI chapters 1-4 follow the handbook's AI part; two 20-hour projects
cover the project hours (CBSE: 100 hours a year in Class 8 = 40 CT + 20 AI + 40 projects). Levels C6-C8."""
import figures_c8 as F

CH = []

# ------------------------------------------------------------------ Part 1: computational thinking (NCERT maths order)
CH.append(dict(
    n=1, title="A Square and a Cube", skill="Test squares and cubes with prime factors and loops", level="C6", color="#14A3A3",
    robo="Is 1728 a perfect cube? Break it into prime factors. If they make groups of three, it is!",
    learn=["A <b>perfect square</b> is a number times itself (49 = 7 x 7); a <b>perfect cube</b> is a number used three times (64 = 4 x 4 x 4). "
           "Write a number as a product of primes: it is a square if the primes <b>pair up</b>, and a cube if they make <b>groups of three</b>.",
           "A computer can also test 'is n a square?' with a loop: try k = 1, 2, 3, ... until k x k reaches n. Squares and cubes also hide patterns, "
           "like 1 + 3 + 5 + ... + (2n - 1) = n x n."],
    words=[("perfect square", "a number times itself"), ("perfect cube", "a number used three times"), ("prime factorisation", "a number as a product of primes"),
           ("square root", "the number that was squared")],
    example=dict(title="Is 1728 a perfect cube?",
                 steps=["Prime factors: 1728 = 2 x 2 x 2 x 2 x 2 x 2 x 3 x 3 x 3.",
                        "Make groups of three: (2 x 2 x 2) (2 x 2 x 2) (3 x 3 x 3). Nothing is left over, so it is a cube.",
                        "Take one number from each group: 2 x 2 x 3 = <b>12</b>, so 1728 = 12 x 12 x 12."]),
    practice=[
        dict(q="How many perfect squares are there between 50 and 150?", boxes=1, answer="5: 64, 81, 100, 121 and 144"),
        dict(q="What is the smallest number you must multiply 72 by to get a perfect square?", opts=["2", "3", "6", "8"], answer="a) 2 (72 = 2 x 2 x 2 x 3 x 3; 144 = 12 x 12)"),
        dict(q="56 x k is a perfect cube. What is the smallest whole number k?", opts=["7", "14", "49", "343"], answer="c) 49 (56 = 2 x 2 x 2 x 7, so two more 7s are needed)"),
        dict(q="Which 2-digit number is both a perfect square and a perfect cube?", opts=["16", "27", "36", "64"], answer="d) 64 = 8 x 8 = 4 x 4 x 4"),
        dict(q="A perfect square can never end in which digit?", opts=["1", "4", "7", "9"], answer="c) 7 (squares end in 0, 1, 4, 5, 6 or 9)"),
    ],
    build=dict(intro="An algorithm that tests whether n is a perfect square.",
               cards=[("Input n", "event", "#E5484D"), ("Set k to 1", "step", "#3B82F6"), ("Repeat until k x k is at least n", "loop", "#F5A524"),
                      ("change k by 1", "step", "#3B82F6"), ("If k x k = n", "if", "#8B5CF6"), ("say 'square', else say 'not a square'", "step", "#3B82F6")],
               task="Trace it for n = 49 and n = 50. Where does k stop, and how many times does the loop run?",
               answer="49: k stops at 7 after 6 loops and it says 'square'. 50: k stops at 8 after 7 loops; 64 is not 50, so 'not a square'"),
    challenge=dict(q="2³ - 1³ = 7, 3³ - 2³ = 19, 4³ - 3³ = 37. Find 13³ - 12³ without working out the cubes. Explain your rule.",
                   answer="469: n³ - (n - 1)³ = 3 x n x (n - 1) + 1, and 3 x 13 x 12 + 1 = 469 (check: 2197 - 1728)"),
    ican=["test squares and cubes with prime factors", "trace a checking algorithm", "find patterns in squares and cubes"],
))

CH.append(dict(
    n=2, title="Power Play", skill="Exponents, doubling and counting combinations", level="C6", color="#F5A524",
    robo="Fold a paper 10 times and it has 2 x 2 x ... x 2 = 1,024 layers. Powers grow fast!",
    learn=["An <b>exponent</b> says how many times the <b>base</b> is multiplied: 2<super>5</super> = 2 x 2 x 2 x 2 x 2 = 32. "
           "When multiplying powers of the same base, add the exponents: 2<super>3</super> x 2<super>4</super> = 2<super>7</super>.",
           "Powers also count <b>combinations</b>. If you make several choices one after another, multiply the number of options: 3 shirts and 4 trousers give 12 outfits. "
           "With n yes/no choices there are 2<super>n</super> combinations, which is why every extra character makes a password much harder to guess."],
    words=[("exponent", "how many times to multiply"), ("base", "the number being multiplied"), ("power", "a base with an exponent"), ("combination", "one way of choosing")],
    example=dict(title="Folding a sheet of paper",
                 steps=["Each fold <b>doubles</b> the number of layers.", "After n folds there are 2<super>n</super> layers.",
                        "After 10 folds: 2<super>10</super> = <b>1,024</b> layers, thicker than a 400-page book."],
                 table=[["Folds", "Layers", "As a power"], ["1", "2", "2<super>1</super>"], ["2", "4", "2<super>2</super>"], ["3", "8", "2<super>3</super>"],
                        ["10", "1,024", "2<super>10</super>"]]),
    practice=[
        dict(q="2<super>5</super> x 2<super>3</super> = 2<super>?</super>", boxes=1, answer="8"),
        dict(q="What comes next? 4, 10, 28, 82, ?", opts=["244", "246", "162", "164"], answer="a) 244: each term is a power of 3 plus 1 (3<super>5</super> + 1)"),
        dict(q="You have 4 shirts and 3 pairs of trousers. How many different outfits can you make?", boxes=1, answer="12"),
        dict(q="How many different 4-digit PINs can be made with the digits 0 to 9?", opts=["40", "1,000", "10,000", "9,999"], answer="c) 10,000 (10<super>4</super>)"),
        dict(q="Which is bigger: 2<super>10</super> or 10<super>3</super>?", opts=["2<super>10</super>", "10<super>3</super>", "equal"], answer="a) 2<super>10</super> = 1,024, against 1,000"),
    ],
    build=dict(intro="The chessboard story: 1 grain on the first square, then double on each square.",
               cards=[("Set grains to 1", "step", "#3B82F6"), ("Set total to 0", "step", "#3B82F6"), ("Repeat 10 times", "loop", "#F5A524"),
                      ("change total by grains", "step", "#3B82F6"), ("set grains to grains x 2", "step", "#3B82F6"), ("say total", "step", "#3B82F6")],
               task="Trace it for the first 10 squares. What does it say? Can you see a shortcut?", answer="1 + 2 + 4 + ... + 512 = 1,023, which is 2<super>10</super> - 1"),
    challenge=dict(q="A team of 3 is chosen from 5 students A, B, C, D and E, but A and B cannot both be in it. How many teams are possible?",
                   answer="7: there are 10 teams of 3 in all, and 3 of them contain both A and B"),
    ican=["use the laws of exponents", "count combinations by multiplying choices", "explain why doubling grows so fast"],
))

CH.append(dict(
    n=3, title="A Story of Numbers", skill="Number bases: binary, ternary and changing base", level="C6", color="#8B5CF6",
    robo="Measure 50 inches with pipes! Decimal pipes are 1, 10, 100 long. Binary pipes are 1, 2, 4, 8, 16, 32. Ternary pipes are 1, 3, 9, 27.",
    learn=["In a <b>place-value</b> system each place is worth the <b>base</b> times the place to its right. Base 10 uses digits 0-9 and places 1, 10, 100, .... "
           "Base 2 (binary) uses 0 and 1 and places 1, 2, 4, 8, .... Base 3 (ternary) uses 0, 1 and 2 and places 1, 3, 9, 27, ....",
           "Any number can be written in any base. To convert, divide by the base again and again and read the remainders backwards. "
           "Older systems like Roman numerals have no place value and no zero, which makes calculating much harder."],
    words=[("number base", "how many digits a system uses"), ("place value", "what a position is worth"), ("ternary", "base 3"), ("numeral", "a symbol for a number")],
    example=dict(title="50 inches with three kinds of pipe",
                 steps=["Decimal: 50 = 5 tens, so <b>50</b>.", "Binary: 50 = 32 + 16 + 2, so <b>110010</b>.",
                        "Ternary: 50 = 1 x 27 + 2 x 9 + 1 x 3 + 2 x 1, so <b>1212</b>. The same length, three different names."],
                 fig=lambda: F.pipes_compare(50, w=430)),
    practice=[
        dict(q="What is 10 in binary?", opts=["1010", "1111", "1000", "1100"], answer="a) 1010"),
        dict(q="What is the largest digit allowed in base 5?", opts=["5", "4", "9", "1"], answer="b) 4"),
        dict(q="(1021) in base 3 is which decimal number?", boxes=1, answer="34 (27 + 0 + 6 + 1)"),
        dict(q="How is 1947 written in Roman numerals?", opts=["MCMXLVII", "MCMXXXXVII", "MDCCCCXLVII", "MCMLXVII"], answer="a) MCMXLVII"),
        dict(q="With binary pipes (one each of 1, 2, 4, 8, 16, 32), how many pipes measure 63 inches?", opts=["2", "5", "6", "7"], answer="c) 6: 32 + 16 + 8 + 4 + 2 + 1"),
    ],
    build=dict(intro="One algorithm that converts to any base.",
               cards=[("Input n and base b", "event", "#E5484D"), ("Repeat until n is 0", "loop", "#F5A524"), ("write down the remainder of n ÷ b", "step", "#3B82F6"),
                      ("set n to n ÷ b, dropping the remainder", "step", "#3B82F6"), ("read the remainders from last to first", "step", "#3B82F6")],
               task="Trace it for n = 100 and b = 3. Write each n and each remainder.",
               answer="100: rem 1, n = 33; rem 0, n = 11; rem 2, n = 3; rem 0, n = 1; rem 1, n = 0. Read backwards: 10201"),
    challenge=dict(q="Why do computers use binary rather than base 10? Then: what is the largest number you can write with 4 ternary digits?",
                   answer="A switch has two states, on and off, so two digits are easy to store reliably. 2222 in base 3 = 54 + 18 + 6 + 2 = 80"),
    ican=["write numbers in base 2, 3 and 10", "convert using repeated division", "compare place value with Roman numerals"],
))

CH.append(dict(
    n=4, title="Quadrilaterals", skill="Classify shapes with if-else rules", level="C6", color="#2BB673",
    robo="I sort shapes like an AI classifier: ask about parallel sides, then right angles, then equal sides!",
    learn=["Quadrilaterals form a family. A <b>trapezium</b> has one pair of parallel sides; a <b>parallelogram</b> has two. A parallelogram with right angles is a "
           "<b>rectangle</b>; with all sides equal it is a <b>rhombus</b>; with both it is a <b>square</b>. A <b>kite</b> has two pairs of equal sides next to each other.",
           "The angles of any quadrilateral add up to <b>360°</b>. Because shapes are defined by properties, we can sort them with a chain of if-else questions, "
           "the same way a decision tree classifies data."],
    words=[("parallelogram", "two pairs of parallel sides"), ("rhombus", "four equal sides"), ("trapezium", "one pair of parallel sides"), ("diagonal", "joins opposite corners")],
    example=dict(title="Properties decide the name",
                 steps=["Two pairs of parallel sides puts a shape in the parallelogram family.", "Add right angles: rectangle. Add equal sides: rhombus. Add both: square.",
                        "So every square is also a rectangle and a rhombus, but not every rectangle is a square."],
                 table=[["Shape", "Parallel sides", "Diagonals"], ["Square", "2 pairs", "equal; bisect at 90°"], ["Rectangle", "2 pairs", "equal; bisect each other"],
                        ["Rhombus", "2 pairs", "bisect at 90°"], ["Parallelogram", "2 pairs", "bisect each other"], ["Trapezium", "1 pair", "no special rule"],
                        ["Kite", "none", "one bisects the other at 90°"]], widths=[110, 110, 200]),
    practice=[
        dict(q="Which of these is always a parallelogram?", opts=["kite", "trapezium", "rhombus", "any quadrilateral"], answer="c) rhombus"),
        dict(q="Three angles of a quadrilateral are 80°, 95° and 110°. What is the fourth?", boxes=1, answer="75°"),
        dict(q="Which statement is true?", opts=["Every square is a rectangle", "Every rectangle is a square", "Every rhombus is a square", "Every kite is a parallelogram"],
             answer="a) every square is a rectangle"),
        dict(q="One angle of a parallelogram is 65°. What is the angle next to it?", boxes=1, answer="115° (neighbouring angles add up to 180°)"),
        dict(q="How many rectangles (including squares) can you find in a 2 by 2 grid of squares?", fig=lambda: F.grid(2, 2, labels=False, cell=36), boxes=1,
             answer="9: 4 small squares, 4 rectangles of 2 squares and 1 big square"),
    ],
    build=dict(intro="A quadrilateral classifier written with if-else.",
               cards=[("Input a quadrilateral", "event", "#E5484D"), ("If it has 2 pairs of parallel sides", "if", "#8B5CF6"), ("If all angles are 90°", "if", "#8B5CF6"),
                      ("all sides equal? 'square', else 'rectangle'", "step", "#3B82F6"), ("else: all sides equal? 'rhombus', else 'parallelogram'", "step", "#3B82F6"),
                      ("else: 1 pair parallel? 'trapezium', else 'other'", "step", "#3B82F6")],
               task="Run it for: (a) 4 equal sides with angles 60° and 120°; (b) only one pair of parallel sides; (c) opposite sides equal and all angles 90°.",
               answer="(a) rhombus (b) trapezium (c) rectangle"),
    challenge=dict(q="The diagonals of a quadrilateral are equal and cut each other in half at right angles. What shape must it be? Explain.",
                   answer="A square: diagonals that bisect each other make a parallelogram, equal diagonals make it a rectangle, and meeting at 90° makes it a rhombus"),
    ican=["sort quadrilaterals by their properties", "use the angle sum of 360°", "write a classifier with if-else rules"],
))

CH.append(dict(
    n=5, title="Number Play", skill="Divisibility rules and remainders as quick tests", level="C7", color="#3B82F6",
    robo="A divisibility rule is a shortcut algorithm: I can test 7,392 for 11 without dividing!",
    learn=["<b>Divisibility rules</b> test a number without long division: by 3 or 9, add the digits; by 4, look at the last two digits; by 8, the last three; "
           "by 11, find the alternating sum of the digits (+, -, +, ...).",
           "The <b>remainder</b> is what is left after dividing. Remainders repeat in cycles, like the days of the week: 100 days after Monday is "
           "the same weekday as 2 days after Monday, because 100 leaves a remainder of 2 when divided by 7."],
    words=[("divisible", "divides with no remainder"), ("remainder", "what is left over"), ("divisibility rule", "a shortcut test"), ("multiple", "in the times table")],
    example=dict(title="Testing 7,392 without dividing",
                 steps=["Digit sum 7 + 3 + 9 + 2 = 21: divisible by 3, but not by 9.", "Last two digits 92 = 4 x 23: divisible by 4. Last three 392 = 8 x 49: divisible by 8.",
                        "Alternating sum 7 - 3 + 9 - 2 = 11: divisible by <b>11</b>. Check: 7,392 = 11 x 672."]),
    practice=[
        dict(q="Which number is divisible by 9?", opts=["4,527", "3,862", "2,915", "7,604"], answer="a) 4,527 (digit sum 18)"),
        dict(q="What is the remainder when 2<super>10</super> = 1,024 is divided by 7?", boxes=1, answer="2 (7 x 146 = 1,022)"),
        dict(q="A lamp glows when the number entered is divisible by 6. Which number makes it glow?", opts=["46", "54", "64", "74"], answer="b) 54"),
        dict(q="A number divisible by both 4 and 6 must also be divisible by ...", opts=["10", "12", "24", "only 2"], answer="b) 12, the lowest common multiple"),
        dict(q="Today is Monday. What day will it be 100 days from today?", opts=["Tuesday", "Wednesday", "Thursday", "Monday"], answer="b) Wednesday (100 = 14 x 7 + 2)"),
    ],
    build=dict(intro="The divisibility test for 11 as an algorithm.",
               cards=[("Input a number", "event", "#E5484D"), ("Set total to 0 and sign to +", "step", "#3B82F6"), ("Repeat for each digit from the left", "loop", "#F5A524"),
                      ("add sign x digit to total, then flip the sign", "step", "#3B82F6"), ("If total is divisible by 11", "if", "#8B5CF6"), ("say 'divisible by 11'", "step", "#3B82F6")],
               task="Trace it for 9,174 and for 5,213.",
               answer="9,174: 9 - 1 + 7 - 4 = 11, divisible (9,174 = 11 x 834). 5,213: 5 - 2 + 1 - 3 = 1, not divisible"),
    challenge=dict(q="Find the smallest number that leaves a remainder of 1 when divided by 2, 3, 4, 5 or 6, and is divisible by 7.",
                   answer="301: numbers 1 more than a multiple of 60 are 61, 121, 181, 241, 301, ...; the first divisible by 7 is 301 = 7 x 43"),
    ican=["use divisibility rules", "work with remainders", "trace a divisibility algorithm"],
))

CH.append(dict(
    n=6, title="We Distribute Yet Things Multiply", skill="The distributive property and identities for fast calculation", level="C7", color="#E5484D",
    robo="23 x 47 looks hard. Break it into (20 + 3) x (40 + 7) and I only need easy multiplications!",
    learn=["The <b>distributive property</b> says a(b + c) = ab + ac. With two brackets, every part multiplies every part: (a + b)(c + d) = ac + ad + bc + bd. "
           "An <b>area model</b> shows each part as a rectangle.",
           "Some results are true for every number. These <b>identities</b> make calculation fast: (a + b)² = a² + 2ab + b², (a - b)² = a² - 2ab + b² and "
           "(a + b)(a - b) = a² - b². So 103 x 97 = 100² - 3² = 9,991. Computers use the same tricks to multiply huge numbers quickly."],
    words=[("distributive property", "a(b + c) = ab + ac"), ("identity", "true for every number"), ("expand", "multiply out the brackets"), ("factorise", "write as a product")],
    example=dict(title="23 x 47 with an area model",
                 steps=["Split: 23 = 20 + 3 and 47 = 40 + 7.", "Multiply each part: 800, 140, 120 and 21 (the model is not to scale).",
                        "Add: 800 + 140 + 120 + 21 = <b>1,081</b>."],
                 fig=lambda: F.area_model((20, 3), (40, 7))),
    practice=[
        dict(q="Use (a + b)(a - b) = a² - b² to work out 102 x 98.", boxes=1, answer="9,996 (10,000 - 4)"),
        dict(q="Expand 3(2x + 5).", opts=["6x + 15", "6x + 5", "5x + 8", "2x + 15"], answer="a) 6x + 15"),
        dict(q="If a + b = 7 and ab = 10, what is a² + b²?", boxes=1, answer="29 (49 - 2 x 10)"),
        dict(q="Work out 47² - 43² the quick way.", opts=["360", "16", "400", "90"], answer="a) 360 = (47 + 43)(47 - 43) = 90 x 4"),
        dict(q="(x + 3)(x + 5) expands to ...", opts=["x² + 8x + 15", "x² + 15", "x² + 8x + 8", "2x + 8"], answer="a) x² + 8x + 15"),
    ],
    build=dict(intro="A function that multiplies two numbers using squares.",
               cards=[("Define times(a, b)", "step", "#14A3A3"), ("set m to (a + b) ÷ 2", "step", "#3B82F6"), ("set d to (a - b) ÷ 2", "step", "#3B82F6"),
                      ("give back m x m - d x d", "step", "#14A3A3")],
               task="Use it for times(54, 46) and times(61, 59). Check one answer the long way.", answer="54 x 46: 50² - 4² = 2,500 - 16 = 2,484. 61 x 59: 60² - 1² = 3,599"),
    challenge=dict(q="Why does times(a, b) work most easily when a and b are both even or both odd? Does it still work for 7 x 4?",
                   answer="Otherwise (a + b) ÷ 2 is not a whole number. It still works with halves: 5.5² - 1.5² = 30.25 - 2.25 = 28"),
    ican=["use the distributive property", "use identities to calculate quickly", "expand two brackets with an area model"],
))

CH.append(dict(
    n=7, title="Proportional Reasoning", skill="Ratios, the unitary method and scaling", level="C7", color="#EC4899",
    robo="To scale a recipe, I find the amount for one person, then multiply. It's the unitary method, and it's an algorithm!",
    learn=["A <b>ratio</b> compares two quantities, like 3 : 5. Ratios are <b>in proportion</b> when they are equivalent: 3 : 5 = 12 : 20, because 3 x 20 = 5 x 12.",
           "In <b>direct proportion</b> both grow together (more people, more rice). In <b>inverse proportion</b> one grows as the other shrinks (more painters, fewer days). "
           "The <b>unitary method</b> finds the value for one unit first, then scales up or down."],
    words=[("ratio", "a comparison like 3 : 5"), ("proportion", "two equal ratios"), ("unitary method", "find the value for one first"), ("inverse proportion", "one up, the other down")],
    example=dict(title="Direct and inverse proportion",
                 steps=["Rice: 4 people need 300 g. One person needs 300 ÷ 4 = 75 g, so 10 people need 75 x 10 = <b>750 g</b> (direct).",
                        "Painting: 6 painters take 10 days, which is 60 painter-days of work.",
                        "15 painters share the same 60 painter-days: 60 ÷ 15 = <b>4 days</b> (inverse)."]),
    practice=[
        dict(q="Simplify 36 : 48.", opts=["3 : 4", "4 : 3", "6 : 8", "9 : 16"], answer="a) 3 : 4"),
        dict(q="A map has a scale of 1 cm : 5 km. Two towns are 7.5 cm apart on the map. How far apart are they?", boxes=1, answer="37.5 km"),
        dict(q="Three children's ages are in the ratio 2 : 3 : 4 and add up to 45. How old is the oldest?", boxes=1, answer="20 (10, 15 and 20)"),
        dict(q="8 workers finish a job in 12 days. How long would 6 workers take?", opts=["9 days", "16 days", "10 days", "18 days"], answer="b) 16 days (96 worker-days ÷ 6)"),
        dict(q="Which ratio is in proportion with 3 : 5?", opts=["12 : 20", "9 : 12", "5 : 3", "6 : 8"], answer="a) 12 : 20"),
    ],
    build=dict(intro="A function that scales a recipe.",
               cards=[("Define scale(amount, from_people, to_people)", "step", "#14A3A3"), ("give back amount ÷ from_people x to_people", "step", "#14A3A3"),
                      ("say scale(300, 4, 10) g of rice", "step", "#3B82F6"), ("say scale(2, 4, 10) cups of milk", "step", "#3B82F6")],
               task="What does the program say? Is a recipe an example of direct or inverse proportion?", answer="750 g of rice and 5 cups of milk; direct proportion"),
    challenge=dict(q="A mixture has milk and water in the ratio 5 : 3 and holds 40 litres. How much water must be added to make the ratio 1 : 1?",
                   answer="10 litres: there are 25 litres of milk and 15 of water, so 10 more litres of water are needed"),
    ican=["simplify and compare ratios", "use the unitary method", "tell direct from inverse proportion"],
))

# ------------------------------------------------------------------ Part 2: artificial intelligence (CBSE handbook AI chapters)
AI = dict(level="C8", skill_prefix="AI skill: ")


def ai(k, **kw):
    d = dict(AI, n=7 + k, badge=f"AI{k}", kicker=f"AI CHAPTER {k}", short=f"AI {k}",
             source=f"Goes with the AI part of CBSE's Class 8 CT&AI handbook, chapter {k}")
    d.update(kw)
    d["toc"] = f"AI {k}. {d['title']}"
    d["header"] = f"AI chapter {k}  ·  {d['title']}"
    return d


CH.append(ai(
    1, title="AI Project Lifecycle", skill="Define, collect, train, test and deploy", color="#8B5CF6",
    robo="Building an AI is a project with stages. Get the problem and the data right first, or the model will be wrong!",
    learn=["An <b>AI project</b> builds a smart system that learns from data. Not every problem needs AI: a car wash that runs the same steps for every car is automation. "
           "The <b>AI project lifecycle</b> has five stages: (1) <b>define the problem</b>, (2) <b>collect and prepare data</b>, (3) <b>train a model</b>, "
           "(4) <b>evaluate and refine</b> it, and (5) <b>deploy</b> it for real use.",
           "Raw data is messy. <b>Cleaning</b> removes missing values, duplicates, wrong values and irrelevant data. A model is tested on <b>test data</b> it has never seen, "
           "and its <b>accuracy</b> is the share of predictions it gets right."],
    words=[("problem statement", "what the AI must do"), ("data cleaning", "fixing messy data"), ("model", "what the AI learns from data"), ("deployment", "putting it to real use")],
    example=dict(title="Cleaning a small dataset before training",
                 steps=["The goal: predict whether a student will score more than 75%. Each row is one past student.",
                        "Rows 2 to 5 each have a problem. Fill or drop the missing value, delete the duplicate, check the impossible value and drop the irrelevant column.",
                        "Only clean, labelled data goes into training. Bad data in means bad predictions out."],
                 table=[["Row", "Data", "Problem"], ["1", "Asha, 6 h study, 92%", "OK"], ["2", "Ben, (blank), 81%", "missing value"], ["3", "Asha, 6 h study, 92%", "duplicate of row 1"],
                        ["4", "Chetan, 25 h a day, 78%", "impossible value"], ["5", "Dev, 4 h, 85%, likes blue", "'likes blue' is irrelevant"]], widths=[40, 200, 170]),
    practice=[
        dict(q="What is the first stage of an AI project?", opts=["define the problem", "deploy the model", "train the model", "collect prizes"], answer="a) define the problem"),
        dict(q="A model gets 18 of 24 test cases right. What is its accuracy?", boxes=1, answer="75%"),
        dict(q="Which of these does NOT need AI?", opts=["a car wash that runs the same steps for every car", "spotting spam emails", "reading handwriting"],
             answer="a) the car wash: it is automation"),
        dict(q="Why is test data kept apart from training data?", opts=["to check the model on data it has not seen", "to make training faster", "it is not needed"],
             answer="a) to check the model on data it has not seen"),
        dict(q="A dataset has the same row twice. Which step fixes this?", opts=["remove duplicates", "fill missing values", "label the data"], answer="a) remove duplicates"),
    ],
    build=dict(intro="An online shop wants an AI that predicts whether a delivery will be late. Plan the project.",
               cards=[("Define: predict 'late' or 'on time' for each order", "step", "#3B82F6"), ("Collect: distance, weather, traffic and result of past orders", "step", "#3B82F6"),
                      ("Prepare: clean the data and label each order", "step", "#3B82F6"), ("Train on 80% of the orders", "step", "#3B82F6"),
                      ("Test on the other 20%; work out accuracy", "step", "#3B82F6"), ("If accuracy is too low, improve the data and retrain", "if", "#8B5CF6")],
               task="The model gets 34 of 40 test orders right. What is its accuracy? The shop needs 90%. Should it deploy the model?",
               answer="85%. Not yet: it should improve the data (for example more orders in bad weather) and retrain"),
    challenge=dict(q="Plan an AI that spots fake news: write one line for each stage of the lifecycle.",
                   answer="Open answer, for example: define 'real or fake headline'; collect checked real and fake headlines; clean and label them; train; test on new headlines; refine and only deploy with human checks"),
    ican=["name the stages of an AI project", "clean a small dataset", "measure accuracy and decide whether to deploy"],
))

CH.append(ai(
    2, title="AI and Its Applications", skill="AI for people and planet; training no-code models", color="#2BB673",
    robo="With a no-code tool I can train my own model: give it labelled examples, train, test, and improve the data!",
    learn=["AI is helping across India: <b>satellite images</b> help find plastic dumping, <b>air-quality forecasts</b> warn people on bad days, <b>camera traps</b> count wildlife, "
           "<b>farm apps</b> diagnose crop problems from photos, and AI tools that read <b>chest X-rays</b> help screen for tuberculosis. Cities use AI for traffic, and schools for personalised learning.",
           "<b>No-code tools</b> let anyone train a model: create <b>classes</b> (labels), add varied examples for each, train, then test with new examples. "
           "If the model fails, the fix is usually <b>better data</b>: more examples, more variety in background, light and voices."],
    words=[("no-code tool", "builds models without coding"), ("class", "one label a model can choose"), ("sensor", "a device that measures"), ("early warning", "an alert before harm")],
    example=dict(title="Training a waste-sorting model with a no-code tool",
                 steps=["Make three classes: plastic, paper and organic. Take 20-30 photos for each, with different backgrounds and light.",
                        "Upload and label the photos, then click train.", "Test with items the model has never seen. Note every mistake, add better photos and train again."],
                 fig=lambda: F.item_cards([("water bottle", "plastic", F.BLUE), ("old newspaper", "paper", F.ORANGE), ("banana peel", "organic", F.GREEN),
                                           ("chips packet", "?", F.SOFT)], w=96)),
    practice=[
        dict(q="Finding plastic dumps in satellite images is AI helping ...", opts=["the environment", "banking", "sport"], answer="a) the environment"),
        dict(q="AI tools that read chest X-rays for signs of TB help ...", opts=["healthcare", "transport", "entertainment"], answer="a) healthcare"),
        dict(q="A no-code AI tool lets you ...", opts=["train a model without writing code", "build a computer", "skip collecting data"], answer="a) train a model without writing code"),
        dict(q="Your waste model works well in class but badly in the canteen. What is the most likely reason?",
             opts=["all its photos had the classroom background", "the canteen is too big", "AI cannot see food"], answer="a) its training photos all had the same background"),
        dict(q="A voice-command model works for you but not for your grandmother. What should you do?",
             opts=["record samples from many different voices", "speak louder", "delete the model"], answer="a) train it with samples from many different voices"),
    ],
    build=dict(intro="Plan a no-code voice-command model.",
               cards=[("Classes: 'lights on', 'lights off', background noise", "step", "#3B82F6"), ("Record 15-20 samples of each: loud, soft, fast, slow", "step", "#3B82F6"),
                      ("Train the model", "step", "#3B82F6"), ("Test with new voices", "step", "#3B82F6"),
                      ("If a class is often wrong, add more varied samples and retrain", "if", "#8B5CF6")],
               task="It was tested 30 times: 'lights on' 9 of 10 right, 'lights off' 6 of 10, noise 10 of 10. Which class needs more data? What is the overall accuracy?",
               answer="'lights off' needs more varied samples; overall 25 of 30, about 83%"),
    challenge=dict(q="Pick a problem in your school or town. Which kind of AI could help (vision, language or data), and what data would it need?",
                   answer="Open answer, for example: a camera model that spots overflowing bins, trained on labelled photos of full and empty bins"),
    ican=["give examples of AI helping society", "describe how a no-code model is trained", "improve a model by improving its data"],
))

CH.append(ai(
    3, title="Data and Fairness in AI", skill="Spot unbalanced data and rebalance it", color="#F5A524",
    robo="I copy the patterns in my training data. If one group is missing or rare, I will be unfair to it, without even knowing!",
    learn=["An AI looks for patterns in its <b>training data</b>. If a group is <b>over-represented</b> (too many examples) or <b>under-represented</b> (too few), "
           "predictions become unfair. A face detector trained mostly on one group may fail for others, and a translator trained on more 'male doctor' sentences "
           "may turn a gender-neutral Hindi sentence into 'He is a doctor'.",
           "Fairness needs <b>representative</b> data: varied examples of every group and situation. Test each group separately, and <b>rebalance</b> the data by "
           "adding examples of the groups that are missing. Do not use features like gender to decide things they should not decide."],
    words=[("representative", "includes every group fairly"), ("over-represented", "too many examples"), ("under-represented", "too few examples"), ("rebalance", "even out the data")],
    example=dict(title="A sports-recommendation model (practice data)",
                 steps=["A survey asked which sport students enjoyed. Most boys chose cricket and most girls chose badminton.",
                        "A model that learns from this would recommend badminton to every new girl, based on a pattern, not on her interest or ability.",
                        "Fairer: recommend from each student's own interests and skills, and do not use gender as a feature."],
                 table=[["Sport", "Boys", "Girls"], ["Cricket", "48", "14"], ["Badminton", "12", "26"]], widths=[130, 130, 130]),
    practice=[
        dict(q="A model was trained on 90 photos of cricket bats and 10 of badminton rackets. Shown an unclear photo, what is it most likely to say?",
             opts=["cricket bat", "badminton racket"], answer="a) cricket bat, because that class dominates its training data"),
        dict(q="How should you fix the model in question 1?", opts=["add more varied racket photos", "add more bat photos", "remove the racket photos"], answer="a) add more varied racket photos"),
        dict(q="A translator turns a gender-neutral sentence into 'He is a doctor'. Why?",
             opts=["its training text had more examples of male doctors", "doctors are always men", "the translator is broken"], answer="a) its training data had more male doctors"),
        dict(q="A face detector works badly for people with darker skin. Its training data was ...", opts=["not representative", "too large", "too colourful"], answer="a) not representative"),
        dict(q="A dataset has 300 dog photos and 100 cat photos. What percentage are cats?", boxes=1, answer="25%"),
    ],
    build=dict(intro="A rebalancing plan for an image dataset.",
               cards=[("Count the examples in each class", "step", "#3B82F6"), ("Repeat until no class is less than half the biggest", "loop", "#F5A524"),
                      ("collect more varied examples of the smallest class", "step", "#3B82F6"), ("Retrain and test each class separately", "step", "#3B82F6")],
               task="Classes: dogs 300, cats 100, rabbits 40. How many more cats and rabbits are needed so that no class is less than half the biggest?",
               answer="Half of 300 is 150, so 50 more cats and 110 more rabbits"),
    challenge=dict(q="Can a dataset be balanced in numbers but still unfair? Give an example.",
                   answer="Yes: 100 cat and 100 dog photos, but every cat is indoors and every dog outdoors, so the model learns the background; or all photos come from one region"),
    ican=["spot over- and under-represented data", "explain how unbalanced data leads to unfair results", "plan how to rebalance a dataset"],
))

CH.append(ai(
    4, title="Ethics and Responsible AI", skill="Privacy, checking facts and human accountability", color="#E5484D",
    robo="An AI can be fast and accurate and still be wrong to use. Responsible AI is fair, safe, open and respects your privacy!",
    learn=["<b>Responsible AI</b> is fair, safe, transparent and good for society. <b>Privacy</b> means your personal data (name, location, photos, health) stays under your control: "
           "give <b>consent</b> only when an app really needs the data for its job.",
           "AI can also spread <b>misinformation</b>, including fake images and videos, so check facts with trusted sources and read beyond headlines. "
           "<b>Accountability</b> means people, not machines, are responsible for decisions made with AI; in hospitals, banks and courts a human must review."],
    words=[("privacy", "control over your personal data"), ("consent", "agreeing to share data"), ("misinformation", "false information that spreads"), ("accountability", "people answer for AI decisions")],
    example=dict(title="Which permissions should an app get?",
                 steps=["Ask: does the app need this data to do its job?", "If not, deny it. If yes, give the smallest permission that works, such as 'only while using the app'.",
                        "Check permissions again from time to time and remove ones you no longer need."],
                 table=[["App asks for", "Needed for its job?", "Decision"], ["Torch app: contacts", "No", "Deny"], ["Maps app: location", "Yes, while in use", "Allow while using"],
                        ["Photo editor: photos", "Only the chosen ones", "Allow selected photos"], ["Quiz game: microphone", "No", "Deny"]], widths=[140, 130, 140]),
    practice=[
        dict(q="A torch app asks to read your contacts. What should you do?", opts=["deny it", "allow it", "allow it once"], answer="a) deny it: a torch does not need contacts"),
        dict(q="A shocking video of a famous person may be fake. What should you do first?", opts=["check trusted news sources", "share it at once", "comment on it"], answer="a) check trusted news sources"),
        dict(q="An AI in a hospital marks a patient as high risk. Who decides the treatment?", opts=["the doctor", "the AI", "the patient's neighbour"], answer="a) the doctor, after reviewing the AI's suggestion"),
        dict(q="Which of these is personal data?", opts=["your home address", "the capital of India", "a maths formula"], answer="a) your home address"),
        dict(q="An AI system is fast and accurate for most people but often wrong for one group. Is it responsible to keep using it as it is?",
             opts=["no: it harms that group, so it must be fixed", "yes: most people are fine"], answer="a) no: it must be fixed for that group"),
    ],
    build=dict(intro="A responsible-AI checklist written as rules.",
               cards=[("Before using an AI tool", "event", "#E5484D"), ("If it asks for data it does not need", "if", "#8B5CF6"), ("deny the permission", "step", "#3B82F6"),
                      ("If its answer affects a person", "if", "#8B5CF6"), ("a human checks before acting", "step", "#3B82F6"), ("If you share its output", "if", "#8B5CF6"),
                      ("check the facts first", "step", "#3B82F6")],
               task="Use the checklist: an AI homework helper asks for your location and contacts, and gives you a 'fact' for your project.",
               answer="Deny location and contacts; check the fact with a trusted source before using it, and say that you used AI"),
    challenge=dict(q="If an AI system makes a harmful mistake, who should be responsible: the machine, its makers, or the people using it? Explain.",
                   answer="People: the makers and the organisation using it are accountable, because a machine cannot be held responsible"),
    ican=["protect my personal data", "check information before sharing", "explain why humans stay accountable for AI"],
))

# ------------------------------------------------------------------ Projects (2 x 20 hours)
PROJECTS = []


def project(k, **kw):
    d = dict(n=100 + k, badge=f"P{k}", kicker=f"PROJECT {k}  ·  20 HOURS", short=f"Project {k}", level="C8", skill_prefix="Project skill: ",
             source="CBSE: 40 project hours a year in Class 8, as two projects of 20 hours")
    d.update(kw)
    d["toc"] = f"Project {k}. {d['title']}"
    d["header"] = f"Project {k}  ·  {d['title']}"
    return d


PROJECTS.append(project(
    1, title="Sports for Everyone", skill="Survey, analyse with ratios and recommend changes", color="#3B82F6",
    question="Which students in our school play sport regularly, and what change could get more students active?",
    brief=["Your team runs an anonymous survey of at least 60 students: which class they are in, whether they play a sport at least three times a week, which sports, "
           "and, if not, why not. Ask permission first and collect no names.",
           "Clean the data, work out percentages and ratios for each class, draw honest charts and look for patterns. Then recommend one or two changes, "
           "backed by your data, and plan how to test whether they work."],
    words=[("survey", "asking people the same questions"), ("anonymous", "no names collected"), ("percentage", "part ÷ whole x 100"), ("recommendation", "advice backed by evidence")],
    robo="Data can change things! Collect it fairly, analyse it honestly, and let the evidence decide your recommendation.",
    plan=[("1", "Define", "Agree the question and what 'plays regularly' means."),
          ("2", "Design", "Write 5-6 clear survey questions. Plan how to ask permission and keep answers anonymous."),
          ("3", "Collect", "Survey at least 60 students from different classes."),
          ("4", "Clean", "Remove duplicates and blank forms. Note anything odd."),
          ("5", "Analyse", "Work out percentages and ratios for each class, and the most common reasons."),
          ("6", "Show", "Draw a bar chart for each class and a pie chart of reasons, with honest scales."),
          ("7", "Find patterns", "Write three observations and one conclusion, with its limits."),
          ("8", "Recommend", "Suggest one or two changes and how you would test them."),
          ("9", "Present", "Present to your class or sports teacher in 3 minutes."),
          ("10", "Reflect", "Score your work with the rubric and write what you would change.")],
    example=dict(title="From survey to recommendation (practice data)",
                 steps=["80 students answered. Participation falls in the higher classes: 72% in Class 6 but only about 36% in Class 8.",
                        "The most common reason given in Class 8 was 'no time after school'.",
                        "Recommendation: a 20-minute lunchtime games slot for Class 8, then survey again after a month to see if participation rises."],
                 table=[["Class", "Play regularly", "Percentage"], ["6", "18 of 25", "72%"], ["7", "15 of 27", "about 56%"], ["8", "10 of 28", "about 36%"]], widths=[100, 150, 150]),
    sheet=dict(title="Survey tally sheet", intro="One row per class. Count answers with tallies first, then fill in the totals.",
               header=["Class", "Students asked", "Play regularly", "Percentage", "Most common reason for not playing"], widths=[55, 85, 95, 75, 205], blank=7, row_h=20),
    draw=[dict(title="My charts", text="Draw a bar chart of the percentage who play regularly in each class. Give it a title, labels and a scale that starts at 0.", h=140)],
    rubric=[("Question", "A clear question about real participation."),
            ("Survey", "Fair, anonymous questions; permission asked; 60 or more answers."),
            ("Analysis", "Percentages and ratios correct; patterns found."),
            ("Charts", "The right chart types, honest scales and clear labels."),
            ("Recommendation", "Changes backed by the data, with a plan to test them."),
            ("Teamwork and talk", "Work shared fairly; a clear presentation.")],
    ethics=["We asked permission and explained how answers would be used.", "We collected no names, only class and answers.",
            "We did not recommend sports to anyone by gender.", "We reported results honestly, even surprising ones."],
    reflect=["What surprised you in your data?", "How would you find out whether your recommendation worked?"],
    answer="Open project: assess with the rubric. Check percentages: part ÷ whole x 100, for example 18 ÷ 25 x 100 = 72%.",
))

PROJECTS.append(project(
    2, title="Fair AI Audit", skill="Test a classifier for bias, rebalance and report", color="#8B5CF6",
    question="Is a picture classifier equally good for everything it is used on, and can we make it fairer?",
    brief=["Your team audits a classifier: one you train with a no-code tool, like the cat-and-dog activity in CBSE's handbook, or the card version from your kit. "
           "Build a balanced test set it has never seen and measure the accuracy for each group.",
           "Then study the training data: which groups or situations are missing or rare? Rebalance it, retrain, test again on the same test set, and write an audit report "
           "with your findings, your fix and the limits that remain."],
    words=[("audit", "a careful, independent check"), ("test set", "examples kept back for checking"), ("group accuracy", "accuracy for one group"), ("gap", "difference between groups")],
    robo="An audit doesn't trust the overall score. Check every group, find the gap, fix the data, and test again!",
    plan=[("1", "Define", "Choose the classifier and the groups to compare (for example cats and dogs, indoor and outdoor)."),
          ("2", "Prepare", "Build a balanced test set: 20 unseen examples per group."),
          ("3", "Test", "Run every test example and record the prediction and the true label."),
          ("4", "Measure", "Work out the accuracy for each group and the gap between them."),
          ("5", "Investigate", "Count the training examples per group. How are they alike, and how are they different?"),
          ("6", "Rebalance", "Add varied examples of the weak group: other backgrounds, lights and types."),
          ("7", "Retest", "Retrain and test again on the same test set."),
          ("8", "Compare", "Make a before-and-after table and a bar chart."),
          ("9", "Report", "Write the audit report: findings, fix, remaining limits and advice."),
          ("10", "Reflect", "Score your work with the rubric. Where could such gaps harm people?")],
    example=dict(title="An audit in numbers (practice data)",
                 steps=["Training data: 120 dog photos of many breeds, mostly outdoors; only 30 cat photos, mostly indoors.",
                        "Before: dogs 95% right but cats only 55%, a gap of 40 points, hidden inside 75% overall.",
                        "After adding 90 varied cat photos: dogs 90%, cats 85%. The gap shrank to 5 points and overall accuracy rose to 87.5%."],
                 table=[["", "Before", "After"], ["Dogs right", "19 of 20 (95%)", "18 of 20 (90%)"], ["Cats right", "11 of 20 (55%)", "17 of 20 (85%)"],
                        ["Overall", "30 of 40 (75%)", "35 of 40 (87.5%)"]], widths=[110, 150, 150]),
    sheet=dict(title="Audit record", intro="One row per test image. Write notes about anything that might matter, like background or light.",
               header=["Image", "Group", "True label", "Predicted", "Right? (Y/N)", "Notes"], widths=[55, 70, 80, 80, 75, 155], blank=9, row_h=19),
    rubric=[("Audit question", "Clear groups to compare and a fair, balanced test set."),
            ("Testing", "Accuracy measured for each group on unseen data."),
            ("Investigation", "Training data counted and its gaps explained."),
            ("Improvement", "Data rebalanced and the model retested on the same test set."),
            ("Report", "Findings, fix and remaining limits stated honestly."),
            ("Teamwork and talk", "Work shared fairly; a clear presentation.")],
    ethics=["We used only pictures we were allowed to use, with no photos of people.", "We tested every group with the same kind of test set.",
            "We reported the gap honestly, even after our fix.", "We said what our audit cannot show."],
    reflect=["What caused the biggest unfairness in your classifier?", "Where in real life could a gap like this harm people?"],
    answer="Open project: assess with the rubric. Group accuracy = right answers for that group ÷ test images in that group.",
))

FACTS = {
    1: "Srinivasa Ramanujan noticed that 1729 is the smallest number that is a sum of two cubes in two ways: 1³ + 12³ and 9³ + 10³.",
    2: "On the chessboard of the story, doubling grains on all 64 squares would need more than 18 quintillion grains in all.",
    3: "Computers store letters as numbers: in Unicode, capital A is number 65, which is 1000001 in binary.",
    4: "Floor tiles and tessellations use quadrilaterals because some of them fit together with no gaps.",
    5: "Book ISBNs end in a check digit worked out with remainders, so a scanner can catch a mistyped number.",
    6: "Fast methods that computers use to multiply huge numbers split them into parts, just like the distributive property.",
    7: "Maps, scale models and recipes all rely on proportion: every part is scaled by the same ratio.",
    8: "AI teams often spend a large share of their time collecting and cleaning data before training any model.",
    9: "In India, AI tools that read chest X-rays are being used to help screen people for tuberculosis.",
    10: "A face-detection program once reported 'faces' in photos of clouds, showing what its training data had taught it.",
    11: "India's Digital Personal Data Protection Act, 2023 generally requires organisations to get your consent before using your personal data.",
}


# ------------------------------------------------------------------ specimen: classroom kit illustration (Classes 6-8)
def _kit_items():
    from reportlab.platypus import Table, TableStyle, Paragraph, Spacer
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib import colors
    sm = ParagraphStyle("kitsm", fontName="Kid", fontSize=9, leading=12, textColor=F.SOFT)
    q = ParagraphStyle("kitq", fontName="Kid", fontSize=10, leading=13.5, textColor=F.INK)
    head = ParagraphStyle("kith", parent=q, fontName="KidB", textColor=colors.white)
    items = Table([[F.pipes_compare(20, (10, 2, 3), w=240, bar_h=14),
                    F.item_cards([("12 km, rain, heavy", "late", F.RED), ("3 km, clear, light", "on time", F.GREEN)], w=100, h=42, per_row=2)],
                   [Paragraph("<b>Number-base pipe strips</b>: decimal, binary, ternary (10 sets)", sm), Paragraph("<b>Dataset cards</b>: deliveries and sports survey (2 decks)", sm)],
                   [F.item_cards([("cat, indoors", "cat", F.ORANGE), ("dog, outdoors", "dog", F.BLUE), ("cat, outdoors", "?", F.SOFT)], w=74, h=42),
                    F.item_cards([("2 pairs parallel", "property", F.PURPLE), ("all angles 90°", "property", F.PURPLE), ("4 equal sides", "property", F.PURPLE)], w=74, h=42)],
                   [Paragraph("<b>AI audit picture cards</b>: cats and dogs, bats and rackets (120)", sm), Paragraph("<b>Shape property and classifier cards</b> (30)", sm)]],
                  colWidths=[515.27 / 2, 515.27 / 2])
    items.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("ALIGN", (0, 0), (-1, -1), "CENTER"), ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                               ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F7F9FC")), ("ROUNDEDCORNERS", [10, 10, 10, 10])]))
    rows = [["Item", "Quantity per kit"], ["Number-base pipe strips", "10 sets"], ["Dataset cards (deliveries, sports survey)", "2 decks of 40"],
            ["AI audit picture cards", "120"], ["Shape property and classifier cards", "30"], ["Function, loop and decision card decks", "4 decks of 54"],
            ["Project data sheet pads (A4)", "2 pads of 50"], ["Project posters: AI lifecycle, rubric, fair AI", "3"], ["Teacher quick-guide card", "1"], ["Sturdy box", "1"]]
    data = [[Paragraph(c, head if i == 0 else q) for c in r] for i, r in enumerate(rows)]
    t = Table(data, colWidths=[515.27 - 140, 140])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#14A3A3")), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("TOPPADDING", (0, 0), (-1, -1), 4),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 5), ("LINEBELOW", (0, 1), (-1, -1), 0.5, colors.HexColor("#D6DEEA")), ("ROUNDEDCORNERS", [8, 8, 8, 8]),
                           ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F3F6FB")])]))
    return [items, Spacer(1, 10), t, Spacer(1, 6), Paragraph("Illustrations show the design. Final materials will be confirmed after the pilot.", sm)]


META = dict(
    textbook_short="NCERT maths, Class 8",
    textbook_long="the NCERT Class 8 maths textbook",
    cover_follows="Follows NCERT Class 8 maths, CBSE's four AI chapters and two projects",
    cover_tag="Computational thinking and AI for Class 8",
    cover_line="Theory, worked examples, practice, coding on paper, AI and projects",
    cover_cards=(("Repeat until n is 0", "step", F.ORANGE), ("give back m² - d²", "step", F.TEAL), ("If data is unbalanced", "step", F.PURPLE)),
    welcome="Welcome to Class 8! I am <b>Robo</b>. This year we write numbers in any base, sort shapes with if-else rules, calculate like a computer, "
            "run a full AI project from problem to model, make AI fairer, and lead two real projects.",
    projects_note="Two 20-hour team projects: plan, collect real data, build, test, present and score your work with a rubric.",
    front_cards=[("Step: do this", "step", "#3B82F6"), ("Repeat: a loop", "loop", "#F5A524"), ("If: a decision", "if", "#8B5CF6"),
                 ("Define: a function", "step", "#14A3A3"), ("When: an event", "event", "#E5484D")],
    chapters_note="Chapters 1-7 go with the same chapters of the NCERT Class 8 maths textbook, so they can be used in maths periods. "
                  "AI chapters 1-4 follow the AI part of CBSE's Class 8 handbook, and the two projects run across the year. ",
    hours_note="CBSE sets 100 hours a year in Class 8: about 40 for computational thinking, 20 for AI and 40 for two projects. "
               "The coding here needs no computer: students write, trace and debug programs on paper, which prepares them for block and text coding. ",
    levels_note="Levels: C6 squares, powers, number bases and shape classifiers; C7 divisibility, identities and proportion; C8 AI projects, fairness and ethics.",
    cutout_cards=[("Define ___", "step"), ("give back ___", "step"), ("Repeat until ___", "loop"), ("Repeat for each ___", "loop"), ("If ___", "if"), ("else", "if"),
                  ("AND", "if"), ("OR", "if"), ("Input ___", "event"), ("Set ___ to ___", "step"), ("change ___ by ___", "step"), ("say ___", "step")],
    sample=[3, 8],  # CT chapter 3 (number bases, C6) and AI chapter 1 (AI project lifecycle, C8)
    sample_projects=[102],  # Project 2: Fair AI Audit
    band=dict(
        about_title="A complete CT&amp;AI programme for Classes 6-8",
        about_intro="From 2026-27, CBSE asks schools to teach Computational Thinking and AI in Classes 3-8. In Classes 6-8 it is <b>100 hours a year</b>; "
                    "in Class 8 that is about 40 hours of computational thinking, 20 hours of AI and two projects of 20 hours each. CBSE's free handbook gives "
                    "puzzles for each maths chapter and four AI chapters. CodeSchool turns it into a full course any teacher can run, with or without a computer lab.",
        compare=[["What schools need", "CBSE's free handbook", "CodeSchool Projects and AI Pack"],
                 ["CT for each maths chapter", "Puzzles", "Theory, worked examples, practice in levels and coding on paper"],
                 ["AI chapters", "Four chapters with exercises and no-code labs", "The same four topics, with step-by-step activities, card versions of the labs and 'build it' tasks"],
                 ["Coding", "No", "Base converters, classifiers, test functions and data cleaning on paper, ready for block or text coding"],
                 ["Projects (40 hours)", "Hours set aside", "Two complete 20-hour projects with plans, data sheets and rubrics"],
                 ["Teacher lesson plans", "Answer keys", "A period-by-period teacher script book"],
                 ["Assessment", "No format given", "Project rubrics, observation journal and term summary"],
                 ["Teacher training", "CBSE workshops", "School orientation, termly workshops and support"]],
        why=["Chapters 1-7 follow NCERT Class 8 maths in order, so the CT work fits the maths period.",
             "The four AI chapters match the AI part of CBSE's handbook, with card versions of the no-code labs for schools without devices.",
             "Two ready-made projects fill the 40 project hours, with plans, data sheets and rubrics.",
             "Works in any classroom: paper, cards and posters. A projector or computer lab helps but is optional."],
        receives=[["For", "What they get", "Classes"],
                  ["Each student", "Projects and AI Pack: workbook with CT chapters, AI chapters, two project units and cut-out cards", "6, 7, 8"],
                  ["Each class section", "Classroom kit: number-base strips, dataset cards, AI audit picture cards, shape cards, data pads, posters, box", "6, 7, 8"],
                  ["Each teacher", "Teacher script book, answer keys, project rubrics, observation journal, short how-to videos", "6, 7, 8"],
                  ["The school", "Orientation at school, a workshop every term, a support line and a term summary format", "All"]],
        series=[["Book", "Levels", "Coder skills"],
                ["Classes 3-5 Practice Packs", "B1-B7", "Steps, loops, if-else, variables, search and a game designed on paper (separate samples)"],
                ["Class 6 Projects and AI Pack", "C1-C3", "Functions, lists, sieve and sorting, debugging, four AI chapters and two projects (separate sample)"],
                ["Class 7 Projects and AI Pack", "C4-C5", "Binary, formulas, logic filters, triangle checks, four AI chapters and two projects (separate sample)"],
                ["Class 8 Projects and AI Pack (this sample)", "C6-C8", "Number bases, classifiers, identities, proportion, the AI project lifecycle, fairness and two projects"]],
        price="<b>Indicative price:</b> Rs 599 per student per year (MRP) for the Classes 6-8 Projects and AI Pack, through the school's book list. "
              "It can replace an existing computer book, so the cost to parents stays about the same. Kits, teacher books and training come with the packs. "
              "Prices are indicative until confirmed in writing.",
        contents_intro="The complete book has 7 CT chapters that follow the NCERT Class 8 maths textbook, 4 AI chapters that follow CBSE's handbook and two 20-hour "
                       "projects, plus answers, a glossary and cut-out code cards. This sample includes CT chapter 3, AI chapter 1 and Project 2 in full.",
        kit_intro="One kit per class section, used all year. Everything is printed, laminated and reusable.",
        kit_items=_kit_items,
        assess=[["Skill", "Beginning", "Developing", "Secure", "Extending"],
                ["Algorithms", "Follows given steps", "Traces loops and conditions", "Writes converters and classifiers", "Designs, tests and improves algorithms"],
                ["Number structure", "Recalls facts", "Uses rules with help", "Uses bases, powers and identities", "Explains why rules work"],
                ["AI projects", "Names the stages", "Cleans data and measures accuracy", "Runs the lifecycle and tests per group", "Finds bias and fixes it with data"],
                ["Projects", "Takes part with help", "Completes stages with help", "Plans, tests and presents with the team", "Improves the work using evidence"]],
        summary=[["Area", "Level", "Teacher comment"],
                 ["Computational thinking (overall)", "Secure", "Converts between bases confidently and writes clear if-else classifiers."],
                 ["AI and ethics", "Secure", "Cleans data and measures accuracy; next step: explaining the limits of an audit."],
                 ["Project 2: Fair AI Audit", "Rubric 21 of 24", "Found a 40-point gap between groups and cut it to 5 points by rebalancing the data."]],
        parents_1="This year your child will learn <b>computational thinking and AI</b>, following CBSE's new curriculum for Classes 3-8. In Class 8 that is about "
                  "100 hours over the year: problem solving linked to maths, four AI chapters and two group projects.",
        parents_2="Your child will use the <i>Think Like a Coder</i> workbook. They will write numbers in different bases, sort shapes with rules, run an AI project "
                  "from problem to model, check AI for fairness, and learn to protect their privacy online.",
        home_tips=["Ask your child to explain how an AI learns from data, using an app you both use.",
                   "Look at the permissions on a family phone together. Does each app really need them?",
                   "When a shocking video or message arrives, check it together with a trusted source before sharing.",
                   "Praise careful thinking and honest results, even when a project does not go to plan."],
        take_home=("Write your year of birth in binary and in base 3. Which needs more digits, and why?", "answers vary; binary needs more digits because each place holds less."),
        cover_tag="Computational thinking and AI for Classes 6-8",
        cover_lines=("A sample for schools: a CT chapter, an AI chapter, a full project,", "a teacher script, the classroom kit and how assessment works"),
        cover_info="Class 8 sample  ·  NCERT maths chapters, CBSE AI chapters and projects  ·  Lab optional",
        cover_price="Projects and AI Pack Rs 599 per student (indicative)  ·  Free pilot, January-March 2027",
        back_line="Computational thinking and AI for Classes 6-8, for CBSE schools",
    ),
    teacher=dict(
        title="An AI project on paper",
        source="From the teacher book, Class 8, AI chapter 1 (<i>AI Project Lifecycle</i>). One 40-minute period. Level C8.",
        need=[["Kit", "Dataset cards: 24 past deliveries (distance, weather, traffic, late or on time), including 2 duplicates and 2 with missing values; scoring slips"],
              ["Book", "AI chapter 1 pages, 'Try it' questions 2-5"],
              ["Goal", "Students run every stage of the AI project lifecycle by hand: define, clean, train a rule, test it on unseen cards and decide whether to deploy"]],
        steps=[["1. Predict and run (8 min)", "Read the problem: predict whether a delivery will be late. Hand out the 24 dataset cards.",
                "Groups predict which features will matter most, then clean the deck: remove duplicates and cards with missing values."],
               ["2. Investigate (8 min)", "Ask groups to put 5 cards aside as test cards without looking at them.",
                "Using the other cards, find a rule, such as 'heavy traffic and over 10 km means late'."],
               ["3. Modify (8 min)", "Groups test their rule on the 5 unseen cards.", "Count correct predictions and work out the accuracy."],
               ["4. Put in order (8 min)", "Give out jumbled stage cards: define, collect, prepare, train, test, deploy.", "Order the lifecycle and match each stage to what they did."],
               ["5. Make (8 min)", "Ask: 'Your rule is 60% accurate. Would you deploy it? What would you change?'", "Improve the rule or suggest new data, and give a deploy decision with a reason."]],
        setup_fig=lambda: F.item_cards([("12 km, rain, heavy traffic", "late", F.RED), ("3 km, clear, light traffic", "on time", F.GREEN),
                                        ("8 km, clear, heavy traffic", "late", F.RED), ("5 km, rain, light traffic", "on time", F.GREEN)], w=108, h=44, per_row=2),
        setup_w=230,
        setup_text="<b>Set-up:</b> shuffle the dataset cards, including the 2 duplicates and 2 cards with missing values, so cleaning is a real step. Keep 5 cards unseen for testing.",
        mistakes=["<b>Testing on the training cards.</b> A rule always looks good on the examples it was made from; only unseen cards give a fair score.",
                  "<b>Skipping cleaning.</b> Duplicates make one order count twice and can tip the rule the wrong way.",
                  "<b>Deploying because it is 'mostly right'.</b> Decide what accuracy is good enough before testing, and say who is affected by the mistakes."],
        paces="<b>Support:</b> give groups a starting rule and ask them only to clean, test and count.<br/><b>Stretch:</b> compare two rules on the same test cards and argue "
              "which to deploy; work out accuracy for 'late' and 'on time' cards separately.",
        check=["Two quick questions at the end of the period:",
               "1. Why must the test cards be kept apart from the training cards? (to check the rule on data it has not seen)&nbsp;&nbsp; "
               "2. A rule gets 4 of 5 test cards right. What is its accuracy? (80%)",
               "Note in the observation journal: <b>Beginning</b> (names some stages), <b>Developing</b> (cleans data with help), "
               "<b>Secure</b> (runs every stage and works out accuracy), <b>Extending</b> (justifies a deploy decision from the results)."],
        link="CBSE's Class 8 handbook presents the AI project lifecycle, from problem definition and data preparation to training, evaluation and deployment. "
             "In this lesson students run every stage by hand before they use a no-code tool.",
    ),
)
