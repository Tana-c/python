def main():
    numbers = []

    while True:
        user_input = input("Enter a number (or 'e', 'E', 'exit' to finish): ")

        if user_input.lower() in ["e", "exit"]:
            break

        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input, please enter a valid number.")

    if numbers:
        average = sum(numbers) / len(numbers)
        print(f"Average is: {average}")
    else:
        print("No numbers were entered.")


if __name__ == "__main__":
    print("\n___________    3.8      _____________\n")
    main()
    print("\n____________________________________\n")
