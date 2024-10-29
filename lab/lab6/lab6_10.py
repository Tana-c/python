import os
import pandas as pd
import numpy as np


def read_distance_matrix(file_path):
    """อ่านตารางระยะทางจากไฟล์ CSV และแปลงเป็น DataFrame"""
    if not os.path.isfile(file_path):
        print(f"ไม่พบไฟล์ที่ตำแหน่ง: {file_path}")
        return None

    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการอ่านไฟล์: {e}")
        return None


def haversine(lat1, lon1, lat2, lon2):
    """คำนวณระยะทางระหว่างสองจุดในหน่วยกิโลเมตร"""
    R = 6371  # Earth's radius in kilometers
    dlat = np.radians(lat2 - lat1)
    dlon = np.radians(lon2 - lon1)
    a = (
        np.sin(dlat / 2) ** 2
        + np.cos(np.radians(lat1)) * np.cos(np.radians(lat2)) * np.sin(dlon / 2) ** 2
    )
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    distance = R * c
    return distance


def calculate_shortest_path(df):
    """คำนวณระยะทางที่สั้นที่สุดโดยใช้ Dynamic Programming กับ Bitmasking"""
    n = len(df)

    # สร้าง matrix สำหรับระยะทาง
    dist = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            lat1 = df.iloc[i, 1]
            lon1 = df.iloc[i, 2]
            lat2 = df.iloc[j, 1]
            lon2 = df.iloc[j, 2]
            dist[i][j] = haversine(lat1, lon1, lat2, lon2)

    # DP Table
    dp = np.full((1 << n, n), float("inf"))
    dp[1][0] = 0  # เริ่มต้นที่เมือง 0

    # การคำนวณ DP
    for mask in range(1 << n):
        for u in range(n):
            if dp[mask][u] == float("inf"):
                continue
            for v in range(n):
                if mask & (1 << v) == 0:  # ถ้า v ยังไม่ได้ถูกเยี่ยมชม
                    next_mask = mask | (1 << v)
                    dp[next_mask][v] = min(dp[next_mask][v], dp[mask][u] + dist[u][v])

    # คำนวณระยะทางกลับไปที่เมืองเริ่มต้น และติดตามเส้นทาง
    min_distance = float("inf")
    final_mask = (1 << n) - 1  # ทุกเมืองถูกเยี่ยมชม
    best_route = []

    for u in range(1, n):
        if dp[final_mask][u] < float("inf"):
            if dp[final_mask][u] + dist[u][0] < min_distance:
                min_distance = dp[final_mask][u] + dist[u][0]
                best_route = [0]  # เริ่มที่เมือง 0
                # ติดตามเส้นทาง
                mask = final_mask
                current_city = u
                for _ in range(n - 1):
                    best_route.append(current_city)
                    # หาค่ากลับ
                    for prev_city in range(n):
                        if (
                            mask & (1 << current_city)
                            and dp[mask][current_city]
                            == dp[mask ^ (1 << current_city)][prev_city]
                            + dist[prev_city][current_city]
                        ):
                            mask ^= 1 << current_city  # ทำเครื่องหมายเมืองปัจจุบันว่าเยี่ยมชมแล้ว
                            current_city = prev_city
                            break
                best_route.append(0)  # กลับไปที่เมืองเริ่มต้น

    return min_distance, best_route


def main():
    current_path = os.getcwd()
    file_path = os.path.join(current_path, "lab6", "travel.csv")
    df = read_distance_matrix(file_path)
    if df is not None:
        print(df)  # แสดงข้อมูล DataFrame
        total_distance, best_route = calculate_shortest_path(df)

        # แสดงผลลัพธ์
        route_names = [df.iloc[i, 0] for i in best_route]
        print(f"เส้นทางที่สั้นที่สุด: {' -> '.join(route_names)}")
        print(f"ระยะทางรวมที่สั้นที่สุด: {total_distance:.2f} กม")


if __name__ == "__main__":
    print("\n____________ 6.10 _________________\n")
    main()
    print("\n____________________________________\n")
