def averageList(xs):
    if not xs:
        return 0

    total = sum(xs)
    count = len(xs)
    return total / count


def main():
    xs = [4, 8, 6, 6]
    result = averageList(xs)
    print(f"List: {xs}")
    print(f"The average is: {result:.2f}")


if __name__ == "__main__":
    print("\n___________________ 4.10 ________________\n")
    main()
    print("\n_________________________________________\n")
