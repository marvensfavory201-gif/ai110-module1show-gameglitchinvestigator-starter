# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- **Purpose:** A modular Streamlit numbers guessing game that uses session states to track user points and attempts accurately across different difficulty levels.
- **Bugs Found:** The "New Game" button logic was completely missing, an accidental variable reassignment constantly overrode the active game status back to playing, even-attempt indexes broke math checks by converting numbers into alphabetical strings, and wrong higher guesses incorrectly increased scores.
- **Fixes Applied:** Restructured core mechanics into an external `logic_utils.py` module, built an active button conditional state wrapper to restart game variables, removed alphabetical type conversions, fixed score reductions, and wrote custom unit test validations.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User chooses a game difficulty setting (e.g., Normal) in the app sidebar.
2. User looks at the allowed attempt limits and current search boundaries.
3. User types a guess into the text block and hits the submit button.
4. Game gives a correct directive warning hint ("Too High" or "Too Low").
5. Score properly updates and drops by 5 points for a wrong guess attempt.
6. Game halts further entries once the answer is found or attempts hit 0.
7. User clicks the "New Game" button to clear arrays and restart.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

