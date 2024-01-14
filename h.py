import random

def choose_word():
    words = ["python", "hangman", "computer", "programming", "gaming", "coding", "developer", "debugging"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts_left = 6

    print("Welcome to Hangman!")
    
    while attempts_left > 0:
        current_display = display_word(word_to_guess, guessed_letters)
        print("\nCurrent word: " + current_display)
        guess = input("Guess a letter: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in word_to_guess:
                print("Good guess!")
                guessed_letters.append(guess)
            else:
                print("Incorrect guess.")
                attempts_left -= 1
                print(f"Attempts left: {attempts_left}")
        else:
            print("Invalid input. Please enter a single letter.")

        if set(guessed_letters) == set(word_to_guess):
            print("\nCongratulations! You guessed the word: " + word_to_guess)
            break

    if attempts_left == 0:
        print("\nSorry, you ran out of attempts. The word was: " + word_to_guess)

if __name__ == "__main__":
    hangman()
