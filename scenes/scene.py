import pygame

from players import Enemy, Player, Target
from constants import DISPLAY_WIDTH, DISPLAY_HEIGHT

KEYS = (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN)


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
    def __init__(self, score=0):
        super(LevelOne, self).__init__()
        self.font = pygame.font.SysFont('Arial', 32)
        self.player = Player(pygame.image.load('green-dot.jpg').convert_alpha())
        self.enemies = [Enemy(pygame.image.load('black-dot.jpg').convert_alpha(), speed=1, y_pos=100) for x in range(5)]
        self.target = Target(pygame.image.load('red-dot.jpg').convert_alpha(), speed=1, y_pos=100)
        self.dead = False
        self.score = score
        self.score_text = score

    def handle_events(self, events):
        pass

    def render(self, screen):
        screen.fill((240, 240, 240))
        screen.blit(self.player.image, self.player.rect)
        score_text = self.font.render(str(self.score), True, (0,0,0))
        screen.blit(score_text, (0,0))
        for enemy in self.enemies:
            screen.blit(enemy.image, enemy.rect)
        screen.blit(self.target.image, self.target.rect)
        if self.dead:
            self.manager.go_to(DeathScene())

    def update(self):
        pressed = pygame.key.get_pressed()
        left, right, up, down = [pressed[key] for key in KEYS]
        self.player.update(left, right, up, down)
        for enemy in self.enemies:
            enemy.update()
        self.target.update()
        collide = any(self.player.rect.colliderect(enemy.rect) for enemy in self.enemies)
        if self.player.rect.colliderect(self.target.rect):
            self.score += 1
            self.enemies.append(Enemy(pygame.image.load('black-dot.jpg').convert_alpha(), speed=1, y_pos=100))
            self.target.rect.top = self.player.rect.left
            self.target.rect.left = self.player.rect.top
        if collide:
            self.dead = True


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
