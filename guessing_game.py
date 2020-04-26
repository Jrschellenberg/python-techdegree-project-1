import random
import sys

DASH_CHARACTER_REPEAT_AMOUNT = 40

def print_repeat_string(string, amount):
    return string * amount

def begin_game():
    hidden_number = random.randint(1, 10)
    number_guesses = 0
    print("")

    while True:
        number_guesses += 1
        try:
            user_input = int(input("Pick a number between 1 and 10:  "))
            if user_input > 10 or user_input < 1:
                raise ValueError
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
            continue

        if user_input > hidden_number:
            print("It's lower")
            continue
        elif user_input < hidden_number:
            print("It's higher")
            continue

        print("You got it! It took you {} tries".format(number_guesses))
        break
    return number_guesses

def play_again():
    try:
        play_again = str(input("Would you like to play again? [y]es/[n]o"))
        if play_again != 'y' and play_again != 'n':
            raise ValueError
    except ValueError:
        raise ValueError

    if play_again == 'y':
        return True
    return False

def start_game():
    print(print_repeat_string("-", DASH_CHARACTER_REPEAT_AMOUNT))
    print("  Welcome to the Number Guessing Game!")
    print(print_repeat_string("-", DASH_CHARACTER_REPEAT_AMOUNT))
    high_score = 0

    while True:
        if high_score != 0:
            print("\nthe HIGHSCORE is {}".format(high_score))

        new_score = begin_game()

        if high_score == 0:
            high_score = new_score
        elif high_score != 0 and new_score < high_score:
            high_score = new_score

        while True:
            try:
                if not play_again():
                    print("Shutting down.....")
                    sys.exit(0)
                break
            except Exception:
                print("Please enter 'y' or 'n' as response")

if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
