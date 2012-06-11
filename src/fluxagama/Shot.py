import pygame, graphics
class Shot(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = graphics.load_image('shot.png')
