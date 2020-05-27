import pygame, sys

from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((300,300))

pygame.display.set_caption('My pygame')

while True:

	for event in pygame.event.get():
	
		if event.type == QUIT:
		
			pygame.quit()
			sys.exit()
		
	pygame.display.update()
	#rect is the shape you can put any shape available there, (0,255,0) is the color in RGB and (100,50) is where to draw and (20,20) is the size
	pygame.draw.rect(DISPLAYSURF, (0,255,0), (100,50,20,20))
	