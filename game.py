import time

import pygame

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
large_text = pygame.font.Font('freesansbold.ttf', 40)
start_time = time.time()


def game_intro(text):
    largeText = pygame.font.Font('freesansbold.ttf',24)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((width/2),(height/2))
    screen.blit(TextSurf, TextRect)

    pygame.display.update()


def text_objects(text, font):
    text_surface = font.render(text, True, BLACK)
    return text_surface, text_surface.get_rect()

def message_display(text):
    text_surface, text_rect = text_objects(text, large_text)
    text_rect.center = (width / 2, height / 2) 
    screen.blit(text_surface, text_rect)
    pygame.display.update()


def game_loop():
    game_on = True
    start = True
    hero = pygame.image.load('black-dot.jpg').convert()
    hero_rect = hero.get_rect()

    while game_on:
        if start:
            if time.time() - start_time < 3:
                game_intro('hi')
                pygame.display.update()
            else:
                print('being')
                start = False
        else:

            if hero_rect.colliderect(villain_rect):
                message_display('Lame Over')
                game_on = False
                #game_over('farts')

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

game_loop()
pygame.display.quit()
pygame.quit()
quit()
