import pygame, random
from pygame.locals import *
from constants import *
import graphics,sound,text
import Enemy,PlayerShip,Shot, explosion

def collidesWith(sprite1, sprite2):
    x1 = sprite1.position[0]
    y1 = sprite1.position[1]
    x2 = sprite2.position[0]
    y2 = sprite2.position[1]
    x1size = sprite1.size[0]
    y1size = sprite1.size[1]
    x2size = sprite2.size[0]
    y2size = sprite2.size[1]
    if y1 + y1size < y2:
        pass
    elif y1 > y2 + y2size:
        pass
    elif x1 + x1size < x2:
        pass
    elif x1 > x2 + x2size:
        pass
    else:
        return True
def generate_enemy_wave(enemies):
    global BORDER_UPPER
    ENEMY_ROWS = 5
    ENEMY_COLUMNS = 11
    
    for i in range(ENEMY_ROWS):
        for j in range(ENEMY_COLUMNS):
            position = [60 + j * 50, BORDER_UPPER + 110 + i * 50]
            enemyType = 2-(i+1)/2
            enemy_sprite = Enemy.Enemy(enemyType, position)
            enemies.append(enemy_sprite)
 
def init():
    global SCREEN_SIZE
    pygame.mixer.pre_init(frequency=22050, size=-16, channels=2, buffer=512)
    pygame.init()
    if pygame.mixer and not pygame.mixer.get_init():
        print 'Warning, no sound'
        pygame.mixer = None
    pygame.display.set_caption('Fluxagama')
    window = pygame.display.set_mode((SCREEN_SIZE[0], SCREEN_SIZE[1]))
    text.init_text()
    
def game_loop():
    global BORDER_LOWER, BORDER_LEFT, BORDER_RIGHT
    global TICKS_PER_SECOND
    global SHOT_SPEED,SHIP_SPEED
    enemies = []
    generate_enemy_wave(enemies)
    screen = pygame.display.get_surface()
    
    shoot_sound = sound.load_sound('psh.ogg')
    enemy_explosion_sound = sound.load_sound('uddh.ogg')
    
    position = [(SCREEN_SIZE[0]) / 2, BORDER_LOWER-10]
    
    ship_sprite = PlayerShip.PlayerShip(position)
    shot_sprite = Shot.Shot([0,0])
    enemy_shot_sprite = Shot.Shot([0,0])
    ship_sprite.size = ship_sprite.image.get_size()
    shotX, shotY = shot_sprite.image.get_size()
    enemy_shotX, enemy_shotY = shotX, shotY
    
    ship_sprite.coorX = ship_sprite.position[0]
    ship_sprite.coorY = ship_sprite.position[1]
    
    shot_coorX = 0.0
    shot_coorY = 0.0
    enemy_shot_coorX = 25.0
    enemy_shot_coorY = 10.0
    ship_sprite.coorX = (SCREEN_SIZE[0] - ship_sprite.size[0]) / 2
    ship_sprite.coorY = BORDER_LOWER - ship_sprite.size[1]
    shot_exists = False
    enemy_shot_exists = False
    score = 0
    clock = pygame.time.Clock()
    ticks = 0
    done = False
    # Main game loop
    while not done:
        clock.tick(TICKS_PER_SECOND)
        ticks += 1
        if (ticks % TICKS_PER_SECOND) == 0:
            fps = clock.get_fps()
            print fps
        #####################################################################################
        # read keyboard and move player ship
        events = pygame.event.get()
        keystate = pygame.key.get_pressed()
        if keystate[K_ESCAPE] == 1:
            done = True
            break
        if keystate[K_a] == 1:
            ship_sprite.move_left()
        if keystate[K_d] == 1:
            ship_sprite.move_right()
        if keystate[K_SPACE] == 1:
            if not shot_exists:
                shoot_sound.play()
                shot_exists = True
                shot_sprite.position[0], shot_sprite.position[1] = ship_sprite.position[0] + (ship_sprite.size[0] - shot_sprite.size[0]) / 2, ship_sprite.position[1] - shot_sprite.size[1] #generate shot near top middle of gun
        if keystate[K_e] == 1:
            if not enemy_shot_exists:
                #shoot_sound.play()
                enemy_shot_exists = True
                enemy_shot_coorX = 400.0 #random.randint(BORDER_LEFT, BORDER_RIGHT)
                enemy_shot_coorY = 400.0
                #shot_coorX, shot_coorY = ship_sprite.coorX + (ship_sprite.size[0] - shotX) / 2, ship_sprite.coorY - shotY #generate shot near top middle of gun
        for event in events: 
            if event.type == QUIT: 
                done = True
                break

        #######################################################################################
        # collision detection shot <-> enemies
        dying_enemies = [] # empty list that gets filled as enemies get shot
        for i in range(len(enemies)):
            if shot_exists:
                if collidesWith(shot_sprite,enemies[i]):
                    # Collision!
                    score += enemies[i].get_score()
                    dying_enemies.append(i)
                    shot_exists = False
                    enemy_explosion_sound.play()
                    # TODO: enemy explosion graphics
                    explosion.create(enemies[i].position)
                    print "zerstort"
        # remove all enemies that were hit.
        delta = 0
        for i in range(len(dying_enemies)):
            del enemies[dying_enemies[i + delta]]
            delta += 1 # each time we remove one, the index of all the others must be reduced. This assumes that the list of dying enemies is sorted
            
        # collision detection enemy_shot <-> PlayerShip
        #dying_enemies = [] # empty list that gets filled as enemies get shot
        
        if enemy_shot_exists:
            if collidesWith(enemy_shot_sprite,ship_sprite):
                # Collision!
                #score += enemies[i].get_score()
                #dying_enemies.append(i)
                enemy_shot_exists = False
                enemy_explosion_sound.play()
                # TODO: enemy explosion graphics
                #explosion.create(enemies[i].position)
        # remove all enemies that were hit.
        # detect end of wave
        if len(enemies) == 0:
            generate_enemy_wave(enemies)
        ############################################################################################
        if shot_exists:
            #move shot
            shot_sprite.position[1] -= SHOT_SPEED
            if shot_sprite.position[1] <= BORDER_UPPER:
                shot_exists = False
        if enemy_shot_exists:
            #move shot
            enemy_shot_coorY += SHOT_SPEED
            if enemy_shot_coorY >= BORDER_LOWER:
                enemy_shot_exists = False
        ############################################################################################
        graphics.draw_background(screen)
        text.draw_text(screen, score)
        if shot_exists:
            # draw shot
            screen.blit (shot_sprite.image, (shot_sprite.position[0], shot_sprite.position[1]))
        if enemy_shot_exists:
            # draw shot
            screen.blit (shot_sprite.image, (enemy_shot_coorX, enemy_shot_coorY))

        for i in range(len(enemies)):
            enemies[i].draw(screen)
        explosion.draw(screen)
        # draw player ship
        ship_sprite.draw(screen)
        # swap back and front buffers
        pygame.display.flip()
        ###############################################################################################

def main():
    init() 
    game_loop()
    pygame.quit()    
main()

