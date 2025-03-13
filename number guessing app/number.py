"""A CLI based python app where the user guesses a chosen number"""

import random
# plan:
# 1. pick number 1-100
# 2. prompt user to guess number
# 3. if correct - user wins! - restart
# 4. if wrong - give user clue higher/lower
# 5. repeat from 2.


def generate_number():
    """generates a random number from 1-100"""
    number = random.randint(1, 100)
    return number


def user_prompt():
    """prompts the user to guess a number"""
    # code


def higher_lower():
    """gives the user a higher or lower hint depending on guess"""
    # code


def win():
    """congratulates the user if they guess correctly"""


def main():
    """the main function"""
    target = generate_number()
    # print(target)

    print("I have randomly selected a number in the range 1 to 100, can you guess which one?")

    while True:
        try:
            choice = int(input(
                "-: "))
            break
        except ValueError:
            print("Please enter a number")
    # evaluate guess
    # reply with hint or congratulations


if __name__ == "__main__":
    main()
