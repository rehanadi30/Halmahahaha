import pygame
from konstanta import *

class Pion:
    PADDING = 15
    OUTLINE = 2
    def __init__(self, baris, kolom, warna, status):
        self.baris = baris
        self.kolom = kolom
        self.warna = warna
        self.status = status #1 or 2. Default: 1 for BOT 2 for player. Tapi karena ada algo vs algo bisa jaadi bot vs bot
        self.x = 0
        self.y = 0
        self.posisi()
        self.isGoal()

    def isJump(self):
        pass
    def isMove(self):
        pass
    def isGoal(self):
        if (self.status == 1):
            return (self.x)
    def posisi(self):
        self.x = SQUARE_SIZE * self.kolom + SQUARE_SIZE//2
        self.y = SQUARE_SIZE * self.baris + SQUARE_SIZE // 2

    def render(self, win):
        rad = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, self.WHITE, (self.x, self.y), rad + self.OUTLINE)
        pygame.draw.circle(win, self.warna, (self.x, self.y), rad)

    def __repr__(self): #mengatasi mengembalikan jenis objek
        return str(self.warna)