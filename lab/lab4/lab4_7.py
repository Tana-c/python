from my_module import introduce, cel_to_fah, average, grade


def main():
    introduce("Ball", 20, "black")

    f = cel_to_fah(37)
    print(f"Temperature {f:.1f} °F")
    avg = average(1, 2, 3)
    print(f"Average is {avg:.2f}")

    g = grade(37)
    print(f"Grade is {g}")


if __name__ == "__main__":
    print("\n________________ 4.7 _________________\n")
    main()
    print("\n____________________________________\n")
