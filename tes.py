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
    kemungkinan = p.possibleMove(state)
    
    # untuk semua kemungkinan dicek nilainya
    for k in kemungkinan: 
        print("---------")
        print(k[0],k[1])
        print("---------")
        