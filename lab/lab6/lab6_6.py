import pandas as pd
import os


def read_and_analyze_csv(file_path):
    """อ่านข้อมูลจากไฟล์ CSV และแสดงข้อมูลและสถิติพื้นฐาน"""
    if not os.path.isfile(file_path):
        print(f"ไม่พบไฟล์ที่ตำแหน่ง: {file_path}")
        return

    try:
        df = pd.read_csv(file_path)
        print("ข้อมูลจากไฟล์ CSV:")
        print(df, "\n")
        print("ข้อมูลทางสถิติพื้นฐาน:")
        stats = df.describe(include="all")
        print(stats[["Lat", "Lng"]])
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการอ่านไฟล์: {e}")


if __name__ == "__main__":
    current_path = os.getcwd()
    file_path = os.path.join(current_path, "lab6", "travel.csv")

    read_and_analyze_csv(file_path)
