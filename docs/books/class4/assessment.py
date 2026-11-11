"""Chapter assessments for 'Think Like a Coder - Class 4'. One 10-mark test per chapter: Section A (3 x 1-mark multiple choice),
Section B (2 x 2-mark short answers), Section C (1 x 3-mark task). Original questions, different from the workbook."""
import figures_c4 as F


def A(q, opts, answer, **kw):
    return dict(s="A", q=q, opts=opts, answer=answer, **kw)


def B(q, answer, guide="", **kw):
    return dict(s="B", q=q, answer=answer, guide=guide, **kw)


def C(q, answer, guide="", **kw):
    return dict(s="C", q=q, answer=answer, guide=guide, **kw)


def flipped_coins():
    return F.coin_grid(["BWBW", "BBBW", "BBWW", "WWWW"], cell=22, check=True)


def network_962():
    return F.sorting_network(inputs=(9, 6, 2), w=300)


def animal_tree():
    return F.decision_tree("Does it have wings?", "bird", "Does it live in water?", "fish", "land animal", w=380)


def mirror_task():
    return F.mirror_grid({(0, 0), (1, 2), (3, 1)}, cell=20)


def colour_votes():
    return F.bar_chart([4, 8, 2, 6], ["Red", "Blue", "Green", "Yellow"], w=300, unit=9)


TESTS = {
    1: [A("How many faces does a cube have?", ["4", "6", "8", "12"], "b) 6"),
        A("The line where two faces meet is called ...", ["an edge", "a net", "a face"], "a) an edge"),
        A("A matchbox is a cuboid. How many corners does it have?", ["6", "8", "10", "12"], "b) 8"),
        B("A dice is a cube. Opposite faces add up to 7. Which number is opposite 2, and which is opposite 6?", "5 is opposite 2; 1 is opposite 6",
          "1 mark for each"),
        B("The net of a closed cube has 6 squares. How many squares does the net of an open box with no lid have? Why?", "5, because the lid is missing",
          "1 mark for 5, 1 mark for the reason"),
        C("Write exact steps to draw a rectangle 4 cm long and 2 cm wide with a ruler.",
          "1. Draw a straight line 4 cm long. 2. At each end draw a line 2 cm long, straight up. 3. Join the two tops with a line 4 cm long.",
          "1 mark for each clear step that gives a length or position")],
    2: [A("In 'if it is raining then take an umbrella else wear a cap', what is the condition?",
          ["it is raining", "take an umbrella", "wear a cap"], "a) it is raining"),
        A("Rule: if the number is more than 5 then say 'big' else say 'small'. What is said for 3?", ["big", "small", "nothing"], "b) small"),
        A("An if-else inside a loop is checked ...", ["only once", "every time the loop repeats", "never"], "b) every time the loop repeats"),
        B("Robo: repeat 4 times: move forward; if on a grey tile then say 'Splash' else say 'Step'. The tiles are white, grey, grey, white. What does Robo say?",
          "Step, Splash, Splash, Step", "2 marks; 1 mark if three words are right"),
        B("Write an if-then-else rule for a street light.", "If it is dark then switch the light on, else switch it off",
          "1 mark for a sensible condition, 1 mark for both actions"),
        C("For each number from 1 to 6: if the number is even then say 'clap' else say 'stamp'. Write what is said, and how many claps there are.",
          "stamp, clap, stamp, clap, stamp, clap; 3 claps", "2 marks for the list (1 mark with one slip), 1 mark for 3 claps")],
    3: [A("Which number is odd?", ["14", "20", "27", "32"], "c) 27"),
        A("Odd + odd is always ...", ["odd", "even", "zero"], "b) even"),
        A("A parity check makes each row have ... number of black coins.", ["an even", "an odd", "a big"], "a) an even"),
        B("A row of coins is black, white, black, black, white. Add one check coin so the row has an even number of black coins. Black or white? Why?",
          "Black, because there are 3 black coins and 3 is odd", "1 mark for black, 1 mark for the reason"),
        B("Each row should have an even number of 1s. Row P: 1 1 0 0. Row Q: 1 0 1 1. Row R: 0 1 0 1. Which row has a mistake?",
          "Row Q (it has three 1s)", "2 marks; 1 mark for counting the 1s correctly in at least two rows"),
        C("Every row and column had an even number of black coins. Then one coin was flipped. Which coin was it? Explain how you found it.",
          "Row 2, column 1. Row 2 has 3 black coins and column 1 has 3 black coins; they cross at that coin.",
          "1 mark for the odd row, 1 mark for the odd column, 1 mark for the coin where they cross", fig=flipped_coins, lines=3)],
    4: [A("In 5,308, what does the 3 stand for?", ["3 ones", "3 tens", "3 hundreds", "3 thousands"], "c) 3 hundreds"),
        A("Which number is the biggest?", ["4,099", "4,909", "4,990", "4,900"], "c) 4,990"),
        A("A comparator gets 7 and 3. Which number goes to the upper wire?", ["7", "3", "both"], "b) 3"),
        B("Write the number: 2 thousands, 0 hundreds, 5 tens and 9 ones. Then write it in words.", "2,059; two thousand fifty-nine",
          "1 mark for each"),
        B("Order from smallest to biggest: 3,210; 3,120; 3,201.", "3,120; 3,201; 3,210", "2 marks; 1 mark if one number is out of place"),
        C("Send 9, 6 and 2 through this network (top two wires, then bottom two, then top two). Write the order after each comparator.",
          "After 1: 6, 9, 2. After 2: 6, 2, 9. After 3: 2, 6, 9.", "1 mark for each comparator", fig=network_962, lines=3)],
    5: [A("A roti is cut into 4 equal parts. Each part is ...", ["one half", "one quarter", "one third"], "b) one quarter"),
        A("Two quarters make ...", ["one whole", "one half", "one third"], "b) one half"),
        A("Which is bigger?", ["1/2", "1/4", "they are equal"], "a) 1/2"),
        B("What is one quarter of 20 laddoos? What is three quarters of 20?", "5 and 15", "1 mark for each"),
        B("Rule: if all the parts are equal then say 'fair' else say 'not fair'. A cake is cut into 2 big and 2 small parts. What does the rule say? Why?",
          "Not fair, because the parts are not equal", "1 mark for 'not fair', 1 mark for the reason"),
        C("Mina has 16 marbles. She gives half to Ravi and a quarter to Asha. How many does Ravi get, how many does Asha get, and how many are left for Mina?",
          "Ravi 8, Asha 4, Mina 4", "1 mark for each")],
    6: [A("1 metre = ... centimetres", ["10", "100", "1,000"], "b) 100"),
        A("3 m 20 cm = ... cm", ["32", "320", "3,020"], "b) 320"),
        A("'Repeat 4 times: forward 3, turn right' draws a ...", ["triangle", "square", "straight line"], "b) square"),
        B("Robo is facing up. It turns right, then turns right again. Which way is it facing now?", "down", "2 marks"),
        B("A rope is 2 m long. You cut off 75 cm. How long is the rope now?", "125 cm (1 m 25 cm)", "2 marks; 1 mark for changing 2 m to 200 cm"),
        C("Write a loop with turns that draws a rectangle 4 steps long and 2 steps wide.",
          "Repeat 2 times: forward 4, turn right, forward 2, turn right.",
          "1 mark for repeat 2 times, 1 mark for both side lengths, 1 mark for the turns")],
    7: [A("A lamp is ON. You press its toggle button once. Now it is ...", ["ON", "OFF", "broken"], "b) OFF"),
        A("A toggle lamp starts OFF. You press it 3 times. Now it is ...", ["ON", "OFF"], "a) ON"),
        A("Writing down the state after every press is called ...", ["tracing", "guessing", "sorting"], "a) tracing"),
        B("Lamps A and B start OFF. Button 1 flips lamp A. Button 2 flips both lamps. Press 2, 2, 1. Which lamps are ON at the end?",
          "Only lamp A is ON (A ON, B OFF)", "2 marks; 1 mark for a correct trace with one slip"),
        B("A gate light starts red. Each press switches it between red and green. After 6 presses, is it red or green? Why?",
          "Red, because 6 is even and every 2 presses bring it back", "1 mark for red, 1 mark for the reason"),
        C("Lamps A and B start OFF. Button 1 flips A, button 2 flips both, button 3 flips B. Make a trace table for the presses 2, 1, 3, 2.",
          "start OFF OFF; 2: ON ON; 1: OFF ON; 3: OFF OFF; 2: ON ON", "3 marks for all four rows; 2 marks for three; 1 mark for two")],
    8: [A("1 kilogram = ... grams", ["10", "100", "1,000"], "c) 1,000"),
        A("On a balance, the left pan goes down. So ...", ["the left side is heavier", "the right side is heavier", "they are equal"],
          "a) the left side is heavier"),
        A("The best unit to measure the water in a bucket is ...", ["litres", "kilograms", "metres"], "a) litres"),
        B("Rule: if bag A is heavier than bag B then put A on the shelf, else put B on the shelf. Bag A is 2 kg and bag B is 1,500 g. Which bag goes on the shelf?",
          "Bag A (2 kg = 2,000 g, more than 1,500 g)", "1 mark for changing to grams, 1 mark for bag A"),
        B("You have a 4 L jug and a 1 L jug. How can you measure exactly 3 litres?", "Fill the 4 L jug, then pour from it to fill the 1 L jug. 3 L are left.",
          "2 marks; 1 mark for a sensible start"),
        C("You have a 3 L jug and a 5 L jug. Write the steps to get exactly 1 litre.",
          "Fill the 3 L jug and pour it into the 5 L jug. Fill the 3 L jug again and pour into the 5 L jug until it is full (2 L go in). 1 L is left in the 3 L jug.",
          "3 marks for steps that work; 2 marks if one step is missing; 1 mark for a sensible start")],
    9: [A("A nested loop is ...", ["a loop inside a loop", "a loop that never stops", "two loops one after the other"], "a) a loop inside a loop"),
        A("Outer loop: repeat 2 times. Inner loop: repeat 5 times: draw a star. How many stars?", ["7", "10", "25"], "b) 10"),
        A("An array has 4 rows of 6 chairs. How many chairs?", ["10", "20", "24", "46"], "c) 24"),
        B("Write a nested loop that draws 3 rows of 5 dots.", "Repeat 3 times: (repeat 5 times: draw a dot), then start a new row",
          "1 mark for the outer loop, 1 mark for the inner loop"),
        B("18 chairs stand in an array, 6 in each row. How many rows are there? Write it as a multiplication.", "3 rows; 3 x 6 = 18",
          "1 mark for each"),
        C("Program: repeat 3 times: clap once, then (repeat 4 times: stamp). How many claps and how many stamps? What would you change to get 15 stamps?",
          "3 claps and 12 stamps. Change the inner loop to repeat 5 times.", "1 mark for claps, 1 mark for stamps, 1 mark for the change")],
    10: [A("In a clue table, a cross means ...", ["not possible", "true", "not sure"], "a) not possible"),
         A("A row has crosses in every box but one. That box must be ...", ["true", "false", "empty"], "a) true"),
         A("A park has 12 elephants, 7 tigers and 9 leopards. Which animal has the fewest?", ["elephants", "tigers", "leopards"], "b) tigers"),
         B("Use the same park. How many more elephants than leopards are there, and how many animals in all?", "3 more; 28 animals",
           "1 mark for each"),
         B("Ravi and Meena own a cat and a dog, one pet each. Ravi does not own the cat. Who owns which pet?", "Ravi owns the dog; Meena owns the cat",
           "1 mark for each"),
         C("Asha, Bilal and Chitra each like a different fruit: apple, banana or mango. Asha likes neither apple nor mango. Bilal does not like apple. Who likes which fruit?",
           "Asha: banana. Bilal: mango. Chitra: apple.", "1 mark for each person")],
    11: [A("How many lines of symmetry does a square have?", ["1", "2", "4"], "c) 4"),
         A("Which capital letter has a line of symmetry going straight down?", ["A", "F", "G", "R"], "a) A"),
         A("A mirror image is ...", ["a flipped copy", "a bigger copy", "a moved copy"], "a) a flipped copy"),
         B("The red line is the mirror. A square in column A has its partner in column ___. A square in column C has its partner in column ___.",
           "F and D", "1 mark for each", fig=mirror_task),
         B("Which word has a line of symmetry straight down its middle: MOM or DAD? Why?", "MOM, because each half is a flipped copy of the other; D is not symmetric that way",
           "1 mark for MOM, 1 mark for the reason"),
         C("Robo draws one petal, then turns right. Write a loop that draws a flower with 4 petals all the way round. Then draw the flower.",
           "Repeat 4 times: draw a petal, turn right. The drawing is a flower with 4 petals, one pointing each way.",
           "1 mark for repeat 4 times, 1 mark for 'draw a petal, turn right' inside the loop, 1 mark for the drawing", lines=3)],
    12: [A("1 hour = ... minutes", ["30", "60", "100"], "b) 60"),
         A("Today is Friday. What day will it be after 7 days?", ["Friday", "Saturday", "Thursday"], "a) Friday"),
         A("A 'repeat until' loop stops when ...", ["the condition becomes true", "it has run 10 times", "it gets tired"], "a) the condition becomes true"),
         B("Start at 2:00. Repeat until the clock shows 3:30: add 15 minutes. How many times does the loop run?", "6 times",
           "2 marks; 1 mark for listing the times with one slip"),
         B("Today is Tuesday. What day will it be after 10 days?", "Friday", "2 marks; 1 mark for seeing that 7 days brings back Tuesday"),
         C("Write a repeat-until loop to fill a 10 litre bucket with a 2 litre mug. How many times does it run?",
           "Repeat until the bucket is full: pour in one mug (2 L). It runs 5 times.", "1 mark for the loop, 1 mark for the condition, 1 mark for 5")],
    13: [A("A decision tree asks questions that have ... answers.", ["yes or no", "any number of", "colour"], "a) yes or no"),
         A("In this tree, an animal with no wings that lives in water is a ...", ["bird", "fish", "land animal"], "b) fish", fig=animal_tree),
         A("To classify means to ...", ["put things into the right group", "count very fast", "draw a picture"], "a) put things into the right group"),
         B("Use the tree above. Where does a cow end up? Where does a crow end up?", "cow: land animal; crow: bird", "1 mark for each"),
         B("Write one yes/no question that splits pencil, apple, ball and banana into two groups of 2.", "For example: Can you eat it?",
           "1 mark for a yes/no question, 1 mark if it splits them 2 and 2"),
         C("Make a decision tree with 2 questions that sorts a car, a bicycle and a boat.",
           "Does it go on water? Yes: boat. No: Does it have an engine? Yes: car. No: bicycle.",
           "1 mark for each good question, 1 mark if all three end in the right place")],
    14: [A("Four lines with one line across them (tally marks) mean ...", ["4", "5", "6"], "b) 5"),
         A("In a bar graph, the tallest bar shows ...", ["the most popular", "the least popular", "the first item"], "a) the most popular"),
         A("Asking many people the same question is called a ...", ["survey", "story", "sum"], "a) survey"),
         B("Which colour is the most popular? How many more children chose Blue than Green?", "Blue; 6 more", "1 mark for each", fig=colour_votes),
         B("Use the same graph. How many children answered in all?", "20", "2 marks; 1 mark for reading all the bars correctly"),
         C("Draw tally marks for: cricket 7, football 4, kho-kho 9. Then write one question this data can answer, and its answer.",
           "Tallies: 5+2, 4, 5+4. For example: Which game is most popular? Kho-kho.",
           "1 mark for the tallies, 1 mark for a question, 1 mark for its answer")],
}
