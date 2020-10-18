#Dependency
import pygame
from konstanta import *
from board import Board

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
    run = True
    clock = pygame.time.Clock()
    papan = Board(size)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                bar, kol = getKoordinat(pos, size)
                print(bar, kol)
        papan.render(WIN)
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()