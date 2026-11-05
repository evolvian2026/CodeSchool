# Level B3: Robo makes choices (paper prototype)

*A test lesson for teacher interviews, not a finished product. Print pages 1-3 for the teacher and page 4 for students.*

| | |
|---|---|
| **Band / Level** | B (Builders, Classes 3-5) · Level B3: conditionals |
| **Written for** | Class 4 (works for Classes 3-5) |
| **Time** | One 40-minute period |
| **Devices** | None needed. Optional: projector for the code cards |
| **Lesson structure** | PRIMM + Parsons: Predict & Run → Investigate → Modify → Parsons puzzle → Make |
| **Learning goal** | Students explain that an **if-else** block makes the program choose between two actions, checked every time the loop repeats |
| **Builds on** | B1 (sequence and loops), B2 (events) |
| **Curriculum link** | CBSE CT&AI Class 4 algorithmic thinking: "Movements on grids or direction-based paths" and "follow a set of well-defined, elaborate conditions", plus block-based coding (competency C-6). **Note:** CBSE makes explicit if-then logic a Class 7 outcome, so if-else at Class 4 is a deliberate stretch that the interviews test. It pairs with the Class 4 handbook chapters *Hide and Seek* (paths, turns, and a rule with an exception) and *The Cleanest Village* (tracing a button sequence): "the puzzle in your book, now you build it". See [CBSE verification](../cbse-verification.md) and [handbook review](../cbse-handbook-review.md). |

**Before class (5 minutes of preparation)**
- Draw a row of 5 squares on the floor or board (see Step 1). Chalk or tape is fine.
- Print one student sheet (page 4) per pair of students.
- Cut out the Parsons blocks on page 4, or let students cut them out.

---

## Page 1: Teacher script

### Step 1. Predict and run (8 minutes)

**Draw on the board:**

```
   1          2          3          4          5
[ START ]  [ PUDDLE ]  [ plain ]  [ PUDDLE ]  [ plain ]
  Robo >
```

**Show code card A** (write it on the board or project it):

```
when green flag clicked
repeat 4 times
    move forward 1 square
    if < on a puddle? > then
        say [Splash!]
    else
        say [Step]
    end
end
```

**Say:** "This is Robo. Robo is on the START square, facing right. Read the program with your partner. **Before we run it**, write down everything Robo will say, in order."

Give them 2 minutes. Take 2-3 guesses and write them on the board without saying which is right.

**Run it:** One student acts as Robo on the floor grid. The class reads the program aloud, one block at a time. Robo moves and speaks.

**Answer:** Robo says **Splash! · Step · Splash! · Step** and ends on square 5.

**Ask:** "Who predicted correctly? If you didn't, where did your guess go wrong?"

### Step 2. Investigate (8 minutes)

Ask these questions one at a time. Pairs discuss for 30 seconds, then share.

| # | Question | Answer | What to listen for |
|---|---|---|---|
| 1 | How many times did Robo say "Splash!"? Why? | 2, because Robo was on a puddle twice | Students linking the output to the squares |
| 2 | Which block makes Robo **choose** what to say? | The **if-else** block | Pointing to the right block, not to "repeat" |
| 3 | If every square were plain, what would Robo say? | Step, Step, Step, Step | Understanding that **else** runs when the condition is false |
| 4 | If we moved the **if-else** block so it came *after* the repeat (outside it), how many times would Robo check for a puddle? | Once, only on square 5, so Robo says "Step" once | The **hardest** question: the check happens every time *only because* it's inside the loop |

**Common misconceptions:**
- *"Robo says Splash and Step every time."* The student thinks both branches run. Point to the words **if… then… else**: only one of them happens each time.
- *"The if checks once at the start."* Act it out again and pause at each square: "Robo, are you on a puddle **now**?"

---

## Page 2: Teacher script (continued)

### Step 3. Modify (8 minutes)

**Draw a new row:**

```
   1          2         3         4         5
[ START ]  [ plain ]  [ STAR ]  [ STAR ]  [ plain ]
  Robo >
```

**Say:** "Change code card A so that Robo says **'Star!'** on a star square and **'Step'** on any other square. Change only the **if-else** block; leave everything else the same."

**Answer:** Inside the if-else, change `< on a puddle? >` to `< on a star? >` and `[Splash!]` to `[Star!]`. The `else` part stays `say [Step]`.

**Output:** Step · Star! · Star! · Step

**Stretch (fast finishers):** "Make Robo **jump** instead of speaking when it lands on a star. Which block do you change?" (Replace `say [Star!]` with `jump`.)

### Step 4. Parsons puzzle (8 minutes)

**Say:** "Robo is in a corridor. Robo must reach the **GOAL** without walking into a wall. Here are the blocks, all jumbled. Put them in the right order. **One block is a trick and isn't needed.**"

**The map** (on the student sheet):

```
        col 1      col 2      col 3      col 4      col 5
row 1  [START >]  [       ]  [       ]  [       ]  [ WALL ]
row 2  [ WALL  ]  [ WALL  ]  [ WALL  ]  [       ]  [ WALL ]
row 3  [ WALL  ]  [ WALL  ]  [ WALL  ]  [ GOAL  ]  [ WALL ]
```

Robo starts on row 1, column 1, facing right.

**Answer:**

```
repeat 6 times
    if < wall ahead? > then
        turn right
    else
        move forward 1 square
    end
end
```

**The trick block:** `turn left`

**How to check (walk through it with the class):**

| Repeat | Where Robo is | Wall ahead? | Robo does |
|---|---|---|---|
| 1 | row 1, col 1, facing right | No | move forward → col 2 |
| 2 | row 1, col 2 | No | move forward → col 3 |
| 3 | row 1, col 3 | No | move forward → col 4 |
| 4 | row 1, col 4 | **Yes** (col 5 is a wall) | turn right → now facing down |
| 5 | row 1, col 4, facing down | No | move forward → row 2 |
| 6 | row 2, col 4, facing down | No | move forward → row 3 = **GOAL** |

### Step 5. Make (6 minutes)

**Say:** "With your partner, draw your own row of 5 squares. Use any two kinds of square you like, for example mud and grass, or red and blue. Write your own rule:

> If Robo is on a ______ square, then ______, else ______.

Swap with the pair next to you. They predict what Robo will do, then you check together."

### Exit ticket (2 minutes)

On a slip of paper, each student answers:

1. Row: `[START] [puddle] [puddle] [plain]`, using code card A with **repeat 3 times**. What does Robo say? *(Answer: Splash! · Splash! · Step)*
2. Draw a circle around the block that makes Robo choose. *(Answer: if-else)*

---

## Page 3: Observation sheet (for the interviewer)

*Fill this in while the teacher reads the lesson aloud or walks through it. Don't help unless the teacher is stuck for more than about 30 seconds.*

| Step | Planned time | Time the teacher estimates | Questions or hesitations (quote them) | Would they change it? |
|---|---|---|---|---|
| 1. Predict and run | 8 min | | | |
| 2. Investigate | 8 min | | | |
| 3. Modify | 8 min | | | |
| 4. Parsons puzzle | 8 min | | | |
| 5. Make | 6 min | | | |
| Exit ticket | 2 min | | | |

**After the walkthrough, ask:**
1. Could you run this in one period tomorrow? What would stop you?
2. Which step would your students find hardest?
3. What would you change?
4. Would you use this on a projector, on paper, or in the computer lab?
5. Is the answer key enough, or would you need more help? What kind?
6. CBSE's CT book for your class follows the maths chapters. Is there a maths chapter this lesson could sit inside? Is if-else too early for Class 4?

**Score (circle one):**
- Teacher could run it without help: **Yes / With small changes / No**
- Estimated total time: **Fits one period / Needs two periods / Unclear**

---

## Page 4: Student sheet

**Names:** ______________________ **Class:** ______

### 1. Predict

```
   1          2          3          4          5
[ START ]  [ PUDDLE ]  [ plain ]  [ PUDDLE ]  [ plain ]
```

Robo will say: ________ , ________ , ________ , ________

### 2. Modify

Change the program so Robo says **"Star!"** on a star square.

```
[ START ]  [ plain ]  [ STAR ]  [ STAR ]  [ plain ]
```

What I changed inside the if-else: _______________________

Robo will say: ________ , ________ , ________ , ________

### 3. Parsons puzzle: help Robo reach the GOAL

```
        col 1      col 2      col 3      col 4      col 5
row 1  [START >]  [       ]  [       ]  [       ]  [ WALL ]
row 2  [ WALL  ]  [ WALL  ]  [ WALL  ]  [       ]  [ WALL ]
row 3  [ WALL  ]  [ WALL  ]  [ WALL  ]  [ GOAL  ]  [ WALL ]
```

**Cut out these blocks and put them in order. One block is a trick!**

```
+-------------------------+   +-------------------------+   +-------------------------+
| move forward 1 square   |   | repeat 6 times          |   | turn left               |
+-------------------------+   +-------------------------+   +-------------------------+

+-------------------------+   +-------------------------+   +-------------------------+
| else                    |   | if < wall ahead? > then |   | turn right              |
+-------------------------+   +-------------------------+   +-------------------------+

+-------------------------+   +-------------------------+
| end (of if)             |   | end (of repeat)         |
+-------------------------+   +-------------------------+
```

### 4. Make your own

Draw 5 squares:

```
[        ]  [        ]  [        ]  [        ]  [        ]
```

Our rule: **If** Robo is on a __________ square, **then** __________, **else** __________.
