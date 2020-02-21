import random

from pygame import time as pytime


class GameObject(object):
    def __init__(self, image, speed=5, x_pos=100):
        self.speed = speed
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left = x_pos
        self.rect.top = 75

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


class Enemy(object):
    def __init__(self, image, speed=1, x_pos=100):
        self.speed = speed
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left = x_pos
        self.rect.top = 100

    def update(self):
        x_change = self.speed * random.choice([-1, 1])
        y_change = self.speed * random.choice([-1, 1])
        self.rect.left += x_change
        self.rect.top += y_change
