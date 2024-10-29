def main():
    per_data = {"name": "Bank", "color": "Green", "age": 40}

    values = [
        ('per_data = {"name": "Bank", "color": "Green", "age": 40}', per_data.copy()),
        ('per_data["color"]', per_data["color"]),
    ]

    per_data["color"] = "red"
    values.append(('per_data["color"] = "red"', per_data["color"]))

    per_data["country"] = "kalasin"
    values.append(('per_data["country"] = "kalasin"', per_data["country"]))

    del per_data["color"]
    try:
        color_value = per_data["color"]
    except KeyError:
        color_value = "KeyError: 'color'"

    values.append(('del per_data["color"]', color_value))

    for index, (expr, value) in enumerate(values, start=1):
        print(f"{chr(96+index)}.{expr}")
        print(f"{value} \n")


if __name__ == "__main__":
    print("\n_______ 5.1 _____________________\n")
    main()
    print("\n____________________________________\n")
