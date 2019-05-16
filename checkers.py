
import pygame, sys
from pygame.locals import *
pygame.init()

class Engine:
    def __init__(self):
        self.Window = pygame.display.set_mode((500,400))
        self.Window.fill((255,255,255))
        self.fieldColorDark=(30,30,30)
        self.fieldColorWhite=(255,204,146)
        self.gameOver=False
    def draw(self):
        x = 0
        y = 0
        color = self.fieldColorWhite
        for loop in range(25):
            pygame.draw.rect(self.Window,color,(0+50*x+x*1,0+50*y+y*1,50,50))
            if color==self.fieldColorDark:
                color=self.fieldColorWhite
            else:
                color=self.fieldColorDark
            if x==4:
                y=y+1
                x=0
                continue
            x=x+1
    def start(self):
        self.draw()
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.guit()
                    sys.exit()
                pygame.display.update()


class Pawn:
    def __init__(self, color, position)
        self.color = color
        self.position = position
        self.size = 30
    def draw(self,window)
        pygame.draw.circle(window, self.color, self.position, self.size)
        

en = Engine()

en.start()
