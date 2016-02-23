import pygame

from Cell import Cell

cells = []
class Player:
    def __init__(self, sur, x, y, cells):
        self.cells = cells
        pygame.draw.circle(sur, (255, 255, 0), (x, y), 20, 0)