import pygame
from Cell import Cell
from Maze import Maze

pygame.init()

Display = pygame.display.set_mode((600,600))
myfont = pygame.font.SysFont("monospace", 30)

# render text
label = myfont.render("Run-In-A-Maze Game!", 15, (255,255,0))
Display.blit(label, (10, 10))

current = Maze(15, 10, 40, 40)
current.mazify()
current.draw(Display, 40, 40)
while True:
    pygame.display.update()
    pygame.time.delay(10)
