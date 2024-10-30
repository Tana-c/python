# game/music.py

import pygame
import librosa
import sys
from settings import songs
def play_music(song_file):
    try:
        pygame.mixer.init()  # Initialize mixer if not already
        pygame.mixer.music.load(song_file)
        pygame.mixer.music.play()
    except pygame.error as e:
        print(f"Error loading music file {song_file}: {e}")
        pygame.quit()
        sys.exit()

def get_beats(song_file):
    try:
        y, sr = librosa.load(song_file)
        tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
        beat_times = librosa.frames_to_time(beats, sr=sr)
        return beat_times
    except Exception as e:
        print(f"Error analyzing beats from {song_file}: {e}")
        pygame.quit()
        sys.exit()
