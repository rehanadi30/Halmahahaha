import pygame
from konstanta import *

class Board():
    def __init__(self):
        self.board = []
        self.BSize = SIZE
        self.bidakTerpilih = None

    def render(self, win):
        win.fill(GREY)
        for baris in range(self.BSize):
            for kolom in range(baris%2, self.BSize, 2):
                pygame.draw.rect(win, WHITE, (baris*SQUARE_SIZE, kolom*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

        #Buat border daerah goal
        if(self.BSize==16):
            #Daerah BOT
            pygame.draw.line(win, RED, (0, 225), (90, 225), 8)
            pygame.draw.line(win, RED, (90, 225), (90, 180), 8)
            pygame.draw.line(win, RED, (90, 180), (135, 180), 8)
            pygame.draw.line(win, RED, (135, 180), (135, 135), 8)
            pygame.draw.line(win, RED, (135, 135), (180, 135), 8)
            pygame.draw.line(win, RED, (180, 135), (180, 90), 8)
            pygame.draw.line(win, RED, (180, 90), (225, 90), 8)
            pygame.draw.line(win, RED, (225, 90), (225, 0), 8)


            #Daerah User
            pygame.draw.line(win, RED, (495, 720), (495, 630), 8)
            pygame.draw.line(win, RED, (495, 630), (540, 630), 8)
            pygame.draw.line(win, RED, (540, 630), (540, 585), 8)
            pygame.draw.line(win, RED, (540, 585), (585, 585), 8)
            pygame.draw.line(win, RED, (585, 585), (585, 540), 8)
            pygame.draw.line(win, RED, (585, 540), (630, 540), 8)
            pygame.draw.line(win, RED, (630, 540), (630, 495), 8)
            pygame.draw.line(win, RED, (630, 495), (720, 495), 8)

        elif(self.BSize==10):
            # Daerah BOT
            pygame.draw.line(win, RED, (0, 360), (72, 360), 8)
            pygame.draw.line(win, RED, (72, 360), (72, 288), 8)
            pygame.draw.line(win, RED, (72, 288), (144, 288), 8)
            pygame.draw.line(win, RED, (144, 288), (144, 216), 8)
            pygame.draw.line(win, RED, (144, 216), (216, 216), 8)
            pygame.draw.line(win, RED, (216, 216), (216, 144), 8)
            pygame.draw.line(win, RED, (216, 144), (288, 144), 8)
            pygame.draw.line(win, RED, (288, 144), (288, 72), 8)
            pygame.draw.line(win, RED, (288, 72), (360, 72), 8)
            pygame.draw.line(win, RED, (360, 72), (360, 0), 8)

            # Daerah User
            pygame.draw.line(win, RED, (360, 720), (360, 648), 8)
            pygame.draw.line(win, RED, (360, 648), (432, 648), 8)
            pygame.draw.line(win, RED, (432, 648), (432, 576), 8)
            pygame.draw.line(win, RED, (432, 576), (504, 576), 8)
            pygame.draw.line(win, RED, (504, 576), (504, 504), 8)
            pygame.draw.line(win, RED, (504, 504), (576, 504), 8)
            pygame.draw.line(win, RED, (576, 504), (576, 432), 8)
            pygame.draw.line(win, RED, (576, 432), (648, 432), 8)
            pygame.draw.line(win, RED, (648, 432), (648, 360), 8)
            pygame.draw.line(win, RED, (648, 360), (720, 360), 8)

        elif(self.BSize==8):
            # Daerah BOT
            pygame.draw.line(win, RED, (0, 360), (90, 360), 8)
            pygame.draw.line(win, RED, (90, 360), (90, 270), 8)
            pygame.draw.line(win, RED, (90, 270), (180, 270), 8)
            pygame.draw.line(win, RED, (180, 270), (180, 180), 8)
            pygame.draw.line(win, RED, (180, 180), (270, 180), 8)
            pygame.draw.line(win, RED, (270, 180), (270, 90), 8)
            pygame.draw.line(win, RED, (270, 90), (360, 90), 8)
            pygame.draw.line(win, RED, (360, 90), (360, 0), 8)

            # Daerah User
            pygame.draw.line(win, RED, (360, 720), (360, 630), 8)
            pygame.draw.line(win, RED, (360, 630), (450, 630), 8)
            pygame.draw.line(win, RED, (450, 630), (450, 540), 8)
            pygame.draw.line(win, RED, (450, 540), (540, 540), 8)
            pygame.draw.line(win, RED, (540, 540), (540, 450), 8)
            pygame.draw.line(win, RED, (540, 450), (630, 450), 8)
            pygame.draw.line(win, RED, (630, 450), (630, 360), 8)
            pygame.draw.line(win, RED, (630, 360), (720, 360), 8)
