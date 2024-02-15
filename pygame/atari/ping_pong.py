import sys
import pygame
import math
import random
from pygame.locals import *

class Block:
    def __init__(self,col,rect):
        self.col = col
        self.rect = rect
    def draw_E(self):
        pygame.draw.rect(SURFACE, self.col,self.rect)
    def draw_R(self)        
        pygame.draw.rect(SURFACE , self.col, self.rect)
    
pygame.init()
FPSCLOCK = pygame.time.Clock()
SURFACE = pygame.display.set_mode((600,400))
pygame.key.set_repeat(1,1)
Bigfont = pygame.font.SysFont(None, 80)
Smallfont = pygame.font.SysFont(None, 30)

def main():
    game_over = 0
    P1_score = 0
    P2_score = 0

    BALL_Xspeed = 5
    BALL_Yspeed = 5
    PADDLE_1 = Block((0,255,0),Rect(0,180, 20, 80))
    PADDLE_2 = Block((0,255,0),Rect(580,180,20,80))

    BALL = Block((255,255,255),Rect(300,200,20,20))

    M_P1 = Bigfont.render("P1",True,(255,255,255))
    M_P2 = Bigfont.render("P2",True,(255,255,255))
    while True:
        SURFACE.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_w:
                    PADDLE_1.rect.centery -= 10
                elif event.key == K_s:
                    PADDLE_1.rect.centery += 10
                elif event.key == K_UP:
                    PADDLE_2.rect.centery -= 10
                elif event.key == K_DOWN:
                    PADDLE_2.rect.centery += 10
        if game_over == 0:
            if P1_score >= 5:
                game_over = 1
            if P2_score
