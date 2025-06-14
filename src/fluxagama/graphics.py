from __future__ import print_function
import os
import pygame
from .constants import *
def load_image(filename):
    "loads an image, prepares it for play"
    print("Loading image " + filename)
    # Get the directory where this module is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Go up two levels to get to the project root, then into data
    data_dir = os.path.join(current_dir, "..", "..", "data")
    filename = os.path.join(data_dir, filename)
    try:
        surface = pygame.image.load(filename)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s' % (filename, pygame.get_error()))
    return surface
def draw_background(surface):
    surface.fill(COLOUR_BACKGROUND)
 