import os


def clear():
    os.system("cls")
    os.system("clear")


def play_game():
    clear()
    input("Welcome to binary4fun! Please press Enter to start playing!")
    input("Please think of a number between 1 and 100. Press Enter if you have one.")
    clear()
    print("I will now try to guess the number. I bet I can do it in within 7 guesses!")

    current_ll, current_ul, current_guess, number_o_guesses = 1, 100, (1 + 100) // 2, 1

    while (
        input(f"Is your number {current_guess}? Please answer 'y' or 'n':\n")
    ) != "y":
        number_o_guesses += 1
        clear()
        direction = input(
            "Is the number higher or lower? Type 'h' for higher or 'l' for lower:\n"
        )
        clear()
        if direction == "l":
            current_ul = current_guess - 1
        elif direction == "h":
            current_ll = current_guess + 1
        if current_ll == current_ul:
            print(f"Okay, I must be {current_ll} then!\n")
            break
        current_guess = (current_ll + current_ul) // 2
    else:
        clear()
    print(
        f"Cool! :) That took only {number_o_guesses} guess{'es' if number_o_guesses > 1 else ''} – which is within 7 guesses!"
    )
    if (
        input(
            "Thank you for playing! Do you want to play again? Please type 'yes or 'no'.\n"
        )
        == "yes"
    ):
        play_game()
    clear()
    print("Okay, goodbye!")


if __name__ == "__main__":
    play_game()
