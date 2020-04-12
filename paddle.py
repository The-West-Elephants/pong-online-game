from constants import *
import pygame


class Paddle:
    def __init__(self, name, x, player_count):
        self.id = player_count
        self.name = name
        self.x = x
        self.y = WINDOW_HEIGHT / 2 - 50
        self.rect = pygame.Rect(self.x, self.y, 20, 100)

    def draw(self, win):
        pygame.draw.rect(win, (255, 255, 255), self.rect)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.y >= 3:
            self.y -= 3
        if keys[pygame.K_DOWN] and self.y <= WINDOW_HEIGHT - 103:
            self.y += 3
        self.update()

    def update(self):
        self.rect = pygame.Rect(self.x, self.y, 20, 100)
