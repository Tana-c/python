def main_a():
    print("โจทย์ a: แสดงข้อมูลจากตาราง scores")
    scores = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [5, 4, 3, 2, 1]]

    N = len(scores)
    for i in range(N):
        print(scores[i])
    print()


def main_b():
    print("โจทย์ b: แสดงแถวที่สามของตาราง scores")
    scores = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [5, 4, 3, 2, 1]]
    print(scores[2], "\n")


def main_c():
    print("โจทย์ c: แสดงแถวที่สอง และตรวจสอบแถวที่สี่ของตาราง scores")
    scores = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [5, 4, 3, 2, 1]]

    print(scores[1])
    if len(scores) > 3:
        print(scores[3], "\n")
    else:
        print("ไม่มีข้อมูลที่แถว index 3", "\n")


def main_d():
    print("โจทย์ d: แก้ไขตัวเลข 4 ให้เป็น 0 ในตาราง scores")
    scores = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [5, 4, 3, 2, 1]]

    N = len(scores)
    for i in range(N):
        for j in range(len(scores[i])):
            if scores[i][j] == 4:
                scores[i][j] = 0

    for i in range(N):
        print(scores[i])
    print()


def main_e():
    print("โจทย์ e: เพิ่มแถวใหม่ที่ประกอบด้วยเลข 0 ทั้งหมดในตาราง scores")
    scores = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [5, 4, 3, 2, 1]]

    N = len(scores)

    for i in range(N):
        for j in range(len(scores[i])):
            if scores[i][j] == 4:
                scores[i][j] = 0

    new_row = [0] * len(scores[0])
    scores.append(new_row)

    for i in range(len(scores)):
        print(scores[i])
    print()


if __name__ == "__main__":
    print("\n__________________ 6.1 _____________\n")
    main_a()
    print("\n____________________________________\n")
    main_b()
    print("\n____________________________________\n")
    main_c()
    print("\n____________________________________\n")
    main_d()
    print("\n____________________________________\n")
    main_e()
    print("\n____________________________________\n")
