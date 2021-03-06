import pygame
from constants import *

score1titletext=None
score1titletextpos=None
def draw_text(surface, score):
    global COLOUR_TEXT
    global BORDER_LOWER
    global SCREEN_SIZE
    global score1titletext
    global score1titletextpos
    global font
    # prepare text rendering
    surface.blit(score1titletext, score1titletextpos)
    scoretext = "%04d" % score
    score1surface = font.render(scoretext, 1, COLOUR_TEXT)
    score1textpos = score1surface.get_rect()
    score1textpos.x = 72
    score1textpos.centery = 90
    surface.blit(score1surface, score1textpos)
    pygame.draw.rect(surface, (0,200,0), (0,BORDER_LOWER+35,SCREEN_SIZE[0],3))
def init_text():
    global score1titletext
    global score1titletextpos
    global font
    font = pygame.font.SysFont("Courier", 36)
    score1titletext = font.render("SCORE<1>", 1, COLOUR_TEXT)
    score1titletextpos = score1titletext.get_rect()
    score1titletextpos.x = 18
    score1titletextpos.centery = 36
