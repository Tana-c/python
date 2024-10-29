def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def main():
    print("This program converts Celsius to Fahrenheit.")
    celsius = float(input("Type in a temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"That is  {fahrenheit} degrees Fahrenheit.")


if __name__ == "__main__":
    print("\n______________ 2.4  _______________\n\n")
    main()
    print("\n____________________________________\n")
