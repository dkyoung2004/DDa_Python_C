import sys
import pygame
import math
import random
from pygame.locals import QUIT,KEYDOWN,K_LEFT,K_RIGHT,K_SPACE,K_w,K_a,K_s,K_d,Rect

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
    PADDLE_1 = Block((0,255,0),Rect(0,))