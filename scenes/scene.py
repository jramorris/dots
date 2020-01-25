import pygame

from players import GameObject


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
        text = self.font.render('> press space to start <', True, (255, 255, 255))
        screen.blit(text, (100, 75))


class LevelOne(GameScene):
    def __init__(self):
        super(LevelOne, self).__init__()
        self.font = pygame.font.SysFont('Arial', 32)
        self.player = GameObject(pygame.image.load('green-dot.jpg'))

    def handle_events(self, events):
        pass

    def render(self, screen):
        screen.fill((240, 240, 240))
        screen.blit(self.player.image, (self.player.x_pos, 75))

    def update(self):
        pressed = pygame.key.get_pressed()
        left, right = [pressed[key] for key in (pygame.K_LEFT, pygame.K_RIGHT)]
        self.player.update(left, right)
        #self.enemy.update(self.platforms)
        #self.camera.update(self.player)
