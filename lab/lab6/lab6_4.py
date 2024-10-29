import matplotlib.pyplot as plt


def main():
    xs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ys = [4, 8, 5, 6, 8, 2, 1, 4, 3, 1]

    values = [
        ("xs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]", xs.copy()),
        ("ys = [4, 8, 5, 6, 8, 2, 1, 4, 3, 1]", ys.copy()),
        ("plt.scatter(xs, ys)", []),
        ("plt.plot(xs, ys, color='blue')", []),
        ("plt.xlabel('X values')", []),
        ("plt.ylabel('Y values')", []),
        ("plt.title('Graph of given X and Y coordinates')", []),
        ("plt.show()", []),
    ]

    for index, (expr, value) in enumerate(values, start=1):
        print(f"{chr(96+index)}. {expr}")
        if value:
            print(f"print({expr.split(' = ')[0]}) \n[{', '.join(map(str, value))}] \n")

    plt.scatter(xs, ys, color="red")
    plt.plot(xs, ys, color="blue")

    for x, y in zip(xs, ys):
        plt.text(x, y, f"({x},{y})", fontsize=9, ha="right")

    plt.xlabel("X values")
    plt.ylabel("Y values")
    plt.title("Graph of given X and Y coordinates")
    plt.show()


if __name__ == "__main__":
    print("\n__________________ 6.4 _____________\n")
    main()
    print("\n____________________________________\n")
