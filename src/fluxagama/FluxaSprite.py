import pygame
import graphics
from constants import *
class FluxaSprite(pygame.sprite.Sprite):
    def __init__(self, position,image):
        pygame.sprite.Sprite.__init__(self)
        self.position = position
        self.image = graphics.load_image(image)
        self.size = self.image.get_size()
    def draw(self,surface):
        surface.blit (self.image, (self.position[0], self.position[1]))
        
        
        
#for ships:
    def move_left(self):
        global BORDER_LEFT, SHIP_SPEED
        if self.position[0] > BORDER_LEFT+60:
            self.position[0] -= SHIP_SPEED
    def move_right(self):
        global BORDER_RIGHT, SHIP_SPEED
        if self.position[0] + self.size[0] < BORDER_RIGHT-60:
            self.position[0] += SHIP_SPEED