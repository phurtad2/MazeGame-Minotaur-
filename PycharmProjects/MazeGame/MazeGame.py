import pygame
from Cell import Cell
from Maze import Maze

pygame.init()
running = True
display = pygame.display.set_mode((500,500))
myfont = pygame.font.SysFont("monospace", 30)

# render text
label = myfont.render("Run-In-A-Maze Game!", 15, (255,255,0))
display.blit(label, (10, 10))

current = Maze(15,15)


current.mazify()
current.placePlayer(display)
current.draw(display, 40, 40)


while running:

    current.draw(display, 40, 40)
    pygame.display.update()

    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                current.turn(display, 0, -1)
                print("up")
            elif event.key == pygame.K_DOWN:
                current.turn(display, 0, 1)
                print("down")
            elif event.key == pygame.K_LEFT:
                current.turn(display, - 1, 0)
                print("left")
            elif event.key == pygame.K_RIGHT:
                current.turn(display, 1, 0)
                print("right")
        elif event.type == pygame.KEYUP:
            pass
    pygame.event.clear()
pygame.quit()
