import pygame
import time

from engine import GameEngine
from constants import DISPLAY_WIDTH, DISPLAY_HEIGHT, BLACK, WHITE

pygame.init()

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('waddupppp')
clock = pygame.time.Clock()

hero = pygame.image.load('green-dot.jpg')


def move_image(img, x, y):
    gameDisplay.blit(img, (x, y))

def game_over():
    message_display('whoops')

def text_objects(text, font):
    text_surface = font.render(text, True, BLACK)
    return text_surface, text_surface.get_rect()

def message_display(text):
    large_text = pygame.font.Font('freesansbold.ttf', 80)
    text_surf, text_rect = text_objects(text, large_text)
    text_rect.center = ((display_width / 2, display_height / 2))
    gameDisplay.blit(text_surf, text_rect)

    pygame.display.update()


def game_loop():
    engine = GameEngine()
    running = True

    while running:
        clock.tick(40)

        if pygame.event.get(pygame.QUIT):
            running = False
            return
        engine.scene.handle_events(pygame.event.get())
        engine.scene.update()
        engine.scene.render(gameDisplay)
        pygame.display.update(engine.scene.rects_to_update)
        engine.scene.rects_to_update = []
    """
    x = display_width / 2
    y = display_height / 2
    key_down = False
    game_on = True
    dead = False

    while game_on:
            if not dead:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change = -5
                        key_down = True
                    elif event.key == pygame.K_RIGHT:
                        x_change = 5
                        key_down = True
                elif event.type == pygame.KEYUP:
                    x_change = 0
                    key_down = False

        gameDisplay.fill(white)
        if key_down:
            x += x_change
        move_image(hero, x, y)

        if not dead:
            if x > display_width or x < 0:
                dead = True
                current_time = pygame.time.get_ticks()

        if dead:
            if pygame.time.get_ticks() > current_time + 2000:
                dead = False
                game_loop()
            else:
                game_over()

        pygame.display.update()
        clock.tick(60)
    """

game_loop()
pygame.quit()
quit()
