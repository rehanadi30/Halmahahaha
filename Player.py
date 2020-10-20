from pion import *


class Player:
    def __init__(self, sizePapan, color, status):
        self.size = sizePapan  # ukuran papan
        self.color = color  # warna pemain 'R' untuk red dan 'G' untuk green
        self.status = status  # 0 for BOT Minimax, 1 for BOT Minimax LS, 2 for player

        # list of pion yang dimiliki player jika ukuran papan 8
        # pionRed8 = [
        #     Pion(0, 0, self.color, self.status), Pion(0, 1, self.color, self.status), Pion(0, 2, self.color, self.status), Pion(0, 3, self.color, self.status), Pion(1, 0, self.color, self.status),
        #     Pion(1, 1, self.color, self.status), Pion(1, 2, self.color, self.status), Pion(2, 0, self.color, self.status), Pion(2, 1, self.color, self.status), Pion(3, 0, self.color, self.status)
        # ]
        # pionGreen8 = [
        #     Pion(7, 7, self.color, self.status), Pion(7, 6, self.color, self.status), Pion(7, 5, self.color, self.status), Pion(7, 4, self.color, self.status), Pion(6, 7, self.color, self.status),
        #     Pion(6, 6, self.color, self.status), Pion(6, 5, self.color, self.status), Pion(5, 7, self.color, self.status), Pion(5, 6, self.color, self.status), Pion(4, 7, self.color, self.status)
        # ]
        pionGreen8 = [
            Pion(0, 0, self.color, self.status), Pion(0, 1, self.color, self.status), Pion(0, 2, self.color, self.status), Pion(0, 3, self.color, self.status), Pion(1, 0, self.color, self.status),
            Pion(1, 1, self.color, self.status), Pion(1, 2, self.color, self.status), Pion(2, 0, self.color, self.status), Pion(2, 1, self.color, self.status), Pion(3, 0, self.color, self.status)
        ]
        pionRed8 = [
            Pion(7, 7, self.color, self.status), Pion(7, 6, self.color, self.status), Pion(7, 5, self.color, self.status), Pion(7, 4, self.color, self.status), Pion(6, 7, self.color, self.status),
            Pion(6, 6, self.color, self.status), Pion(6, 5, self.color, self.status), Pion(5, 7, self.color, self.status), Pion(5, 6, self.color, self.status), Pion(4, 7, self.color, self.status)
        ]

        # list of pion yang dimiliki player jika ukuran papan 10
        pionRed10 = [
            Pion(0, 0, self.color, self.status), Pion(0, 1, self.color, self.status), Pion(0, 2, self.color, self.status), Pion(0, 3, self.color, self.status), Pion(0, 4, self.color, self.status), Pion(1, 0, self.color, self.status), Pion(1, 1, self.color, self.status),
            Pion(1, 2, self.color, self.status), Pion(1, 3, self.color, self.status), Pion(2, 0, self.color, self.status), Pion(2, 1, self.color, self.status), Pion(2, 2, self.color, self.status), Pion(3, 0, self.color, self.status), Pion(3, 1, self.color, self.status), Pion(4, 0, self.color, self.status)
        ]
        pionGreen10 = [
            Pion(9, 9, self.color, self.status), Pion(9, 8, self.color, self.status), Pion(9, 7, self.color, self.status), Pion(9, 6, self.color, self.status), Pion(9, 5, self.color, self.status), Pion(8, 9, self.color, self.status), Pion(8, 8, self.color, self.status),
            Pion(8, 7, self.color, self.status), Pion(8, 6, self.color, self.status), Pion(7, 9, self.color, self.status), Pion(7, 8, self.color, self.status), Pion(7, 7, self.color, self.status), Pion(6, 9, self.color, self.status), Pion(6, 8, self.color, self.status), Pion(5, 9, self.color, self.status)
        ]
        
        
        # list of pion yang dimiliki player jika ukuran papan 16
        pionRed16 = [
            Pion(0, 0, self.color, self.status), Pion(0, 1, self.color, self.status), Pion(0, 2, self.color, self.status), Pion(0, 3, self.color, self.status), Pion(0, 4, self.color, self.status), Pion(1, 0, self.color, self.status), Pion(1, 1, self.color, self.status), Pion(1, 2, self.color, self.status), Pion(1, 3, self.color, self.status), Pion(1, 4, self.color, self.status),
            Pion(2, 0, self.color, self.status), Pion(2, 1, self.color, self.status), Pion(2, 2, self.color, self.status), Pion(2, 3, self.color, self.status), Pion(3, 0, self.color, self.status), Pion(3, 1, self.color, self.status), Pion(3, 2, self.color, self.status), Pion(4, 0, self.color, self.status), Pion(4, 1, self.color, self.status)
        ]
        pionGreen16 = [
            Pion(15, 15, self.color, self.status), Pion(15, 14, self.color, self.status), Pion(15, 13, self.color, self.status), Pion(15, 12, self.color, self.status), Pion(15, 11, self.color, self.status), Pion(14, 15, self.color, self.status), Pion(14, 14, self.color, self.status), Pion(14, 13, self.color, self.status), Pion(14, 12, self.color, self.status), Pion(14, 11, self.color, self.status),
            Pion(13, 15, self.color, self.status), Pion(13, 14, self.color, self.status), Pion(13, 13, self.color, self.status), Pion(13, 12, self.color, self.status), Pion(12, 15, self.color, self.status), Pion(12, 14, self.color, self.status), Pion(12, 13, self.color, self.status), Pion(11, 15, self.color, self.status), Pion(11, 14, self.color, self.status)
        ]

        # list of posisi goal yang harus dituju untuk size papan 8
        goalRed8 = [(7, 7), (7, 6), (7, 5), (7, 4), (6, 7),(6, 6), (6, 5), (5, 7), (5, 6), (4, 7)]
        goalGreen8 = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0),(1, 1), (1, 2), (2, 0), (2, 1), (3, 0)]

        # list of posisi goal yang harus dituju untuk size papan 10
        goalRed10 = [(9, 9), (9, 8), (9, 7), (9, 6), (9, 5), (8, 9), (8, 8),(8, 7), (8, 6), (7, 9), (7, 8), (7, 7), (6, 9), (6, 8), (5, 9)]
        goalGreen10 = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1),(1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (4, 0)]

        # list of posisi goal yang harus dituju untuk size papan 16
        goalRed16 = [(15, 15), (15, 14), (15, 13), (15, 12), (15, 11), (14, 15), (14, 14), (14, 13), (14, 12), (14, 11),(13, 15), (13, 14), (13, 13), (13, 12), (12, 15), (12, 14), (12, 13), (11, 15), (11, 14)]
        goalGreen16 = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4),(2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (4, 0), (4, 1)]

        

        if(self.size == 8):
            # jika ukuran papan 8x8
            if(self.color == 'R'):
                # jika warna player Red
                self.listOfPion = pionRed8  # list pion yang dimiliki pemain
                self.listOfGoal = goalRed8  # set posisi goal yang harus dituju pemain
                self.listOfGoalStore=goalRed8[:]
            elif(self.color == 'G'):
                # jika warna player Green
                self.listOfPion = pionGreen8
                self.listOfGoal = goalGreen8
                self.listOfGoalStore = goalGreen8[:]
        elif(self.size == 10):
            # jika ukuran papan 10x10
            if(self.color == 'R'):
                # jika warna player Red
                self.listOfPion = pionRed10
                self.listOfGoal = goalRed10
                self.listOfGoalStore = goalRed10[:]
            elif(self.color == 'G'):
                # jika warna player Green
                self.listOfPion = pionGreen10
                self.listOfGoal = goalGreen10
                self.listOfGoalStore = goalGreen10[:]
        elif(self.size == 16):
            # jika ukuran papan 16x16
            if(self.color == 'R'):
                # jika warna player Red
                self.listOfPion = pionRed16
                self.listOfGoal = goalRed16
                self.listOfGoalStore = goalRed16[:]
            elif(self.color == 'G'):
                # jika warna player Green
                self.listOfPion = pionGreen16
                self.listOfGoal = goalGreen16
                self.listOfGoal = goalGreen16[:]

    # getter
    def getListOfPion(self):
        return self.listOfPion

    def getListOfGoal(self):
        return self.listOfGoal

    def getListOfGoalStore(self):
        return self.listOfGoalStore
    
    def getColorPlayer(self):
        return self.color

    def getStatus(self):
        return self.status
    
    def getPion(self, baris, kolom):
        # cek list pion
        for el in self.getListOfPion():
            if(el.getBaris()==baris)and(el.getKolom()==kolom):
                # pion ditemukan
                return el
        return None

    # setter
    def removeGoal(self, position):
        # position dalam bentuk tuple (baris,kolom)
        # I.S. position selalu valid
        self.listOfGoal.remove(position)

    def movePion(self, currBaris, currKol, newBaris, newKol):
        # Mengganti posisi pion curr menjadi new
        for el in self.listOfPion:
            if(el.getBaris() == currBaris)and(el.getKolom() == currKol):
                # jika pion ditemukan
                # set posisi baru untuk pion
                el.setBaris(newBaris)
                el.setKolom(newKol)
                # jika sudah ditemukan keluar dari loop
                break


# contoh create player
# this this this
#  v v v v v v 

# A = Player(8, 'R', 1)
# for el in A.getListOfPion():
#     print(el.getBaris() , el.getKolom())
# print("=============")
# A.movePion(0,0,5,7)
# for el in A.getListOfPion():
#     print(el.getBaris() , el.getKolom())
# print(A.getListOfGoal())