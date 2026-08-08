# ============================================================
#                    HANGMAN GAME (PYTHON)
# ============================================================
import random

# -----------------------------
# List of 5 predefined words
# -----------------------------
words = ["apple", "tiger", "house", "chair", "robot"]

# Randomly choose a word
word = random.choice(words)

# -----------------------------
# Hangman Stages
# -----------------------------
hangman = [
    """
          +-------+
          |       |
                  |
                  |
                  |
                  |
    =========================
    """,
    """
          +-------+
          |       |
          O       |
                  |
                  |
                  |
    =========================
    """,
    """
          +-------+
          |       |
          O       |
          |       |
                  |
                  |
    =========================
    """,
    """
          +-------+
          |       |
          O       |
         /|       |
                  |
                  |
    =========================
    """,
    """
          +-------+
          |       |
          O       |
         /|\\      |
                  |
                  |
    =========================
    """,
    """
          +-------+
          |       |
          O       |
         /|\\      |
         /        |
                  |
    =========================
    """,
    """
          +-------+
          |       |
          O       |
         /|\\      |
         / \\      |
                  |
    =========================
    """
]

# -----------------------------
# Game Variables
# -----------------------------
guessed_letters = []     # Stores all guessed letters
correct_letters = []     # Stores correct guesses
wrong_letters = []       # Stores incorrect guesses

wrong_guesses = 0
max_guesses = 6

# -----------------------------
# Welcome Screen
# -----------------------------
print("=" * 55)
print("              🎮 WELCOME TO HANGMAN 🎮")
print("=" * 55)
print("Guess the hidden word one letter at a time.")
print("You are allowed only 6 incorrect guesses.")
print("=" * 55)

# -----------------------------
# Main Game Loop
# -----------------------------
while wrong_guesses < max_guesses:

    # Display current hangman stage
    print(hangman[wrong_guesses])

    # Display hidden word
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("-" * 55)
    print("WORD TO GUESS")
    print(display)
    print("-" * 55)

    # Display game information
    print(f"❤️ Lives Left : {max_guesses - wrong_guesses}")

    if correct_letters:
        print("✅ Correct Guesses :", " ".join(correct_letters))
    else:
        print("✅ Correct Guesses : None")

    if wrong_letters:
        print("❌ Wrong Guesses   :", " ".join(wrong_letters))
    else:
        print("❌ Wrong Guesses   : None")

    # Check if player has won
    if "_" not in display:
        print("\n" + "=" * 55)
        print("🎉 CONGRATULATIONS!")
        print(f"You guessed the word: {word.upper()}")
        print("🏆 YOU WIN!")
        print("=" * 55)
        break

    # Ask player for input
    guess = input("\nEnter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("\n⚠ Please enter only ONE alphabet letter.\n")
        continue

    # Check duplicate guess
    if guess in guessed_letters:
        print("\n⚠ You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    # Check guess
    if guess in word:
        correct_letters.append(guess)
        print("\n✅ Great! Correct Guess.\n")
    else:
        wrong_letters.append(guess)
        wrong_guesses += 1
        print("\n❌ Oops! Wrong Guess.\n")

# -----------------------------
# Game Over
# -----------------------------
if wrong_guesses == max_guesses:

    print(hangman[wrong_guesses])

    print("\n" + "=" * 55)
    print("💀 GAME OVER 💀")
    print(f"The correct word was: {word.upper()}")
    print("Better luck next time!")
    print("=" * 55)