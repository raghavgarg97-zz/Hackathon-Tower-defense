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
bullet_size=15
bomb_size=20
FPS=25
castle=pygame.image.load('castle.png')
clouds = pygame.image.load('clouds.png')
gamename='RANDOM VARIABLE'
explosion=pygame.mixer.Sound('explosion.wav')
gameDisplay=pygame.display.set_mode((display_width,display_height));
pygame.display.set_caption(gamename)
intro_sound=pygame.mixer.Sound('intro_sound.wav')
intro_background=pygame.image.load('game_intro.jpg')
monster_1=pygame.image.load('monster_1.jpg')
dragon_1=pygame.image.load('black_dragon.jpg')
pygame.mixer.music.load('game.mp3')
score=0
music=pygame.mixer.Sound('story.wav')
fireball=pygame.image.load('fireball.png')
tower1=pygame.image.load('tower1.jpg')
tower2=pygame.image.load('tower2.jpg')
tower3=pygame.image.load('tower3.jpg')
tower4=pygame.image.load('tower4.jpg')
tower5=pygame.image.load('tower5.jpg')
ground = pygame.image.load('ground.png')
grass = pygame.image.load('grass.jpg')
gamepause= pygame.image.load('pause.jpg')
musicpause=pygame.image.load('sound.jpg')
blast=pygame.image.load('blast.gif')
blast_sound=pygame.mixer.Sound('bomb.wav')
pause=False
p=1


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

def special_button(x,y,img_object,action=None):
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        if x+30>mouse[0]>x and y+30>mouse[1]>y:
                gameDisplay.blit(img_object,(x,y))
                if click[0]==1 and action!=None:
                        action()
        else:
		gameDisplay.blit(img_object,(x,y))

def music_pause():
	global p
	if p==1:
		pygame.mixer.music.pause()
		p=p*(-1)
	else:
		pygame.mixer.music.unpause()
		p=p*(-1)


def gamequit():
	pygame.quit()
	quit()

def destroy(bulletList,bulletList_slope,bombList,bombList_slope,thing_startx, thing_starty1, thing_starty2,monster_identify, hit_point):
    global score
    global prev_score
    global bomb_left
    for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                                pygame.quit()
                                quit()
    c=0
    for XnY in bombList:
        if XnY[1]>=480:
            i=0
            del bombList[c]
            del bombList_slope[c]
            c-=1
            while i<len(thing_startx):
                if monster_identify[i]==1:
                    del thing_startx[i]
                    del thing_starty2[i]
                    del monster_identify[i]
                    del hit_point[i]
                    score+=10
                    i-=1
                i+=1
        c+=1
    c=0
    for XnY in bulletList:
        i=0
        while i<len(thing_startx):
            if monster_identify[i]==0:
                if XnY[0]>=thing_startx[i] and XnY[0]<=thing_startx[i]+100  and XnY[1]>=thing_starty2[i] and XnY[1]<=thing_starty2[i]+100:
                    hit_point[i]-=1
                    del bulletList[c]
		    del bulletList_slope[c]
                    c-=1
                    if hit_point[i]==0:
                    	del thing_startx[i]
			del thing_starty2[i]
			del hit_point[i]
			del monster_identify[i]
			i-=1
			score+=10
			if score-prev_score>=75:
                            if bomb_left<3:
                             bomb_left+=1
                             prev_score=score
			
            else:
                if XnY[0]>=thing_startx[i] and XnY[0]<=thing_startx[i]+100  and XnY[1]>=thing_starty1 and XnY[1]<=thing_starty1+100:
                    hit_point[i]-=1
                    del bulletList[c]
		    del bulletList_slope[c]
		    c-=1
                    if hit_point[i]==0:
                    	del thing_startx[i]
			del hit_point[i]
			del monster_identify[i]
			del thing_starty2[i]
			i-=1
			score+=10
			if score-prev_score>=75:
                            if bomb_left<3:
                             bomb_left+=1
                             prev_score=score
	    i+=1
        c+=1


def fire(bulletList,bombList):
    for XnY in bulletList:
        gameDisplay.blit(fireball,(XnY[0],XnY[1]))
    for XnY in bombList:
        gameDisplay.blit(fireball,(XnY[0],XnY[1]))

def story_line():
	i=1
        pygame.mixer.Sound.stop(intro_sound)
	pygame.mixer.Sound.play(music) 	
	gameDisplay.blit(tower1,(0,0))
	button("skip",1000,100,100,50,bright_green,green,game_loop)
	pygame.display.update()
        time.sleep(10) 	
	gameDisplay.blit(tower2,(0,0))
	pygame.display.update()
	time.sleep(8)	
	gameDisplay.blit(tower3,(0,0))
	pygame.display.update()	
	time.sleep(8)
	gameDisplay.blit(tower4,(0,0))
	pygame.display.update()
	time.sleep(5)
	pygame.mixer.Sound.stop(music)	
	gameDisplay.blit(tower5,(0,0))
	pygame.display.update()
	pygame.mixer.Sound.stop(music)
	time.sleep(5)
	game_loop()

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
                button("Play!!",300,450,100,50,bright_green,green,story_line)
                button("Quit!",750,450,100,50,bright_red,red,gamequit)
		button("Skip To Game",470,450,220,50,black,black,game_loop)
                pygame.display.update()
                clock.tick(15)

def game_unpause():
	global pause
	pause=False
	pygame.mixer.music.unpause()

def game_pause():
        
	global  pause
	pause=True
	pygame.mixer.music.pause()
        while pause:
                for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                                pygame.quit()
                                quit()
            	large_text=pygame.font.Font('freesansbold.ttf',50)
                TextSurf=large_text.render("GAME PAUSED",True,white)
		TextRect=TextSurf.get_rect()
                TextRect.center=((display_width/2),(display_height/2))
                gameDisplay.blit(TextSurf,TextRect)
                button("CONTINUE",400,400,200,50,bright_green,green,game_unpause)
                button("Quit!",700,400,100,50,bright_red,red,gamequit)
                pygame.display.update()
                clock.tick(15)

def game_over_l():
	pygame.mixer.music.stop()	
	gameDisplay.fill(black)
	pygame.mixer.Sound.play(blast_sound)
	pygame.display.update()
	time.sleep(8)
	gameDisplay.blit(blast,(0,0))
	pygame.display.update()
	game_over()
	
	



def game_over():
        while True:
            for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                                pygame.quit()
                                quit()	
            TextSurf=pygame.font.Font('freesansbold.ttf',50).render('Game Over',True,black)
            TextRect=TextSurf.get_rect()
            TextRect.center=((display_width/2),(display_height/2))
            gameDisplay.blit(TextSurf,TextRect)
            button("Play Again!!",400,450,200,50,bright_green,green,game_loop)
            button("Quit!",750,450,100,50,bright_red,red,gamequit)
            pygame.display.update()
            clock.tick(15)


	

def game_loop():
	pygame.mixer.Sound.stop(intro_sound)
	global score
	global prev_score
	global bomb_left
        enemy_count=1
        thing_startx=random.sample(range(1200,2000),enemy_count)
        thing_starty1=400
	thing_starty2=[150]
        x_change=-10
        lead_x=210
        lead_y=220
        lead_x_change=0
        bulletList=[]
        bulletList_slope=[]
        bombList=[]
        bombList_slope=[]
	monster_identify=[1]
	hit_point=[2]
	pygame.mixer.music.play()
	tower_point=100
	score=0
	prev_score=0
	bomb_left=0
	while True:
		blast=0
        	for event in pygame.event.get():
                	if event.type==pygame.QUIT:
                    		pygame.quit()
				quit()
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            if event.button == 1:
                                bulletList.append([lead_x,lead_y])
                                mouse_x,mouse_y=pygame.mouse.get_pos()
                                bulletList_slope.append((float)(mouse_y-lead_y)/(mouse_x-lead_x))
                            if event.button == 3:
                                if len(bombList)<3 and bomb_left>0:
                                    bombList.append([lead_x,lead_y])
                                    mouse_x,mouse_y=pygame.mouse.get_pos()
                                    bombList_slope.append((float)(mouse_y-lead_y)/(mouse_x-lead_x))
                                    bomb_left-=1


                c=0;
                for XnY in bulletList:
                    XnY[0] += bullet_size
                    XnY[1] += bullet_size*bulletList_slope[c]
                    if XnY[0]>display_width or XnY[1]>display_height or XnY[1]<0:
                        del bulletList[c]
                        del bulletList_slope[c]
                    c += 1

                c=0;
                for XnY in bombList:
                    XnY[0] += bomb_size
                    XnY[1] += bomb_size*bombList_slope[c]
                    if XnY[0]>display_width or XnY[1]>display_height or XnY[1]<0:
                        del bombList[c]
                        del bombList_slope[c]
                    c += 1
            	gameDisplay.fill(black)
            	gameDisplay.blit(ground, [0,500])
                pygame.draw.rect(gameDisplay,colour_sky,[0,0,1200,500])
                gameDisplay.blit(castle,[10,105])
                gameDisplay.blit(clouds, [50,0])
                gameDisplay.blit(clouds, [550,00])
                gameDisplay.blit(clouds, [400,40])
                gameDisplay.blit(clouds, [1000,40])
                gameDisplay.blit(grass,[400,442])
                gameDisplay.blit(grass,[850,442])
                gameDisplay.blit(grass,[260,442])
                fire(bulletList,bombList)
                gameDisplay.blit(pygame.font.Font('freesansbold.ttf',30).render('SCORE:'+str(score),True,red),[10,520])
                gameDisplay.blit(pygame.font.Font('freesansbold.ttf',30).render('Tower_point:'+str(tower_point),True,red),[200,520])
		special_button(1100,10,gamepause,game_pause)
		pygame.display.update()
		special_button(1020,10,musicpause,music_pause)

		if len(thing_startx)==0:
                        thing_startx=random.sample(range(1200,2400),enemy_count)
                        for i in range(0,len(thing_startx)):
                                x=random.choice([True,False])
                                if x==True:
                                	monster_identify.append(1)
					thing_starty2.append(0)
					hit_point.append(2)
                                else:
                                	monster_identify.append(0)
					thing_starty2.append(random.randrange(150,300))
					hit_point.append(3)

                for i in range(0,len(thing_startx)):
                        if monster_identify[i]==1:
                                gameDisplay.blit(monster_1,(thing_startx[i],thing_starty1))
                        else :
                                gameDisplay.blit(dragon_1,(thing_startx[i],thing_starty2[i]))
                for i in range(0,len(thing_startx)):
                        thing_startx[i]=thing_startx[i]+x_change
                pygame.display.update()
 	        destroy(bulletList,bulletList_slope,bombList,bombList_slope,thing_startx,thing_starty1,thing_starty2,monster_identify,hit_point)
                if score>10:
                        enemy_count=6
		if score>100:
			enemy_count=3
		if score>400:
			enemy_count=4
		hp_counter=1	
	        i=0
		while i<len(monster_identify):
                        if monster_identify[i]==1:
				if thing_startx[i]<249:
					del thing_startx[i]
					del monster_identify[i]
					del hit_point[i]
					del thing_starty2[i]
					i-=1
					tower_point-=10
					if tower_point==0:
                                            hp_counter=0
                                            break
					
			else:
				if thing_startx[i]<210:
                                        del thing_startx[i]
					del monster_identify[i]
					del hit_point[i]
					del thing_starty2[i]
					tower_point-=10
					i-=1
                                        if tower_point==0:
                                            hp_counter=0
                                            break
			i+=1

                if hp_counter==0:
                    game_over_l()
                                        

		
            	clock.tick(FPS)

    

intro()
