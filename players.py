import random

from pygame import time as pytime

from constants import DISPLAY_WIDTH, DISPLAY_HEIGHT


class GameObject(object):
    def __init__(self, image, speed=5, x_pos=100, y_pos=75):
        self.speed = speed
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left = x_pos
        self.rect.top = y_pos

    def update(self, left, right, up, down):
        raise NotImplementedError

    def swap_borders(self):
        if self.rect.top < 0:
            self.rect.top = DISPLAY_HEIGHT
        if self.rect.top > DISPLAY_HEIGHT:
            self.rect.top = 0
        if self.rect.left > DISPLAY_WIDTH:
            self.rect.left = 0
        if self.rect.left < 0:
            self.rect.left = DISPLAY_WIDTH


class Player(GameObject):
    def update(self, left, right, up, down):
        x_change = 0
        y_change = 0
        if left:
            x_change += -self.speed
        if right:
            x_change += self.speed
        if up:
            y_change += -self.speed
        if down:
            y_change += self.speed
        self.rect.left += x_change
        self.rect.top += y_change
        self.swap_borders()


class Enemy(GameObject):
    def update(self):
        x_change = self.speed * random.choice([-1, 1])
        y_change = self.speed * random.choice([-1, 1])
        self.rect.left += x_change
        self.rect.top += y_change
        self.swap_borders()


class Target(Enemy):
    pass
