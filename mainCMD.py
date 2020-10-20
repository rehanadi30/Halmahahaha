from state import *
import time
from MiniMaxBiasa import *
from minimax_LS import *

def moveOnePionStatusPlayer(player,state,t):
    timestart=time.time()

    while(time.time()<timestart+t):
        #print kondisi papan setelah dilakukan perpindahan
        for el in state.getBoard().getMatrixofColor():
            print(el)
        print(timestart+t)
        print(time.time())

        pionIsPlayers=False #validasi pion yang dipilih
        # pemilihan pion
        while(not pionIsPlayers):
            pionBaris, pionKolom = map(int,input("Masukkan baris dan kolom pion yang ingin dipindahkan: ").split())
            movingPion = player.getPion(pionBaris,pionKolom)
            if movingPion in player.getListOfPion():
                pionIsPlayers=True
            else:
                print("================================")
                print("Pion yang anda pilih tidak valid")
                print("================================")
        temp=True #end of movement
        i=1
        listOfMove=[] #list move yang ingin dilakukan

        print("Masukkan baris dan kolom baru untuk memindahkan pion, akhiri dengan \"lock move\": ")
        # perpindahan pion
        while(temp):
            newBaris, newKolom = input("Step-"+str(i)+(":")).split()
            if(newBaris!="lock"):
                newKoor=(int(newBaris),int(newKolom))
                listOfMove.append(newKoor)
                print(newBaris)
                print(newKolom)
                i+=1
            else:
                temp=False
        # jika ada perpindahan yang dimasukkan
        if len(listOfMove)!=0:
            if(state.movePioninOneTurn(movingPion,listOfMove)):
                print("===========================")
                print("Perpindahan pion valid yiy!")
                print("===========================")
                
                state.switchTurn()
                return
            else:
                print("=============================")
                print("Perpindahan pion tidak valid!")
                print("coba lagi..")
                print("=============================")
                
        # jika tidak ada perpindahan / player skip turn
        else:
            print("==================")
            print("switch turn tedeng")
            print("==================")
            
            state.switchTurn()
            return
    # jika waktu habis
    print("TimesUp")
    state.switchTurn()
    
    

def moveOnePionStatusBOTM(state,player,enemy,t):
    #print kondisi papan setelah dilakukan perpindahan
    for el in state.getBoard().getMatrixofColor():
        print(el)
    bestMove(state,player,enemy,t, -Infinity, Infinity)
    
    
def moveOnePionStatusBOTMLS(state,player,enemy,t):
    for el in state.getBoard().getMatrixofColor():
        print(el)
    bestMoveLS(state,player,enemy,t,-Infinity, Infinity)



# main program
size = int(input("Masukkan ukuran papan: ")) #ukuran papan
t = int(input("Masukkan time: ")) #lama waktu
playerRed = Player(size, 'R', 1) #pembuatan player merah
playerGreen = Player(size, 'G', 0) #pembuatan player hijau
state = State(playerRed, playerGreen,size) #pembuatan state



while not state.isGameOver():
    print("=====================")
    print("Now is your turn: ", end="")
    print (state.getTurn().getColorPlayer())
    print("=====================")
  
    if(state.getTurn().getColorPlayer()=='R'): #turn playerRed
        # jika player memiliki status 2 sebagai Player
        if(playerRed.getStatus()==2):
            
            moveOnePionStatusPlayer(playerRed,state,t)
            for el in playerRed.getListOfPion():
                print(el.getBaris() , el.getKolom())
        # status 1 sebagai BOT minimax-lS
        elif(playerRed.getStatus()==1):
            moveOnePionStatusBOTMLS(state,playerRed,playerGreen,t)
        # status 0 sebagai BOT minimax
        elif(playerRed.getStatus()==0):
            moveOnePionStatusBOTM(state,playerRed,playerGreen,t)

    elif(state.getTurn().getColorPlayer()=='G'): #turn playerGreen
        if(playerGreen.getStatus()==2):
            moveOnePionStatusPlayer(playerGreen,state,t)
        # status 1 sebagai BOT minimax-lS
        elif(playerGreen.getStatus()==1):
            moveOnePionStatusBOTMLS(state,playerGreen,playerRed,t)
        # status 0 sebagai BOT minimax
        elif(playerGreen.getStatus()==0):
            moveOnePionStatusBOTM(state,playerGreen,playerRed,t)
    
