def grade(score):
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"


def main():
    scores = [85, 72, 67, 49, 90, 55]
    grades = [grade(score) for score in scores]
    for i in range(len(scores)):
        print(f"{i+1}. Score: {scores[i]}, Grade: {grades[i]}")


if __name__ == "__main__":
    print("\n__________________ 4.6 __________________\n")
    main()
    print("\n______________________________________\n")
