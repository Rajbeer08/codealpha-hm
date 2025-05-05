import random

def choose_word():
    words = ['python', 'hangman', 'challenge', 'programming', 'computer', 'science', 'developer']
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display.strip()

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts_left = 6

    print("Welcome to Hangman!")
    print("Try to guess the word one letter at a time.")

    while attempts_left > 0:
        print("\nWord: ", display_word(word_to_guess, guessed_letters))
        print("Attempts left:", attempts_left)
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Good guess!")
        else:
            print("Wrong guess.")
            attempts_left -= 1

        if all(letter in guessed_letters for letter in word_to_guess):
            print("\nCongratulations! You guessed the word:", word_to_guess)
            break
    else:
        print("\nGame over! The word was:", word_to_guess)

if __name__=="__main__": hangman()
