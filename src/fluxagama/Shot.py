import pygame, graphics
class Shot(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.position = position
        self.image = graphics.load_image('shot.png')
        self.size = self.image.get_size()

