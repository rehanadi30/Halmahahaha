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
    global clickedButtons2
    global listofpion
    clickedButtons=set()
    clickedButtons2=set()
    listofpion = []

    def __init__(self, size,state):
        self.board = []
        self.BSize = size
        self.bidakTerpilih = None
        self.state = state

    # 

    def render(self, win,FPS):
        SQUARE_SIZE = WIDTH // self.BSize
        clock = pygame.time.Clock()
        run = True
        
        while run:

            if(self.state.isGameOver()):
                print("GAMEEEOVERR")
                run = False
            
            win.fill(YELLOW2)
            pygame.font.init()
            # print(pygame.display.get_surface().get_size())
            # screen = pygame.display.set_mode((640,480), FULLSCREEN)
            for baris in range(self.BSize):
                for kolom in range(baris%2, self.BSize, 2):
                    pygame.draw.rect(win, YELLOW, (baris*SQUARE_SIZE, kolom*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            
            if(self.state.getTurn().getColorPlayer()=='R'): 
                pygame.draw.rect(win, RED1, (0 ,720, 720,820))
            else:
                pygame.draw.rect(win, BLUE1, (0 ,720, 720,820))
            
            # print(mouse)
           
            # print(pygame.font.get_fonts())
            
            

                
            # if click[0] == 1:
            #     print(x,end=" ")
            #     print(y)
            #     if(a in clickedButtons):  
            #         clickedButtons.remove(a)
            #     else:
            #         clickedButtons.add(a)
            #     print(clickedButtons)

            #Buat border daerah goal
            
            self.move(win)
            self.undo(win)
            if(self.BSize==16):
                p1 = self.state.getPlayer1()
                p2 = self.state.getPlayer2()
                l1 = p1.getListOfPion()
                l2 = p2.getListOfPion()

                for i in range(len(l1)):
                    self.pieces16(win,RED1,l1[i].getKolom(),l1[i].getBaris())
                for i in range(len(l2)):
                    self.pieces16(win,BLUE1,l2[i].getKolom(),l2[i].getBaris())
                #Daerah BOT
                pygame.draw.line(win, RED1, (0, 225), (90, 225), 8)
                pygame.draw.line(win, RED1, (90, 225), (90, 180), 8)
                pygame.draw.line(win, RED1, (90, 180), (135, 180), 8)
                pygame.draw.line(win, RED1, (135, 180), (135, 135), 8)
                pygame.draw.line(win, RED1, (135, 135), (180, 135), 8)
                pygame.draw.line(win, RED1, (180, 135), (180, 90), 8)
                pygame.draw.line(win, RED1, (180, 90), (225, 90), 8)
                pygame.draw.line(win, RED1, (225, 90), (225, 0), 8)


                #Daerah User
                pygame.draw.line(win, BLUE1, (495, 720), (495, 630), 8)
                pygame.draw.line(win, BLUE1, (495, 630), (540, 630), 8)
                pygame.draw.line(win, BLUE1, (540, 630), (540, 585), 8)
                pygame.draw.line(win, BLUE1, (540, 585), (585, 585), 8)
                pygame.draw.line(win, BLUE1, (585, 585), (585, 540), 8)
                pygame.draw.line(win, BLUE1, (585, 540), (630, 540), 8)
                pygame.draw.line(win, BLUE1, (630, 540), (630, 495), 8)
                pygame.draw.line(win, BLUE1, (630, 495), (720, 495), 8)

            elif(self.BSize==10):
                p1 = self.state.getPlayer1()
                p2 = self.state.getPlayer2()
                l1 = p1.getListOfPion()
                l2 = p2.getListOfPion()

                for i in range(len(l1)):
                    # self.pieces10(win,RED,l1[i].getBaris(),l1[i].getKolom())
                    self.pieces10(win,RED1,l1[i].getKolom(),l1[i].getBaris())
                for i in range(len(l2)):
                    # self.pieces10(win,GREEN,l2[i].getBaris(),l2[i].getKolom())
                    self.pieces10(win,BLUE1,l2[i].getKolom(),l2[i].getBaris())
                # cb2 = clickedButtons2.copy()
                # for x in cb2:
                #     self.pieces102(win,WHITE,x[1],x[0])
                    
                # Daerah BOT
                pygame.draw.line(win, RED1, (0, 360), (72, 360), 8)
                pygame.draw.line(win, RED1, (72, 360), (72, 288), 8)
                pygame.draw.line(win, RED1, (72, 288), (144, 288), 8)
                pygame.draw.line(win, RED1, (144, 288), (144, 216), 8)
                pygame.draw.line(win, RED1, (144, 216), (216, 216), 8)
                pygame.draw.line(win, RED1, (216, 216), (216, 144), 8)
                pygame.draw.line(win, RED1, (216, 144), (288, 144), 8)
                pygame.draw.line(win, RED1, (288, 144), (288, 72), 8)
                pygame.draw.line(win, RED1, (288, 72), (360, 72), 8)
                pygame.draw.line(win, RED1, (360, 72), (360, 0), 8)

                # Daerah User
                pygame.draw.line(win, BLUE1, (360, 720), (360, 648), 8)
                pygame.draw.line(win, BLUE1, (360, 648), (432, 648), 8)
                pygame.draw.line(win, BLUE1, (432, 648), (432, 576), 8)
                pygame.draw.line(win, BLUE1, (432, 576), (504, 576), 8)
                pygame.draw.line(win, BLUE1, (504, 576), (504, 504), 8)
                pygame.draw.line(win, BLUE1, (504, 504), (576, 504), 8)
                pygame.draw.line(win, BLUE1, (576, 504), (576, 432), 8)
                pygame.draw.line(win, BLUE1, (576, 432), (648, 432), 8)
                pygame.draw.line(win, BLUE1, (648, 432), (648, 360), 8)
                pygame.draw.line(win, BLUE1, (648, 360), (720, 360), 8)

            elif(self.BSize==8):
                p1 = self.state.getPlayer1()
                p2 = self.state.getPlayer2()
                l1 = p1.getListOfPion()
                l2 = p2.getListOfPion()

                for i in range(len(l1)):
                    self.pieces8(win,RED1,l1[i].getKolom(),l1[i].getBaris())
                for i in range(len(l2)):
                    self.pieces8(win,BLUE1,l2[i].getKolom(),l2[i].getBaris())
                
                # Daerah BOT
                pygame.draw.line(win, RED1, (0, 360), (90, 360), 8)
                pygame.draw.line(win, RED1, (90, 360), (90, 270), 8)
                pygame.draw.line(win, RED1, (90, 270), (180, 270), 8)
                pygame.draw.line(win, RED1, (180, 270), (180, 180), 8)
                pygame.draw.line(win, RED1, (180, 180), (270, 180), 8)
                pygame.draw.line(win, RED1, (270, 180), (270, 90), 8)
                pygame.draw.line(win, RED1, (270, 90), (360, 90), 8)
                pygame.draw.line(win, RED1, (360, 90), (360, 0), 8)

                # Daerah User
                
                pygame.draw.line(win, BLUE1, (360, 720), (360, 630), 8)
                pygame.draw.line(win, BLUE1, (360, 630), (450, 630), 8)
                pygame.draw.line(win, BLUE1, (450, 630), (450, 540), 8)
                pygame.draw.line(win, BLUE1, (450, 540), (540, 540), 8)
                pygame.draw.line(win, BLUE1, (540, 540), (540, 450), 8)
                pygame.draw.line(win, BLUE1, (540, 450), (630, 450), 8)
                pygame.draw.line(win, BLUE1, (630, 450), (630, 360), 8)
                pygame.draw.line(win, BLUE1, (630, 360), (720, 360), 8)

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
                bar, kol = getKoordinat(pos, self.BSize)
                t =(bar,kol)
                print(t)
                # clickedButtons2.add(t)
                if t not in listofpion:
                    listofpion.append(t)
                print(listofpion)
                print("")

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
            pygame.draw.circle(win, WHITE, (x1,y1), 40) 
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
            pygame.draw.circle(win, WHITE, (x1,y1), 30) 
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
            pygame.draw.circle(win, WHITE, (x1,y1), 18) 
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
    def pieces102(self,win,color,x,y,action=None): 
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        # print(click)
        clicked = False
        x1 = int(x*72+36)
        y1 = int(y*72+36)
        a = (x,y)
    
        if(a in clickedButtons2):
            pygame.draw.circle(win, WHITE, (x1,y1), 30) 
        else:
            pygame.draw.circle(win, color, (x1,y1), 30)
        if x1-36 < mouse[0] < x1+36 and  y1-36 < mouse[1] < y1+36:
            if(y1<=720):  
                pygame.draw.circle(win, WHITE, (x1,y1), 30)
                if(clicked):
                    print(clicked)
                    
                if click[0] == 1:
                    print(x,end=" ")
                    print(y)
                    if(a in clickedButtons2):  
                        clickedButtons2.remove(a)
                    else:
                        clickedButtons2.add(a)
                    print("cb2", clickedButtons2)
    
    def move(self,win):
        mouse = pygame.mouse.get_pos()
        click1 = pygame.mouse.get_pressed()
    
        if 285 < mouse[0] < 285+150 and 745 < mouse[1] < 745+50:
            pygame.draw.rect(win, YELLOW, (285,745,150,50))
            if click1[0] == 1:
                print("yeyy move")
                x0 = listofpion.pop(0)
                x1 = x0[0]
                x2 = x0[1]
                # print(self.state.getTurn())
                player = self.state.getTurn()
                
                x = player.getPion(x1,x2)
                print("listofpion",listofpion)
                buang = listofpion.pop()
                y = listofpion[:]
                listofpion.clear()
                # clickedButtons2.clear()
                # clickedButtons.clear()
                print(x0)
                print(y)

                # a = self.state.getPlayer1().getListOfPion()
                # b = self.state.getPlayer2().getListOfPion()
                # for i in range(len(a)):
                #     print(a[i].getBaris(), a[i].getKolom())
                # print("")
                # for i in range(len(b)):
                #     print(b[i].getBaris(), b[i].getKolom())
                self.state.movePioninOneTurn(x,y)
                self.state.switchTurn()
                clickedButtons.clear()
                

                # a = self.state.getPlayer1().getListOfPion()
                # b = self.state.getPlayer2().getListOfPion()
                
                # print("")
                # for i in range(len(a)):
                #     print(a[i].getBaris(), a[i].getKolom())
                # print("")
                # for i in range(len(b)):
                #     print(b[i].getBaris(), b[i].getKolom())
        else:
            pygame.draw.rect(win, YELLOW2, (285,745,150,50))

        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = self.text_objects("MOVE!", smallText)
        textRect.center = ( (285+(150/2)), (745+(50/2)) )
        win.blit(textSurf, textRect)

    def undo(self,win):
        mouse = pygame.mouse.get_pos()
        click1 = pygame.mouse.get_pressed()
    
        if 500 < mouse[0] < 500+150 and 745 < mouse[1] < 745+50:
            pygame.draw.rect(win, YELLOW, (500,745,150,50))
            if click1[0] == 1:
                # print("yeyy move")
                # x0 = listofpion.pop(0)
                # x1 = x0[0]
                # x2 = x0[1]
                # # print(self.state.getTurn())
                # player = self.state.getTurn()
                
                # x = player.getPion(x1,x2)
                # buang = listofpion.pop()
                # y = listofpion[:]
                listofpion.clear()
                clickedButtons.clear()
                # clickedButtons2.clear()
                # clickedButtons.clear()
                print(listofpion)

                # a = self.state.getPlayer1().getListOfPion()
                # b = self.state.getPlayer2().getListOfPion()
                # for i in range(len(a)):
                #     print(a[i].getBaris(), a[i].getKolom())
                # print("")
                # for i in range(len(b)):
                #     print(b[i].getBaris(), b[i].getKolom())
                # self.state.movePioninOneTurn(x,y)
                # self.state.switchTurn()

                # a = self.state.getPlayer1().getListOfPion()
                # b = self.state.getPlayer2().getListOfPion()
                
                # print("")
                # for i in range(len(a)):
                #     print(a[i].getBaris(), a[i].getKolom())
                # print("")
                # for i in range(len(b)):
                #     print(b[i].getBaris(), b[i].getKolom())
        else:
            pygame.draw.rect(win, YELLOW2, (500,745,150,50))

        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = self.text_objects("UNDO!", smallText)
        textRect.center = ( (500+(150/2)), (745+(50/2)) )
        win.blit(textSurf, textRect)
        
        
