# game/blocks.py

import pygame
import random
from settings import BLOCK_WIDTH, BLOCK_HEIGHT, SCREEN_HEIGHT, HIT_LINE_Y, BLACK

class Block:
    def __init__(self, speed):
        self.column = random.randint(0, 3)
        self.x = self.column * BLOCK_WIDTH
        self.y = -BLOCK_HEIGHT
        self.speed = speed

    def move(self):
        self.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, (self.x, self.y, BLOCK_WIDTH, BLOCK_HEIGHT))
    def is_off_screen(self):
        return self.y > SCREEN_HEIGHT
