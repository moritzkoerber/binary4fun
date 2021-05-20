import os


def clear():
    os.system("cls")
    os.system("clear")


def play_game():
    clear()
    input("Welcome to binary4fun! Please press any key to start playing!")
    input("Please think of a number between 1 and 100. Press any key if you have one.")
    clear()
    print("I will now try to guess the number. I bet I can do it in within 7 guesses!")

    current_guess, current_ul, current_ll, number_o_guesses = 50, 100, 0, 0

    while (
        answer := input(
            f"Is your number {current_guess}? Please answer 'yes' or 'no':\n"
        )
    ) != "yes":
        number_o_guesses += 1
        clear()
        direction = input(
            "Is the number higher or lower? Type 'h' for higher or 'l' for lower:\n"
        )
        if direction == "h":
            current_ll, current_guess = (
                current_guess,
                (current_guess + current_ul) // 2,
            )
            clear()
        if direction == "l":
            current_ul, current_guess = (
                current_guess,
                (current_guess + current_ll) // 2,
            )
            clear()
        else:
            direction = input(
                "Is the number higher or lower? Type 'h' for higher or 'l' for lower\n"
            )

    clear()
    print(
        f"Cool! :) That took only {number_o_guesses + 1} guess{'es' if number_o_guesses > 0 else ''}. That's within 7 guesses! \n"
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
