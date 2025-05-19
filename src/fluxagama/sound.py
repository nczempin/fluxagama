from __future__ import print_function
import pygame
import os

class dummysound:
    def play(self): pass
    
def load_sound(filename):
    if not pygame.mixer: return dummysound()
    print("Loading sound " + filename)
    filename = os.path.join("../../data", filename)
    try:
        sound = pygame.mixer.Sound(filename)
        return sound
    except pygame.error:
        print('Warning, unable to load,', filename)
    return dummysound()
