# game/utils.py

import pygame
import sys
import os
import time
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK, BLUE, YELLOW, songs
from game.score import load_high_score
from PIL import Image


# โหลดเอฟเฟกต์เสียง
select_sound = pygame.mixer.Sound("C:/3_1/BABANK_PY/game02/PianoTapTap/assets/Effect/Select.mp3")
play_sound = pygame.mixer.Sound("C:/3_1/BABANK_PY/game02/PianoTapTap/assets/Effect/play.mp3")
game_over_sound = pygame.mixer.Sound("C:/3_1/BABANK_PY/game02/PianoTapTap/assets/Effect/gameover.mp3")

# ฟังก์ชันสำหรับการโหลดฟอนต์ที่กำหนดเอง
def get_font(size=36):
    font_path = os.path.join("C:/3_1/BABANK_PY/game02/PianoTapTap/fonts", "font2.ttf")
    return pygame.font.Font(font_path, size)

def draw_text_centered(text, font, color, screen, y):
    """วาดข้อความให้อยู่ตรงกลางตามแกน X"""
    text_surface = font.render(text, True, color)
    x = (SCREEN_WIDTH - text_surface.get_width()) // 2
    screen.blit(text_surface, (x, y))

def show_song_menu(screen):
    font_title = get_font(60)
    font_button = get_font(36)
    screen.fill((30, 30, 30))  # พื้นหลังสีเข้ม
    draw_text_centered("Select Song", font_title, YELLOW, screen, 80)

    buttons = []
    for i, (song_name, song_file) in enumerate(songs.items()):
        button_text = font_button.render(song_name, True, BLACK)
        button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, 200 + i * 80, 200, 60)
        buttons.append((button_rect, song_name, song_file))

        # วาดปุ่มสีเหลืองและมุมโค้ง
        pygame.draw.rect(screen, YELLOW, button_rect, border_radius=15)
        screen.blit(button_text, (button_rect.x + (button_rect.width - button_text.get_width()) // 2,
                                  button_rect.y + (button_rect.height - button_text.get_height()) // 2))

    pygame.display.flip()

    selected_song = None
    last_hovered_button = None  # ปุ่มที่เคยเลื่อนผ่านล่าสุด
    flash_timer = 0  # กำหนดตัวจับเวลา Flash Effect

    while selected_song is None:
        current_time = pygame.time.get_ticks()  # เวลาในหน่วยมิลลิวินาที
        mouse_pos = pygame.mouse.get_pos()  # ตำแหน่งเมาส์ปัจจุบัน

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button_rect, song_name, song_file in buttons:
                    if button_rect.collidepoint(mouse_pos):
                        play_sound.play()  # เล่นเสียงกดปุ่ม
                        selected_song = (song_name, song_file)

        # Flash Effect เมื่อเลื่อนผ่านปุ่ม
        screen.fill((30, 30, 30))  # รีเซ็ตพื้นหลัง
        draw_text_centered("Select Song", font_title, YELLOW, screen, 80)

        for button_rect, song_name, song_file in buttons:
            if button_rect.collidepoint(mouse_pos):
                # วาด Flash Effect รอบปุ่มเมื่อเมาส์เลื่อนผ่าน
                if last_hovered_button != button_rect:
                    select_sound.play()  # เล่นเสียงเลื่อนผ่านปุ่ม
                    last_hovered_button = button_rect
                    flash_timer = current_time + 100  # ตั้งเวลา Flash ให้ค้าง 100 มิลลิวินาที

                # วาดกรอบสีขาวเป็น Flash Effect
                if flash_timer > current_time:
                    pygame.draw.rect(screen, pygame.Color("white"), button_rect.inflate(10, 10), 4, border_radius=18)

            # วาดปุ่มปกติ
            pygame.draw.rect(screen, YELLOW, button_rect, border_radius=15)
            button_text = font_button.render(song_name, True, BLACK)
            screen.blit(button_text, (button_rect.x + (button_rect.width - button_text.get_width()) // 2,
                                      button_rect.y + (button_rect.height - button_text.get_height()) // 2))

        # รีเซ็ต Flash Effect เมื่อเมาส์ออกจากปุ่ม
        if not any(button_rect.collidepoint(mouse_pos) for button_rect, _, _ in buttons):
            last_hovered_button = None

        # อัปเดตหน้าจอ
        pygame.display.flip()

    return selected_song


def show_leaderboard(screen, song_name):
    font_title = get_font(48)
    font_score = get_font(36)
    high_scores = load_high_score()
    scores = high_scores.get(song_name, [])

    # เรียงคะแนนจากมากไปน้อย และจำกัดการแสดงเพียง 5 อันดับแรก
    scores = sorted(scores, reverse=True)[:5]

    # ตั้งค่าพื้นหลังและข้อความหัวข้อ
    screen.fill((40, 40, 40))  # สีพื้นหลังแบบเข้ม
    draw_text_centered(f"Leaderboard for {song_name}", font_title, YELLOW, screen, 50)

    # แสดงคะแนนสูงสุด 5 อันดับในแนวตั้งพร้อมหมายเลขลำดับ
    y_start = 150
    for i, score in enumerate(scores):
        score_text = f"{i + 1}. {score}"  # เพิ่มหมายเลขลำดับหน้าคะแนน
        text_surface = font_score.render(score_text, True, BLUE)
        screen.blit(text_surface, (SCREEN_WIDTH // 2 - text_surface.get_width() // 2, y_start + i * 50))

    pygame.display.flip()

    # รอให้ผู้ใช้ปิดหน้าจอ
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False
                return True
    return False


def show_end_screen(screen, song_name, score):
    # หยุดเพลงเมื่อเข้าสู่หน้าจอจบเกม
    pygame.mixer.music.stop()
    game_over_sound.play()  # เล่นเสียงแพ้เมื่อจบเกม

    font_title = get_font(48)
    font_text = get_font(36)
    high_scores = load_high_score()
    
    # ดึงคะแนนสำหรับเพลงที่เล่น และเรียงลำดับจากมากไปน้อย โดยแสดงเฉพาะ 5 อันดับแรก
    scores = high_scores.get(song_name, [])
    top_scores = sorted(scores, reverse=True)[:5]  # เรียงจากมากไปน้อยและเลือก 5 อันดับแรก

    # ล้างหน้าจอและแสดงข้อความคะแนน
    screen.fill((50, 50, 50))
    draw_text_centered("Game Over!", font_title, YELLOW, screen, 80)
    draw_text_centered(f"Score: {score}", font_text, WHITE, screen, 150)

    # แสดงคะแนนสูงสุด 5 อันดับ
    for i, high_score in enumerate(top_scores):
        score_text = font_text.render(f"{i + 1}. {high_score}", True, pygame.Color("red"))
        screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 220 + i * 40))

    # ปุ่มเล่นใหม่
    retry_text = font_text.render("Play Again", True, BLACK)
    retry_button = pygame.Rect(SCREEN_WIDTH // 2 - 100, 420, 200, 60)
    pygame.draw.rect(screen, BLUE, retry_button, border_radius=15)
    screen.blit(retry_text, (retry_button.x + (retry_button.width - retry_text.get_width()) // 2,
                             retry_button.y + (retry_button.height - retry_text.get_height()) // 2))

    pygame.display.flip()

    # รอให้ผู้ใช้คลิกปุ่มเล่นใหม่
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if retry_button.collidepoint(event.pos):
                    waiting = False
                    return True
    return False