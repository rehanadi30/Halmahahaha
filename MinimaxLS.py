from state import *

def MinimaxLS(state, depth, isMaximizing=True, time):
    bestMove = state
    kemungkinanLangkah = LocalSearch(state, depth)

    #Buat kasus atomic (Daun gapunya anak)
    if(bestMove != None):
        return bestMove
    #Buat player
    if(isMaximizing == True):
        if(bestMove.isValidMove()):
            possibleNextMove = MinimaxLS(state, depth+1, False, time)
            if(possibleNextMove.getNilai() > bestMove.getNilai()):
                bestMove = possibleNextMove

    # Buat player
    elif(isMaximizing == False):
        if (bestMove.isValidMove()):
            possibleNextMove = MinimaxLS(state, depth + 1, True, time)
            if (possibleNextMove.getNilai() < bestMove.getNilai()):
                bestMove = possibleNextMove

    return bestMove

def LocalSearch(state, n):
    pass
