import sys

from players import GameObject
import pygame
from pygame.locals import *

pygame.init()

size = width, height = 240, 320
speed = [10, 10]
white = (240, 240, 240)

screen = pygame.display.set_mode(size)

dot = pygame.image.load('black-dot.jpg').convert()
dotrect = dot.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            print(event)
            if event.key == 273:
                dotrect = dotrect.move(0, -speed[1])
            elif event.key == 274:
                dotrect = dotrect.move(0, speed[1])
            elif event.key == 275:
                dotrect = dotrect.move(speed[0], 0)
            elif event.key == 276:
                dotrect = dotrect.move(-speed[0], 0)

    if dotrect.top < 0:
        dotrect.bottom = height
    elif dotrect.bottom > height:
        dotrect.top = 0
    elif dotrect.left < 0:
        dotrect.right = width
    elif dotrect.right > width:
        dotrect.left = 0

    screen.fill(white)
    screen.blit(dot, dotrect)
    pygame.display.flip()
