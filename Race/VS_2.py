import pygame
import random
import time
import math
import os
from os import path
import pygame.mixer
pygame.init()
img_dir= path.join(path.dirname(__file__), 'img')
pygame.mixer.init()
width=1400
height=700
w=pygame.display.set_mode((width,height))
pygame.display.set_caption("Race with swag")
fps=100
pygame_quit=False
clock=pygame.time.Clock()

# set up assets folders
game_folder= os.path.dirname(__file__)
image_folder= os.path.join(game_folder,'img')# a variable for image , this will allow the game to work in any os


ri=pygame.image.load(r'Race/R.jpg')
ri=pygame.transform.scale(ri,(1500,100))
def r(x,y):
	w.blit(ri,(x,y))

#crash image
c_image=pygame.image.load(r'Race/c.png')
c_image=pygame.transform.scale(c_image,(340,340))
cx=900
cy=100
def c(x,y):
	w.blit(c_image,(x,y))

#icon for main screen
back_image=pygame.image.load(r'Race/back.png')
bx=300
by=-50
def i(x,y):
	w.blit(back_image,(x,y))

#player
p_image=pygame.image.load(r'Race/car.png')
p_image=pygame.transform.scale(p_image,(470,470))
pimage = p_image.get_rect()
def player(x,y):
	w.blit(p_image,(x,y))

#obstacle
o_image=pygame.image.load(r'Race/barricade_2.png')
o_image=pygame.transform.scale(o_image,(460,460))
oimage=o_image.get_rect()
def o(x,y):
	w.blit(o_image,(x,y))

#icon for second page
h=pygame.image.load(r'Race/hpr.png')
h=pygame.transform.scale(h,(380,240))
hx=530
hy=280
def hpr(x,y):
	w.blit(h,(x,y))

#font large
font1=pygame.font.Font(None,75)
def screen_text1(text,color,x ,y):
	screen_text1=font1.render(text,True,color)
	w.blit(screen_text1,(x,y))

#font medium
font2=pygame.font.Font(r'Race/kenvector_future_thin.ttf',30)
def screen_text2(text,color,x ,y):
	screen_text2=font2.render(text,True,color)
	w.blit(screen_text2,(x,y))

font3=pygame.font.Font(r'Race/kenvector_future_thin.ttf',25)
def screen_text3(text,color,x ,y):
	screen_text3=font3.render(text,True,color)
	w.blit(screen_text3,(x,y))

#pause page
def p():
	game_over1=False
	pygame.mixer.music.stop()
	while not game_over1:
		screen_text2('PAUSED',(0,0,255),600,100)
		screen_text2('C to continue',(0,255,0),600,200)
		screen_text2('Or Q to quit',(255,0,0),600,250)
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_c:
					game_over1=True
					pygame.mixer.music.play()
				if event.key==pygame.K_q:
					home2()
		clock.tick(10)
		pygame.display.update()

#rule page
def rules():
	exit_game=False
	fps=50
	while not exit_game:
		w.fill((0,0,255))
		hpr(hx,hy)
		r(0,0)
		screen_text2('1.Avoiding each obstacle will be awarded with 10 points',(0,0,0),20,120)
		screen_text2('2. As soon as car crashes with the red part of the obstacle, game is over',(0,0,0),20,200)
		screen_text1('PRESS ENTER TO PLAY. HAPPY RACING :)',(0,255,0),80,590)
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_RETURN:
					game_loop()
		clock.tick(fps)
		pygame.display.update()

def crash():
	with open(r'Race/untitled2.txt','r') as f:
		hiscore=f.read()
	w.fill((255,255,255))
	screen_text1('CRASH!',(0,0,255),590,100)
	screen_text1('PRESS ENTER REPLAY :)',(0,255,0),10,280)
	screen_text1('OR Press space to return to home ',(255,0,0),10,350)
	screen_text2('* The winner is not one with ',(0,0,0),420,550)
	screen_text2('the fastest car ; it is the one who refuses to lose',(0,0,0),300,600)
	c(cx,cy)

#home
def home1():
	exit_game=False
	pygame.mixer.init()
	#pygame.mixer.music.load('E:/Race/bm1.mp3')
	#pygame.mixer.music.play(-1)
	while not exit_game:
		w.fill((0,255,0))
		i(bx,by)
		screen_text1('Hello there racers!!',(255,255,0),480,110)
		screen_text1('Press Enter to play',(255,0,0),480,510)
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_RETURN:
					rules()
		clock.tick(fps)
		pygame.display.update()
def home2():
	exit_game=False
	pygame.mixer.music.load(r'Race/sad.mp3')
	pygame.mixer.music.play(-1)
	while not exit_game:
		w.fill((0,255,0))
		i(bx,by)
		screen_text1('Hello there racers!!',(255,255,0),480,110)
		screen_text1('Press Enter to play',(255,0,0),480,510)
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_RETURN:
					rules()
		clock.tick(fps)
		pygame.display.update()
#gameloop

def game_loop():
	exit_game1=False
	game_over=False
	black=(0,0,0)
	white=(255,255,255)
	red=(255,0,0)
	brown=(210,105,30)
	p_x=280
	p_y=350
	v=5
	v_x=0
	ox1=random.randint(-200,500)
	oy1=-300
	ox2=random.randint(550,1200)
	oy2=-300
	size_1=250
	size_2=150
	bx=0
	by=0
	rx=700
	ry=-700
	o_y_c1=5
	o_y_c2=5
	ry_c=5
	score=0
	y=200
	#collide=pygame.Rect.colliderect(pimage,oimage,True)
	#pygame.mixer.music.load('E:/Race/bm.mp3')
	#pygame.mixer.music.play(-1)
	with open(r'Race/untitled2.txt','r') as f:
		hiscore=f.read()
	while not exit_game1:
		if game_over:
			with open('untitled2.txt','w') as f:
				f.write(str(hiscore))
			crash()
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					pygame.quit()
					quit()
				if event.type==pygame.KEYDOWN:
					if event.key==pygame.K_RETURN:
						game_loop()
					if event.key==pygame.K_SPACE:
						home1()
		else:
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					pygame.quit()
					quit()
				if event.type==pygame.KEYDOWN:
					if event.key==pygame.K_RIGHT or event.key==pygame.K_d or event.key==pygame.K_6:
						v_x=v
					if event.key==pygame.K_LEFT or event.key==pygame.K_a or event.key==pygame.K_4  :
						v_x=-v
					if event.key==pygame.K_p:
						p()
			p_x+=v_x
			#motion of obstacle and track marks
			oy1+=o_y_c1
			oy2+=o_y_c2
			ry+=ry_c
			#repositioning and score increasing
			if oy1>=600 and oy2>=600:
							#ox1=random.randint(-250,500)
							ox1=p_x
							oy1=-500
							ox2=random.randint(300,1000)
							oy2=-500
							score+=10
							#s.append(score)
			if score>int(hiscore):
				hiscore=score
		    #boundaries of car
			if p_x<-180:
										p_x=-180
			if p_x>1100:
										p_x=1100
#tracks
			if ry>700:
				ry=-700
			#collision
			if math.sqrt(math.pow(p_x-ox1,2)+math.pow(p_y-oy1,2)) <=80 or math.sqrt(math.pow(p_x-ox2,2)+math.pow(p_y-oy2,2)) <=80:
				#pygame.mixer.music.load('E:/Race/crash.mp3')
				#pygame.mixer.music.play()
				game_over=True

			#increasing difficulty
			if score==80:
				ry_c=8
				o_y_c1=8
				o_y_c2=8
			if score==170:
				ry_c=13
				o_y_c1=13
				o_y_c2=13
			if score==260:
				ry_c=15
				o_y_c1=15
				o_y_c2=15
			if score==320:
				ry_c=17
				o_y_c1=17
				o_y_c2=17
			if score==380:
				ry_c=19
				o_y_c1=19
				o_y_c2=19
			if score==440:
				ry_c=21
				o_y_c1=21
				o_y_c2=21
			if score==500:
				ry_c=23
				o_y_c1=23
				o_y_c2=23

			w.fill(black)
			pygame.draw.rect(w,white,(rx,ry,30,400))
			o(ox1,oy1)
			o(ox2,oy2)
			player(p_x,p_y)

			#score
			screen_text1(str(score),(0,0,255),int(width/2),10)
			screen_text2('Hiscore: '+str(hiscore),(0,255,0),20,10)
			screen_text3('Press (p) to pause the game',(0,255,255),width-410,10)
		pygame.display.flip()
		clock.tick(fps)
	pygame.quit()
	quit()
home1()
