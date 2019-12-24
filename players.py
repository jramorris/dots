class GameObject(object):
    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(0, height)

    def move(self, direction):
        if event.key == 273:
            hero_rect = hero_rect.move(0, -speed[1])
        elif event.key == 274:
            hero_rect = hero_rect.move(0, speed[1])
        elif event.key == 275:
            hero_rect = hero_rect.move(speed[0], 0)
        elif event.key == 276:
            hero_rect = hero_rect.move(-speed[0], 0)
