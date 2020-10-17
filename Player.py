class Player:
    def __init__(self, sizePapan, color):
        self.size = sizePapan  # ukuran papan
        self.color = color  # warna pemain

        # list of pion yang dimiliki player jika ukuran papan 8
        pionRed8 = {
            "1": (0, 0), "2": (0, 1), "3": (0, 2), "4": (0, 3), "5": (1, 0),
            "6": (1, 1), "7": (1, 2), "8": (2, 0), "9": (2, 1), "10": (3, 0)
        }
        pionGreen8 = {
            "1": (7, 7), "2": (7, 6), "3": (7, 5), "4": (7, 4), "5": (6, 7),
            "6": (6, 6), "7": (6, 5), "8": (5, 7), "9": (5, 6), "10": (4, 7)
        }

        # list of pion yang dimiliki player jika ukuran papan 10
        pionRed10 = {
            "1": (0, 0), "2": (0, 1), "3": (0, 2), "4": (0, 3), "5": (0, 4), "6": (1, 0), "7": (1, 1),
            "8": (1, 2), "9": (1, 3), "10": (2, 0), "11": (2, 1), "12": (2, 2), "13": (3, 0), "14": (3, 1), "15": (4, 0)
        }
        pionGreen10 = {
            "1": (9, 9), "2": (9, 8), "3": (9, 7), "4": (9, 6), "5": (9, 5), "6": (8, 9), "7": (8, 8),
            "8": (8, 7), "9": (8, 6), "10": (7, 9), "11": (7, 8), "12": (7, 7), "13": (6, 9), "14": (6, 8), "15": (5, 9)
        }

        # list of pion yang dimiliki player jika ukuran papan 16
        pionRed16 = {
            "1": (0, 0), "2": (0, 1), "3": (0, 2), "4": (0, 3), "5": (0, 4), "6": (1, 0), "7": (1, 1), "8": (1, 2), "9": (1, 3), "10": (1, 4),
            "11": (2, 0), "12": (2, 1), "13": (2, 2), "14": (2, 3), "15": (3, 0), "16": (3, 1), "17": (3, 2), "18": (4, 0), "19": (4, 1)
        }
        pionGreen16 = {
            "1": (15, 15), "2": (15, 14), "3": (15, 13), "4": (15, 12), "5": (15, 11), "6": (14, 15), "7": (14, 14), "8": (14, 13), "9": (14, 12), "10": (14, 11),
            "11": (13, 15), "12": (13, 14), "13": (13, 13), "14": (13, 12), "15": (12, 15), "16": (12, 14), "17": (12, 13), "18": (11, 15), "11": (11, 14)
        }

        # list of posisi goal yang harus dituju untuk size papan 8
        goalRed8 = [(7, 7), (7, 6), (7, 5), (7, 4), (6, 7),
                    (6, 6), (6, 5), (5, 7), (5, 6), (4, 7)]
        goalGreen8 = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0),
                      (1, 1), (1, 2), (2, 0), (2, 1), (3, 0)]

        # list of posisi goal yang harus dituju untuk size papan 10
        goalRed10 = [(9, 9), (9, 8), (9, 7), (9, 6), (9, 5), (8, 9), (8, 8),
                     (8, 7), (8, 6), (7, 9), (7, 8), (7, 7), (6, 9), (6, 8), (5, 9)]
        goalGreen10 = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1),
                       (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (4, 0)]

        # list of posisi goal yang harus dituju untuk size papan 16
        goalRed16 = [(15, 15), (15, 14), (15, 13), (15, 12), (15, 11), (14, 15), (14, 14), (14, 13), (14, 12), (14, 11),
                     (13, 15), (13, 14), (13, 13), (13, 12), (12, 15), (12, 14), (12, 13), (11, 15), (11, 14)]
        goalGreen16 = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4),
                       (2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (4, 0), (4, 1)]

        if(self.size == 8):
            # jika ukuran papan 8x8
            if(self.color == 'R'):
                # jika warna player Red
                self.listOfPion = pionRed8  # list pion yang dimiliki pemain
                self.listOfGoal = goalRed8  # set posisi goal yang harus dituju pemain
            elif(self.color == 'G'):
                # jika warna player Green
                self.listOfPion = pionGreen8
                self.listOfGoal = goalGreen8
        elif(self.size == 10):
            # jika ukuran papan 10x10
            if(self.color == 'R'):
                # jika warna player Red
                self.listOfPion = pionRed10
                self.listOfGoal = goalRed10
            elif(self.color == 'G'):
                # jika warna player Green
                self.listOfPion = pionGreen10
                self.listOfGoal = goalGreen10
        elif(self.size == 16):
            # jika ukuran papan 16x16
            if(self.color == 'R'):
                # jika warna player Red
                self.listOfPion = pionRed16
                self.listOfGoal = goalRed16
            elif(self.color == 'G'):
                # jika warna player Green
                self.listOfPion = pionGreen16
                self.listOfGoal = goalGreen16


A = Player(8, 'R')
