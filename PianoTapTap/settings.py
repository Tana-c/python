# settings.py

# Screen settings
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SCREEN_WIDTH, SCREEN_HEIGHT = 400, 700

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Block settings
BLOCK_WIDTH = SCREEN_WIDTH // 4
BLOCK_HEIGHT = 150
HIT_TOLERANCE = 20

# Hit line position
HIT_LINE_Y = SCREEN_HEIGHT - 150
HIT_TOLERANCE = 120  # เพิ่มช่วงยอมรับการตี

# Difficulty settings
difficulty_settings = {
    "Easy": 3,
    "Medium": 5,
    "Hard": 7
}

# Song options
songs = {
    "Song 1": os.path.join(BASE_DIR, "assets/songs/Christina.mp3"),
    "Song 2": os.path.join(BASE_DIR, "assets/songs/Rush_E_Hard.mp3"),
    "Song 3": os.path.join(BASE_DIR, "assets/songs/Wellerman.mp3")
}

# High score file
high_score_file = "high_scores.json"
