# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|Attempts |Attempts should be 8 |Attempts 7 |Console Ouput: none |
|Output |The output should be saying HIGHER |HIGHER | Output: Go HIGHER! |
|New game should start with 8 not a negative number|Attempts left: 8| Attempts left: -68| |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

A: I used Gemini to fix one of my bugs you see. The game would not reset back to 8 attempts so I asked AI to steer me to the right direction turns out I had to change the name of one the code.

A2: The AI  generated test cases that caused an error because it forgot to unpack the tuple returned by `check_guess()`. I caught this error during testing, and the AI fixed it by adjusting the code to match the tuple output.


---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I verified fixes by manually checking that the "New Game" button reset the interface and counters correctly, and by checking the developer debug menu to ensure numbers processed without glitching.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
I ran an automated `pytest` called `test_update_score_penalizes_too_high_even_attempts()`. It confirmed that making an incorrect "Too High" guess now correctly deducts 5 points from the score instead of mistakenly rewarding the player.

- Did AI help you design or understand any tests? How?
Yes. The AI explained how to do the function's tuple outputs in the test file and provided the `python -m pytest` terminal command to resolve a module import path error.


---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Every time you click something, Streamlit restarts your code from scratch. "Session state" is like a memory notepad that saves your data (like your score or attempts) so it doesn't get wiped out when the app restarts.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  Separating core game logic into a separate utilities file (`logic_utils.py`) to keep the code organized and much easier to test.

- What is one thing you would do differently next time you work with AI on a coding task?
Carefully double-checking function output types instead of assuming the AI got the syntax perfect on the first try.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
It taught me that AI code can look functional on the surface but still contain hidden logical flaws. I now know it always requires thorough testing and critical review before use.
