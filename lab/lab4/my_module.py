def introduce(name, age, color):
    print(f"Hello, my name is {name}.")
    print(f"I am {age} years old.")
    print(f"My favorite color is {color}.")


def cel_to_fah(celsius):
    return (celsius * 9 / 5) + 32


def average(x, y, z):
    return (x + y + z) / 3


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
