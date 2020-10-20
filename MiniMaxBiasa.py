import math
import time
from konstanta import Infinity

def max(a, b):
    if(a>b):
        return a
    else:
        return b

def min(a, b):
    return a + b - max(a, b)

def bestMove(state, botPlayer, humanPlayer, t,alpha,beta):
    bestNilai = -math.inf
    # timestart=time.time()
    # init currpion
    currpion = botPlayer.getListOfPion()[0]
    # init move
    move=currpion.possibleMove(state)[0]
    # while(time.time()<timestart+t):
        
    # untuk semua pion yang dimiliki player
    for p in botPlayer.getListOfPion():
        # kemungkinan koordinat move pion
        kemungkinan = p.possibleMove(state)
        
        # untuk semua kemungkinan dicek nilainya
        for k in kemungkinan:          
            prevBaris = p.getBaris()
            prevKolom = p.getKolom()
            prevKoor = (prevBaris,prevKolom)
            # pindahkan pion
            state.movePionMinimax(p,k,botPlayer)
            # cek nilai minimax
            newNilai = minimax(state,0,False,botPlayer,humanPlayer,alpha,beta)
            # kembalikan state ke state sebelumnya
            state.movePionMinimax(p,prevKoor,botPlayer)

            # jika newNilai>bestNilai
            if (newNilai>bestNilai):
                bestNilai=newNilai
                currBarisPion = p.getBaris()
                currKolomPion = p.getKolom()
                currpion = botPlayer.getPion(currBarisPion,currKolomPion)
                move=k
        
    state.movePionMinimax(currpion, move, botPlayer)
    state.switchTurn()


def minimax(state, depth, isMaximizing, botPlayer, humanPlayer,alpha,beta):
    nilai = state.objectiveFunction()
    if(state.isGameOver() or depth==1):
        return nilai
        
    if(isMaximizing):
        bestNilai = -math.inf
        # untuk semua pion yang dimiliki player
        for p in botPlayer.getListOfPion():
            # kemungkinan koordinat move pion
            kemungkinan = p.possibleMove(state)
            # untuk semua kemungkinan dicek nilainya
            for k in kemungkinan:
                
                prevBaris = p.getBaris()
                prevKolom = p.getKolom()
                prevKoor = (prevBaris,prevKolom)
                
                # pindahkan pion
                state.movePionMinimax(p,k,botPlayer)
                # cek nilai minimax
                newNilai = minimax(state,(depth+1),False,botPlayer,humanPlayer,alpha,beta)
                # kembalikan state ke state sebelumnya
                state.movePionMinimax(p,prevKoor,botPlayer)
                # jika newNilai>bestNilai
                bestNilai= max(bestNilai, newNilai)
                alpha = max(bestNilai, alpha)
                if(beta <= alpha):
                    break
                
        return bestNilai
    else:
        bestNilai = math.inf
        # untuk semua pion yang dimiliki player
        for p in humanPlayer.getListOfPion():
            # kemungkinan koordinat move pion
            kemungkinan = p.possibleMove(state)
            # untuk semua kemungkinan dicek nilainya
            for k in kemungkinan:
                prevBaris = p.getBaris()
                prevKolom = p.getKolom()
                prevKoor = (prevBaris,prevKolom)
                # pindahkan pion
                state.movePionMinimax(p,k,humanPlayer)
                # cek nilai minimax
                newNilai = minimax(state,(depth+1),True,botPlayer,humanPlayer,alpha,beta)
                # kembalikan state ke state sebelumnya
                state.movePionMinimax(p,prevKoor,humanPlayer)
                # jika newNilai>bestNilai
                bestNilai = min(bestNilai, newNilai)
                alpha = min(bestNilai, alpha)
                if (beta <= alpha):
                    break
               
        return bestNilai



            