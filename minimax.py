from state import *

def Minimax(state, depth, isMaximizing, time):
    bestMove = state

    #Buat kasus atomic (Daun gapunya anak)
    if(bestMove != None):
        return bestMove
    #Buat player
    if(isMaximizing == True):
        for kemungkinan in bestMove:
            possibleNextMove = Minimax(kemungkinan, depth + 1, False, time)
            if(possibleNextMove.getNilai() > bestMove.getNilai()):
                bestMove = possibleNextMove
            else:
                break

    # Buat player
    elif(isMaximizing == False):
        for gerakan in possible:
            possibleNextMove = Minimax(gerakan, depth + 1, True, time)
            if (possibleNextMove.getNilai() < bestMove.getNilai()):
                bestMove = possibleNextMove
            else:
                break

    return bestMove
