import pygame, graphics,Sprite
class Shot(Sprite.Sprite):
    def __init__(self, position):
        Sprite.Sprite.__init__(self,position,'shot.png')
        #self.position = position
        #self.image = graphics.load_image('shot.png')
        #self.size = self.image.get_size()

