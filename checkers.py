
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
        self.Pawn1B=Pawn(self.blackPawnColor,25,25)
        self.Pawn2B=Pawn(self.blackPawnColor,125,25)
        self.Pawn3B=Pawn(self.blackPawnColor,225,25)
        self.pawnB_List = [self.Pawn1B, self.Pawn2B, self.Pawn3B]
        self.Pawn1W=Pawn(self.whitePawnColor,25,225)
        self.Pawn2W=Pawn(self.whitePawnColor,125,225)
        self.Pawn3W=Pawn(self.whitePawnColor,225,225)
        self.pawnW_List = [self.Pawn1W, self.Pawn2W, self.Pawn3W]
    def draw(self):
        x = 0
        y = 0
        color = self.fieldColorWhite
        for loop in range(25):
            pygame.draw.rect(self.Window,color,(0+50*x,0+50*y,50,50))
            if color==self.fieldColorDark:
                color=self.fieldColorWhite
            else:
                color=self.fieldColorDark
            if x==4:
                y=y+1
                x=0
                continue
            x=x+1
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
            if tmp==True:
                self.Move(self.Pawn1B,125,125)
                pygame.display.update(self.Pawn1B)
                tmp=False
    def Move(self,Pawn_f, x, y):
        Pawn_f.setPosition(x,y)


class Pawn:
    def __init__(self, color, pX, pY):
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
        

en = Engine()

en.start()
