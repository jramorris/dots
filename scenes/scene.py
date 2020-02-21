import pygame

from players import GameObject, Enemy
from constants import DISPLAY_WIDTH, DISPLAY_HEIGHT


class GameScene(object):
    def __init__(self):
        pass

    def render(self, screen):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def handle_events(self, events):
        raise NotImplementedError


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
        screen.fill((0,0,0))
        text = self.font.render('Ready?', True, (255, 255, 255))
        width = text.get_rect().width / 2
        height = text.get_rect().height / 2
        screen.blit(text, (DISPLAY_WIDTH / 2 - width, DISPLAY_HEIGHT / 2 - height))


class LevelOne(GameScene):
    def __init__(self):
        super(LevelOne, self).__init__()
        self.font = pygame.font.SysFont('Arial', 32)
        self.player = GameObject(pygame.image.load('green-dot.jpg'))
        self.enemies = [Enemy(pygame.image.load('black-dot.jpg')) for x in range(5)]
        self.dead = False

    def handle_events(self, events):
        pass

    def render(self, screen):
        screen.fill((240, 240, 240))
        screen.blit(self.player.image, (self.player.rect))
        for enemy in self.enemies:
            screen.blit(enemy.image, (enemy.rect))
        if self.dead:
            self.manager.go_to(DeathScene())

    def update(self):
        pressed = pygame.key.get_pressed()
        left, right, up, down = [pressed[key] for key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN)]
        self.player.update(left, right, up, down)
        for enemy in self.enemies:
            enemy.update()
        collide = any(self.player.rect.colliderect(enemy.rect) for enemy in self.enemies)
        if collide:
            self.dead = True
        #self.camera.update(self.player)


class DeathScene(GameScene):
    def __init__(self):
        super(DeathScene, self).__init__()
        self.start_time = pygame.time.get_ticks()
        self.font = pygame.font.SysFont('Arial', 32)

    def handle_events(self, events):
        if pygame.time.get_ticks() - self.start_time > 2000:
            self.manager.go_to(TitleScene())

    def update(self):
        pass

    def render(self, screen):
        # beware: ugly! 
        if pygame.time.get_ticks() - self.start_time > 500:
            screen.fill((255, 255, 255))
            text = self.font.render('Dead', True, (0,0,0))
            screen.blit(text, (10, 75))
