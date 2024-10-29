from lab5_3 import line_base
from lab5_4 import top_leaf


def tree():
    print("__________")
    top_leaf()
    mid_leaf()
    bot_leaf()
    base()
    print("__________")
    print


def top_leaf():
    line_base(2, 1)
    line_base(1, 3)
    line_base(0, 5)


def mid_leaf():

    print("2. Draw middel leaf")


def bot_leaf():
    print("3. Draw bottom leaf")


def base():
    line_base(1, 3)
    line_base(1, 3)
    line_base(1, 3)


if __name__ == "__main__":
    tree()
