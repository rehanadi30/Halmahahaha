#Dependency
import pygame
from konstanta import *
from board import Board
from inputPage import *

FPS = 60 #FPS game

pygame.display.set_caption('Halmahaha')
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def getKoordinat(pos, size):
    x, y = pos
    bar = y//(WIDTH//size)
    kol = x//(WIDTH//size)
    return bar, kol

def main():
    size = int(input("Masukkan ukuran papan: "))
    clock = pygame.time.Clock()
    papan = Board(size)
    inputUser = inputPage()
    click = False
    runHome =True
    while runHome:
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                runHome=False
                pygame.quit()
              
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click=True
                    runHome=False
                    
                    
        inputUser.render(WIN,papan,click,FPS)
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()