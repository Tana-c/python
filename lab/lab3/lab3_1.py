def main():
    expressions = [
        "5 != 2",
        "age > 20",
        "True and (not False)",
        "(4 < 5) and ((2 > 3) or False)",
        "age > 10 and weight < 20",
    ]

    age = 10
    weight = 15

    values_1 = [eval(expr) for expr in expressions]

    values_2 = [
        5 != 2,
        age > 20,
        True and (not False),
        (4 < 5) and ((2 > 3) or False),
        age > 10 and weight < 20,
    ]

    for index, (expr, calculated_value, manual_value) in enumerate(
        zip(expressions, values_1, values_2), start=1
    ):
        print(f"{chr(96+index)}.print( {expr} )")
        print(f"ค่าที่คำนวณด้วยตนเอง {manual_value}")
        print(f"โปรแกรม {calculated_value} \n")


if __name__ == "__main__":
    print("\n___________ 3.1   _____________\n")
    main()
    print("__________________________________\n")
