import pygame
from konstanta import *
from board import *

class inputPage:
    def __init__(self):
        self.size=8 #inisialisasi ukuran 8
        self.red=2 #inisialisasi as a player
        self.green=2 #inisialisasi as a player
        self.background = pygame.image.load('./img/bg-2.png')

    def render(self,screen,board,click,FPS):
        screen.fill(YELLOW)
        screen.blit(self.background, (0,0))
        
        mx, my = pygame.mouse.get_pos()

        startImg= pygame.image.load("./img/startButton.png")
        buttonStart = pygame.Rect(290,550,180,80)
        pygame.draw.rect(screen, WHITE, buttonStart)
        screen.blit(startImg, [280,540])

        if buttonStart.collidepoint((mx,my)):
            if click:
                board.render(screen,FPS)
        
        

