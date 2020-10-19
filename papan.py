import pygame
from konstanta import *
from Player import *

class papan:
    def __init__(self,bsize):
        self.size = bsize
        self.color = [['n' for i in range(self.size)] for j in range(self.size)]
        self.init_board()

    def getSize(self):
        return self.size

    def changeColor(self, bar, col, warna):
        self.color[bar][col]= warna

    def getMatrixofColor(self):
        return self.color

    def getColor(self, bar, col):
        return self.color[bar][col]

    def init_board(self):
        # for i in range(self.bsize):
        #     for j in range(self.bsize):
        #         if(i<(self.bsize/2) && j<(self.bsize/2)-i){
        #             self.color[i][j]='red'
        #         }elif(i>=(self.bsize/2) && j)
        if(self.size==8):
            self.color[0][0] = 'r'
            self.color[0][1] = 'r'
            self.color[0][2] = 'r'
            self.color[0][3] = 'r'
            self.color[1][0] = 'r'
            self.color[1][1] = 'r'
            self.color[1][2] = 'r'
            self.color[2][0] = 'r'
            self.color[2][1] = 'r'
            self.color[3][0] = 'r'
            self.color[4][7] = 'g'
            self.color[5][6] = 'g'
            self.color[5][7] = 'g'
            self.color[6][5] = 'g'
            self.color[6][6] = 'g'
            self.color[6][7] = 'g'
            self.color[7][4] = 'g'
            self.color[7][5] = 'g'
            self.color[7][6] = 'g'
            self.color[7][7] = 'g'
        elif(self.size==10):
            self.color[0][0] = 'r'
            self.color[0][1] = 'r'
            self.color[0][2] = 'r'
            self.color[0][3] = 'r'
            self.color[0][4] = 'r'
            self.color[1][0] = 'r'
            self.color[1][1] = 'r'
            self.color[1][2] = 'r'
            self.color[1][3] = 'r'
            self.color[2][0] = 'r'
            self.color[2][1] = 'r'
            self.color[2][2] = 'r'
            self.color[3][0] = 'r'
            self.color[3][1] = 'r'
            self.color[4][0] = 'r'
            self.color[5][9] = 'g'
            self.color[6][8] = 'g'
            self.color[6][9] = 'g'
            self.color[7][7] = 'g'
            self.color[7][8] = 'g'
            self.color[7][9] = 'g'
            self.color[8][6] = 'g'
            self.color[8][7] = 'g'
            self.color[8][8] = 'g'
            self.color[8][9] = 'g'
            self.color[9][5] = 'g'
            self.color[9][6] = 'g'
            self.color[9][7] = 'g'
            self.color[9][8] = 'g'
            self.color[9][9] = 'g'
        elif(self.size==16):
            self.color[0][0] = 'r'
            self.color[0][1] = 'r'
            self.color[0][2] = 'r'
            self.color[0][3] = 'r'
            self.color[0][4] = 'r'
            self.color[1][0] = 'r'
            self.color[1][1] = 'r'
            self.color[1][2] = 'r'
            self.color[1][3] = 'r'
            self.color[1][4] = 'r'
            self.color[2][0] = 'r'
            self.color[2][1] = 'r'
            self.color[2][2] = 'r'
            self.color[2][3] = 'r'
            self.color[3][0] = 'r'
            self.color[3][1] = 'r'
            self.color[3][2] = 'r'
            self.color[4][0] = 'r'
            self.color[4][1] = 'r'
            self.color[11][14] = 'g'
            self.color[11][15] = 'g'
            self.color[12][13] = 'g'
            self.color[12][14] = 'g'
            self.color[12][15] = 'g'
            self.color[13][12] = 'g'
            self.color[13][13] = 'g'
            self.color[13][14] = 'g'
            self.color[13][15] = 'g'
            self.color[14][11] = 'g'
            self.color[14][12] = 'g'
            self.color[14][13] = 'g'
            self.color[14][14] = 'g'
            self.color[14][15] = 'g'
            self.color[15][11] = 'g'
            self.color[15][12] = 'g'
            self.color[15][13] = 'g'
            self.color[15][14] = 'g'
            self.color[15][15] = 'g'
        
