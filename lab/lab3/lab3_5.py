def main():
    row = int(input("Enter number of rows: "))
    column = int(input("Enter number of columns: "))

    print(f"This block of {row} rows x {column} columns:")
    for i in range(row):
        print(column * "o")


if __name__ == "__main__":
    print("\n______________ 3.5 __________________\n")
    main()
    print("\n____________________________________\n")
