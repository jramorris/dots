from scenes.scene import TitleScene

class GameEngine(object):
    def __init__(self):
        self.go_to(TitleScene())
        self.score = 0

    def go_to(self, scene):
        self.scene = scene
        self.scene.manager = self
