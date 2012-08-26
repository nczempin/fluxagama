import pygame, graphics, Sprite
from constants import *
class PlayerShip(Sprite.Sprite):
    def __init__(self,position):
        Sprite.Sprite.__init__(self,position,'gun.png')
