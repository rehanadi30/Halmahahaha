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

    def isJump(self, newBaris, newKolom, papan):
        # I.S. blok pasti valid atau ada dalam board
        # mengembalikan true jika bergerak melompati satu bidak
        # else false

        # jika posisi baru yang ingin ditempati kosong
        if(papan[newBaris][newKolom]=='N'):
            # melakukan lompatan vertikal
            if(newBaris==self.getBaris()-2)and(newKolom==self.getKolom()):
                # lompatan ke atas
                # True jika satu kotak di depannya terdapat bidak
                pass
                # if papan[self.getBaris()-1][self.getKolom()] != Kosong
                # return true
            elif(newBaris==self.getBaris()+2)and(newKolom==self.getKolom()):
                # lompatan ke bawah
                # True jika satu kotak di depannya terdapat bidak
                pass
                # if papan[self.getBaris()+1][self.getKolom()] != Kosong
                # return true

            # melakukan lompatan horizontal
            elif(newBaris==self.getBaris())and(newKolom==self.getKolom()-2):
                # lompatan ke kiri
                # True jika satu kotak di depannya terdapat bidak
                pass
                # if papan[self.getBaris()][self.getKolom()-1] != Kosong
                # return true
            elif(newBaris==self.getBaris())and(newKolom==self.getKolom()+2):
                # lompatan ke kanan
                # True jika satu kotak di depannya terdapat bidak
                pass
                # if papan[self.getBaris()][self.getKolom()+1] != Kosong
                # return true

            # melakukan lompatan diagonal
            elif(newBaris==self.getBaris()-2)and(newKolom==self.getKolom()+2):
                # lompatan ke kanan atas
                # True jika satu kotak di depannya terdapat bidak
                pass
                # if papan[self.getBaris()-1][self.getKolom()+1] != Kosong
                # return true
            elif(newBaris==self.getBaris()-2)and(newKolom==self.getKolom()-2):
                # lompatan ke kiri atas
                # True jika satu kotak di depannya terdapat bidak
                pass
                # if papan[self.getBaris()-1][self.getKolom()-1] != Kosong
                # return true
            elif(newBaris==self.getBaris()+2)and(newKolom==self.getKolom()+2):
                # lompatan ke kanan bawah
                # True jika satu kotak di depannya terdapat bidak
                pass
                # if papan[self.getBaris()+1][self.getKolom()+1] != Kosong
                # return true
            elif(newBaris==self.getBaris()+2)and(newKolom==self.getKolom()-2):
                # lompatan ke kiri bawah
                # True jika satu kotak di depannya terdapat bidak
                pass
                # if papan[self.getBaris()+1][self.getKolom()-1] != Kosong
                # return true
            
            # selain itu bukan jump
            else:
                return False
        else:
            return False

    def isMove(self, newBaris, newKolom, papan):
        # I.S. blok pasti valid atau ada dalam board
        # mengembalikan true jika bergerak/berpindah satu kotak
        # else false

        # jika posisi baru yang ingin ditempati kosong
        if(papan[newBaris][newKolom]=='N'):
            # melakukan move vertikal
            if(newBaris==self.getBaris()-1)and(newKolom==self.getKolom()):
                # move ke atas
                return True
            elif(newBaris==self.getBaris()+1)and(newKolom==self.getKolom()):
                # move ke bawah
                return True

            # melakukan move horizontal
            elif(newBaris==self.getBaris())and(newKolom==self.getKolom()-1):
                # move ke kiri
                return True
            elif(newBaris==self.getBaris())and(newKolom==self.getKolom()+1):
                # move ke kanan
                return True

            # melakukan lompatan diagonal
            elif(newBaris==self.getBaris()-1)and(newKolom==self.getKolom()+1):
                # move ke kanan atas
                return True
            elif(newBaris==self.getBaris()-1)and(newKolom==self.getKolom()-1):
                # move ke kiri atas
                return True
            elif(newBaris==self.getBaris()+1)and(newKolom==self.getKolom()+1):
                # move ke kanan bawah
                return True
            elif(newBaris==self.getBaris()+1)and(newKolom==self.getKolom()-1):
                # move ke kiri bawah
                return True
            
            # selain itu bukan jump
            else:
                return False
        else:
            return False


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
