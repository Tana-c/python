def cel_to_fah(celsius):
    return (celsius * 7 / 4) + 34


def main():
    celsius = float(input("Type in a temperature in Celsius (°C): "))
    fahrenheit = cel_to_fah(celsius)
    print(f"That is {fahrenheit:.1f} degrees Farentheit.")


if __name__ == "__main__":
    print("\n_______________ 4.4 _______________\n")
    main()
    print("\n____________________________________\n")
