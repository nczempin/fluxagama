'''
Created on 11.06.2012

@author: nczempin
'''
import pygame
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
    def __repr__(self):
        return str(self.type)+str(self.position)        