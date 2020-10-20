import math

def bestMove(state,botPlayer,humanPlayer):
    bestNilai = -math.inf

    # untuk semua pion yang dimiliki player
    for p in botPlayer.getListOfPion():
        # kemungkinan koordinat move pion
        kemungkinan = p.possibleMove(state)
        
        # untuk semua kemungkinan dicek nilainya
        for k in kemungkinan: 
            print("awal")
            print (k[0],k[1])          
            prevBaris = p.getBaris()
            prevKolom = p.getKolom()
            prevKoor = (prevBaris,prevKolom)
            print(prevKoor[0],prevKoor[1])
            # pindahkan pion
            state.movePionMinimax(p,k,botPlayer)
            # cek nilai minimax
            newNilai = minimax(state,0,False,botPlayer,humanPlayer)
            # kembalikan state ke state sebelumnya
            state.movePionMinimax(p,prevKoor,botPlayer)

            # jika newNilai>bestNilai
            if (newNilai>bestNilai):
                bestNilai=newNilai
                move=k
    state.movePionMinimax(p,move,botPlayer)
    #print kondisi papan setelah dilakukan perpindahan
    for el in state.getBoard().getMatrixofColor():
        print(el)
    state.switchTurn()


def minimax(state, depth, isMaximizing, botPlayer, humanPlayer):
    nilai = state.objectiveFunction()
    if(state.isGameOver() or depth==1):
        #print kondisi papan setelah dilakukan perpindahan
        for el in state.getBoard().getMatrixofColor():
            print(el)
        print(nilai)
        return nilai
        
    if(isMaximizing):
        bestNilai = -math.inf
        # untuk semua pion yang dimiliki player
        for p in botPlayer.getListOfPion():
            # kemungkinan koordinat move pion
            kemungkinan = p.possibleMove(state)
            # untuk semua kemungkinan dicek nilainya
            for k in kemungkinan:
                print("maximizing")
                print (k[0],k[1]) 
                prevBaris = p.getBaris()
                prevKolom = p.getKolom()
                prevKoor = (prevBaris,prevKolom)
                # pindahkan pion
                state.movePionMinimax(p,k,botPlayer)
                print(prevKoor[0],prevKoor[1])
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
                print("manimizing")
                print (k[0],k[1]) 
                prevBaris = p.getBaris()
                prevKolom = p.getKolom()
                prevKoor = (prevBaris,prevKolom)
                # pindahkan pion
                state.movePionMinimax(p,k,humanPlayer)
                print(prevKoor[0],prevKoor[1])
                # cek nilai minimax
                newNilai = minimax(state,(depth+1),True,botPlayer,humanPlayer)
                # kembalikan state ke state sebelumnya
                state.movePionMinimax(p,prevKoor,humanPlayer)
                # jika newNilai>bestNilai
                if (newNilai<bestNilai):
                    bestNilai=newNilai
        return bestNilai



            