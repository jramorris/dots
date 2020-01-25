class GameObject(object):
    def __init__(self, image, speed=5):
        self.speed = speed
        self.image = image
        self.x_pos = 100

    def update(self, left, right):
        x_change = 0
        if left:
            x_change += -self.speed
        if right:
            x_change += self.speed
        self.x_pos += x_change
