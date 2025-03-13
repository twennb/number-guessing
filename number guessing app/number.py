"""A CLI based python app where the user guesses a chosen number"""

import random
import sys
# plan:
# 1. pick number 1-100
# 2. prompt user to guess number
# 3. if correct - user wins! - restart
# 4. if wrong - give user clue higher/lower
# 5. repeat from 2.

counter = []


def generate_number(number_ceiling):
    """generates a random number from 1 to a user specified max"""
    number = random.randint(1, number_ceiling)
    return number


def prompt_user(number_ceiling):
    """prompts the user to guess a number"""
    while True:
        try:
            guess = int(input(
                "-: "))
            if not (1 <= guess <= number_ceiling):
                print(
                    f"Please enter a number in the range 1 to {number_ceiling}!")
            else:
                break
        except ValueError:
            print("Please enter a number")
    return guess


def evaluate_guess(target, guess):
    """gives the user a higher or lower hint depending on guess"""
    if guess > target:
        print("Lower!")
        counter.append(guess)
    elif guess < target:
        print("Higher!")
        counter.append(guess)
    else:
        win()


def win():
    """congratulates the user if they guess correctly"""
    print(f"\nYou win! You guess it in {len(counter) + 1} guesses!")
    play_again()


def play_again():
    """prompts the player whether they want to play again or quit"""
    while True:
        again = input(
            "\nWould you like to play again?\n(yes/no) -: ").strip().lower()

        if again == "yes":
            counter.clear()
            main()
        elif again == "no":
            sys.exit()
        else:
            print("Please enter yes or no")


def main():
    """the main function"""
    while True:
        try:
            number_ceiling = int(input(
                "=====================================================================\n"
                "In this game I will generate a random number within a specified range\n"
                "and you will guess that number while being given 'higher' or 'lower'\n"
                "clues after each guess.\n"
                "What would you like the highest number in the range to be?\n"
                "-: "
            ))
            break
        except ValueError:
            print("please enter a number!")
    target = generate_number(number_ceiling)
    print(
        f"\nI have randomly selected a number in the range 1 to {number_ceiling}, "
        "can you guess which one?"
    )
    while True:
        guess = prompt_user(number_ceiling)
        evaluate_guess(target, guess)


if __name__ == "__main__":
    main()
