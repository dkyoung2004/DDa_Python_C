import pygame
import sys
import random
import math
from pygame.locals import QUIT,KEYDOWN,K_LEFT,K_RIGHT,K_SPACE,Rect
class Block:
    def __init__(self, col,rect,speed = 0):
        self.col = col
        self.rect = rect
        self.speed = speed
        self.dir = random.randint(-45,45) +270
    def move(self) : 
        self.rect.centerx += math.cos(math.radians(self.dir)) * self.speed
        self.rect.centery -= math.sin(math.radians(self.dir)) * self.speed
    def draw_E(self) : 
        pygame.draw.ellipse(SURFACE , self.col , self.rect)
    def draw_R(self) :
        pygame.draw.rect(SURFACE , self.col, self.rect)

pygame.init()
pygame.display.set_caption('Block_breaker')
pygame.key.set_repeat(10,10)
SURFACE = pygame.display.set_mode((1000,800))
FPSCLOCK = pygame.time.Clock()
Bigfont = pygame.font.SysFont(None,80)
Smallfont = pygame.font.SysFont(None, 50)
M_Game_Start1 = Bigfont.render("DO YOU WANT GAME?",True,(255,255,255))
M_Game_Start2 = Bigfont.render("CLICK THE SPACE_BAR",True,(255,255,255))
BLOCK = []
Score = 0
PADDLE = Block((200,200,0),Rect(375,700,100,30))
BALL = Block((200,200,0),Rect(375,650,20,20),10)
colors = [(255,0,0),(255,150,0),(255,228,0),(11,201,4),(0,84,255)]
M_CLEAR = Bigfont.render("CLEAR!!",True,(255,255,255))
M_FAIL = Bigfont.render("FAILED", True , (255,255,255))
M_SCORE = Smallfont.render("SCORE : {}".format(Score) , True , (255,255,255))
M_SPEED = Smallfont.render("SPEED : {}".format(BALL.speed),True,(255,255,255))


def main():
    Game_Start = False
    Score = 0
    BLOCK = []
    PADDLE = Block((200,200,0),Rect(375,700,100,30))
    BALL = Block((200,200,0),Rect(375,650,20,20),10)
    colors = [(255,0,0),(255,150,0),(255,228,0),(11,201,4),(0,84,255)]
