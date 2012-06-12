import pygame, graphics
from constants import *
class PlayerShip(pygame.sprite.Sprite):
    def __init__(self):
        #TODO initialize position
        pygame.sprite.Sprite.__init__(self)
        self.image = graphics.load_image('gun.png')
    def move_left(self):
        global BORDER_LEFT, SHIP_SPEED
        if self.coorX > BORDER_LEFT+60:
            self.coorX -= SHIP_SPEED
    def move_right(self):
        global BORDER_RIGHT, SHIP_SPEED
        if self.coorX + self.size[0] < BORDER_RIGHT-60:
            self.coorX += SHIP_SPEED
    def draw(self,surface):
        surface.blit (self.image, (self.coorX, self.coorY))
