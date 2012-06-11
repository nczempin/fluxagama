import os, pygame
def load_image(filename):
    "loads an image, prepares it for play"
    print "Loading image "+filename
    filename = os.path.join("../../data", filename)
    try:
        surface = pygame.image.load(filename)
    except pygame.error:
        raise SystemExit, 'Could not load image "%s" %s' % (filename, pygame.get_error())
    return surface
