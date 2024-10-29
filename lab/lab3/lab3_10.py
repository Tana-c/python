def main():
    score = float(input("Enter your score: "))

    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "F"

    if grade != "F" and grade != "A":
        if score % 10 >= 5:
            grade += "+"

    print(f"Your grade is {grade}")


if __name__ == "__main__":
    print("\n________________ 3.10 ______________\n")
    main()
    print("\n____________________________________\n")
