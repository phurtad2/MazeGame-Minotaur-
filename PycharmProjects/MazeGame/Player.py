import pygame

from Cell import Cell

cells = []
xcoord = 0
ycoord = 0
color = (255, 255, 0)
class Player:
    def __init__(self, x, y):
        self.xcoord = x
        self.ycoord = y
        self.color = (255, 255, 0)

    def move(self, x, y):
        self.xcoord = self.xcoord + x
        self.ycoord = self.ycoord + y

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def getX(self):
        return self.xcoord

    def getY(self):
        return self.ycoord