from scenes.scene import Menu

class GameEngine(object):
    def __init__(self):
        self.go_to(Menu())
        self.score = 0
        self.white = (255, 255, 255)
        self.underwater = (135, 206, 250)
        self.theme = self.white

    def go_to(self, scene, update=False):
        if update:
            self.update_theme()
        self.scene = scene
        self.scene.manager = self

    def update_theme(self):
        if self.theme == self.white:
            self.theme = self.underwater
        else:
            self.theme = self.white
