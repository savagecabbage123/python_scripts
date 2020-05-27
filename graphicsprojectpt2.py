#file name must be named: gridprojectpt2.py

#zach
#lawrence
#5th pd

import pygame

#define some colors---Ive given you several
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN2 = (0, 128, 0)
RED2 = (150, 0, 50)
BLUE2 = (0, 206, 209)
YELLOW = (255, 255, 0)
BLUE3 = (0, 0, 128)

pygame.init()

#set width and height of screen
size = (800, 800)
screen = pygame.display.set_mode(size)

# Loops until user clicks close button.
done = False

# used to manage how fast screen updates
clock = pygame.time.Clock()

# main program loop
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
			
	#fill screen before any drawing
	screen.fill(YELLOW)
	
	pygame.draw.polygon(screen, BLUE3, [(400,400),(0,0),(0,800)])
	pygame.draw.polygon(screen, BLACK, [(400,400),(0,0),(0,800)], 2)# puts black line border around triangle
	pygame.draw.polygon(screen, BLUE3, [(800-400,400),(800-0,0),(800-0,800)])#switches sides of where the first triangle was and flipping it
	pygame.draw.polygon(screen, BLACK, [(800-400,400),(800-0,0),(800-0,800)], 2)# puts border around the new triangle
	# i notice the reflections
	
	pygame.draw.polygon(screen, RED2, [(400,0),(100,400),(400,800)])# makes red triangle in the middle of the screen
	pygame.draw.polygon(screen, BLACK, [(400,0),(100,400),(400,800)], 2)# puts black line border around red triangle
	pygame.draw.polygon(screen, RED2, [(800-400,0),(800-0,0),(800-0,800)])# makes half of a triangle on the right side of the screen
	pygame.draw.polygon(screen, BLACK, [(800-400,0),(800-0,0),(800-0,800)], 2)# puts black line border around the new half triangle
	
	pygame.draw.rect(screen, GREEN2,(0,0,200,100))
	pygame.draw.rect(screen, BLACK,(0,0,200,100), 2)# puts border around the green rectangle
	pygame.draw.rect(screen, GREEN2,(600-0,0,200,100))# makes new rectangle on the other side
	pygame.draw.rect(screen, BLACK,(600-0,0,200,100), 2)# puts border around the new green rectangle on the other side
	
	pygame.draw.rect(screen, GREEN2,(0,700-0,200,100))
	pygame.draw.rect(screen, BLACK,(0,700-0,200,100), 2)# puts border around the green rectangle
	pygame.draw.rect(screen, GREEN2,(600-0,700-0,200,100))# makes new rectangle on the other side
	pygame.draw.rect(screen, BLACK,(600-0,700-0,200,100), 2)# puts border around the new green rectangle on the other side
	
	pygame.draw.circle(screen, RED2, (140,60),40)# makes a circle at top left
	pygame.draw.circle(screen, RED2, (140,800-60),40)# makes another circle at bottom left
	pygame.draw.circle(screen, RED2, (800-140,60),40)# makes another circle at top right
	pygame.draw.circle(screen, RED2, (800-140,800-60),40)# makes another circle at bottom right
	
	pygame.display.flip()
	
	clock.tick(60)
	
pygame.quit()