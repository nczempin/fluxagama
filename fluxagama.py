import pygame, os
from pygame.locals import *

def load_image(filename):
    "loads an image, prepares it for play"
    filename = os.path.join("data", filename)
    try:
        surface = pygame.image.load(filename)
    except pygame.error:
        raise SystemExit, 'Could not load image "%s" %s' % (filename, pygame.get_error())
    return surface
class dummysound:
    def play(self): pass
    
def load_sound(filename):
    if not pygame.mixer: return dummysound()
    print "Lade Sound"
    filename = os.path.join("data", filename)
    try:
        sound = pygame.mixer.Sound(filename)
        return sound
    except pygame.error:
        print 'Warning, unable to load,', filename
    return dummysound()

 

def handle_input(events):
    global ship_coorX
    global ship_coorY  
    global shot_exists
    global shot_coorX
    global shot_coorY
    keystate = pygame.key.get_pressed()
    
    if keystate[K_w] == 1:
        print "W"
        ship_coorY -= 1
    if keystate[K_a] == 1:
        print "A"
        ship_coorX -= 1
    if keystate[K_s] == 1:
        print "S"
        ship_coorY += 1
    if keystate[K_d] == 1:
        print "D"
        ship_coorX += 1
    if keystate[K_SPACE] == 1:
        if not shot_exists:
            shoot_sound.play()
            shot_exists = True
            shot_coorX, shot_coorY = ship_coorX + (shipX - shotX) / 2, ship_coorY - shotY

    for event in events: 
        if event.type == QUIT:# or
        #if event.key == K_ESCAPE: 
            return True
#        elif event.type == KEYDOWN:
#            print event.scancode
#            if event.scancode == 57 and not shot_exists:
                 
# Main program starts here
pygame.mixer.pre_init(frequency=22050, size=-16, channels=2, buffer=512)
pygame.init()
if pygame.mixer and not pygame.mixer.get_init():
    print 'Warning, no sound'
    pygame.mixer = None
screenX = 672
screenY = 768
window = pygame.display.set_mode((screenX, screenY)) 
pygame.display.set_caption('LOLOLOL') 
screen = pygame.display.get_surface()


shoot_sound = load_sound('psh.ogg')

ship_surface = load_image("Flieger.png")
shot_surface = load_image("Schuss.png")
enemy0_surface = load_image("UFO.png")

shipX, shipY = ship_surface.get_size()
shotX, shotY = shot_surface.get_size()
enemy0X, enemy0Y = enemy0_surface.get_size()

ship_coorX = (screenX - shipX) / 2
ship_coorY = screenY - shipY

shot_coorX = 0
shot_coorY = 0

enemy0_coorX = 300
enemy0_coorY = 20

shot_exists = False
enemy0_exists = True
done = False
#clock = pygame.time.Clock()
# Main game loop
try:
    while not done:
        # clip to 60 fps
        #clock.tick(60)
        # draw black background
        screen.fill((0, 0, 0))
        
        if enemy0_exists:
            # collision detection shot <-> enemy
            if enemy0_coorY + enemy0Y < shot_coorY:
                None
            elif enemy0_coorY > shot_coorY + shotY:
                None
            elif enemy0_coorX > shot_coorX + shotX:
                None
            elif enemy0_coorX + enemy0X < shot_coorX:
                None
            else:
                # Collision!
                enemy0_exists = False
                shot_exists = False
                # TODO: enemy explosion
        if shot_exists:
            # draw and move shot
            screen.blit (shot_surface, (shot_coorX, shot_coorY))
            shot_coorY -= 1
            if shot_coorY <= 0:
                shot_exists = False

        if enemy0_exists:
            # draw enemy TODO move enemy
            screen.blit (enemy0_surface, (enemy0_coorX, enemy0_coorY))
      
        # draw player ship
        screen.blit (ship_surface, (ship_coorX, ship_coorY))

        # swap baCK AND FRONT BUFFERS
        pygame.display.flip()
        # read keyboard and move player ship
        done = handle_input(pygame.event.get())
except:
    print 'Warning, Error,', file
pygame.quit()