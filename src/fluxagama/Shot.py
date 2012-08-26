import pygame, graphics,Sprite
class Shot(Sprite.Sprite):
    def __init__(self, position):
        Sprite.Sprite.__init__(self,position,'shot.png')