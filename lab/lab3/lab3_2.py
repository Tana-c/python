def main():
    name = input("Enter your name: ")
    age = input("Enter your age: ")

    age = int(age)
    if name == "Alice":
        result = f"Hi, {name}"
    elif age < 12:
        result = f"You are not Alice, {name}."
    else:
        result = f"You are neither Alice not a little kid."
    print(result)


if __name__ == "__main__":
    print("\n____________________ 3.2 ______________________\n")
    main()
    print("\n_________________________________________________\n")
