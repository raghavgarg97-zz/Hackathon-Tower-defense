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
colour_sky=(0,100,200)
display_width=1200
display_height=600
FPS=20
castle=pygame.image.load('castle.png')
clouds = pygame.image.load('clouds.png')
gamename='RANDOM VARIABLE'
explosion=pygame.mixer.Sound('explosion.wav')
gameDisplay=pygame.display.set_mode((display_width,display_height));
pygame.display.set_caption(gamename)
intro_sound=pygame.mixer.Sound('intro_sound.wav')
intro_background=pygame.image.load('game_intro.jpg')
monster_1=pygame.image.load('monster_1.jpg')

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
	pygame.mixer.Sound.stop(intro_sound)
	score=0
        no_of_elements=[1]
        enemy_count=1
        thing_startx=random.sample(range(1200,2400),enemy_count)
        thing_starty=400
        x_change=-10
	
	while True:
		blast=0
        	for event in pygame.event.get():
                	if event.type==pygame.QUIT:
                    		pygame.quit()
				quit()
            	gameDisplay.fill(black)
            	pygame.draw.rect(gameDisplay,colour_ground,[0,500,1200,100])
                pygame.draw.rect(gameDisplay,colour_sky,[0,0,1200,500])
                gameDisplay.blit(castle,[10,105])
                gameDisplay.blit(clouds, [50,0])
                gameDisplay.blit(clouds, [550,00])
                gameDisplay.blit(clouds, [400,40])
                gameDisplay.blit(clouds, [1000,20])
		for pos in thing_startx:
                        gameDisplay.blit(monster_1,(pos,thing_starty))
                for i in range(0,len(thing_startx)):
                        thing_startx[i]=thing_startx[i]+x_change
	    	pygame.display.update()
		for i in range(0,len(thing_startx)):
                        if thing_startx[i]<249:
				del thing_startx[i]
				blast=1
		if blast==1:
			pygame.mixer.Sound.play(explosion)
			blast=0
            	clock.tick(FPS)

    

intro()
