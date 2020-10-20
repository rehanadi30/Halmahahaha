from state import *

def Minimax(state, depth, isMaximizing, time):
    bestMove = state

    #Buat kasus atomic (Daun gapunya anak karena udah menang)
    if(bestMove.isGameOver()):
        return bestMove

    #Buat maximizing agent
    if(isMaximizing == True):
        for kemungkinan in bestMove.board.pion.possibleMove():
            possibleNextMove = Minimax(kemungkinan, depth + 1, False, time)
            if(possibleNextMove.getNilai() > bestMove.getNilai()):
                bestMove = possibleNextMove
            else:
                break
                #Pruning. Kalo dia udah kalah langsung ambil best move yang udah menang sejak awal

    # Buat minimizing agent
    elif(isMaximizing == False):
        for kemungkinan in bestMove.board.pion.possibleMove():
            possibleNextMove = Minimax(kemungkinan, depth + 1, True, time)
            if (possibleNextMove.getNilai() < bestMove.getNilai()):
                bestMove = possibleNextMove
            else:
                break

    return bestMove
