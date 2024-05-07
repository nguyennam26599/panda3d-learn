from direct.showbase.ShowBase import ShowBase
from panda3d.core import load_prc_file


load_prc_file('config.prc')
class Game(ShowBase):
    def __init__(self, fStartDirect=True, windowType=None):
        super().__init__(fStartDirect, windowType)
        self.sphere = self.loader.loadModel('assets/models/sphere.glb')
        self.sphere.setPos(0, 50, 0)
        self.sphere.reparentTo(self.render)


if __name__ == '__main__':
    app = Game()
    app.run()