import random

words = ["apple", "banana", "grape", "orange", "mango"]
stages = ["Stage6", "Stage5", "Stage4", "Stage3", "Stage2", "Stage1"]

secret = random.choice(words)   # Pick random word
chances = len(stages)

guessed = ["_"] * len(secret)
guessed_letters = set()

while True:
    letter = input("Guess a letter [a-z]: ").lower()

    # Input validation
    if not letter.isalpha() or len(letter) != 1:
        print("Please enter a single alphabet letter.")
        continue

    if letter in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.add(letter)

    if letter in secret:
        for i in range(len(secret)):
            if secret[i] == letter:
                guessed[i] = letter

        print(" ".join(guessed))

        if "_" not in guessed:
            print("🎉 Congratulations! You guessed it right!")
            break
    else:
        chances -= 1
        print(stages[chances - 1])

        if chances == 0:
            print("❌ You lost the game.")
            print("The correct word was:", secret)
            break