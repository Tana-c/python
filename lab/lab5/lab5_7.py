from lab5_3 import line_base
from lab5_4 import top_leaf


def tree():
    print("_____________")
    top_leaf()
    mid_leaf()
    bot_leaf()
    base()
    print("_____________")
    print


def top_leaf():
    line_base(7, 1)
    line_base(6, 3)
    line_base(5, 5)


def mid_leaf():
    line_base(6, 3)
    line_base(5, 5)
    line_base(3, 9)


def bot_leaf():
    line_base(5, 5)
    line_base(3, 9)
    line_base(0, 15)


def base():
    line_base(6, 3)
    line_base(6, 3)
    line_base(6, 3)


if __name__ == "__main__":
    tree()
