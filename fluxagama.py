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
def generate_enemy_wave(enemies):
    global BORDER_UPPER
    for i in range(5):
        for j in range(11):
            position = [60 + j * 50, BORDER_UPPER + 80 + i * 40]
            enemies.append(position)
# Main program starts here
pygame.mixer.pre_init(frequency=22050, size= -16, channels=2, buffer=512)
pygame.init()
if pygame.mixer and not pygame.mixer.get_init():
    print 'Warning, no sound'
    pygame.mixer = None
    
SCREEN_SIZE = (672, 768)
BORDER_LEFT = 0
BORDER_RIGHT = SCREEN_SIZE[0]
BORDER_LOWER = SCREEN_SIZE[1] - 100
BORDER_UPPER = 100
COLOUR_TEXT = (200, 200, 200) #light grey
COLOUR_BACKGROUND = (0, 0, 0) #black

window = pygame.display.set_mode((SCREEN_SIZE[0], SCREEN_SIZE[1])) 
pygame.display.set_caption('Fluxagama') 
screen = pygame.display.get_surface()

shoot_sound = load_sound('psh.ogg')
enemy_explosion_sound = load_sound('uddh.ogg')

ship_surface = load_image("gun.png")
shot_surface = load_image("shot.png")
enemy0_surface = load_image("UFO.png")

shipX, shipY = ship_surface.get_size()
shotX, shotY = shot_surface.get_size()
enemy0X, enemy0Y = enemy0_surface.get_size()

ship_coorX = (SCREEN_SIZE[0] - shipX) / 2
ship_coorY = BORDER_LOWER - shipY

shot_coorX = 0
shot_coorY = 0

enemies = []
generate_enemy_wave(enemies)

shot_exists = False
done = False

clock = pygame.time.Clock()
ticks = 0
# prepare text rendering
font = pygame.font.Font(None, 36)
score1titletext = font.render("SCORE<1>", 1, COLOUR_TEXT)
score1titletextpos = score1titletext.get_rect()
score = 0
# Main game loop
while not done:
    clock.tick()
    ticks += 1
    if (ticks % 1000) == 0:
        fps = clock.get_fps()
        print fps
    # draw black background
    screen.fill(COLOUR_BACKGROUND)
    #draw text
    screen.blit(score1titletext, score1titletextpos)
    scoretext = "%06d" % score
    score1surface = font.render(scoretext, 1, COLOUR_TEXT)
    score1textpos = score1surface.get_rect()
    score1textpos.centery = 36
    screen.blit(score1surface, score1textpos)
    dying_enemies = [] # empty list that gets filled when enemies get shot
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
            score += 10
            dying_enemies.append(i)
            shot_exists = False
            enemy_explosion_sound.play()
            # TODO: enemy explosion
    delta = 0
    for i in range(len(dying_enemies)):
        del enemies[dying_enemies[i + delta]]
        delta += 1 # each time we remove one, the index of all the others must be reduced. This assumes that the list of dying enemies is sorted
    if len(enemies) == 0:
        generate_enemy_wave(enemies)
    if shot_exists:
        # draw and move shot
        screen.blit (shot_surface, (shot_coorX, shot_coorY))
        shot_coorY -= 1
        if shot_coorY <= BORDER_UPPER:
            shot_exists = False
    # draw player ship
    screen.blit (ship_surface, (ship_coorX, ship_coorY))
    # swap back and front buffers
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
            shot_coorX, shot_coorY = ship_coorX + (shipX - shotX) / 2, ship_coorY - shotY #generate shot near top middle of gun
    for event in events: 
        if event.type == QUIT or event.key == K_ESCAPE: 
            done = True
pygame.quit()
