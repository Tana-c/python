import random


def main():
    number_to_guess = random.randint(1, 1000)
    max_attempts = 11

    print("Welcome to the Number Guessing Game!")
    print(f"You have {max_attempts} attempts to guess the number between 1 and 1000.")

    for attempt in range(1, max_attempts + 1):
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(
                f"Congratulations! You've guessed the number {number_to_guess} correctly in {attempt} attempts!"
            )
            break
    else:
        print(
            f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}."
        )


if __name__ == "__main__":
    print("\n______________ 3.7 _________________\n")
    main()
    print("\n____________________________________\n")
