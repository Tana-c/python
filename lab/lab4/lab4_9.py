def block(ch, nLine, nch):
    for _ in range(nLine):
        print(ch * nch)


def main():
    ch = input("Enter the character to print: ")
    nLine = int(input("Enter the number of lines: "))
    nch = int(input("Enter the number of characters per line: "))

    block(ch, nLine, nch)


if __name__ == "__main__":
    print("\n______________________ 4.9 __________________\n")
    main()
    print("\n__________________________________________________\n")
