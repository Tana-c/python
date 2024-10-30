import pygame
pygame.init()

import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, difficulty_settings
from game.utils import show_song_menu, show_end_screen, show_leaderboard
from game.music import play_music
from game.loop import game_loop

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Piano Tap Tap")

# Run the game
selected_song = show_song_menu(screen)
while selected_song:  # Loop to replay if user selects "Play Again"
    song_name, song_file = selected_song
    play_music(song_file)  # Replay the song each time the game starts
    game_loop(screen, difficulty_settings["Medium"], song_name, song_file)

    # After game loop ends, show leaderboard and end screen
    show_leaderboard(screen, song_name)  # Show leaderboard after game
    if not show_end_screen(screen, song_name, score=0):  # Replace score=0 with the actual score variable
        break  # Exit the loop if the player doesn't want to replay
    selected_song = show_song_menu(screen)

pygame.quit()
sys.exit()
