import pygame, graphics, FluxaSprite
from constants import *
class PlayerShip(FluxaSprite.FluxaSprite):
    def __init__(self,position):
        FluxaSprite.FluxaSprite.__init__(self,position,'gun.png')