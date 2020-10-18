from Player import *
from board import *

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
        # print(goal)
        for i in range(len(goal)):
            if(pos[0]==goal[i][0] and pos[1]==goal[i][1]):
                # print("True")
                return True
        # print("False")
        return False

    def hn(self,n):

        start = 10
        count = 1
        i = 3
        track = [15,10]
        

        matriks = [[0 for i in range(16)] for j in range(16)]
        
        while(start>=0):
            current = track
            for x in range(i):
                if(x!=0):
                    current[0] = current[0] - 1
                print(current)
                matriks[current[0]][current[1]] = count
            print(track)
                
            print("")
            for x in range(5):
                if(x%2==0):
                    current[1] = current[1] + 1
                else:
                    current[0] = current[0] - 1
                print(current)
                matriks[current[0]][current[1]] = count
            print(track)
            print("")

            
            for x in range(i):
                if(x==0):
                    current[0] = current[0] - 1
                else:
                    current[1] = current[1] + 1
                print(current)
                matriks[current[0]][current[1]] = count
            print(track)
            print("")
            
            
            start-=1
            count+=1
            i+=1
            track[1]-=1
            print(current)
            print("--------------------------------")


            
            




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

        h1_size8 = [(6,5,5,4,4,4,4,4),
                    (5,5,4,4,3,3,3,3),
                    (5,4,4,3,3,2,2,2),
                    (4,4,3,3,2,2,1,1),
                    (4,3,3,2,2,1,1,0),
                    (4,3,2,2,1,1,0,0),
                    (4,3,2,1,1,0,0,0),
                    (4,3,2,1,0,0,0,0)]

        h2_size8 = [(0,0,0,0,1,2,3,4),
                    (0,0,0,1,1,2,3,4),
                    (0,0,1,1,2,2,3,4),
                    (0,1,1,2,2,3,3,4),
                    (1,1,2,2,3,3,4,4),
                    (2,2,2,3,3,4,4,5),
                    (3,3,3,3,4,4,5,5),
                    (4,4,4,4,4,5,5,6)]

        for i in range(len(pion1)):
            x = pion1[i].getBaris()
            y = pion1[i].getKolom()
            h1 += h1_size8[x][y]

        
        for i in range(len(pion2)):
            x = pion2[i].getBaris()
            y = pion2[i].getKolom()
            h2 += h2_size8[x][y]

        print("g1 = " + str(g1))
        print("g2 = " + str(g2))
        print("h1 = " + str(h1))
        print("h2 = " + str(h2))
        f1 = g1 + h1
        f2 = g2 + h2
        f = f1 - f2
        print("f1 = " + str(f1))
        print("f2 = " + str(f2))
        print("f = " + str(f))


        return
    
    # def isGameOver(self):
    #     p = self.board.matriksofpion
    #     n = SIZE
    #     gameover = False
    #     pion = 10

    #     red = 0
    #     green = 0
    #     not_goal = 0

    #     for i in range(SIZE):
    #         for j in range(SIZE):
    #             current = p[i][j]
    #             if(p.isGoal()):
    #                 if(p.warna = 'r'):
    #                     red+=1
    #                 elif(p.warna ='g'):
    #                     green+=1
    #             else:
    #                 not_goal +=1
        
    #     if(red==10 or green==10):
    #         return true
    #     else:
    #         return false

# p1 = Player (SIZE,"R",1)
# p2 = Player (SIZE,"G",2)
# board = Board()

# a = State(p1,p2,board,1)

# # a.objectiveFunction()
# a.hn(16)

start = 10
count = 1
i = 3
track = [15,10]


matriks = [[0 for i in range(16)] for j in range(16)]

while(start>=0):
    current = track
    for x in range(i):
        if(x!=0):
            current[0] = current[0] - 1
        print(current)
        matriks[current[0]][current[1]] = count
    print(track)
        
    print("")
    for x in range(5):
        if(x%2==0):
            current[1] = current[1] + 1
        else:
            current[0] = current[0] - 1
        print(current)
        matriks[current[0]][current[1]] = count
    print(track)
    print("")

    
    for x in range(i):
        if(x==0):
            current[0] = current[0] - 1
        else:
            current[1] = current[1] + 1
        print(current)
        matriks[current[0]][current[1]] = count
    print(track)
    print("")
    
    
    start-=1
    count+=1
    i+=1
    track[1]-=1
    print(current)
    print("--------------------------------")










