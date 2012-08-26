import pygame, Sprite
import graphics
enemy_filenames = ("enemy00.png","enemy01.png", "enemy02.png")
class Enemy(Sprite.Sprite):
    '''
    classdocs
    '''
    def __init__(self, enemyType, position):
        '''
        Constructor
        '''
        global enemy_surface
       # enemy_surface = (graphics.load_image("enemy00.png"),graphics.load_image("enemy01.png"), graphics.load_image("enemy02.png"))
        self.type = enemyType
        Sprite.Sprite.__init__(self,position,enemy_filenames[self.type])
        #self.position = position
        #self.enemy0X, self.enemy0Y = enemy_surface[0].get_size() #TODO we assume for now that all enemies have the same size
        #self.size = enemy_surface[0].get_size()
   
#    def draw(self,surface):
#        surface.blit (enemy_surface[self.type], self.position)

    def get_score(self):
        return 10 * (self.type+1)
    def __repr__(self):
        return str(self.type)+str(self.position)        