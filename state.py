from Player import *
from board import *
from pion import *

class State:

    def __init__(self,p1,p2,papan,turn):
        self.p1 = p1 #bot
        self.p2 =  p2 #pemain
        self.board = board
        self.turn = turn
        # self.time = 

    def getPlayer1(self):
        return self.p1
        
    def getPlayer2(self):
        return self.p2

    def getBoard(self):
        return self.board

    def getTime(self):
        pass

    def GetTurn(self):
        return self.turn

    def isGoal(self,pos,player):
        goal = player.getListOfGoal()
        for i in range(len(goal)):
            if(pos[0]==goal[i][0] and pos[1]==goal[i][1]):
                return True
        return False
    
    def movePioninOneTurn(self,pion):
        currPlayer = self.turn[:]
        while(self.turn == currPlayer):
            # pion move jika perpindahan valid
            if(pion.isJump()):
                currPlayer.movePion(pion.getBaris(), pion.getKolom(), newBaris, newKol)
    

    def ha(self,n):

        n = 10
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
        h2_size= self.ha(self.board.getSize())

        for i in range(len(pion1)):
            x = pion1[i].getBaris()
            y = pion1[i].getKolom()
            h1 += h1_size[x][y]

        
        for i in range(len(pion2)):
            x = pion2[i].getBaris()
            y = pion2[i].getKolom()
            h2 += h2_size[x][y]

        print("g1 = " + str(g1))
        print("g2 = " + str(g2))
        print("h1 = " + str(h1))
        print("h2 = " + str(h2))
        # f1 = g1 + h1
        # f2 = g2 + h2
        # f = f1 - f2
        f = g1-g2-h1+h2
        print("f1 = " + str(f1))
        print("f2 = " + str(f2))
        print("f = " + str(f))
        return f
    
    def isGameOver(self):
        if(len(self.p1.getListOfGoal)==0 or len(self.p1.getListOfGoal)==0):
            return True
        else:
            return False






