
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
        #INIT 
        self.Fields_list[0].leftT = self.Fields_list[3]
        self.Fields_list[0].leftB = None
        self.Fields_list[0].leftTaway = self.Fields_list[6]
        self.Fields_list[0].leftBaway = None
        self.Fields_list[0].rightB = None
        self.Fields_list[0].rightT = None
        self.Fields_list[0].rightBaway = None
        self.Fields_list[0].rightTaway = None
        self.Fields_list[0].currentPawn = self.pawnW_List[0]

        self.Fields_list[1].leftT = self.Fields_list[4]
        self.Fields_list[1].leftB = None
        self.Fields_list[1].leftTaway = self.Fields_list[7]
        self.Fields_list[1].leftBaway = None
        self.Fields_list[1].rightB = None
        self.Fields_list[1].rightT = self.Fields_list[3]
        self.Fields_list[1].rightBaway = None
        self.Fields_list[1].rightTaway = self.Fields_list[5]
        self.Fields_list[1].currentPawn = self.pawnW_List[1]

        self.Fields_list[2].leftT = None
        self.Fields_list[2].leftB = None
        self.Fields_list[2].leftTaway = None
        self.Fields_list[2].leftBaway = None
        self.Fields_list[2].rightB = None
        self.Fields_list[2].rightT = self.Fields_list[4]
        self.Fields_list[2].rightBaway = None
        self.Fields_list[2].rightTaway = self.Fields_list[6]
        self.Fields_list[2].currentPawn = self.pawnW_List[2]

        self.Fields_list[3].leftT = self.Fields_list[6]
        self.Fields_list[3].leftB = self.Fields_list[1]
        self.Fields_list[3].leftTaway = self.Fields_list[9]
        self.Fields_list[3].leftBaway = None
        self.Fields_list[3].rightB = self.Fields_list[0]
        self.Fields_list[3].rightT = self.Fields_list[5]
        self.Fields_list[3].rightBaway = None
        self.Fields_list[3].rightTaway = None

        self.Fields_list[4].leftT = self.Fields_list[7]
        self.Fields_list[4].leftB = self.Fields_list[2]
        self.Fields_list[4].leftTaway = None
        self.Fields_list[4].leftBaway = None
        self.Fields_list[4].rightB = self.Fields_list[1]
        self.Fields_list[4].rightT = self.Fields_list[6]
        self.Fields_list[4].rightBaway = None
        self.Fields_list[4].rightTaway = self.Fields_list[8]

        self.Fields_list[5].leftT = self.Fields_list[8]
        self.Fields_list[5].leftB = self.Fields_list[3]
        self.Fields_list[5].leftTaway = self.Fields_list[11]
        self.Fields_list[5].leftBaway = self.Fields_list[1]
        self.Fields_list[5].rightB = None
        self.Fields_list[5].rightT = None
        self.Fields_list[5].rightBaway = None
        self.Fields_list[5].rightTaway = None

        self.Fields_list[6].leftT = self.Fields_list[9]
        self.Fields_list[6].leftB = self.Fields_list[4]
        self.Fields_list[6].leftTaway = self.Fields_list[12]
        self.Fields_list[6].leftBaway = self.Fields_list[2]
        self.Fields_list[6].rightB = self.Fields_list[5]
        self.Fields_list[6].rightT = self.Fields_list[8]
        self.Fields_list[6].rightBaway = self.Fields_list[0]
        self.Fields_list[6].rightTaway = self.Fields_list[10]

        self.Fields_list[7].leftT = None
        self.Fields_list[7].leftB = None
        self.Fields_list[7].leftTaway = None
        self.Fields_list[7].leftBaway = None
        self.Fields_list[7].rightB = self.Fields_list[4]
        self.Fields_list[7].rightT = self.Fields_list[9]
        self.Fields_list[7].rightBaway = self.Fields_list[1]
        self.Fields_list[7].rightTaway = self.Fields_list[11]
        
        self.Fields_list[8].leftT = self.Fields_list[11]
        self.Fields_list[8].leftB = self.Fields_list[6]
        self.Fields_list[8].leftTaway = None
        self.Fields_list[8].leftBaway = self.Fields_list[4]
        self.Fields_list[8].rightB = self.Fields_list[5]
        self.Fields_list[8].rightT = self.Fields_list[10]
        self.Fields_list[8].rightBaway = None
        self.Fields_list[8].rightTaway = None

        self.Fields_list[9].leftT = self.Fields_list[12]
        self.Fields_list[9].leftB = self.Fields_list[7]
        self.Fields_list[9].leftTaway = None
        self.Fields_list[9].leftBaway = None
        self.Fields_list[9].rightB = self.Fields_list[6]
        self.Fields_list[9].rightT = self.Fields_list[11]
        self.Fields_list[9].rightBaway = self.Fields_list[3]
        self.Fields_list[9].rightTaway = None

        self.Fields_list[10].leftT = None
        self.Fields_list[10].leftB = self.Fields_list[8]
        self.Fields_list[10].leftTaway = None
        self.Fields_list[10].leftBaway = self.Fields_list[6]
        self.Fields_list[10].rightB = None
        self.Fields_list[10].rightT = None
        self.Fields_list[10].rightBaway = None
        self.Fields_list[10].rightTaway = None
        self.Fields_list[10].currentPawn = self.pawnB_List[2]

        self.Fields_list[11].leftT = None
        self.Fields_list[11].leftB = self.Fields_list[9]
        self.Fields_list[11].leftTaway = None
        self.Fields_list[11].leftBaway = self.Fields_list[7]
        self.Fields_list[11].rightB = self.Fields_list[8]
        self.Fields_list[11].rightT = None
        self.Fields_list[11].rightBaway = self.Fields_list[5]
        self.Fields_list[11].rightTaway = None
        self.Fields_list[11].currentPawn = self.pawnB_List[1]

        self.Fields_list[12].leftT = None
        self.Fields_list[12].leftB = None
        self.Fields_list[12].leftTaway = None
        self.Fields_list[12].leftBaway = None
        self.Fields_list[12].rightB = self.Fields_list[9]
        self.Fields_list[12].rightT = None
        self.Fields_list[12].rightBaway = self.Fields_list[6]
        self.Fields_list[12].rightTaway = None
        self.Fields_list[12].currentPawn = self.pawnB_List[0]

        self.move = None
        self.Current = None
        self.tmp_fields = []

    def draw(self):
        for x in self.defaultField_list:
            x.draw(self.Window)
        for x in self.Fields_list:
            x.draw(self.Window)
        for x in self.Fields_list:
            if x.currentPawn != None:
                x.currentPawn.draw(self.Window)
    def start(self):
        clock = pygame.time.Clock()
        self.update()
        self.draw()
        while True:
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.guit()
                    sys.exit()
            pygame.display.update()
            if self.gameOver!=True:
                if self.Current != None:
                    self.Current=None
                if self.round==True:
                    self.Current=self.getBeatPawn(0)
                else:
                    self.Current=self.getBeatPawn(1)
                if self.Current != None:
                    self.Move()
                    if self.round == True:
                        self.round = False
                    else:
                        self.round = True
                else:
                    if self.round==True:
                        self.Current=self.getMovePawn(0)
                    else:
                        self.Current=self.getMovePawn(1)
                    if self.Current != None:
                        self.Move()
                        if self.round == True:
                            self.round = False
                        else:
                            self.round = True
                    else:
                        self.gameOver = True
            
    def Move(self):
        self.move.currentPawn = self.Current.currentPawn
        self.Current.currentPawn = None
        self.update()
        self.draw()
        pygame.time.wait(1000)
    def update(self):
        for x in self.Fields_list:
            x.update()   
    def getMovePawn(self, wb):
        if wb == 0:
            for i in range(3):
                for x in range(13):
                    if self.Fields_list[x].currentPawn == self.pawnW_List[i]:
                        field = self.Fields_list[x]
                        if field.leftT != None:
                            if field.leftT.currentPawn == None:
                                self.move = field.leftT
                                return field
                        if field.rightT != None:
                            if field.rightT.currentPawn == None:
                                self.move = field.rightT
                                return field
        else:
            for i in range(3):
                for x in range(13):
                    if self.Fields_list[x].currentPawn == self.pawnB_List[i]:
                        field = self.Fields_list[x]
                        if field.leftB != None:
                            if field.leftB.currentPawn == None:
                                self.move = field.leftB
                                return field
                        if field.rightB != None:
                            if field.rightB.currentPawn == None:
                                self.move = field.rightB
                                return field
        return None
    def getBeatPawn(self, wb):
        if wb == 0:
            self.tmp_fields = self.pawnW_List
        else:
            self.tmp_fields = self.pawnB_List
        for i in range(3):
            for x in range(13):
                if self.Fields_list[x].currentPawn == self.tmp_fields[i]:
                    field = self.Fields_list[x]
                    if field.currentPawn.color == (255,0,255):
                        if field.leftT != None:
                            if field.leftT.currentPawn != None:
                                if field.leftT.currentPawn.color == (0,255,0):
                                    if field.leftTaway.currentPawn == None:
                                        self.move = field.leftTaway
                                        field.leftT.currentPawn = None
                                        return field
                        if field.rightT != None:
                            if field.rightT.currentPawn != None:
                                if field.rightT.currentPawn.color == (0,255,0):
                                    if field.rightTaway.currentPawn == None:
                                        self.move = field.rightTaway
                                        field.rightT.currentPawn = None
                                        return field
                    if field.currentPawn.color == (0,255,0):
                        if field.leftB != None:
                            if field.leftB.currentPawn != None:
                                if field.leftB.currentPawn.color == (255,0,255):
                                    if field.leftBaway.currentPawn == None:
                                        self.move = field.leftBaway
                                        field.leftB.currentPawn = None
                                        return field
                        if field.rightB != None:
                            if field.rightB.currentPawn != None:
                                if field.rightB.currentPawn.color == (255,0,255):
                                    if field.rightBaway.currentPawn == None:
                                        self.move = field.rightBaway
                                        field.rightB.currentPawn = None
                                        return field
        return None
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
        self.positionY = y
    def getPosition(self):
        return (self.positionX, self.positionY)

class Field:
    def __init__(self, color, pX, pY):
        self.rightT = None
        self.leftT = None
        self.rightTaway = None
        self.leftTaway = None
        self.rightB = None
        self.leftB = None
        self.rightBaway = None
        self.leftBaway = None

        self.currentPawn = None

        self.color = color
        self.positionX = pX
        self.positionY = pY 
        self.pawnPx = pX+25
        self.pawnPy = pY+25 
        self.size = 50
    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.positionX, self.positionY, self.size, self.size))
    def update(self):
        if self.currentPawn != None:
            self.currentPawn.positionX = self.pawnPx
            self.currentPawn.positionY = self.pawnPy


en = Engine()

en.start()
