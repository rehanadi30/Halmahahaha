from Player import *
from papan import *
from pion import *
from konstanta import Infinity

class State:

    def __init__(self,p1,p2,size):
        self.p1 = p1 #bot
        self.p2 =  p2 #pemain
        self.board = papan(size)
        self.turn = p1 #selalu p1 mulai turn duluan
        self.nilai = self.objectiveFunction()
        # self.time = 

    def getPlayer1(self):
        return self.p1
        
    def getPlayer2(self):
        return self.p2

    def getBoard(self):
        return self.board

    def getTime(self):
        pass
    
    def switchTurn(self):
        if(self.turn == self.getPlayer1()):
            self.turn = self.p2
        else:
            self.turn = self.p1
        

    def getTurn(self):
        return self.turn
    

    def getNilai(self):
        return self.nilai

    def isGoal(self,pos,player):
        goal = player.getListOfGoal()
        for i in range(len(goal)):
            if(pos[0]==goal[i][0] and pos[1]==goal[i][1]):
                return True
        return False
    
    # def movePioninOneTurn(self,pion):
    #     currPlayer=self.turn
    #     currColorPlayer = self.turn.getColorPlayer()[:]
    #     # menyimpan pergerakan pion sebelum
    #     prev = ''
    #     prevRow=''
    #     prevCol=''
    #     newRow=''
    #     newCol=''
    #     while(self.turn.getColorPlayer() == currColorPlayer):
    #         newBaris,newKolom=map(int,input("Masukkan baris dan kolom baru: ").split())
    #         # move awal
    #         if(prev==''):
    #             # valid jika pion move atau jump
    #             if(pion.isJump(newBaris,newKolom,self.getBoard())):
    #                 prevRow = pion.getBaris()
    #                 prevCol = pion.getKolom()
    #                 newRow = newBaris
    #                 newCol = newKolom

    #                 currPlayer.movePion(pion.getBaris(), pion.getKolom(), newBaris, newKolom)
    #                 # simpan pergerakan saat ini
    #                 prev='jump'
    #             elif(pion.isMove(newBaris,newKolom,self.getBoard())):
    #                 prevRow = pion.getBaris()
    #                 prevCol = pion.getKolom()
    #                 newRow = newBaris
    #                 newCol = newKolom

    #                 # move pisisi pion di player
    #                 currPlayer.movePion(pion.getBaris(), pion.getKolom(), newBaris, newKolom)
    #                 # simpan pergerakan saat ini
    #                 prev='move'
    #                 # setelah move, switch player
    #                 self.switchTurn()
                    
    #             else:
    #                 # bisa move lagi with another pion
    #                 return None
    #         # move selanjutnya (khusus jump)
    #         else:
    #             # valid jika pion jump
    #             if(pion.isJump(newBaris,newKolom,self.getBoard())):
    #                 newRow = newBaris
    #                 newCol = newKolom

    #                 currPlayer.movePion(pion.getBaris(), pion.getKolom(), newBaris, newKolom)
    #                 # simpan pergerakan saat ini
    #                 prev='jump'
    #             else:
    #                 # bisa move lagi with another pion
    #                 return None

    #     # jika ada pergerakan maka ubah warna blok
    #     if(prev!=''):
    #         for el in currPlayer.getListOfPion():
    #             print(el.getBaris() , el.getKolom())
    #         # ganti warna blok 
    #         # posisi new diganti warna player
    #         self.board.changeColor(newRow,newCol,currColorPlayer.lower())
    #         # pisisi sebelum diganti 'n'
    #         self.board.changeColor(prevRow, prevCol,'n')
    #         return prev
    def movePionMinimax(self,pion,newPosition,currPlayer):
        currColorPlayer = currPlayer.getColorPlayer()[:] #warna player

        newBaris = newPosition[0]
        newKolom = newPosition[1]
        # movement pasti valid
        prevRow = pion.getBaris()
        prevCol = pion.getKolom()
        newRow = newBaris
        newCol = newKolom
        # pindahin pion ke posisi baru
        currPlayer.movePion(pion.getBaris(), pion.getKolom(), newBaris, newKolom)
        # ganti warna blok 
        # posisi new diganti warna player
        self.board.changeColor(newRow,newCol,currColorPlayer.lower())
        # pisisi sebelum diganti 'n'
        self.board.changeColor(prevRow, prevCol,'n')
        # jika newRow dan newCol merupakan goal maka remove goal dari listofgoal
        
        newKoor=(newRow,newCol)
        if newKoor in currPlayer.getListOfGoal():
            currPlayer.removeGoal(newKoor)
    def movePioninOneTurn(self,pion,listOfNewPosition):
        print("masukmovepioninoneturn")
        # List of new position --> list of tuple dari new position dari sebuah pion
        currPlayer=self.turn #player
        currColorPlayer = self.turn.getColorPlayer()[:] #warna player

        # menyimpan pergerakan pion sebelum
        prev = ''

        # loop sepanjang listOfNewPosition
        for koor in listOfNewPosition:
            newBaris = koor[0]
            newKolom = koor[1]

            # move awal
            if(prev==''):
                # valid jika pion move atau jump
                if(pion.isJump(newBaris,newKolom,self)):
                    prevRow = pion.getBaris()
                    prevCol = pion.getKolom()
                    newRow = newBaris
                    newCol = newKolom
                    # pindahin pion ke posisi baru
                    currPlayer.movePion(pion.getBaris(), pion.getKolom(), newBaris, newKolom)
                    # simpan pergerakan saat ini
                    prev='jump'
                elif(pion.isMove(newBaris,newKolom,self)):
                    prevRow = pion.getBaris()
                    prevCol = pion.getKolom()
                    newRow = newBaris
                    newCol = newKolom

                    # move pisisi pion di player
                    currPlayer.movePion(pion.getBaris(), pion.getKolom(), newBaris, newKolom)
                    # simpan pergerakan saat ini
                    prev='move'
                    
                else:
                    # movement tidak valid
                    return False
            # move selanjutnya
            else:
                # jika move sebelum adalah move
                if(prev=='move'):
                    # kembalikan pion ke posisi awal
                    currPlayer.movePion(pion.getBaris(),pion.getKolom(),prevRow,prevCol)
                    return False #tidak boleh ada pergerakan setelah move
                # jika move sebelum adalah jump
                if(prev=='jump'):
                    # valid jika pion jump
                    if(pion.isJump(newBaris,newKolom,self)):
                        newRow = newBaris
                        newCol = newKolom
                        # pindahin pion ke posisi baru
                        currPlayer.movePion(pion.getBaris(), pion.getKolom(), newBaris, newKolom)
                        # simpan pergerakan saat ini
                        prev='jump'
                    else:
                        # kembalikan pion ke posisi awal
                        currPlayer.movePion(pion.getBaris(),pion.getKolom(),prevRow,prevCol)
                        # selain jump gerakan tidak valid
                        return False

        # jika pergerakan valid ubah warna di board
        
        # ganti warna blok 
        # posisi new diganti warna player
        self.board.changeColor(newRow,newCol,currColorPlayer.lower())
        # pisisi sebelum diganti 'n'
        self.board.changeColor(prevRow, prevCol,'n')
        # jika newRow dan newCol merupakan goal maka remove goal dari listofgoal
        
        newKoor=(newRow,newCol)
        if newKoor in currPlayer.getListOfGoal():
            currPlayer.removeGoal(newKoor)
        return True #movement valid



    def ha(self,n):
        matriks = [[0 for i in range(n)] for j in range(n)]

        count = 1
        if(n==16):
            start = 12
            i = 3
            track = [15,10]
            jump = 5
        elif(n==8):
            start = 5
            i = 2
            track = [7,3]
            jump = 5
        else:
            start = 6
            i = 2
            track = [9,4]
            jump = 7

        while(start>=0):
            current = track[:]
            if(start==0):
                matriks[0][0] = count
                if(n==10):
                    matriks[1][0] = count
                    matriks[0][1] = count
            elif(start==1):
                if(n==16 or n==8):
                    matriks[1][0] = count
                    matriks[2][0] = count
                    matriks[0][1] = count
                    matriks[1][1] = count
                    matriks[0][2] = count
                else:
                    matriks[2][0] = count
                    matriks[3][0] = count
                    matriks[1][1] = count
                    matriks[2][1] = count
                    matriks[0][2] = count
                    matriks[1][2] = count
                    matriks[0][3] = count

            else:
                for x in range(i):
                    if(x!=0):
                        current[0] = current[0] - 1
                    # print(current)
                    matriks[current[0]][current[1]] = count
                # print("")

                for x in range(jump):
                    if(x%2==0):
                        current[1] = current[1] + 1
                    else:
                        current[0] = current[0] - 1
                    # print(current)
                    matriks[current[0]][current[1]] = count
                # print("")

                for x in range(i):
                    if(x==0):
                        current[0] = current[0] - 1
                    else:
                        current[1] = current[1] + 1
                    # print(current)
                    matriks[current[0]][current[1]] = count
                # print("")
            
            
            start-=1
            count+=1
            i+=1
            track[1]-=1
        # for i in range(n):
        #     for j in range(n):
        #         print(matriks[i][j], end="")
        #     print()
        return matriks

    def hb(self,n):
        matriks1 = [[0 for i in range(n)] for j in range(n)]
        count = 1
        if(n==16):
            start = 12
            i = 3
            track = [0,5]
            jump = 5
        elif(n==8):
            start = 5
            i = 2
            track = [0,4]
            jump = 5
        else:
            start = 6
            i = 2
            track = [0,5]
            jump = 7

        while(start>=0):
            current = track[:]
            if(start==0):
                matriks1[n-1][n-1] = count
                if(n==10):
                    matriks1[n-1][n-2] = count
                    matriks1[n-2][n-1] = count
            elif(start==1):
                if(n==16 or n==8):
                    matriks1[n-3][n-1] = count
                    matriks1[n-2][n-1] = count
                    matriks1[n-2][n-2] = count
                    matriks1[n-1][n-2] = count
                    matriks1[n-1][n-3] = count
                else:
                    matriks1[n-4][n-1] = count
                    matriks1[n-3][n-1] = count
                    matriks1[n-3][n-2] = count
                    matriks1[n-2][n-2] = count
                    matriks1[n-2][n-3] = count
                    matriks1[n-1][n-3] = count
                    matriks1[n-1][n-4] = count

            else:
                for x in range(i):
                    if(x!=0):
                        current[0] = current[0] + 1
                    # print(current)
                    matriks1[current[0]][current[1]] = count
                # print("")

                for x in range(jump):
                    if(x%2==0):
                        current[1] = current[1] - 1
                    else:
                        current[0] = current[0] + 1
                    # print(current)
                    matriks1[current[0]][current[1]] = count
                # print("")

                for x in range(i):
                    if(x==0):
                        current[0] = current[0] + 1
                    else:
                        current[1] = current[1] - 1
                    # print(current)
                    matriks1[current[0]][current[1]] = count
                # print("")
            
            
            start-=1
            count+=1
            i+=1
            track[1]+=1
        
        # for i in range(n):
        #     for j in range(n):
        #         print(matriks1[i][j], end="")
        #     print()
        return matriks1

    def objectiveFunction(self):

        # size = self.board.getSize()
        size = 8
        if(size==8):
            n = 10
        elif(size==10):
            n = 15
        elif(size==16):
            n = 19

        
        pion1 = self.p1.getListOfPion()
        pion2 = self.p2.getListOfPion()

        g1 = n - len(self.p1.getListOfGoal())
        g2 = n - len(self.p2.getListOfGoal())

        h1 = 0
        h2 = 0

        h1_size= self.ha(self.board.getSize())
        h2_size= self.hb(self.board.getSize())

        for i in range(len(pion1)):
            x = pion1[i].getBaris()
            y = pion1[i].getKolom()
            h1 += h1_size[x][y]

        
        for i in range(len(pion2)):
            x = pion2[i].getBaris()
            y = pion2[i].getKolom()
            h2 += h2_size[x][y]

        
        # f1 = g1 + h1
        # f2 = g2 + h2
        # f = f1 - f2
        f = g1-g2-h1+h2
        # print("f1 = " + str(f1))
        # print("f2 = " + str(f2))
       
        return f
    
    def isGameOver(self):
        if(len(self.p1.getListOfGoal())==0 or len(self.p2.getListOfGoal())==0):
            return True
        else:
            return False


# a = Player(8,"R",1)
# b = Player(8,"G",2)

# c = State(a,b,8)
# c.ha(8)
# c.hb(8)
# c.objectiveFunction()




