import random

import pygame

from players import Enemy, Player, Target
from constants import DISPLAY_WIDTH, DISPLAY_HEIGHT

LEFT = (pygame.K_LEFT, pygame.K_a)
RIGHT = (pygame.K_RIGHT, pygame.K_d)
UP = (pygame.K_UP, pygame.K_w)
DOWN = (pygame.K_DOWN, pygame.K_s)
KEYS = (LEFT, RIGHT, UP, DOWN)
KEYS_2 = (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN)


class GameScene(object):
    def __init__(self):
        self.rects_to_update = []

    def render(self, screen):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def handle_events(self, events):
        raise NotImplementedError


class Menu(GameScene):
    def __init__(self):
        super(Menu, self).__init__()
        self.font = pygame.font.SysFont('Arial', 32)
        self.texts = [('Press Enter', TitleScene), ('Change Theme', Menu)]
        self.val = 0

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    update = False
                    if self.val:
                        update = True
                    self.manager.go_to(self.texts[self.val][1](), update)
                else:
                    self.toggle_val()

    def update(self):
        pass

    def render(self, screen):
        screen.fill(self.manager.theme)
        counter = 0
        for idx, text_tuple in enumerate(self.texts):
            counter = idx + 1
            copy = text_tuple[0]
            if idx == self.val:
                copy = '> ' + copy + ' <'
            text = self.font.render(copy, True, (34, 139, 34))
            width = text.get_rect().width / 2
            height = text.get_rect().height / 2
            item_height = DISPLAY_HEIGHT / (len(self.texts) + 1)
            screen.blit(text, (DISPLAY_WIDTH / 2 - width, (item_height * counter) - height))
            self.rects_to_update.append(text.get_rect())

    def toggle_val(self):
        if self.val:
            self.val = 0
        else:
            self.val = 1


class Settings(Menu):
    pass


class TitleScene(GameScene):
    def __init__(self):
        super(TitleScene, self).__init__()
        self.start_time = pygame.time.get_ticks()
        self.font = pygame.font.SysFont('Arial', 32)

    def handle_events(self, events):
        if pygame.time.get_ticks() - self.start_time > 2000:
            self.manager.go_to(LevelOne())

    def update(self):
        pass

    def render(self, screen):
        # beware: ugly! 
        screen.fill(self.manager.theme)
        text = self.font.render('Ready?', True, (255, 255, 255))
        width = text.get_rect().width / 2
        height = text.get_rect().height / 2
        screen.blit(text, (DISPLAY_WIDTH / 2 - width, DISPLAY_HEIGHT / 2 - height))
        self.rects_to_update.append(text.get_rect())


class LevelOne(GameScene):
    def __init__(self, score=0):
        super(LevelOne, self).__init__()
        self.font = pygame.font.SysFont('Arial', 32)
        self.player = Player(pygame.image.load('green-dot.jpg').convert_alpha())
        self.enemies = [Enemy(pygame.image.load('black-dot.jpg').convert_alpha(), speed=1, y_pos=100) for x in range(5)]
        self.target = Target(pygame.image.load('red-dot.jpg').convert_alpha(), speed=2, y_pos=100)
        self.dead = False
        self.score = score
        self.score_text = score

    def handle_events(self, events):
        pass

    def render(self, screen):
        screen.fill(self.manager.theme)
        screen.blit(self.player.image, self.player.rect)
        self.rects_to_update.append(self.player.rect)
        score_text = self.font.render(str(self.score), True, (0,0,0))
        screen.blit(score_text, (0,0))
        for enemy in self.enemies:
            screen.blit(enemy.image, enemy.rect)
            self.rects_to_update.append(enemy.rect)
        screen.blit(self.target.image, self.target.rect)
        self.rects_to_update.append(self.target.rect)

    def update(self):
        if self.dead:
            self.manager.go_to(DeathScene())

        pressed = pygame.key.get_pressed()
        left, right, up, down = [any(pressed[key] for key in key_set) for key_set in KEYS]
        self.player.update(left, right, up, down)

        for enemy in self.enemies:
            enemy.update()

        self.target.update()
        collide = any(self.player.rect.colliderect(enemy.rect) for enemy in self.enemies)
        if self.player.rect.colliderect(self.target.rect):
            self.score += 1
            self.enemies.append(Enemy.init_random())
            self.target.reset()
        if collide:
            self.dead = True


class DeathScene(GameScene):
    def __init__(self):
        super(DeathScene, self).__init__()
        self.start_time = pygame.time.get_ticks()
        self.font = pygame.font.SysFont('Arial', 32)
        pygame.mixer.music.load('fart.mp3')
        self.played = False

    def handle_events(self, events):
        if pygame.time.get_ticks() - self.start_time > 2000:
            self.manager.go_to(Menu())

    def update(self):
        pass

    def render(self, screen):
        if pygame.time.get_ticks() - self.start_time > 400 and not self.played:
            self.played = True
            pygame.mixer.music.play()

        if pygame.time.get_ticks() - self.start_time > 500:
            screen.fill((255, 255, 255))
            text = self.font.render('Dead', True, (0,0,0))
            width = text.get_rect().width / 2
            height = text.get_rect().height / 2
            screen.blit(text, (DISPLAY_WIDTH / 2 - width, DISPLAY_HEIGHT / 2 - height))
            self.rects_to_update.append(text.get_rect())
