import sys
import time

import pygame
from players import GameObject
from pygame.locals import *

from scenes.end import game_over

BLACK = (0, 0, 0)

pygame.init()

clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)

size = width, height = 240, 320
speed = [10, 10]
white = (240, 240, 240)

screen = pygame.display.set_mode(size)
screen.fill(white)

hero = pygame.image.load('black-dot.jpg').convert()
hero_rect = hero.get_rect()

villain = pygame.image.load('green-dot.jpg').convert()
villain_rect = villain.get_rect()
villain_rect = villain_rect.move(120, 120)

pygame.display.set_caption('Gimme them dots')
large_text = pygame.font.Font(None, 80)

game_on = True

def game_intro():
    text = large_text.render('Willkommen', True, BLACK)
    text_rect = text.get_rect()
    text_x = screen.get_width() / 2 - text_rect.width / 2
    text_y = screen.get_height() / 2 - text_rect.height / 2
    screen.blit(text, [text_x, text_y])
    pygame.display.update()

while game_on:
    #if pygame.time.get_ticks() < 3000:
    #    game_intro()
    #    print('here')
    #    pygame.display.update()
    #else:

    if hero_rect.colliderect(villain_rect):
        game_over('farts')

    screen.blit(villain, villain_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False

        #screen.fill(white)
        screen.fill(white, hero_rect)
        #pygame.display.update(hero_rect)

        if event.type == pygame.KEYDOWN:
            print(event)
            if event.key == 273:
                hero_rect = hero_rect.move(0, -speed[1])
            elif event.key == 274:
                hero_rect = hero_rect.move(0, speed[1])
            elif event.key == 275:
                hero_rect = hero_rect.move(speed[0], 0)
            elif event.key == 276:
                hero_rect = hero_rect.move(-speed[0], 0)

    if hero_rect.top < 0:
        hero_rect.bottom = height
    elif hero_rect.bottom > height:
        hero_rect.top = 0
    elif hero_rect.left < 0:
        hero_rect.right = width
    elif hero_rect.right > width:
        hero_rect.left = 0

    screen.blit(hero, hero_rect)
    #pygame.display.update()
    pygame.display.update(hero_rect)

pygame.display.quit()
pygame.quit()
quit()
