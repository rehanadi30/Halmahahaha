from Player import *
from state import *
# cobacoba
playerRed = Player(8, 'R', 2) #pembuatan player merah
playerGreen = Player(8, 'G', 0) #pembuatan player hijau
state = State(playerRed, playerGreen,8) #pembuatan state
for p in playerGreen.getListOfPion():
    print("============")
    print(p.getBaris(),p.getKolom())
    # kemungkinan koordinat move pion
    kemungkinan = p.possibleMoveLS(state)
    print("---------")
    print(kemungkinan[0],kemungkinan[1])
    print("---------")
    
        
        