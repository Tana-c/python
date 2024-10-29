def average(x, y, z):
    return (x + y + z) / 3


def main():
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    z = float(input("Enter the third number: "))

    result = average(x, y, z)

    print(f"The average of {x}, {y}, and {z} is {result:.2f}")


if __name__ == "__main__":
    print("\n______________ 4.5 ________________\n")
    main()
    print("\n____________________________________\n")
