from state import *
import time


size = int(input("Masukkan ukuran papan: "))
playerRed = Player(size, 'R', 2)
playerGreen = Player(size, 'G', 2)
state = State(playerRed, playerGreen,size)


for el in state.getBoard().getMatrixofColor():
    print(el)



run=True

while run:
    print("Now is your turn: ", end="")
    print (state.getTurn().getColorPlayer())
    pionBaris='999'
    if(state.getTurn().getColorPlayer()=='R'):
        if(playerRed.getStatus()==2):
            pionBaris, pionKolom = map(int,input("Masukkan baris dan kolom pion yang ingin dipindahkan: ").split())
            movingPion = playerRed.getPion(pionBaris,pionKolom)
            state.movePioninOneTurn(movingPion)
    elif(state.getTurn().getColorPlayer()=='G'):
        if(playerGreen.getStatus()==2):
            pionBaris, pionKolom = map(int,input("Masukkan baris dan kolom pion yang ingin dipindahkan: ").split())
            movingPion = playerRed.getPion(pionBaris,pionKolom)
            state.movePioninOneTurn(movingPion)
    if(pionBaris=='-1'):
        run=False
    for el in state.getBoard().getMatrixofColor():
        print(el)
