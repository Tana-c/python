import json
import os
from settings import high_score_file

def load_high_score():
    if os.path.exists(high_score_file):
        with open(high_score_file, "r") as file:
            return json.load(file)
    return {}

def save_high_score(song_name, score):
    high_scores = load_high_score()
    
    # ตรวจสอบว่าเพลงนี้มีลิสต์ของคะแนนหรือไม่ ถ้าไม่มีให้สร้างใหม่
    if song_name not in high_scores or not isinstance(high_scores[song_name], list):
        high_scores[song_name] = []  # สร้างลิสต์ใหม่หากยังไม่มี

    # เพิ่มคะแนนใหม่ลงในลิสต์
    high_scores[song_name].append(score)
    # จัดเรียงลิสต์คะแนนจากมากไปน้อย และเก็บแค่ 5 อันดับแรก
    high_scores[song_name] = sorted(high_scores[song_name], reverse=True)[:5]

    # บันทึกคะแนนใหม่ลงไฟล์
    with open(high_score_file, "w") as file:
        json.dump(high_scores, file)

def display_high_scores(song_name):
    high_scores = load_high_score()

    # ตรวจสอบว่าเพลงนี้มีคะแนนบันทึกอยู่หรือไม่
    if song_name in high_scores:
        print(f"High Scores for '{song_name}':")
        for index, score in enumerate(high_scores[song_name], start=1):
            print(f"{index}: {score}")
        # เติมช่องว่างถ้าคะแนนไม่ถึง 5
        for index in range(len(high_scores[song_name]) + 1, 6):
            print(f"{index}: -")
    else:
        print(f"No high scores recorded for '{song_name}'.")
