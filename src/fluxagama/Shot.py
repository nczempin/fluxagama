import pygame, graphics,FluxaSprite
class Shot(FluxaSprite.FluxaSprite):
    def __init__(self, position):
        FluxaSprite.FluxaSprite.__init__(self,position,'shot.png')