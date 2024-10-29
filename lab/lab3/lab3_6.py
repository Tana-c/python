def main():
    row = int(input("Enter number of rows: "))
    for i in range(row):
        left_os = "o" * (row - i - 1)
        hashes = "#" * (2 * i + 1)
        right_os = "o" * (row - i - 1)
        print(left_os + hashes + right_os)


if __name__ == "__main__":
    print("\n________________ 3.6 __________________\n")
    main()
    print("\n______________________________________\n")
