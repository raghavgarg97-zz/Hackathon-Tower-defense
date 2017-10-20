import pygame
import time
import random

pygame.init()

clock=pygame.time.Clock()
white=(255,255,255)
black=(0,0,0)
red=(200,0,0)
green=(0,200,0)
bright_green=(0,255,0)
bright_red=(255,0,0)
colour_ground=(240,245,33)
colour_sky=(121,188,255)
display_width=1200
display_height=600
FPS=20

gamename='RANDOM VARIABLE'

gameDisplay=pygame.display.set_mode((display_width,display_height));
pygame.display.set_caption(gamename)
intro_sound=pygame.mixer.Sound('intro_sound.wav')
intro_background=pygame.image.load('game_intro.jpg')

def button(msg,x,y,w,h,ic,ac,action=None):
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        if x+w>mouse[0]>x and y+h>mouse[1]>y:
                pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
                if click[0]==1 and action!=None:
                        action()
        else:
                pygame.draw.rect(gameDisplay,ic,(x,y,w,h))
        small_text=pygame.font.Font('freesansbold.ttf',30)
        TextSurf=small_text.render(msg,True,white)
	TextRect=TextSurf.get_rect()
        TextRect.center=(x+w/2,y+h/2)
        gameDisplay.blit(TextSurf,TextRect)

def gamequit():
	pygame.quit()
	quit()

def intro():
	while True:
                for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                                pygame.quit()
                                quit()
                gameDisplay.blit(intro_background,(0,0))
		pygame.mixer.Sound.play(intro_sound)
                large_text=pygame.font.Font('freesansbold.ttf',50)
                TextSurf=large_text.render(gamename,True,white)
		TextRect=TextSurf.get_rect()
                TextRect.center=((display_width/2),(display_height/2))
                gameDisplay.blit(TextSurf,TextRect)
                button("Play!!",450,450,100,50,bright_green,green,game_loop)
                button("Quit!",750,450,100,50,bright_red,red,gamequit)
                pygame.display.update()
                clock.tick(15)

def game_loop():
	while True:
        	for event in pygame.event.get():
                	if event.type==pygame.QUIT:
                    		pygame.quit()
				quit()
            	gameDisplay.fill(white)
            	pygame.draw.rect(gameDisplay,colour_ground,[0,500,1200,100])
                pygame.draw.rect(gameDisplay,colour_sky,[0,0,1200,500])
            	pygame.display.update()

            	clock.tick(FPS)

    

intro()
