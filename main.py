import time
from src.utils import halver


print("Welcome to binary4fun. Please press Enter to start a game!")

print("Let's go! Please think of a number between 1 and 100.")

time.sleep(2)
print("To play the game, please tell me the number.")

num = input()

print(
    "Thank you! I will now try to guess your number. I bet I need fewer than 7 guesses. Don't you think?"
)
time.sleep(0.5)

guess = 50

while (answer := ans) != "yes":

    print(f'Please tell me, is your number {guess}? Type "yes" or "no".')

    ans = input().lower()

    if answer not in ("yes", "no"):
        print("Please answer with 'yes' or 'no'.")
        continue

    print(f'Is your number smaller or larger than {guess}? Type "smaller" or "larger"')

    direction = input().lower()

    if answer not in ("smaller", "larger"):
        print("Please answer with 'smaller' or 'larger'.")
        continue

    guess = guess / 2 if direction == "smaller" else guess * 2

print("Great! Thank you for playing!")
