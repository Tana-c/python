def calculate_perimeter(width, length):
    return 2 * (width + length)


def main():
    width = float(input("Enter width in meters: "))
    length = float(input("Enter length in meters: "))

    perimeter = calculate_perimeter(width, length)

    print(f"Perimeter is {perimeter:.2f} meters.")


if __name__ == "__main__":
    print("\n____________  2.7    ________________\n")
    main()
    print("\n#____________________________________\n")
