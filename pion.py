import pygame
from konstanta import *

class Pion:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, baris, kolom, warna, status):
        self.baris = baris
        self.kolom = kolom
        self.warna = warna
        self.status = status #1 or 2. Default: 1 for BOT 2 for player. Tapi karena ada algo vs algo bisa jadi bot vs bot
        self.goal = False
        self.masukGoal()

    # Getter
    def getBaris(self):
        return self.baris

    def getKolom(self):
        return self.kolom

    def getWarna(self):
        return self.warna

    def getStatus(self):
        return self.status

    # Setter
    def setBaris(self, newBaris):
        self.baris = newBaris

    def setKolom(self, newKolom):
        self.kolom = newKolom

    def isJump(self):
        # mengembalikan true jika bergerak melompati satu bidak
        # else false
        pass

    def isMove(self):
        # mengembalikan true jika bergerak/berpindah satu kotak
        # else false
        pass

    def isGoal(self, size):
    #Boolean, ngereturn kondisi ketika masuk kondisi goal
        if(self.status == 1):
            if (size == 16):
                if(self.getBaris() != 0 or self.getKolom() != 0):
                    return (self.getBaris()+self.getKolom() <= 5)
                else:
                    return (self.getBaris()+self.getKolom < 5)
            elif(size == 10):
                return (self.getBaris()+self.getKolom() <= 4)
            elif(size == 8):
                return (self.getBaris() + self.getKolom() <= 3)
        elif(self.status == 2):
            if (self.status == 1):
                if (size == 16):
                    if (self.getBaris() != 15 or self.getKolom() != 15):
                        return (self.getBaris() + self.getKolom() >= 25)
                    else:
                        return (self.getBaris() + self.getKolom > 25)
                elif (size == 10):
                    return (self.getBaris() + self.getKolom() >= 14)
                elif (size == 8):
                    return (self.getBaris() + self.getKolom() > 11)

    def masukGoal(self):
    #Buat ngubah state goal. Setiap isGoal berubah status, fungsi ini dipanggil
        if(self.isGoal()):
            self.goal = True
        else:
            self.goal = False

    def render(self, win):
         rad = SQUARE_SIZE//2 - self.PADDING
         pygame.draw.circle(win, self.WHITE, (self.getBaris(), self.getKolom()), rad + self.OUTLINE)
         pygame.draw.circle(win, self.warna, (self.getBaris(), self.getBaris()), rad)

    """
    Mengatasi mengembalikan jenis objek
    Contoh sebelum dihandle: print(pion) -> 0xBAjsabdasjbdjab
    Contoh sesudah dihandle: print(pion) -> Hijau
    """
    def __repr__(self):
        return str(self.warna)
