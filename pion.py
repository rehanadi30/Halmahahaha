# import pygame

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
        # self.masukGoal()

    # Getter
    def getBaris(self):
        return self.baris

    def getKolom(self):
        return self.kolom

    def getWarna(self):
        return self.warna

    def getStatus(self):
        return self.status
    
    def getPionOwner(self,state):
        if self in state.getPlayer1().getListOfPion():
            return state.getPlayer1()
        else:
            return state.getPlayer2()
    
    def getPionEnemy(self, state):
        if self in state.getPlayer1().getListOfPion():
            return state.getPlayer2()
        else:
            return state.getPlayer1()

    # Setter
    def setBaris(self, newBaris):
        self.baris = newBaris

    def setKolom(self, newKolom):
        self.kolom = newKolom

    def possibleMove(self, state):
        # mengecek pemilik pion
        owner = self.getPionOwner(state)
        enemy = self.getPionEnemy(state)
        # mengembalikan list of tuple dari kemungkinan koordinat move yang mungkin
        result=[]
        # posisi pion saat ini
        currBaris=self.getBaris()
        currKolom=self.getKolom()
        currKoor=(currBaris,currKolom)
        # iterasi semua block 
        for i in range(state.getBoard().getSize()):
            for j in range(state.getBoard().getSize()):
                # jika i dan j bukan posisi pion
                if(i!=self.getBaris())or(j!=self.getKolom()):
                    # jika posisi pion tidak di rumah / goal lawan
                    # maka pion hanya boleh berpindah jika koor tidak di rumah
                    if ((currKoor not in enemy.getListOfGoalStore()) and (currKoor not in owner.getListOfGoalStore()))and((i,j) not in enemy.getListOfGoalStore()):
                        # jika perpindahan valid
                        if self.isJump(i,j,state) or self.isMove(i,j,state):
                            new1 = (i,j)
                            result.append(new1)
                    # jika posisi pion di rumah, bebas pindah kemanapun
                    elif(currKoor in enemy.getListOfGoalStore()):
                        # jika perpindahan valid
                        if self.isJump(i,j,state) or self.isMove(i,j,state):
                            new2 = (i,j)
                            result.append(new2)
        return result

    def possibleMoveLS(self, state):
        owner = self.getPionOwner(state)
        enemy = self.getPionEnemy(state)
        
        # posisi pion saat ini
        currBaris=self.getBaris()
        currKolom=self.getKolom()
        currKoor=(currBaris,currKolom)
        result=(currBaris,currKolom)
        # iterasi semua block 
        for i in range(state.getBoard().getSize()):
            for j in range(state.getBoard().getSize()):
                # jika i dan j bukan posisi pion
                if(i!=self.getBaris())or(j!=self.getKolom()):
                    # jika posisi pion tidak di rumah / goal lawan dan tidak di goal
                    # maka pion hanya boleh berpindah jika koor tidak di rumah
                    if ((currKoor not in enemy.getListOfGoalStore()) and (currKoor not in owner.getListOfGoalStore()))and((i,j) not in enemy.getListOfGoalStore()):
                        # jika perpindahan valid
                        if self.isJump(i,j,state) or self.isMove(i,j,state):
                            new1 = (i,j)
                            if(owner.getColorPlayer()=="R"):
                                ha=state.ha(state.getBoard().getSize())
                                val = ha[currBaris][currKolom]
                                if(val > ha[i][j]):
                                    # result.append(new1)
                                    result = new1
                            elif (owner.getColorPlayer()=="G"):
                                hb=state.hb(state.getBoard().getSize())
                                val = hb[currBaris][currKolom]
                                if(val > hb[i][j]):
                                    # result.append(new1)
                                    result = new1
                    # jika posisi pion di rumah, bebas pindah kemanapun
                    elif(currKoor in enemy.getListOfGoalStore()):
                        # jika perpindahan valid
                        if self.isJump(i,j,state) or self.isMove(i,j,state):
                            new2 = (i,j)
                            if(owner.getColorPlayer()=="R"):
                                ha=state.ha(state.getBoard().getSize())
                                val = ha[currBaris][currKolom]
                                if(val > ha[i][j]):
                                    # result.append(new2)
                                    result = new2
                            elif (owner.getColorPlayer()=="G"):
                                hb=state.hb(state.getBoard().getSize())
                                val = hb[currBaris][currKolom]
                                if(val > hb[i][j]):
                                    # result.append(new2)
                                    result = new2
                            
        return result


    def isJump(self, newBaris, newKolom, state):
        # I.S. blok pasti valid atau ada dalam board
        # mengembalikan True jika bergerak melompati satu bidak
        # else false
        # mengecek pemilik pion
        owner = self.getPionOwner(state)
        enemy = self.getPionEnemy(state)
        # posisi pion saat ini
        currBaris=self.getBaris()
        currKolom=self.getKolom()
        currKoor=(currBaris,currKolom)
        # valid jika
        # 1. posisi pion (tidak di rumah dan tidak di goal) dan posisi pion baru tidak di rumah
        # atau
        # 2. posisi pion di rumah
        
        if (((currKoor not in enemy.getListOfGoalStore()) and (currKoor not in owner.getListOfGoalStore()) )and((newBaris,newKolom) not in enemy.getListOfGoalStore()))or(currKoor in enemy.getListOfGoalStore()):
            # jika posisi baru yang ingin ditempati kosong
            if(state.getBoard().getColor(newBaris,newKolom)=='n'):
                # melakukan lompatan vertikal
                if(newBaris==self.getBaris()-2)and(newKolom==self.getKolom()):
                    # lompatan ke atas
                    # True jika satu kotak di depannya terdapat bidak
                    if state.getBoard().getColor(self.getBaris()-1,self.getKolom()) != 'n':
                        return True
                elif(newBaris==self.getBaris()+2)and(newKolom==self.getKolom()):
                    # lompatan ke bawah
                    # True jika satu kotak di depannya terdapat bidak
                    if state.getBoard().getColor(self.getBaris()+1,self.getKolom()) != 'n':
                        return True

                # melakukan lompatan horizontal
                elif(newBaris==self.getBaris())and(newKolom==self.getKolom()-2):
                    # lompatan ke kiri
                    # True jika satu kotak di depannya terdapat bidak
                    if state.getBoard().getColor(self.getBaris(),self.getKolom()-1) != 'n':
                        return True
                elif(newBaris==self.getBaris())and(newKolom==self.getKolom()+2):
                    # lompatan ke kanan
                    # True jika satu kotak di depannya terdapat bidak
                    if state.getBoard().getColor(self.getBaris(),self.getKolom()+1) != 'n':
                        return True

                # melakukan lompatan diagonal
                elif(newBaris==self.getBaris()-2)and(newKolom==self.getKolom()+2):
                    # lompatan ke kanan atas
                    # True jika satu kotak di depannya terdapat bidak
                    if state.getBoard().getColor(self.getBaris()-1,self.getKolom()+1) != 'n':
                        return True
                elif(newBaris==self.getBaris()-2)and(newKolom==self.getKolom()-2):
                    # lompatan ke kiri atas
                    # True jika satu kotak di depannya terdapat bidak
                    if state.getBoard().getColor(self.getBaris()-1,self.getKolom()-1) != 'n':
                        return True
                elif(newBaris==self.getBaris()+2)and(newKolom==self.getKolom()+2):
                    # lompatan ke kanan bawah
                    # True jika satu kotak di depannya terdapat bidak
                    if state.getBoard().getColor(self.getBaris()+1,self.getKolom()+1) != 'n':
                        return True
                elif(newBaris==self.getBaris()+2)and(newKolom==self.getKolom()-2):
                    # lompatan ke kiri bawah
                    # True jika satu kotak di depannya terdapat bidak
                    if state.getBoard().getColor(self.getBaris()+1,self.getKolom()-1) != 'n':
                        return True
                
                # selain itu bukan jump
                else:
                    return False
            else:
                return False
        else:
            return False

    def isMove(self, newBaris, newKolom, state):
        # I.S. blok pasti valid atau ada dalam board
        # mengembalikan True jika bergerak/berpindah satu kotak
        # else false

        # mengecek pemilik pion
        owner = self.getPionOwner(state)
        enemy = self.getPionEnemy(state)
        # posisi pion saat ini
        currBaris=self.getBaris()
        currKolom=self.getKolom()
        currKoor=(currBaris,currKolom)
        # valid jika
        # 1. posisi pion (tidak di rumah dan tidak di goal) dan posisi pion baru tidak di rumah
        # atau
        # 2. posisi pion di rumah
        
        if (((currKoor not in enemy.getListOfGoalStore()) and (currKoor not in owner.getListOfGoalStore()) )and((newBaris,newKolom) not in enemy.getListOfGoalStore()))or(currKoor in enemy.getListOfGoalStore()):

            # jika posisi baru yang ingin ditempati kosong
            if(state.getBoard().getColor(newBaris,newKolom)=='n'):
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
        return False

    def isGoal(self, size):
    #Boolean, ngereturn kondisi ketika masuk kondisi goal
        if(self.color == 'G'):
            if (size == 16):
                if(self.getBaris() != 0 or self.getKolom() != 0):
                    return (self.getBaris()+self.getKolom() <= 5)
                else:
                    return (self.getBaris()+self.getKolom < 5)
            elif(size == 10):
                return (self.getBaris()+self.getKolom() <= 4)
            elif(size == 8):
                return (self.getBaris() + self.getKolom() <= 3)
        elif(self.color == 'R'):
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
        
    def masukGoal(self,size):
    #Buat ngubah state goal. Setiap isGoal berubah status, fungsi ini dipanggil
        if(self.isGoal(size)):
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


