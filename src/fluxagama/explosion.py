import pygame
import graphics
explosion_image = graphics.load_image("explosion00.png")
e = None
def create(position):
    global e
    e = Explosion(position)
    #explosions.append(e)
def draw(surface):
    global e, explosion_image
    if e != None:
        if e.ttl >0:
            surface.blit(explosion_image,e.position)
            e.ttl -= 1
        else:
            e = None
class Explosion(pygame.sprite.Sprite):
    def __init__(self,position):
        self.position = position
        self.ttl = 60 #number of ticks that this will "live"