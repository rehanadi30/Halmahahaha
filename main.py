#Dependency
import pygame
from konstanta import *
from board import Board

FPS = 60 #FPS game

pygame.display.set_caption('Halmahaha')
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
def main():
    #size = int(input("Masukkan ukuran papan: "))
    run = True
    clock = pygame.time.Clock()
    papan = Board()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        papan.render(WIN)
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()