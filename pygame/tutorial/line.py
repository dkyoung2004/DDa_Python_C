import pygame
import sys
from pygame.locals import QUIT

pygame.init()
Surface = pygame.display.set_mode((600,600))
FPSCLOCK = pygame.time.Clock()
pygame.display.set_caption("Test Window")

def main():
    while True:
        Surface.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.draw.line(Surface, (255,0,0),(30,30),(150,30))
        pygame.draw.line(Surface, (255,0,0),(30,70),(150,70),8)
        
        pygame.display.update()
        FPSCLOCK.tick(30)
if __name__ == '__main__':
    main()
    