from state import *
from konstanta import Infinity

def max(a, b):
    if(a > b):
        return a
    else:
        return b
def min(a, b):
    if(a < b):
        return a
    else:
        return b
def Minimax(state, depth, isMaximizing=True, time):
    bestMove = state.objectiveFunction()
    if(bestMove != None):
        return bestMove
    if(isMaximizing == True):
        bestValue = -Infinity
        for(i in range(0, board.BSize)):
            for (j in range(0, board.BSize)):
                if(state.isValidMove()):
                    possibleNextMove = minimax(board, depth+1, False)
                    bestNextMove = max(bestValue, )
