import os
import matplotlib.pyplot as plt


def read_points_from_file(file_path):
    xs, ys = [], []
    with open(file_path, "r", encoding="utf-8-sig") as file:
        for line in file:
            x, y = map(int, line.strip().split(","))
            xs.append(x)
            ys.append(y)
    return xs, ys


def main():
    current_path = os.getcwd()
    file_path = os.path.join(current_path, "lab6", "points.txt")
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        return

    xs, ys = read_points_from_file(file_path)

    values = [
        (f"xs = {xs}", xs.copy()),
        (f"ys = {ys}", ys.copy()),
        ("plt.scatter(xs, ys)", []),
        ("plt.xlabel('X values')", []),
        ("plt.ylabel('Y values')", []),
        ("plt.title('Graph of points from points.txt')", []),
        ("plt.show()", []),
    ]

    for index, (expr, value) in enumerate(values, start=1):
        print(f"{chr(96+index)}. {expr}")
        if value:
            print(f"print({expr.split(' = ')[0]}) \n[{', '.join(map(str, value))}] \n")

    plt.scatter(xs, ys, color="red")
    plt.xlabel("X values")
    plt.ylabel("Y values")
    plt.title("Graph of points from points.txt")
    plt.show()


if __name__ == "__main__":
    print("\n           _______ 6.5 __________          \n")
    main()
    print("\n____________________________________\n")
