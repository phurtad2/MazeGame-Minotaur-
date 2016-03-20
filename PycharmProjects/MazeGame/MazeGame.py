import pygame
from Cell import Cell
from Maze import Maze
import random


pygame.init()

moves = 0
turns = 0

running = True
display = pygame.display.set_mode((700,700))
myfont = pygame.font.SysFont("monospace", 30)

# render text
title = myfont.render("Run-In-A-Maze Game!", 15, (255,255,0))

display.blit(title, (10, 10))



# SURFACES ARE PASSED BY REFERENCE
current = Maze(display, 18, 20)
current.mazify()

#current.place(display, random.randint(0, current.getrow()), random.randint(0, current.getcol()))
current.draw(40, 60)


while running:
    display.blit(myfont.render("Turns: " + str(turns), 15, (255, 255, 0)), (10, 30))
    pygame.display.update()

    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                current.turn( 0, -1)
            elif event.key == pygame.K_DOWN:
                current.turn(0, 1)
            elif event.key == pygame.K_LEFT:
                current.turn(-1, 0)
            elif event.key == pygame.K_RIGHT:
                current.turn(1, 0)
            turns += 1
            current.draw(40, 60)
        elif event.type == pygame.KEYUP:
            pass
    pygame.display.update()
pygame.quit()
