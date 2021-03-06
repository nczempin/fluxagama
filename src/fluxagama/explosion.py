import pygame
import graphics
import FluxaSprite
#explosion_image = graphics.load_image("explosion00.png")

e = None
def create(position):
    global e
    e = Explosion(position)
    #explosions.append(e)
def draw(surface):
    global e
    if e != None:
        if e.ttl > 0:
            e.draw(surface)
        else:
            e = None
class Explosion(FluxaSprite.FluxaSprite):
    def __init__(self,position):
        FluxaSprite.FluxaSprite.__init__(self,position,"explosion00.png")
        #self.position = position
        #pygame.sprite.Sprite.__init__(self)
        #self.image = graphics.load_image("explosion00.png")
        self.ttl = 10 #number of ticks that this will "live"
    def draw(self, surface):
        surface.blit(self.image,self.position)
        self.ttl -= 1