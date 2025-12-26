subwords = [
    ['well', 'yell', 'low', 'owl'],           
    ['monk', 'key', 'money', 'yoke'],               
    ['bird', 'bride', 'grid', 'ridge']              
]

words = ["yellow", "monkey", "bridge"]

level = 0
total_score = 0

def play_game(level):
    print("\nGuess the subwords of the word:", words[level])
    print("You have to guess", len(subwords[level]), "subwords.")

    level_score = 0
    guesses = []

    for _ in range(len(subwords[level])):
        guess = input("Enter your guess: ").lower()
        guesses.append(guess)

    for guess in guesses:
        if guess in subwords[level]:
            level_score += 1
        else:
            level_score -= 1

    return level_score

def main():
    global level, total_score

    while level < len(words):
        level_score = play_game(level)

        if level_score == len(subwords[level]):
            total_score += level_score
            level += 1
            print("---- NEXT LEVEL -----")
        else:
            print("You failed this level!")
            break

    print("\nYour Total Score:", total_score)
    print("Number of levels played:", level)

main()
