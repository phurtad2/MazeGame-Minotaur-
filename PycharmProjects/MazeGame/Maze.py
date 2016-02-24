from Cell import Cell
from Player import Player
import pygame

import random


class Maze:
    cells = []
    unvisitedNeighbors = []

    px = 0
    py = 0

    lx = 0
    ly = 0
    row = 0
    col = 0

    def __init__(self, row, col):
        # self.cells = np.arange(row*col).reshape(row, col)

        if row <=0 or col <= 0:
            print("This isn't a maze...Setting to (1, 1)")
            row = 1
            col = 1
        self.row = row
        self.col = col
        for x in range(self.col):
            z = []
            for y in range(self.row):
                z.append(Cell())
            self.cells.append(z)

    def reset(self):
        self.cells = []
        self.unvisitedNeighbors = []
        for x in range(self.col):
            z = []
            for y in range(self.row):
                z.append(Cell())
            self.cells.append(z)

    def draw(self, sur, locx, locy):
        i = len(self.cells)
        j = len(self.cells[0])
        originx = locx
        originy = locy
        for x in range(i):
            for y in range(j):
                # self.cells[x][y].setColor((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
                self.cells[x][y].draw(sur, (locx, locy))

                locy += self.cells[x][y].getSize()

            locx += self.cells[x][0].getSize()
            locy = originy

    def redraw(self, x, y):
        pass

    def getNorthNeighbor(self, x, y):
        if ((y - 1) >= 0):
            return self.cells[x][y - 1]
        else:
            return None

    def getSouthNeighbor(self, x, y):
        if ((y + 1) < len(self.cells[0])):
            return self.cells[x][y + 1]
        else:
            return None

    def getWestNeighbor(self, x, y):
        if ((x - 1) >= 0):
            return self.cells[x - 1][y]
        else:
            return None

    def getEastNeighbor(self, x, y):
        if ((x + 1) < len(self.cells)):
            return self.cells[x + 1][y]
        else:
            return None

    def isValid(self, x, y):
        return 0 <= x < len(self.cells) and 0 <= y < len(self.cells[0])

    def mazify(self):
        self.reset()

        if len(self.cells) <= 1 or len(self.cells[0]) <= 1:
            print("That isn't a maze...")
            return
        # Randomly picks a starting point for Prim's Algorithm
        x = random.randint(0, len(self.cells) - 1)
        y = random.randint(0, len(self.cells[0]) - 1)

        print("Maze Time!")
        # Neighbors will hold all possible neighbors of the visited nodes
        self.unvisitedNeighbors = []

        while True:
            picked = ''
            # Immediate neighbors we have visited of current will be held in 'immediate'
            immediate = []

            current = self.cells[x][y]
            # print(str(x) + ":" + str(y))

            # Checks to see where we can go and what we have already visited
            # if we can go north and have not already...
            if self.getNorthNeighbor(x, y) is not None and self.getNorthNeighbor(x, y).didVisit() == False:
                self.unvisitedNeighbors.append((x, y - 1, self.cells[x][y - 1].getValue()))
            # if we can go there and have been, it is an immediate neighbor
            elif self.isValid(x, y - 1) and self.getNorthNeighbor(x, y).didVisit():
                immediate.append((x, y - 1))
            else:
                pass

            # if we can go south and have not already...
            if self.getSouthNeighbor(x, y) is not None and self.getSouthNeighbor(x, y).didVisit() == False:
                self.unvisitedNeighbors.append((x, y + 1, self.cells[x][y + 1].getValue()))
            # if we can go there and have been, it is an immediate neighbor
            elif self.isValid(x, y + 1) and self.getSouthNeighbor(x, y).didVisit():
                immediate.append((x, y + 1))
            else:
                pass

            # if we can go west and have not already...
            if self.getWestNeighbor(x, y) is not None and self.getWestNeighbor(x, y).didVisit() == False:
                self.unvisitedNeighbors.append((x - 1, y, self.cells[x - 1][y].getValue()))
            # if we can go there and have been, it is an immediate neighbor
            elif self.isValid(x - 1, y) and self.getWestNeighbor(x, y).didVisit():
                immediate.append((x - 1, y))
            else:
                pass

            # if we can go east and have not already...
            if self.getEastNeighbor(x, y) is not None and self.getEastNeighbor(x, y).didVisit() == False:
                self.unvisitedNeighbors.append((x + 1, y, self.cells[x + 1][y].getValue()))
            # if we can go there and have been, it is an immediate neighbor
            elif self.isValid(x + 1, y) and self.getEastNeighbor(x, y).didVisit():
                immediate.append((x + 1, y))

            else:
                pass

            # Sort the neighbors so that the lowest value is the 0th element
            self.unvisitedNeighbors = sorted(self.unvisitedNeighbors, key=lambda k: k[2], reverse=False)
            # Takes out dupes
            self.unvisitedNeighbors = list(set(self.unvisitedNeighbors))
            # sort again, you know, to be on the safe side?
            self.unvisitedNeighbors = sorted(self.unvisitedNeighbors, key=lambda k: k[2], reverse=False)


            #If this is a brave new world, no known neighbors, pick the lowest element in neighbors
            if len(immediate) == 0:
                picked = (self.unvisitedNeighbors[0][0], self.unvisitedNeighbors[0][1])
            else:
                #if we have visited neighbors, pick one at random to connect to the rest of the visited
                picked = immediate[random.randint(0, len(immediate) - 1)]

            if x < picked[0] and self.cells[x][y].eThick:  # picked east
                self.cells[x][y].destroy('e')
                self.cells[picked[0]][picked[1]].destroy('w')

            elif x > picked[0] and self.cells[x][y].wThick:  # picked west
                self.cells[x][y].destroy('w')
                self.cells[picked[0]][picked[1]].destroy('e')

            elif y > picked[1] and self.cells[x][y].nThick:  # picked north
                self.cells[x][y].destroy('n')
                self.cells[picked[0]][picked[1]].destroy('s')

            elif y < picked[1] and self.cells[x][y].sThick:  # picked south
                self.cells[x][y].destroy('s')
                self.cells[picked[0]][picked[1]].destroy('n')

            # Just in case I want to see the array of neighbors
            # print(self.unvisitedNeighbors)

            # Take our next unvisited neighbor and make him current, deleting him from neighbors
            x = self.unvisitedNeighbors[0][0]
            y = self.unvisitedNeighbors[0][1]
            del self.unvisitedNeighbors[0]

            #we now have visited him
            current.setVisit(True)
            current = self.cells[x][y]

            # If we at the last element of the maze
            if len(self.unvisitedNeighbors) == 0:
                # So not TOTALLY random here...the r will be implemented later.
                r = random.randint(1, 4)
                if self.isValid(x, y - 1):
                    self.cells[x][y].destroy('n')
                    self.cells[x][y - 1].destroy('s')
                elif self.isValid(x, y + 1):
                    self.cells[x][y].destroy('s')
                    self.cells[x][y + 1].destroy('n')
                elif self.isValid(x - 1, y):
                    self.cells[x][y].destroy('w')
                    self.cells[x - 1][y].destroy('e')
                elif self.isValid(x + 1, y):
                    self.cells[x][y].destroy('e')
                    self.cells[x + 1][y].destroy('w')
                print(str(x) + ":" + str(y))
                print("Finished Generating Maze!")
                break

    def placePlayer(self, sur):
        Player(sur, 0, 0, self.cells)

    def turn(self, sur, x, y):
        self.cells[self.px][self.py].player = False
        self.cells[self.px][self.py].redraw(sur)
        self.cells[self.px + x][self.py + y].placePlayer(sur)
        self.cells[self.px + x][self.py + y].redraw(sur)


