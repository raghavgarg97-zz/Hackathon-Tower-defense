import pygame
import time
import random

pygame.init()

clock=pygame.time.Clock()
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,155,0)
colour_ground=(240,245,33)
colour_sky=(121,188,255)

display_width=1200
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
            pygame.draw.rect(gameDisplay,colour_ground,[0,500,1200,100])
            pygame.draw.rect(gameDisplay,colour_sky,[0,0,1200,500])
            pygame.display.update()

            clock.tick(FPS)

    pygame.quit()
    quit()

gameLoop()
