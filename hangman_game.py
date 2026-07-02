import random

print("==============================")
print(" Welcome to Hangman ")
print("==============================")
print("Guess the word one letter at a time.")
print("You have 6 lives.\n")


def choose_word(words):
    secret_word= random.choice(words)
    return secret_word


def initialize_display(secret_word):

    display_word = list("_" * len(secret_word))
    return display_word


def display_status(display_word,lives,guessed_letters):
    print(" ".join(display_word))

    print(f"Remaining lives: {lives}")

    print(f"Guessed letters so far: {', '.join(guessed_letters)}")


def get_guess(guessed_letters):
     
    while True:
        guess = input("Enter your guess: ").lower()
        if not guess.isalpha() or len(guess)!=1:
            print("Please enter a valid input(single letter)!!")
            continue 

        if guess in guessed_letters:
            print(f"You have already guessed {guess}. Try another letter!!")
            continue
    
        guessed_letters.append(guess)
        return guess


def update_display(secret_word,display_word,guess):

    found = False

    for i in range(len(secret_word)):
        if secret_word[i] == guess:
            display_word[i] = guess
            found = True
        
    return found


def play_game(secret_word,display_word):

    guessed_letters =[]
    lives =6
    while lives>0 and "".join(display_word)!=secret_word:

        display_status(display_word,lives,guessed_letters)

        guess=get_guess(guessed_letters)

        found=update_display(secret_word,display_word,guess)

        if not found:
            lives-=1

    return display_word


def print_result(display_word,secret_word):
    if "".join(display_word) == secret_word:
        print("===============================")
        print(f"Congratulations!!\nYou guessed the word: {secret_word}")
        print("===============================")

    else:
        print("===============================")
        print(f"Game Over!!\nThe word was {secret_word}")
        print("===============================")


def main():
    
    words = ["analyze","cricket", "practice","learn","improve"]

    secret_word =choose_word(words)
    display_word = initialize_display(secret_word)

    display_word= play_game(secret_word,display_word)
    print_result(display_word,secret_word)


if __name__ == "__main__":
    main()