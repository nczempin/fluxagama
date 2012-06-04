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
                
# Main program starts here
pygame.mixer.pre_init(frequency=22050, size=-16, channels=2, buffer=512)
pygame.init()
if pygame.mixer and not pygame.mixer.get_init():
    print 'Warning, no sound'
    pygame.mixer = None
screenX = 672
screenY = 768
window = pygame.display.set_mode((screenX, screenY)) 
pygame.display.set_caption('Fluxagama') 
screen = pygame.display.get_surface()


BORDER_LEFT = 0
BORDER_RIGHT = screenX
BORDER_LOWER = screenY-100
BORDER_UPPER = 100


shoot_sound = load_sound('psh.ogg')
enemy_explosion_sound = load_sound('uddh.ogg')

ship_surface = load_image("gun.png")
shot_surface = load_image("shot.png")
enemy0_surface = load_image("UFO.png")

shipX, shipY = ship_surface.get_size()
shotX, shotY = shot_surface.get_size()
enemy0X, enemy0Y = enemy0_surface.get_size()

ship_coorX = (screenX - shipX) / 2
ship_coorY = BORDER_LOWER - shipY

shot_coorX = 0
shot_coorY = 0

#converted enemy x and y to first and second item in enemies[0]
#enemy0_coorX = 300
#enemy0_coorY = BORDER_UPPER
enemies = [[300,BORDER_UPPER],[400,BORDER_UPPER]]

shot_exists = False
enemy0_exists = True
done = False

clock = pygame.time.Clock()
ticks = 0

font = pygame.font.Font(None, 36)
score1titletext = font.render("SCORE<1>", 1, (200, 200, 200))
score1titletextpos = score1titletext.get_rect()
score1text = font.render("00000", 1, (200, 200, 200))
score1textpos = score1text.get_rect()
score1textpos.centery = 36


# Main game loop
try:
    while not done:
        clock.tick()
        ticks += 1
        if (ticks % 1000)==0:
            fps = clock.get_fps()
            print fps
        # draw black background
        screen.fill((0, 0, 0))
        #draw text
        screen.blit(score1titletext, score1titletextpos)
        screen.blit(score1text, score1textpos)
       
        for i in range(len(enemies)):
            screen.blit (enemy0_surface, (enemies[i][0], enemies[i][1]))
            # collision detection shot <-> enemy
            if enemies[i][1] + enemy0Y < shot_coorY:
                pass
            elif enemies[i][1] > shot_coorY + shotY:
                pass
            elif enemies[i][0] > shot_coorX + shotX:
                pass
            elif enemies[i][0] + enemy0X < shot_coorX:
                pass
            else:
                # Collision!
                enemy0_exists = False
                shot_exists = False
                enemy_explosion_sound.play()
                # TODO: enemy explosion
        if shot_exists:
            # draw and move shot
            screen.blit (shot_surface, (shot_coorX, shot_coorY))
            shot_coorY -= 1
            if shot_coorY <= BORDER_UPPER:
                shot_exists = False

        if enemy0_exists:
            # draw enemy TODO move enemy
            pass#screen.blit (enemy0_surface, (enemies[0][0], enemies[0][1]))
      
        # draw player ship
        screen.blit (ship_surface, (ship_coorX, ship_coorY))

        # swap baCK AND FRONT BUFFERS
        pygame.display.flip()
        # read keyboard and move player ship
        events = pygame.event.get()
        keystate = pygame.key.get_pressed()
    
        if keystate[K_a] == 1:
            if ship_coorX > BORDER_LEFT:
                ship_coorX -= 1
        if keystate[K_d] == 1:
            if ship_coorX + shipX < BORDER_RIGHT:
                ship_coorX += 1
        if keystate[K_SPACE] == 1:
            if not shot_exists:
                shoot_sound.play()
                shot_exists = True
                shot_coorX, shot_coorY = ship_coorX + (shipX - shotX) / 2, ship_coorY - shotY
    
        for event in events: 
            if event.type == QUIT:# or
            #if event.key == K_ESCAPE: 
                done= True
    #        elif event.type == KEYDOWN:
    #            print event.scancode
    #            if event.scancode == 57 and not shot_exists:

except:
    print 'Warning, Error'
pygame.quit()