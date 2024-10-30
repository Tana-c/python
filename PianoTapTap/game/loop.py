import random
import pygame
from game.blocks import Block
from game.score import save_high_score
from game.music import get_beats
from game.utils import show_end_screen, show_song_menu  # นำเข้า show_song_menu
from settings import BLOCK_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH, WHITE, GREEN, HIT_LINE_Y, BLOCK_HEIGHT, difficulty_settings
from PIL import Image  # Import for GIF handling

def check_hit(block, key):
    # จับคู่ปุ่มกับคอลัมน์
    key_column_map = {
        pygame.K_1: 0,
        pygame.K_2: 1,
        pygame.K_3: 2,
        pygame.K_4: 3
    }
    # ตรวจสอบว่าคอลัมน์ของปุ่มที่กดตรงกับคอลัมน์ของบล็อก
    return key_column_map.get(key) == block.column
# ฟังก์ชันโหลด GIF frames
def load_gif_frames(gif_path, size=(SCREEN_WIDTH, SCREEN_HEIGHT)):
    gif = Image.open(gif_path)
    frames = []

    # Iterate over GIF frames and resize them
    try:
        while True:
            frame = gif.copy()
            frame = frame.convert("RGBA")
            frame = frame.resize(size)
            frames.append(pygame.image.fromstring(frame.tobytes(), frame.size, frame.mode))
            gif.seek(len(frames))  # Move to next frame
    except EOFError:
        pass  # End of frames

    return frames

# Load GIF frames
gif_path = "C:/3_1/BABANK_PY/game02/PianoTapTap/assets/images/bg5.gif"
background_frames = load_gif_frames(gif_path)
frame_count = len(background_frames)
frame_index = 0

# Frame duration settings
frame_duration = 100  # Duration for each frame in milliseconds
last_update_time = pygame.time.get_ticks()

def game_loop(screen, speed, song_name, song_file):
    score = 0
    combo = 0
    missed_attempts = 0  # ตัวแปรนับจำนวนครั้งที่กดพลาด
    clock = pygame.time.Clock()
    blocks = []
    running = True
    paused = False
    
    # ตั้งค่าจังหวะสำหรับบล็อกใหม่
    beat_times = get_beats(song_file)
    beat_index = 0
    start_time = pygame.time.get_ticks()

    # ตั้งค่าเริ่มต้นสำหรับ GIF background
    frame_index = 0
    last_update_time = pygame.time.get_ticks()  # กำหนดค่าเริ่มต้นที่นี่
    frame_duration = 100  # กำหนดระยะเวลาแสดงแต่ละเฟรมของ GIF

    # ตัวจับเวลา Flash สำหรับบล็อก
    flash_timer = 0
    flash_block_pos = None  # ตำแหน่งของบล็อกที่กดถูกต้อง

    while running:
        # อัพเดตเฟรมพื้นหลัง GIF ตามเวลา
        current_time = pygame.time.get_ticks()
        if current_time - last_update_time >= frame_duration:
            frame_index = (frame_index + 1) % frame_count  # Loop back to start after last frame
            last_update_time = current_time

        # วาดพื้นหลังเฟรม GIF
        screen.blit(background_frames[frame_index], (0, 0))

        delta_time = clock.tick(60) / 1000  # เวลาต่อเฟรม

        # จัดการอีเวนต์
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and not paused:
                # ตรวจสอบการกดคีย์
                if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
                    if blocks:  # ตรวจสอบว่ามีบล็อกอยู่ในลิสต์
                        block = blocks[0]
                        if check_hit(block, event.key):  # ตรวจสอบบล็อกในคอลัมน์ที่ถูกต้อง
                            score += 1
                            combo += 1
                            speed += 0.1
                            flash_timer = current_time + 100  # แสดง Flash 100 มิลลิวินาที
                            flash_block_pos = (block.x, block.y)
                            blocks.pop(0)  # ลบบล็อกที่กดถูก
                        else:
                            combo = 0  # รีเซ็ตคอมโบหากกดผิด
                            missed_attempts += 1  # เพิ่มการนับการกดผิด
                            if missed_attempts >= 10:  # เช็คว่ากดผิดครบ 10 ครั้งหรือไม่
                                running = False  # จบเกมทันทีเมื่อกดผิดครบ 10 ครั้ง

        # สร้างบล็อกใหม่ตามจังหวะ
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
        if beat_index < len(beat_times) and elapsed_time >= beat_times[beat_index]:
            blocks.append(Block(speed))
            beat_index += 1

        # อัพเดตและวาดบล็อก
        for block in blocks[:]:
            block.move()
            block.draw(screen)
            
            if block.is_off_screen():  # ตรวจสอบว่าบล็อกหลุดขอบล่างหรือไม่
                blocks.remove(block)
                combo = 0
                missed_attempts += 1  # นับว่ากดพลาดหากบล็อกเลยขอบล่างของหน้าจอ
                if missed_attempts >= 10:  # จบเกมถ้ากดพลาดเกิน 10 ครั้ง
                    running = False

        # วาด Flash Effect รอบบล็อกที่ถูกกด
        if flash_timer > current_time and flash_block_pos:
            flash_x, flash_y = flash_block_pos
            pygame.draw.rect(screen, pygame.Color("white"), (flash_x - 5, flash_y - 5, BLOCK_WIDTH + 10, BLOCK_HEIGHT + 10), 3)

        # วาดเส้นและแสดงคะแนน
        pygame.draw.line(screen, GREEN, (0, HIT_LINE_Y + BLOCK_HEIGHT), (screen.get_width(), HIT_LINE_Y + BLOCK_HEIGHT), 3)
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, pygame.Color("red"))
        combo_text = font.render(f"Combo: {combo}", True, pygame.Color("blue"))
        missed_text = font.render(f"Missed: {missed_attempts}/10", True, pygame.Color("orange"))  # แสดงจำนวนครั้งที่กดพลาด
        
        screen.blit(score_text, (10, 10))
        screen.blit(combo_text, (10, 50))
        screen.blit(missed_text, (10, 90))  # เพิ่มข้อความแสดงการกดพลาด
        
        pygame.display.flip()

    # บันทึกคะแนนและแสดงหน้าจอจบเกม
    save_high_score(song_name, score)
    if show_end_screen(screen, song_name, score):
        selected_song = show_song_menu(screen)
        game_loop(screen, difficulty_settings["Medium"], selected_song[0], selected_song[1])