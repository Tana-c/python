def main():
    numbers = [1, 2, 3, 5]

    values = [
        ("numbers=[1, 2, 3, 5]", numbers.copy()),
        ("numbers.append(4)", [1, 2, 3, 5, 4]),
        ("numbers.remove(3)", [1, 2, 5, 4]),
        ("numbers.pop(3)", [1, 2, 5]),
        ("numbers.insert(3, 2)", [1, 2, 5, 2]),
    ]

    for index, (expr, value) in enumerate(values, start=1):
        print(f"{chr(96+index)}.{expr}")
        print(f"print(numbers) \n[{', '.join(map(str, value))}] \n")


if __name__ == "__main__":
    print("\n____________________ 4.1 __________________\n")
    main()
    print("\n___________________________________________\n")
