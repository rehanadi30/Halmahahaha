import math
import time

def bestMoveLS(state,botPlayer,humanPlayer,t):
    bestNilai = -math.inf
    timestart=time.time()
    while(time.time()<timestart+t):
        # currpion = botPlayer.getListOfPion()[0]
        # move = currpion.possibleMoveLS(state)[0]
        # untuk semua pion yang dimiliki player
        for p in botPlayer.getListOfPion():
            # kemungkinan koordinat move pion
            kemungkinan = p.possibleMoveLS(state)
            
            # untuk satu kemungkinan dicek nilainya
            state.movePionMinimax(p,kemungkinan,botPlayer)
            # cek nilai minimax
            newNilai = minimaxLS(state,0,False,botPlayer,humanPlayer)
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


def minimaxLS(state, depth, isMaximizing, botPlayer, humanPlayer):
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
                newNilai = minimax(state,(depth+1),False,botPlayer,humanPlayer)
                # kembalikan state ke state sebelumnya
                state.movePionMinimax(p,prevKoor,botPlayer)
                # jika newNilai>bestNilai
                if (newNilai>bestNilai):
                    bestNilai=newNilai
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
                newNilai = minimax(state,(depth+1),True,botPlayer,humanPlayer)
                # kembalikan state ke state sebelumnya
                state.movePionMinimax(p,prevKoor,humanPlayer)
                # jika newNilai>bestNilai
                if (newNilai<bestNilai):
                    bestNilai=newNilai
        return bestNilai



            