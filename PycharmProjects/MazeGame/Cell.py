import pygame
import random


class Cell:
    # default size of box(20,20)

    visited = False
    value = random.randint(0, 10000)

    size = 28
    nThick = True
    sThick = True
    wThick = True
    eThick = True
    player = False

    red = (200, 0, 0)
    blue = (0, 0, 200)
    yellow = (255, 255, 0)
    black = (0, 0, 0)
    white = (255, 255, 255)
    color = blue
    nw = (0, 0)
    ne = (0, 0)
    se = (0, 0)
    sw = (0, 0)

    def __init__(self):
        self.visited = False
        self.player = False

        self.eThick = True
        self.wThick = True
        self.nThick = True
        self.sThick = True
        self.value = random.randint(0, 10000)

    def draw(self, sur, x):
        self.nw = x
        self.ne = (x[0] + self.size, x[1])
        self.se = (x[0] + self.size, x[1] + self.size)
        self.sw = (x[0], x[1] + self.size)

        north = pygame.draw.line
        south = pygame.draw.line
        east = pygame.draw.line
        west = pygame.draw.line
        if(self.nThick):
            north(sur, self.color, self.nw, self.ne, 3)
        if(self.sThick):
            south(sur, self.color, self.sw, self.se, 3)
        if(self.wThick):
            west(sur, self.color, self.nw, self.sw, 3)
        if(self.eThick):
            east(sur, self.color, self.ne, self.se, 3)
        if(self.player):
            pygame.draw.circle(sur, self.yellow, \
                               ( int(self.nw[0] + self.getSize()/2), int(self.nw[1] + self.getSize()/2)),\
                               int(self.getSize()/4), 0)



    def destroy(self, wall):
        #Destroy which wall?

        if(wall == 'n'):
            self.nThick = False
        elif(wall == 's'):
            self.sThick = False
        elif(wall == 'w'):
            self.wThick = False
        elif(wall == 'e'):
            self.eThick = False

        #self.redraw(sur)
        # print("it worked")

    def allBlack(self,sur):
        self.north(sur, self.black, self.nw, self.ne, self.nThick)
        self.south(sur, self.black, self.sw, self.se, self.sThick)
        self.west(sur, self.black, self.nw, self.sw, self.wThick)
        self.east(sur, self.black, self.ne, self.se, self.eThick)

    def redraw(self, sur):
        north = pygame.draw.line
        south = pygame.draw.line
        east = pygame.draw.line
        west = pygame.draw.line

        if(self.nThick):
            north(sur, self.color, self.nw, self.ne, 3)
        if(self.sThick):
            south(sur, self.color, self.sw, self.se, 3)
        if(self.wThick):
            west(sur, self.color, self.nw, self.sw, 3)
        if(self.eThick):
            east(sur, self.color, self.ne, self.se, 3)
        if(self.player):
            pygame.draw.circle(sur, self.yellow, \
                                   ( int(self.nw[0] + self.getSize()/2), int(self.nw[1] + self.getSize()/2)),\
                                   int(self.getSize()/4), 0)
        else:
            pygame.draw.circle(sur, self.black, \
                             ( int(self.nw[0] + self.getSize()/2), int(self.nw[1] + self.getSize()/2)),\
                            int(self.getSize()/4), 0)



    def getSize(self):
        return self.size

    def getValue(self):
        return self.value

    def didVisit(self):
        return self.visited

    def setVisit(self, bool):
        self.visited = bool

    def getX(self):
        return self.nw[0]

    def getY(self):
        return self.nw[1]

    def setColor(self, color):
        self.color = color

    def placePlayer(self, sur):
        self.player = True
