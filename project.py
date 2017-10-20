import pygame
import time
import random

pygame.init()

clock=pygame.time.Clock()
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,155,0)
display_width=800
display_height=600
FPS=20

gameDisplay=pygame.display.set_mode((display_width,display_height));

pygame.display.update()


def gameLoop():
    gameExit=False
    while not gameExit:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    gameExit=True


            gameDisplay.fill(white)
            pygame.display.update()

            clock.tick(FPS)

    pygame.quit()
    quit()

gameLoop()
