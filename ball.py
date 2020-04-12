from constants import *
from random import choice
import pygame
pygame.init()


class Ball:
    def __init__(self):
        self.x, self.y, self.dx, self.dy, self.rect = self.restart()
        self.score1 = 0
        self.score2 = 0
        self.winner = None

    def restart(self):
        x = WINDOW_WIDTH / 2 - 8
        y = WINDOW_HEIGHT / 2 - 8
        dx = choice([2, 4]) * choice([-1, 1])
        dy = choice([2, 4]) * choice([-1, 1])
        rect = pygame.Rect(x, y, 16, 16)
        return x, y, dx, dy, rect

    def draw(self, win):
        pygame.draw.rect(win, (255, 255, 255), self.rect)

    def move(self, paddle1, paddle2):
        self.x += self.dx
        self.y += self.dy
        if self.y <= 0 or self.y >= WINDOW_HEIGHT - 72:
            self.dy *= -1
        if self.x <= 0:
            self.score1 += 1
            self.x, self.y, self.dx, self.dy, self.rect = self.restart()
        if self.x >= WINDOW_WIDTH - 16:
            self.score2 += 1
            self.x, self.y, self.dx, self.dy, self.rect = self.restart()
        if self.rect.colliderect(paddle1.rect) or self.rect.colliderect(paddle2.rect):
            self.dx *= -1
            if self.rect.colliderect(paddle1.rect):
                self.x = paddle1.rect.x - 16
            else:
                self.x = paddle2.rect.x + 20
        if self.score1 >= 7:
            self.dx = 0
            self.dy = 0
            self.winner = paddle1
        if self.score2 >= 7:
            self.dx = 0
            self.dy = 0
            self.winner = paddle2
        self.update()

    def update(self):
        self.rect = pygame.Rect(self.x, self.y, 16, 16)
