from state import *

def Minimax(state, depth, isMaximizing=True, time):
    bestMove = state
    if(bestMove != None):
        return bestMove
    #Buat player
    if(isMaximizing == True):
        for(i in range(0, board.BSize)):
            for (j in range(0, board.BSize)):
                if(state.isValidMove()):
                    possibleNextMove = Minimax(state, depth+1, False, time)
                    if(state.getNilai() > bestMove.getNilai()):
                        return state
                    else:
                        return bestMove
        # Buat player
        elif(isMaximizing == False):
            for (i in range(0, board.BSize)):
                for (j in range(0, board.BSize)):
                    if (state.isValidMove()):
                        possibleNextMove = Minimax(state, depth + 1, True, time)
                        if (state.getNilai() > bestMove.getNilai()):
                            return state
                        else:
                            return bestMove
