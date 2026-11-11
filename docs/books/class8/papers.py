"""Sample examination papers for 'Think Like a Coder - Class 8': half-yearly (term-1 chapters) and annual (whole year), plus
unplugged practical stations. Each question: s (section), q, m or parts [(text, marks)], ch, lv (R, U, Ap, An), answer, guide."""

AR = ["Both A and R are true, and R explains A.", "Both A and R are true, but R does not explain A.", "A is true, but R is false.",
      "A is false, but R is true."]


def Q(s, ch, lv, q, answer, guide="", m=None, **kw):
    if m is None and "parts" not in kw:
        m = {"A": 1, "B": 2, "C": 3, "D": 5}[s]
    return dict(s=s, ch=ch, lv=lv, q=q, m=m, answer=answer, guide=guide, **kw)


def ar(ch, lv, a, r, answer):
    return Q("A", ch, lv, f"<b>Assertion (A):</b> {a}<br/><b>Reason (R):</b> {r}", answer, opts=AR)


def pw(b, e):
    return f"{b}<super>{e}</super>"


HALF = [
    Q("A", 1, "Ap", "Which number is a perfect cube?", "a) 64", opts=["64", "100", "144"]),
    Q("A", 1, "R", "The square root of 196 is ...", "b) 14", opts=["13", "14", "16"]),
    Q("A", 2, "Ap", f"{pw(2, 3)} x {pw(2, 2)} = ...", f"a) {pw(2, 5)}", opts=[pw(2, 5), pw(2, 6), pw(4, 5)]),
    Q("A", 2, "Ap", "A coin is tossed 4 times. How many different results (such as HTHH) are possible?", "b) 16", opts=["8", "16", "4"]),
    Q("A", 3, "Ap", "The binary number 1010 is ... in decimal.", "a) 10", opts=["10", "12", "1010"]),
    Q("A", 4, "R", "A quadrilateral with two pairs of equal sides next to each other is a ...", "a) kite", opts=["kite", "trapezium", "rectangle"]),
    Q("A", 8, "U", "The share of test predictions a model gets right is its ...", "a) accuracy", opts=["accuracy", "deployment", "dataset"]),
    Q("A", 9, "U", "AI forecasts of air quality help to ...", "a) warn people on bad-air days", opts=["warn people on bad-air days", "count wildlife", "translate languages"]),
    ar(1, "U", "72 is not a perfect square.", "72 = 2 x 2 x 2 x 3 x 3, and its prime factors do not all pair up.", "a) Both A and R are true, and R explains A."),
    ar(8, "An", "Every problem needs an AI solution.", "AI learns patterns from data.", "d) A is false, but R is true. (Some problems need only fixed steps: automation.)"),
    Q("B", 1, "Ap", "By what smallest number must 252 be divided to get a perfect square? What is the square root of the result?",
      "252 = 2 x 2 x 3 x 3 x 7, so divide by 7. 36, whose square root is 6.", "1 mark for 7, 1 mark for 6"),
    Q("B", 2, "Ap", f"Simplify ({pw(2, 5)} x {pw(2, 3)}) ÷ {pw(2, 6)}, and write 81 as a power of 3.", f"{pw(2, 2)} = 4; {pw(3, 4)}", "1 mark for each"),
    Q("B", 3, "Ap", "Write 22 in base 3.", "211 (2 x 9 + 1 x 3 + 1)", "1 mark for the method, 1 mark for 211"),
    Q("B", 4, "Ap", "One angle of a parallelogram is 65°. Find the other three angles.", "115°, 65°, 115°", "2 marks; 1 mark for 115°"),
    Q("B", 9, "Ap", "A no-code model mixes up paper and plastic in dim light. Give two ways to fix it.",
      "Add more photos of both classes taken in dim light; add more variety in backgrounds and angles; then retrain and test.", "1 mark for each fix"),
    Q("C", 1, "Ap", "Is 3375 a perfect cube? Use prime factors, and find its cube root if it is.",
      "3375 = (3 x 3 x 3) x (5 x 5 x 5): the factors make groups of three, so yes. Cube root = 3 x 5 = 15.",
      "1 mark for the prime factors, 1 mark for the groups, 1 mark for 15"),
    Q("C", 2, "Ap", "A lock has 3 dials, each with the digits 0 to 9. How many codes are possible? How many with 4 dials? How many times harder is the 4-dial lock to guess?",
      f"{pw(10, 3)} = 1,000; {pw(10, 4)} = 10,000; 10 times", "1 mark for each"),
    Q("C", 3, "Ap", "Change the binary number 101101 into decimal, and then into base 3.", "45; 1200 in base 3 (1 x 27 + 2 x 9 + 0 + 0)",
      "1 mark for 45, 2 marks for 1200 (1 mark for the method)"),
    Q("C", 4, "Ap", "Use if-else rules on properties to name each shape: (a) only one pair of parallel sides; (b) two pairs of parallel sides, all sides equal, "
      "angles of 70° and 110°; (c) two pairs of parallel sides, all sides equal, all angles 90°.", "(a) trapezium (b) rhombus (c) square", "1 mark for each"),
    Q("C", 8, "An", "A model predicts 'rain' or 'no rain'. On 40 test days it is right on 34. Find its accuracy. The goal is 90%: should it be deployed? What next?",
      "85%. No, it is below the goal. Collect more and cleaner data, refine the model and test again.", "1 mark for 85%, 1 mark for the decision, 1 mark for the next step"),
    Q("D", 8, "An", "Plan an AI project that predicts which canteen items will sell out each day.",
      "Open answer, for example: (a) predict which items will sell out so the canteen makes enough (b) past daily sales, day of the week, weather, events "
      "(c) remove duplicate days; fill or drop missing sales (d) test on days the model has not seen and measure accuracy (e) use it daily, check its predictions each week and retrain",
      "1 mark for each stage",
      parts=[("Define the problem in one sentence.", 1), ("What data would you collect?", 1), ("Give two cleaning steps.", 1), ("How would you evaluate the model?", 1),
             ("How would you deploy and keep checking it?", 1)]),
    Q("D", 2, "Ap", "Passwords and powers.", f"(a) {pw(26, 2)} = 676 (b) {pw(26, 4)} (c) {pw(36, 4)} (d) each extra character multiplies the number of passwords "
      f"by 36, so guessing takes 36 times longer (e) {pw(2, 10)} = 1,024, which is just over a thousand", "1 mark for each part",
      parts=[("How many 2-letter passwords can be made from the 26 small letters?", 1), ("Write the number of 4-letter passwords as a power.", 1),
             ("If the digits 0-9 are also allowed, write the number of 4-character passwords as a power.", 1),
             ("Why does each extra character make a password much harder to guess?", 1), (f"Work out {pw(2, 10)}. Why do people say it is 'about a thousand'?", 1)]),
    Q("E", 9, "An", "An AI tool reads chest X-rays to help screen people for tuberculosis (TB) in villages without many specialists.",
      "(a) Computer Vision (b) many X-rays, each labelled 'TB' or 'no TB' by doctors (c) the AI can be wrong, and a doctor is responsible for the diagnosis "
      "(d) more people can be screened quickly and early (e) it may work badly on X-rays from other machines, so test it on varied images",
      "1 mark for each part",
      parts=[("Which AI domain is this?", 1), ("What labelled data was it trained on?", 1), ("Why must a doctor review its results?", 1),
             ("Give one way it helps people in villages.", 1), ("What could go wrong if all its training X-rays came from one hospital's machine?", 1)]),
]

ANNUAL = [
    Q("A", 5, "Ap", "Which number is divisible by 4?", "b) 3,516", opts=["1,234", "3,516", "2,822"]),
    Q("A", 5, "Ap", "What is the remainder when 2,026 is divided by 9?", "a) 1", opts=["1", "2", "6"]),
    Q("A", 6, "Ap", "99 x 101 = ...", "a) 9,999", opts=["9,999", "10,099", "9,899"]),
    Q("A", 6, "U", "(a - b)<super>2</super> = ...", "b) a<super>2</super> - 2ab + b<super>2</super>",
      opts=["a<super>2</super> - b<super>2</super>", "a<super>2</super> - 2ab + b<super>2</super>", "a<super>2</super> + b<super>2</super>"]),
    Q("A", 7, "Ap", "15 : 25 in simplest form is ...", "a) 3 : 5", opts=["3 : 5", "5 : 3", "1 : 5"]),
    Q("A", 10, "U", "A group with far too many examples in the training data is ...", "a) over-represented", opts=["over-represented", "under-represented"]),
    Q("A", 11, "R", "Checking a news story against trusted sources is called ...", "a) fact-checking", opts=["fact-checking", "phishing", "piracy"]),
    Q("A", 4, "R", "The angles of a quadrilateral add up to ...", "b) 360°", opts=["180°", "360°", "540°"]),
    ar(5, "Ap", "8,316 is divisible by 11.", "Its alternating digit sum is 8 - 3 + 1 - 6 = 0.", "a) Both A and R are true, and R explains A."),
    ar(7, "An", "If 4 workers finish a job in 6 days, 8 workers finish it in 12 days.", "When more workers share a job, it takes fewer days (inverse proportion).",
       "d) A is false, but R is true. (8 workers take 3 days.)"),
    Q("B", 5, "Ap", "Test 5,148 for divisibility by 3, 4 and 9 without dividing.", "Digit sum 18: divisible by 3 and 9. Last two digits 48: divisible by 4.",
      "1 mark for 3 and 9, 1 mark for 4"),
    Q("B", 6, "Ap", "Use identities to work out 48<super>2</super> and 52 x 48.", "(50 - 2)<super>2</super> = 2,304; 50<super>2</super> - 2<super>2</super> = 2,496",
      "1 mark for each"),
    Q("B", 7, "Ap", "6 kg of rice costs ₹390. Use the unitary method to find the cost of 10 kg.", "₹65 per kg, so ₹650", "1 mark for each step"),
    Q("B", 10, "Ap", "A dataset has 300 records of city students and 60 of village students. Which group is under-represented? Give one fix.",
      "Village students. Collect more village records (or check the model on each group separately).", "1 mark for each"),
    Q("B", 11, "Ap", "A quiz app asks to use your camera and your contacts. Which would you allow? Why?", "Neither: a quiz does not need them to work",
      "1 mark for the decision, 1 mark for the reason"),
    Q("C", 5, "Ap", "What day of the week is it 250 days after a Wednesday? Explain using remainders.",
      "250 = 35 x 7 + 5, so the remainder is 5. 5 days after Wednesday is Monday.", "1 mark for the remainder, 1 mark for Monday, 1 mark for the explanation"),
    Q("C", 6, "Ap", "Expand (x + 5)(x + 3) with an area model. Check your answer by putting x = 10.",
      "x<super>2</super> + 3x + 5x + 15 = x<super>2</super> + 8x + 15. Check: 15 x 13 = 195 and 100 + 80 + 15 = 195.",
      "1 mark for the four parts, 1 mark for the expansion, 1 mark for the check"),
    Q("C", 7, "Ap", "A map has the scale 1 : 50,000. How far is 6 cm on the map in real life? How long is a 4.5 km road on the map?",
      "6 x 50,000 = 3,00,000 cm = 3 km; 4.5 km = 4,50,000 cm, which is 9 cm on the map", "1 mark for the method, 1 mark for each answer"),
    Q("C", 10, "An", "A voice assistant understands men's voices well but often fails with women's and children's voices. Give the likely cause, how to test it, and a fix.",
      "Cause: few women's and children's voices in the training data. Test: measure accuracy for each group separately. Fix: add more varied voices and retrain.",
      "1 mark for each"),
    Q("C", 11, "U", "An AI-made picture of a famous monument under floodwater is being shared widely. Name three checks before you share it.",
      "Look for the story on trusted news sites; check who posted it first and when; look for signs of editing or AI (odd details), or do a reverse image search.",
      "1 mark for each check"),
    Q("D", 6, "An", "The identity (a + b)(a - b) = a<super>2</super> - b<super>2</super>.",
      "(a) (a + b)(a - b) = a<super>2</super> - ab + ab - b<super>2</super> = a<super>2</super> - b<super>2</super> (b) 100<super>2</super> - 5<super>2</super> = 9,975 "
      "(c) (63 + 37)(63 - 37) = 100 x 26 = 2,600 (d) it swaps a hard multiplication for easy squares and one subtraction",
      "(a) 2 marks (b) 1 mark (c) 1 mark (d) 1 mark",
      parts=[("Show why the identity is true by expanding the brackets.", 2), ("Use it to work out 105 x 95.", 1),
             ("Use it to work out 63<super>2</super> - 37<super>2</super>.", 1), ("Why are identities like this useful for fast calculation?", 1)]),
    Q("D", 7, "Ap", "A school trip: the bus costs ₹12,000, shared equally by the students who go. Food costs ₹150 for each student.",
      "(a) ₹300 (b) ₹200 (c) inverse (d) ₹6,000 and ₹9,000 (e) direct", "1 mark for each part",
      parts=[("If 40 students go, how much does each pay for the bus?", 1), ("If 60 students go, how much does each pay for the bus?", 1),
             ("Is the bus share per student in direct or inverse proportion to the number of students?", 1),
             ("What is the total food cost for 40 students, and for 60?", 1), ("Is the total food cost in direct or inverse proportion to the number of students?", 1)]),
    Q("E", 10, "An", "A school uses AI to choose students for its science olympiad team. It learnt from five years of past choices, in which 80% of the students chosen were boys.",
      "(a) historical bias (b) compare how often girls and boys with similar scores are chosen (c) add more examples of girls who did well, or train only on scores, "
      "and test again (d) gender (e) the teachers, because people stay accountable for decisions made with AI", "1 mark for each part",
      parts=[("What kind of bias is this?", 1), ("How would you check whether it is fair?", 1), ("How would you rebalance it?", 1),
             ("Which feature should it not use?", 1), ("Who should make the final choice, and why?", 1)]),
]

PAPERS = [dict(key="half", name="Half-yearly examination", scope="chapters 1-4 and AI 1-2 (term 1)", questions=HALF),
          dict(key="annual", name="Annual examination", scope="all chapters, mostly chapters 5-7 and AI 3-4 (term 2)", questions=ANNUAL)]

PRACTICAL = dict(stations=[
    ("1. Factor tiles (chapter 1)", "Break three numbers into prime-factor tiles and decide whether each is a square, a cube, both or neither.",
     "How do pairs and groups of three show squares and cubes?"),
    ("2. Base converter (chapter 3)", "Show one number in base 10, base 2 and base 3 with place-value cards.", "How do you convert by repeated division? Why does binary suit computers?"),
    ("3. Shape classifier (chapter 4)", "Sort twelve quadrilateral cards with a chain of if-else questions, then write the rules.",
     "Why must 'square' be checked before 'rectangle'? Is every square a rhombus?"),
    ("4. Divisibility race (chapter 5)", "Test six numbers for divisibility by 3, 4, 8, 9 and 11 without dividing.", "Why does the digit-sum rule work for 9?"),
    ("5. Clean the data (AI 1)", "Find and fix the problems in a printed dataset (missing, duplicate, wrong and irrelevant values), then compute accuracy from a results table.",
     "Why must data be cleaned before training? Is the accuracy good enough to deploy?"),
    ("6. Fairness audit (AI 3)", "Check a printed training set for over- and under-represented groups and plan how to rebalance it.",
     "Which group is missing? How would you test the fixed model?"),
])
