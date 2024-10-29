import pandas as pd
import matplotlib.pyplot as plt
import os


def plot_data(df):
    """แสดงกราฟพิกัดสถานที่ท่องเที่ยว"""
    if "Lat" in df.columns and "Lng" in df.columns:
        plt.figure(figsize=(12, 8))
        plt.scatter(df["Lat"], df["Lng"], color="red", edgecolor="k", s=100, alpha=0.7)
        plt.xlabel("Latitude")
        plt.ylabel("Longitude")
        plt.title("Scatter Plot of Tourist Attractions")

        for i, (index, row) in enumerate(df.iterrows(), start=1):
            label = f"T{i}"
            plt.text(row["Lat"], row["Lng"], label, fontsize=9, ha="right", va="bottom")

        plt.grid(True)
        plt.show()


def read_and_analyze_csv(file_path):
    """อ่านข้อมูลจากไฟล์ CSV และแสดงข้อมูลและสถิติพื้นฐาน"""
    if not os.path.isfile(file_path):
        print(f"ไม่พบไฟล์ที่ตำแหน่ง: {file_path}")
        return

    try:
        df = pd.read_csv(file_path)
        plot_data(df)
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการอ่านไฟล์: {e}")


if __name__ == "__main__":
    print("\n_____________ 6.7 _________________\n")
    current_path = os.getcwd()
    file_path = os.path.join(current_path, "lab6", "travel.csv")
    read_and_analyze_csv(file_path)
    print("\n____________________________________\n")
