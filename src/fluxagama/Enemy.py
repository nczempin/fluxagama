import pygame
import graphics
enemy_surface = (graphics.load_image("enemy00.png"),graphics.load_image("enemy01.png"), graphics.load_image("enemy02.png"))
class Enemy(pygame.sprite.Sprite):
    '''
    classdocs
    '''
    def __init__(self, enemyType, position):
        '''
        Constructor
        '''
        self.type = enemyType
        self.position = position
        self.enemy0X, self.enemy0Y = enemy_surface[0].get_size() #TODO we assume for now that all enemies have the same size
   
    def draw(self,surface):
        surface.blit (enemy_surface[self.type], self.position)
    def __repr__(self):
        return str(self.type)+str(self.position)        