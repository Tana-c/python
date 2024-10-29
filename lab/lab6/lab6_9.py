import pandas as pd
import os


def read_distance_matrix(file_path):
    """อ่านตารางระยะทางจากไฟล์ CSV และแปลงเป็น DataFrame"""
    if not os.path.isfile(file_path):
        print(f"ไม่พบไฟล์ที่ตำแหน่ง: {file_path}")
        return None

    try:
        df = pd.read_csv(file_path, header=None)
        return df
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการอ่านไฟล์: {e}")
        return None


def calculate_total_distance(df, route):
    """คำนวณระยะทางรวมตามเส้นทางที่กำหนด"""
    total_distance = 0
    for i in range(len(route) - 1):
        start = route[i]
        end = route[i + 1]
        total_distance += df.iloc[start, end]

    total_distance += df.iloc[route[-1], route[0]]

    return total_distance


def main():
    current_path = os.getcwd()
    file_path = os.path.join(current_path, "lab6", "DM.csv")

    df = read_distance_matrix(file_path)
    if df is not None:
        route = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        total_distance = calculate_total_distance(df, route)
        print(
            f"ระยะทางรวมสำหรับเส้นทาง T1 -> T2 -> T3 -> T4 -> T5 -> T6 -> T7 -> T8 -> T9 -> T10 -> T1: {total_distance} หน่วย"
        )


if __name__ == "__main__":
    print("\n_____________ 6.9 _________________\n")
    main()
    print("\n____________________________________\n")
