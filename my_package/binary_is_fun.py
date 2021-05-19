import statistics as stats
import os


def clear():
    os.system("cls")
    os.system("clear")


def play_game():
    clear()
    repeat = "yes"
    while repeat == "yes":
        guess = False
        input("\nWelcome to binary4fun! Please press Enter to start playing!")
        clear()
        number = input("\nPlease enter a number between 1 and 100:\n")
        clear()
        print(
            "\nI will now try to guess the number. I bet I can do it in fewer than 8 guesses!\n"
        )
        current_guess = 50
        current_ul = 100
        current_ll = 0
        number_o_guesses = 0
        while guess == False:
            answer = input(
                f"\nIs your number {current_guess}? Please type 'yes' or 'no':\n"
            )
            number_o_guesses += 1
            if answer == "yes":
                clear()
                print("Cool! :)\n")
                if number_o_guesses > 1:
                    print(
                        "That took {} guesses. That's fewer than 8! \n\nThank you for playing!\n".format(
                            number_o_guesses
                        )
                    )
                else:
                    print(
                        "That took only {} guess. That's fewer than 8! \n\nThank you for playing!\n".format(
                            number_o_guesses
                        )
                    )
                repeat = input(
                    "Do you want to play again? Please type 'yes or 'no'.\n\n"
                )
                if repeat == "yes":
                    clear()
                    guess = True
                    continue
                if repeat == "no":
                    clear()
                    print("\nOkay, goodbye!\n")
                    guess = True
                    break

            if answer == "no":
                clear()
                direction = input(
                    "\nIs the number higher or lower? Type 'h' for higher or 'l' for lower:\n"
                )
                if direction == "h":
                    current_ll, current_guess = (
                        current_guess,
                        int(round(stats.mean([current_guess, current_ul]), 0)),
                    )
                    clear()
                    continue
                if direction == "l":
                    current_ul, current_guess = (
                        current_guess,
                        int(round(stats.mean([current_guess, current_ll]), 0)),
                    )
                    clear()
                    continue
                else:
                    direction = input(
                        "\nIs the number higher or lower? Type 'h' for higher or 'l' for lower"
                    )
            else:
                answer = input(
                    "\nIs your number {}? Please type 'yes' or 'no':\n".format(
                        current_guess
                    )
                )


if __name__ == "__main__":
    play_game()
