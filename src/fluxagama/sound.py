from __future__ import print_function
import pygame
import os

class dummysound:
    def play(self): pass
    
def load_sound(filename):
    if not pygame.mixer: return dummysound()
    print("Loading sound " + filename)
    # Get the directory where this module is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Go up two levels to get to the project root, then into data
    data_dir = os.path.join(current_dir, "..", "..", "data")
    filename = os.path.join(data_dir, filename)
    try:
        sound = pygame.mixer.Sound(filename)
        return sound
    except pygame.error:
        print('Warning, unable to load,', filename)
    return dummysound()
