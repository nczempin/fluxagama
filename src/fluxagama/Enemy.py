import pygame
import graphics
import FluxaSprite
enemy_filenames = ("enemy00.png","enemy01.png", "enemy02.png")
class Enemy(FluxaSprite.FluxaSprite):
    '''
    classdocs
    '''
    def __init__(self, enemyType, position):
        '''
        Constructor
        '''
        global enemy_surface
        self.type = enemyType
        FluxaSprite.FluxaSprite.__init__(self,position,enemy_filenames[self.type])
    def get_score(self):
        return 10 * (self.type+1)
    def __repr__(self):
        return str(self.type)+str(self.position)        