
import pygame, sys
from pygame.locals import *
pygame.init()

class Engine:
    def __init__(self):
        self.Window = pygame.display.set_mode((500,400))
        self.Window.fill((255,255,255))
        self.fieldColorDark=(30,30,30)
        self.fieldColorWhite=(255,204,146)
        self.blackPawnColor=(0,255,0)
        self.whitePawnColor=(255,0,255)
        self.gameOver=False
        self.round=True
        self.pawnB_List = []
        self.pawnW_List = []
        self.Fields_list = []
        self.defaultField_list = []
        for x in range(3):
            self.pawnB_List.append(Pawn(self.blackPawnColor,25+(x*100),25))
            self.pawnW_List.append(Pawn(self.whitePawnColor,25+(x*100),225))
        x = 0
        y = 0
        for f in range(25):
            if f%2 == 0:
                self.Fields_list.append(Field(self.fieldColorWhite,0+50*x,0+50*y))
            else:
                self.defaultField_list.append(Field(self.fieldColorDark,0+50*x,0+50*y))
            if x==4:
                y=y+1
                x=0
                continue
            x=x+1
    def draw(self):
        for x in self.defaultField_list:
            x.draw(self.Window)
        for x in self.Fields_list:
            x.draw(self.Window)
        for x in self.pawnB_List:
            x.draw(self.Window)
        for x in self.pawnW_List:
            x.draw(self.Window)
    def start(self):
        clock = pygame.time.Clock()
        self.draw()
        tmp = True
        while True:
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.guit()
                    sys.exit()
           # Current = None
           # while self.gameOver!=True:
            #    if Current != None:
             #       Current=None
              #  if(round==True):
               #     Current=self.getBeatPawn()

            pygame.display.update()
    def Move(self,Pawn_f, x, y):
        Pawn_f.setPosition(x,y)


class Pawn:
    def __init__(self, color, pX, pY):
        self.rightP = None
        self.leftP = None
        self.rightPaway = None
        self.leftPaway = None
        self.color = color
        self.positionX = pX
        self.positionY = pY
        self.size = 20
    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.positionX, self.positionY), self.size)
    def setPosition(self, x, y):
        self.positionX = x
        print(self.positionX)
        self.positionY = y
        print(self.positionY)
    def getPosition(self):
        return (self.positionX, self.positionY)

class Field:
    def __init__(self, color, pX, pY):
        self.color = color
        self.positionX = pX
        self.positionY = pY 
        self.pawnPx = pX-25
        self.pawnPy = pY-25 
        self.size = 50
    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.positionX, self.positionY, self.size, self.size))


en = Engine()

en.start()
