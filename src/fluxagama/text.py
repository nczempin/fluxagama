import pygame
from constants import *
COLOUR_TEXT = (255, 255, 255) # white
def draw_text(surface, score):
    global BORDER_LOWER
    global SCREEN_SIZE
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
