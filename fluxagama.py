import pygame, os
from pygame.locals import *

SCREEN_SIZE = (672, 780)
BORDER_LEFT = 0
BORDER_RIGHT = SCREEN_SIZE[0]
BORDER_LOWER = SCREEN_SIZE[1] - 100
BORDER_UPPER = 100
COLOUR_TEXT = (255, 255, 255) # white
SHOT_SPEED = 10
SHIP_SPEED = 4


class Enemy:
    def __init__(self, enemyType, position):
        self.type = enemyType
        self.position = position
    def __repr__(self):
        return str(self.type)+str(self.position)
class PlayerShip(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('gun.png')
class Shot(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('shot.png')
def load_image(filename):
    "loads an image, prepares it for play"
    print "Loading image "+filename
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
    print "Loading sound "+filename
    filename = os.path.join("data", filename)
    try:
        sound = pygame.mixer.Sound(filename)
        return sound
    except pygame.error:
        print 'Warning, unable to load,', filename
    return dummysound()
def generate_enemy_wave(enemies):
    global BORDER_UPPER
    ENEMY_ROWS = 5
    ENEMY_COLUMNS = 11
    for i in range(ENEMY_ROWS):
        for j in range(ENEMY_COLUMNS):
            position = [60 + j * 50, BORDER_UPPER + 110 + i * 50]
            enemyType = 2-(i+1)/2
            enemy = Enemy(enemyType, position)
            enemies.append(enemy)
            
def draw_background(surface):
    COLOUR_BACKGROUND = (0, 0, 0) #black
    surface.fill(COLOUR_BACKGROUND)
    
def draw_text(surface, score):
    global BORDER_LOWER
    global SCREEN_SIZE
    global score1titletext
    global score1titletextpos
    font = pygame.font.SysFont("Courier", 36)
    # prepare text rendering
    score1titletext = font.render("SCORE<1>", 1, COLOUR_TEXT)
    score1titletextpos = score1titletext.get_rect()
    score1titletextpos.x = 18
    score1titletextpos.centery = 36
    surface.blit(score1titletext, score1titletextpos)
    scoretext = "%04d" % score
    score1surface = font.render(scoretext, 1, COLOUR_TEXT)
    score1textpos = score1surface.get_rect()
    score1textpos.x = 72
    score1textpos.centery = 90
    surface.blit(score1surface, score1textpos)
    pygame.draw.rect(surface, (0,200,0), (0,BORDER_LOWER+35,SCREEN_SIZE[0],3))
def main():
    # Main program starts here
    pygame.display.set_caption('Fluxagama') 
    
    
    pygame.mixer.pre_init(frequency=22050, size= -16, channels=2, buffer=512)
    pygame.init()
    if pygame.mixer and not pygame.mixer.get_init():
        print 'Warning, no sound'
        pygame.mixer = None
    window = pygame.display.set_mode((SCREEN_SIZE[0], SCREEN_SIZE[1])) 
    game_loop()
    pygame.quit()    
    
def game_loop():
    enemies = []
    generate_enemy_wave(enemies)
    screen = pygame.display.get_surface()
    
    shoot_sound = load_sound('psh.ogg')
    enemy_explosion_sound = load_sound('uddh.ogg')
    
    
    ship_sprite = PlayerShip()
    shot_sprite = Shot()
    enemy_surface = (load_image("UFO.png"),load_image("enemy01.png"), load_image("enemy02.png"))
    ship_size = ship_sprite.image.get_size()
    shotX, shotY = shot_sprite.image.get_size()
    enemy0X, enemy0Y = enemy_surface[0].get_size() #TODO we assume for now that all enemies have the same size
    
    
    shot_coorX = 0.0
    shot_coorY = 0.0
    ship_coorX = (SCREEN_SIZE[0] - ship_size[0]) / 2
    ship_coorY = BORDER_LOWER - ship_size[1]
    shot_exists = False
    score = 0
    clock = pygame.time.Clock()
    ticks = 0
    done = False
    # Main game loop
    while not done:
        clock.tick(60)
        ticks += 1
        if (ticks % 60) == 0:
            fps = clock.get_fps()
            print fps
        # draw black background
        draw_background(screen)
        #draw text
        draw_text(screen, score)
        
        dying_enemies = [] # empty list that gets filled as enemies get shot
        for i in range(len(enemies)):
            pos = enemies[i].position
            screen.blit (enemy_surface[enemies[i].type], pos)
            # collision detection shot <-> enemy
            if shot_exists:
                if pos[1] + enemy0Y < shot_coorY:
                    pass
                elif pos[1] > shot_coorY + shotY:
                    pass
                elif pos[0] > shot_coorX + shotX:
                    pass
                elif pos[0] + enemy0X < shot_coorX:
                    pass
                else:
                    # Collision!
                    score += 10 * (enemies[i].type+1)
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
            screen.blit (shot_sprite.image, (shot_coorX, shot_coorY))
            shot_coorY -= SHOT_SPEED
            if shot_coorY <= BORDER_UPPER:
                shot_exists = False
        # draw player ship
        screen.blit (ship_sprite.image, (ship_coorX, ship_coorY))
        # swap back and front buffers
        pygame.display.flip()
        # read keyboard and move player ship
        events = pygame.event.get()
        keystate = pygame.key.get_pressed()
        if keystate[K_a] == 1:
            if ship_coorX > BORDER_LEFT+60:
                ship_coorX -= SHIP_SPEED
        if keystate[K_d] == 1:
            if ship_coorX + ship_size[0] < BORDER_RIGHT-60:
                ship_coorX += SHIP_SPEED
        if keystate[K_SPACE] == 1:
            if not shot_exists:
                shoot_sound.play()
                shot_exists = True
                shot_coorX, shot_coorY = ship_coorX + (ship_size[0] - shotX) / 2, ship_coorY - shotY #generate shot near top middle of gun
        for event in events: 
            if event.type == QUIT: 
                done = True


main()

