import time

import pygame

pygame.init()
size = width, height = 240, 320
screen = pygame.display.set_mode(size)
font = pygame.font.Font(None, 36)
BLACK = (0, 0, 0)
white = (240, 240, 240)
clock = pygame.time.Clock()


def game_over(end_text='Game Over'):
    text = font.render(end_text, True, BLACK)
    text_rect = text.get_rect()
    text_x = screen.get_width() / 2 - text_rect.width / 2
    text_y = screen.get_height() / 2 - text_rect.height / 2
    screen.blit(text, [text_x, text_y])

