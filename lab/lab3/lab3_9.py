def main():
    while True:
        name = input("Enter your name: ")
        password = input("Enter your password: ")

        if name == "thanachote" and password == "5555":
            result = "login success!"
            print(result)
            break  
        elif name == "thanachote":
            result = "login password incorrect!"
        elif password == "5555":
            result = "login user incorrect!"
        else:
            result = "error"

        print(result)


if __name__ == "__main__":
    print("\n______________ 3.9 _________________\n")
    main()
    print("\n____________________________________\n")
