def main():
    name = input("Enter your name: ")
    password = input("Enter your password: ")

    if name == "thanachote" and password == "5555":
        result = "login success!"
    elif name == "thanachote":
        result = "login password incorrect!"
    elif password == "5555":
        result = "login user incorrect!"
    else:
        result = "error"

    print(result)


if __name__ == "__main__":
    print("\n____________ 3.3 _________________\n")
    main()
    print("\n____________________________________\n")
