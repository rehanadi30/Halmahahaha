import pygame
from konstanta import *
from Player import *


def getKoordinat(pos, size):
    x, y = pos
    bar = y//(WIDTH//size)
    kol = x//(WIDTH//size)
    return bar, kol

class Board:
    global clickedButtons
    global listofpion
    clickedButtons=set()
    listofpion = []

    def __init__(self, size):
        self.board = []
        self.BSize = size
        self.bidakTerpilih = None

    # 

    def render(self, win,FPS):
        SQUARE_SIZE = WIDTH // self.BSize
        clock = pygame.time.Clock()
        run = True
        
        while run:
            win.fill(YELLOW2)
            pygame.font.init()
            # print(pygame.display.get_surface().get_size())
            # screen = pygame.display.set_mode((640,480), FULLSCREEN)
            for baris in range(self.BSize):
                for kolom in range(baris%2, self.BSize, 2):
                    pygame.draw.rect(win, YELLOW, (baris*SQUARE_SIZE, kolom*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            
            pygame.draw.rect(win, WHITE, (0 ,720, 720,820))
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            # print(mouse)
            clicked = False
            # print(pygame.font.get_fonts())
        
            if 285 < mouse[0] < 285+150 and 745 < mouse[1] < 745+50:
                pygame.draw.rect(win, YELLOW, (285,745,150,50))
            else:
                pygame.draw.rect(win, YELLOW2, (285,745,150,50))

            smallText = pygame.font.Font("freesansbold.ttf",20)
            textSurf, textRect = self.text_objects("MOVE!", smallText)
            textRect.center = ( (285+(150/2)), (745+(50/2)) )
            win.blit(textSurf, textRect)
                
                
            # if click[0] == 1:
            #     print(x,end=" ")
            #     print(y)
            #     if(a in clickedButtons):  
            #         clickedButtons.remove(a)
            #     else:
            #         clickedButtons.add(a)
            #     print(clickedButtons)

            #Buat border daerah goal
            if(self.BSize==16):
                p1 = Player(16,"R",1)
                p2 = Player(16,"G",2)
                l1 = p1.getListOfPion()
                l2 = p2.getListOfPion()

                for i in range(len(l1)):
                    self.pieces16(win,BLUE,l1[i].getBaris(),l1[i].getKolom())
                for i in range(len(l2)):
                    self.pieces16(win,GREEN,l2[i].getBaris(),l2[i].getKolom())
                #Daerah BOT
                pygame.draw.line(win, RED, (0, 225), (90, 225), 8)
                pygame.draw.line(win, RED, (90, 225), (90, 180), 8)
                pygame.draw.line(win, RED, (90, 180), (135, 180), 8)
                pygame.draw.line(win, RED, (135, 180), (135, 135), 8)
                pygame.draw.line(win, RED, (135, 135), (180, 135), 8)
                pygame.draw.line(win, RED, (180, 135), (180, 90), 8)
                pygame.draw.line(win, RED, (180, 90), (225, 90), 8)
                pygame.draw.line(win, RED, (225, 90), (225, 0), 8)


                #Daerah User
                pygame.draw.line(win, GREEN, (495, 720), (495, 630), 8)
                pygame.draw.line(win, GREEN, (495, 630), (540, 630), 8)
                pygame.draw.line(win, GREEN, (540, 630), (540, 585), 8)
                pygame.draw.line(win, GREEN, (540, 585), (585, 585), 8)
                pygame.draw.line(win, GREEN, (585, 585), (585, 540), 8)
                pygame.draw.line(win, GREEN, (585, 540), (630, 540), 8)
                pygame.draw.line(win, GREEN, (630, 540), (630, 495), 8)
                pygame.draw.line(win, GREEN, (630, 495), (720, 495), 8)

            elif(self.BSize==10):
                p1 = Player(10,"R",1)
                p2 = Player(10,"G",2)
                l1 = p1.getListOfPion()
                l2 = p2.getListOfPion()

                for i in range(len(l1)):
                    self.pieces10(win,RED,l1[i].getBaris(),l1[i].getKolom())
                for i in range(len(l2)):
                    self.pieces10(win,GREEN,l2[i].getBaris(),l2[i].getKolom())
                # Daerah BOT
                pygame.draw.line(win, RED, (0, 360), (72, 360), 8)
                pygame.draw.line(win, RED, (72, 360), (72, 288), 8)
                pygame.draw.line(win, RED, (72, 288), (144, 288), 8)
                pygame.draw.line(win, RED, (144, 288), (144, 216), 8)
                pygame.draw.line(win, RED, (144, 216), (216, 216), 8)
                pygame.draw.line(win, RED, (216, 216), (216, 144), 8)
                pygame.draw.line(win, RED, (216, 144), (288, 144), 8)
                pygame.draw.line(win, RED, (288, 144), (288, 72), 8)
                pygame.draw.line(win, RED, (288, 72), (360, 72), 8)
                pygame.draw.line(win, RED, (360, 72), (360, 0), 8)

                # Daerah User
                pygame.draw.line(win, GREEN, (360, 720), (360, 648), 8)
                pygame.draw.line(win, GREEN, (360, 648), (432, 648), 8)
                pygame.draw.line(win, GREEN, (432, 648), (432, 576), 8)
                pygame.draw.line(win, GREEN, (432, 576), (504, 576), 8)
                pygame.draw.line(win, GREEN, (504, 576), (504, 504), 8)
                pygame.draw.line(win, GREEN, (504, 504), (576, 504), 8)
                pygame.draw.line(win, GREEN, (576, 504), (576, 432), 8)
                pygame.draw.line(win, GREEN, (576, 432), (648, 432), 8)
                pygame.draw.line(win, GREEN, (648, 432), (648, 360), 8)
                pygame.draw.line(win, GREEN, (648, 360), (720, 360), 8)

            elif(self.BSize==8):
                p1 = Player(8,"R",1)
                p2 = Player(8,"G",2)
                l1 = p1.getListOfPion()
                l2 = p2.getListOfPion()

                for i in range(len(l1)):
                    self.pieces8(win,RED,l1[i].getBaris(),l1[i].getKolom())
                for i in range(len(l2)):
                    self.pieces8(win,BLUE,l2[i].getBaris(),l2[i].getKolom())
                
                # Daerah BOT
                pygame.draw.line(win, RED, (0, 360), (90, 360), 8)
                pygame.draw.line(win, RED, (90, 360), (90, 270), 8)
                pygame.draw.line(win, RED, (90, 270), (180, 270), 8)
                pygame.draw.line(win, RED, (180, 270), (180, 180), 8)
                pygame.draw.line(win, RED, (180, 180), (270, 180), 8)
                pygame.draw.line(win, RED, (270, 180), (270, 90), 8)
                pygame.draw.line(win, RED, (270, 90), (360, 90), 8)
                pygame.draw.line(win, RED, (360, 90), (360, 0), 8)

                # Daerah User
                
                pygame.draw.line(win, RED, (360, 720), (360, 630), 8)
                pygame.draw.line(win, RED, (360, 630), (450, 630), 8)
                pygame.draw.line(win, RED, (450, 630), (450, 540), 8)
                pygame.draw.line(win, RED, (450, 540), (540, 540), 8)
                pygame.draw.line(win, RED, (540, 540), (540, 450), 8)
                pygame.draw.line(win, RED, (540, 450), (630, 450), 8)
                pygame.draw.line(win, RED, (630, 450), (630, 360), 8)
                pygame.draw.line(win, RED, (630, 360), (720, 360), 8)

            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    run = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    bar, kol = getKoordinat(pos, self.BSize)

            
            press = pygame.mouse.get_pressed()
            if(press[0]==1):
                pos = pygame.mouse.get_pos()
                # print(pos)
                bar, kol = getKoordinat(pos, 10)
                t =(bar,kol)
                if t not in listofpion:
                    listofpion.append(t)
                print(listofpion)

                # print(bar, kol)
            

            pygame.display.update()
            clock.tick(FPS)

    def text_objects(self,text, font):
        textSurface = font.render(text, True, BLACK)
        return textSurface, textSurface.get_rect()
    def pieces8(self,win,color,x,y,action=None): 
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        # print(click)
        clicked = False
        x1 = int(x*90+45)
        y1 = int(y*90+45)
        a = (x,y)
    
        if(a in clickedButtons):
            pygame.draw.circle(win, BLACK, (x1,y1), 40) 
        else:
            pygame.draw.circle(win, color, (x1,y1), 40)
        if x1-45 < mouse[0] < x1+45 and  y1-45 < mouse[1] < y1+45:
            pygame.draw.circle(win, WHITE, (x1,y1), 40)
            if(clicked):
                print(clicked)
                
            if click[0] == 1:
                print(x,end=" ")
                print(y)
                if(a in clickedButtons):  
                    clickedButtons.remove(a)
                else:
                    clickedButtons.add(a)
                print(clickedButtons)

    def pieces10(self,win,color,x,y,action=None): 
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        # print(click)
        clicked = False
        x1 = int(x*72+36)
        y1 = int(y*72+36)
        a = (x,y)
    
        if(a in clickedButtons):
            pygame.draw.circle(win, BLACK, (x1,y1), 30) 
        else:
            pygame.draw.circle(win, color, (x1,y1), 30)
        if x1-36 < mouse[0] < x1+36 and  y1-36 < mouse[1] < y1+36:
            pygame.draw.circle(win, WHITE, (x1,y1), 30)
            if(clicked):
                print(clicked)
                
            if click[0] == 1:
                print(x,end=" ")
                print(y)
                if(a in clickedButtons):  
                    clickedButtons.remove(a)
                else:
                    clickedButtons.add(a)
                print(clickedButtons)
            
    def pieces16(self,win,color,x,y,action=None): 
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        # print(click)
        clicked = False
        x1 = int(x*45+23)
        y1 = int(y*45+23)
        a = (x,y)
    
        if(a in clickedButtons):
            pygame.draw.circle(win, BLACK, (x1,y1), 18) 
        else:
            pygame.draw.circle(win, color, (x1,y1), 18)
        if x1-23 < mouse[0] < x1+23 and  y1-23 < mouse[1] < y1+23:
            pygame.draw.circle(win, WHITE, (x1,y1), 18)
            if(clicked):
                print(clicked)
                
            if click[0] == 1:
                print(x,end=" ")
                print(y)
                if(a in clickedButtons):  
                    clickedButtons.remove(a)
                else:
                    clickedButtons.add(a)
                print(clickedButtons)
     