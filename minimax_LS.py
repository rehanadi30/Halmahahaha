import math
import time


def max(a, b):
    if(a>b):
        return a
    else:
        return b

def min(a, b):
    return a + b - max(a, b)


def bestMoveLS(state,botPlayer,humanPlayer,t,alpha,beta):
    bestNilai = -math.inf
    # timestart=time.time()
    # while(time.time()<timestart+t):
    # init currpion
    currpion = botPlayer.getListOfPion()[0]
    # init move
    move=currpion.possibleMoveLS(state)
    # untuk semua pion yang dimiliki player
    for p in botPlayer.getListOfPion():
        # kemungkinan koordinat move pion
        kemungkinan = p.possibleMoveLS(state)
        # posisi pion sebelum
        prevBaris = p.getBaris()
        prevKolom = p.getKolom()
        prevKoor = (prevBaris,prevKolom)

        # pindahkan pion
        state.movePionMinimax(p,kemungkinan,botPlayer)
        # cek nilai minimax
        newNilai = minimaxLS(state,0,False,botPlayer,humanPlayer,alpha,beta)
        # kembalikan state ke state sebelumnya
        state.movePionMinimax(p,prevKoor,botPlayer)

        # jika newNilai>bestNilai
        if (newNilai>bestNilai):
            bestNilai=newNilai
            currBarisPion = p.getBaris()
            currKolomPion = p.getKolom()
            currpion = botPlayer.getPion(currBarisPion,currKolomPion)
            move=kemungkinan
        
    state.movePionMinimax(currpion,move,botPlayer)
    state.switchTurn()


def minimaxLS(state, depth, isMaximizing, botPlayer, humanPlayer,alpha,beta):
    nilai = state.objectiveFunction()
    if(state.isGameOver() or depth==1):
        return nilai
        
    if(isMaximizing):
        bestNilai = -math.inf
        # untuk semua pion yang dimiliki player
        for p in botPlayer.getListOfPion():
            # kemungkinan koordinat move pion
            kemungkinan = p.possibleMoveLS(state)
            # posisi pion sebelum
            prevBaris = p.getBaris()
            prevKolom = p.getKolom()
            prevKoor = (prevBaris,prevKolom)

            # pindahkan pion
            state.movePionMinimax(p,kemungkinan,botPlayer)
            # cek nilai minimax
            newNilai = minimaxLS(state,(depth+1),False,botPlayer,humanPlayer,alpha,beta)
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
            kemungkinan = p.possibleMoveLS(state)
            # posisi pion sebelum
            prevBaris = p.getBaris()
            prevKolom = p.getKolom()
            prevKoor = (prevBaris,prevKolom)

            # pindahkan pion
            state.movePionMinimax(p,kemungkinan,humanPlayer)
            # cek nilai minimax
            newNilai = minimaxLS(state,(depth+1),True,botPlayer,humanPlayer,alpha,beta)
            # kembalikan state ke state sebelumnya
            state.movePionMinimax(p,prevKoor,humanPlayer)
        
            # jika newNilai>bestNilai
            bestNilai = min(bestNilai, newNilai)
            alpha = min(bestNilai, alpha)
            if (beta <= alpha):
                break
        return bestNilai



            