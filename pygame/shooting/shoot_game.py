import pygame
import sys
import random
from pygame.locals import QUIT, KEYDOWN,K_UP,K_DOWN,K_SPACE,K_a,Rect


pygame.init()
pygame.display.set_caption('Shoot~')
pygame.key.set_repeat(15, 15)
SURFACE = pygame.display.set_mode((1000,600))
FPSCLOCK = pygame.time.Clock()
Big_font = pygame.font.SysFont(None , 80)
Small_font = pygame.font.SysFont(None, 40)
black = (255,255,255)

class Draw:
    def __init__(self,col,rect,speed = 0):
        self.col = col
        self.rect = rect
        self.speed = speed
    def move(self):
        self.rect.centerx += self.speed
    def draw_E(self):
        pygame.draw.ellipse(SURFACE,self.col,self.rect)
    def draw_R(self):
        pygame.draw.rect(SURFACE,self.col,self.rect)


def Game_border():
    Start_Point = [(100,150),(100,150),(100,550),(900,150)]
    End_Point = [(100,550),(900,150),(900,550),(900,550)]
    for index in range(len(Start_Point)):
        pygame.draw.line(SURFACE,(255,255,255),Start_Point[index],End_Point[index])

def main():
    rock_speed = -5
    RockWIDTH = 50
    RockHEIGHT = 50
    xpos = 880
    ypos = random.randint(0,8)
    Rock = []
    game_start = False
    Miss = 0
    Score = 0
    Beam_Count = 0
    Cir = Draw(black,Rect(50,300,30,30))
    Beam = Draw((255,255,0),Rect(Cir.rect.centerx, Cir.rect.centery,5,5),10)

    Score = 0
    Miss = 0

    while True:
        message_Title = Big_font.render("SHoot Game" , True , black)
        message_Score = Small_font.render("Score : {}".format(Score), True, black)
        message_Miss = Small_font.render("Miss_Point: {}".format(Miss),True,black)
        message_game_start = Small_font.render('Game Start : press the space bar',True,black)
        message_game_over = Small_font.render("Game Over : {}".format(Score),True,black)
        message_caution = Small_font.render("Missile : A", True, black)
        SURFACE.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    rock_speed = -5
                    Miss = 0
                    Score = 0
                    game_start = True
                elif event.key == K_UP:
                    Cir.rect.centery -= 10
                elif event.key == K_DOWN:
                    Cir.rect.centery += 10
                elif event.key == K_a:
                    if Beam_Count == 0 :
                        Beam_Count = 1
                        Beam.rect.center = Cir.rect.center
                    else:
                        Beam.draw_E()
        if game_start:
            SURFACE.blit(message_Title,(350,20))
            SURFACE.blit(message_Score,(770,160))
            SURFACE.blit(message_caution,(280,100))
            SURFACE.blit(message_Miss,(700,200))
            Game_border()
            Cir.draw_E()
            if Cir.rect.centery <= 170:
                Cir.rect.centery = 170
            elif Cir.rect.centery >= 530:
                Cir.rect.centery = 530
            if Beam_Count ==1:
                Beam.draw_E()
                Beam.move()
                if Beam.rect.centerx >=900:
                    Beam.rect.center = Cir.rect.center
                    Beam_Count = 0
            if len(Rock) == 0:
                Rock.append(Draw((0, 255,0), Rect(xpos,ypos * 40 + 170, RockWIDTH - ypos*3 , RockHEIGHT - ypos*3), rock_speed))
            elif len(Rock) == 1:
                Rock[0].draw_R()
                Rock[0].move()
                if Rock[0].rect.colliderect(Beam.rect):
                    Beam.rect.center = Cir.rect.center
                    Beam_Count = 0
                    Score += 100
                    rock_speed -= 0.25
                    del Rock[0]
                    ypos = random.randint(0,8)
                elif Rock[0].rect.centerx <= 100:
                    Beam.rect.center = Cir.rect.center
                    Beam_Count = 0
                    Miss += 1
                    del Rock[0]
                    ypos = random.randint(0,8)
            if Miss == 3:
                game_start = False
        elif not game_start and Miss == 3:
            SURFACE.blit(message_game_over, (250,200))
            SURFACE.blit(message_game_start, (300,300))
        else:
            SURFACE.blit(message_Title, (320,200))
            SURFACE.blit(message_game_start, (300,300))
        pygame.display.update()
        FPSCLOCK.tick(30)
    
if __name__ == '__main__':
    main()