import pygame
from konstanta import *

class Pion:
    PADDING = 15
    OUTLINE = 2
    def __init__(self, baris, kolom, warna):
        self.baris = baris
        self.kolom = kolom
        self.warna = warna
        self.x = 0
        self.y = 0
        self.posisi()
        self.isGoal = False

    def isJump(self):
        pass
    def isMove(self):
        pass
    def posisi(self):
        self.x = SQUARE_SIZE * self.kolom + SQUARE_SIZE//2
        self.y = SQUARE_SIZE * self.baris + SQUARE_SIZE // 2
    def render(selfself, win):
        rad = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, RED, (self.x, self.y), rad)