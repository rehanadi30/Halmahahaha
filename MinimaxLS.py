from state import *

def MinimaxLS(state, depth, isMaximizing=True, time):
    bestMove = state
    kemungkinanLangkah = LocalSearch(state, state.board.size)

    #Buat kasus atomic (Daun gapunya anak)
    if(bestMove.isGameOver()):
        return bestMove
    #Buat maximizing agent
    if(isMaximizing == True):
        if(bestMove.isValidMove()):
            possibleNextMove = MinimaxLS(state, depth+1, False, time)
            if(possibleNextMove.getNilai() > bestMove.getNilai()):
                bestMove = possibleNextMove

    # Buat minimizing agent
    elif(isMaximizing == False):
        if (bestMove.isValidMove()):
            possibleNextMove = MinimaxLS(state, depth + 1, True, time)
            if (possibleNextMove.getNilai() < bestMove.getNilai()):
                bestMove = possibleNextMove

    return bestMove

def LocalSearch(state, n):
    pass
