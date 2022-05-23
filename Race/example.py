import pygame
pygame.init()
w=pygame.display.set_mode((1300,700))
pygame.display.set_caption("RACE")
bx=0
by=0
fps=50
exit_game=False
pygame.display.update()
clock=pygame.time.Clock()
back_image=pygame.image.load('C:/Race/back.png')
bx=1
by=1
def back(x,y):
	w.blit(back_image,(x,y))
font=pygame.font.SysFont(None,75)
def screen_text(text,color,x ,y):
	screen_text=font.render(text,True,color)
	w.blit(screen_text,(x,y))
def home():
	white=(255,255,255)
	exit_game=False
	while not exit_game:
		#w=pygame.display.set_mode((1440,700))
		for event in pygame.event.get():
			if  event.type==pygame.QUIT:
				exit_game=True
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_RETURN:
					#game_loop()
					print('varun')

		w.fill(white)
		screen_text('Hello there racers!!',(255,255,0),10,40)
		back(bx,by)

		pygame.display.update()
		clock.tick(fps)
	pygame.quit()
	quit()

home()
