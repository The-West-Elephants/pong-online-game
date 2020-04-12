from constants import *
from network import Network
from paddle import Paddle
from ball import Ball
import pygame
pygame.init()

font = pygame.font.SysFont(None, 60)
big_font = pygame.font.SysFont(None, 80)


class Client:
    def __init__(self):
        port = int(input('Which port are you going to connect to? '))
        self.name = input('What is your name? ')
        n = Network(port)
        x = n.get_xpos()
        player_count = n.get_player_count()
        self.player = Paddle(self.name, x, player_count)
        self.player2 = n.send_paddle(self.player)
        print('Connected to server.')
        self.main(n)

    def main(self, n):
        window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('You are ' + self.name + '!')
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
            ball = n.get_ball()
            self.player2 = n.send_paddle(self.player)
            self.update_window(window, ball)

    def update_window(self, win, ball):
        win.fill((0, 0, 0))
        score1 = font.render(str(ball.score1), False, (255, 255, 255))
        score2 = font.render(str(ball.score2), False, (255, 255, 255))
        win.blit(score1, (WINDOW_WIDTH / 2 + 220, 20))
        win.blit(score2, (WINDOW_WIDTH / 2 - 220, 20))
        name1 = font.render(self.player.name, False, (255, 255, 255))
        name2 = font.render(self.player2.name, False, (255, 255, 255))
        if self.player.id == 1:
            win.blit(name1, (WINDOW_WIDTH - list(name1.get_rect())[2] - 100, 20))
            win.blit(name2, (100, 20))
        else:
            win.blit(name1, (100, 20))
            win.blit(name2, (WINDOW_WIDTH - list(name2.get_rect())[2] - 100, 20))
        if ball.score1 < 7 and ball.score2 < 7:
            ball.draw(win)
            self.player.move()
            self.player.draw(win)
            self.player2.draw(win)
            pygame.draw.rect(win, (255, 255, 255), (WINDOW_WIDTH / 2 - 5, 0, 10, WINDOW_HEIGHT))
        else:
            if ball.winner.id == self.player.id:
                won = big_font.render('You won!', False, (0, 255, 0))
                pos = (WINDOW_WIDTH / 2 - list(won.get_rect())[2] / 2, WINDOW_HEIGHT / 2 - list(won.get_rect())[3] / 2)
                win.blit(won, pos)
            else:
                lost = big_font.render('You lost!', False, (255, 0, 0))
                pos = (WINDOW_WIDTH / 2 - list(lost.get_rect())[2] / 2, WINDOW_HEIGHT / 2 - list(lost.get_rect())[3] / 2)
                win.blit(lost, pos)
        pygame.display.update()


if __name__ == '__main__':
    client = Client()
