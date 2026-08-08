# 🎮 Hangman Game

A simple **text-based Hangman Game built with Python** as part of my **CodeAlpha Internship**.

The player has to guess a hidden word one letter at a time. The game randomly selects a word from a predefined list, and the player has a maximum of **6 incorrect guesses**.

## 🎯 Project Goal

The goal of this project is to create a simple text-based Hangman game where the player:

* Guesses a hidden word one letter at a time
* Receives feedback for correct and incorrect guesses
* Has a maximum of 6 incorrect guesses
* Tries to guess the complete word before the Hangman is completed

## 📌 Project Scope

The project is intentionally kept simple and beginner-friendly.

* 5 predefined words
* Random word selection
* Basic console input/output
* Maximum 6 incorrect guesses
* ASCII Hangman display
* No external files
* No API
* No graphics or audio

## 🧠 Key Concepts Used

* `random`
* `while` loop
* `for` loop
* `if / elif / else`
* Strings
* Lists
* `input()`
* `print()`
* Basic program logic

## 🎮 How the Game Works

1. The program selects a random word from a list of 5 predefined words.
2. The hidden word is displayed using underscores.
3. The player enters one letter at a time.
4. If the letter is correct, it is revealed in the word.
5. If the letter is incorrect, the Hangman drawing progresses.
6. Correct and incorrect guesses are displayed separately.
7. The player wins by guessing the complete word.
8. The game ends after 6 incorrect guesses.

## 🖥️ Example

```text
=======================================================
              🎮 WELCOME TO HANGMAN 🎮
=======================================================
Guess the hidden word one letter at a time.
You are allowed only 6 incorrect guesses.
=======================================================

          +-------+
          |       |
                  |
                  |
                  |
                  |
    =========================

-------------------------------------------------------
WORD TO GUESS
_ _ _ _ _
-------------------------------------------------------
❤️ Lives Left : 6
✅ Correct Guesses : None
❌ Wrong Guesses   : None

Enter a letter: a

✅ Great! Correct Guess.
```

## 🏆 Winning Example

```text
=======================================================
🎉 CONGRATULATIONS!
You guessed the word: APPLE
🏆 YOU WIN!
=======================================================
```

## 💀 Game Over Example

```text
=======================================================
💀 GAME OVER 💀
The correct word was: TIGER
Better luck next time!
=======================================================
```

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

### 2. Open the project folder

```bash
cd your-project-folder
```

### 3. Run the Python file

```bash
python hangman.py
```

## 📁 Project Structure

```text
Hangman-Game/
│
├── hangman.py
└── README.md
```

## 🚀 Future Improvements

Possible improvements for future versions:

* Add difficulty levels
* Add more words
* Add hints
* Add score tracking
* Add multiple rounds
* Add colored console output
* Add a graphical user interface

## 👩‍💻 Internship

This project was developed as part of my **Python project work during my CodeAlpha Internship**.

## 📚 Learning Outcome

This project helped me practice Python fundamentals including lists, strings, loops, conditional statements, random selection, user input, and basic game logic.

---

⭐ Thanks for checking out my project!
