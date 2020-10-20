#Dependency
import pygame
from konstanta import *
from board import Board
from inputPage import *
from state import *

FPS = 60 #FPS game

pygame.display.set_caption('Halmahahaha')
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def main():
    size = int(input("Masukkan ukuran papan: "))
    time = int(input("Masukkan timer: "))
    print("")
    print("Tipe Player:")
    print("0. Minimax")
    print("1. Minimax + Local Search")
    print("2. Manusia")
    player1 = int(input("Masukkan player 1: "))
    player2 = int(input("Masukkan player 2: "))
    clock = pygame.time.Clock()
    playerRed = Player(size, 'R', player1) #pembuatan player merah
    playerGreen = Player(size, 'G', player2) #pembuatan player hijau
    state = State(playerRed, playerGreen,size) #pembuatan state
    papan = Board(size,state,time)
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