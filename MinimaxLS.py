from state import *

def MinimaxLS(state, depth, isMaximizing=True, time):
    bestMove = state

    # Buat kasus atomic (Daun gapunya anak)
    if (bestMove != None):
        return bestMove
    # Buat player
    if (isMaximizing == True):
        for (i in range(0, board.BSize)):
            for (j in range(0, board.BSize)):
                if (bestMove.isValidMove()):
                    possibleNextMove = MinimaxLS(state, depth + 1, False, time)
                    if (possibleNextMove.getNilai() > bestMove.getNilai()):
                        bestMove = possibleNextMove

    # Buat player
    elif (isMaximizing == False):
        for (i in range(0, board.BSize)):
            for (j in range(0, board.BSize)):
                if (bestMove.isValidMove()):
                    possibleNextMove = MinimaxLS(state, depth + 1, True, time)
                    if (possibleNextMove.getNilai() < bestMove.getNilai()):
                        bestMove = possibleNextMove

    return bestMove