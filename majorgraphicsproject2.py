import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (139, 69, 19)
YELLOW = (255, 215, 0)
BLUE = 	(0, 0, 205)

pygame.init()

size = (800, 800)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("irish wrist watch")

done = False

clock = pygame.time.Clock()

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
			
	screen.fill(WHITE)
	
	# drawing code here
	# outline of giraffe and colors of it filled in
	pygame.draw.polygon(screen, YELLOW, [[0, 800], [133, 400], [233, 200], [301, 200], [235, 100], [268, 100], [333, 200], [433, 266], [475, 275], [500, 323], [733, 533], [750, 566], [705, 566], [570, 505], [490, 450], [400, 466], [300, 415], [266, 433], [150, 800]], 0)
	pygame.draw.polygon(screen, BLACK, [[0, 800], [133, 400], [233, 200], [301, 200], [235, 100], [268, 100], [333, 200], [433, 266], [475, 275], [500, 323], [733, 533], [750, 566], [705, 566], [747, 572], [747, 572], [750, 566], [705, 566], [570, 505], [490, 450], [400, 466], [300, 415], [266, 433], [150, 800]], 2)
	pygame.draw.polygon(screen, YELLOW, [[250, 240], [249, 270], [115, 315], [170, 229]], 0)
	pygame.draw.polygon(screen, BLACK, [[250, 240], [249, 270], [115, 315], [170, 229]], 2)
	pygame.draw.polygon(screen, BROWN, [[150, 295], [180, 240], [230, 250]], 0)
	pygame.draw.polygon(screen, BLACK, [[150, 295], [180, 240], [230, 250]], 2)
	pygame.draw.circle(screen, BROWN, [249, 75], 32, 0)
	
	# the eyes
	pygame.draw.circle(screen, WHITE, [366, 300], 50, 0)
	pygame.draw.circle(screen, BLUE, [370, 300], 25, 0)
	pygame.draw.circle(screen, BLACK, [370, 300], 25, 2)
	pygame.draw.circle(screen, BLACK, [375, 300], 5, 0)
	
	# the spots
	pygame.draw.polygon(screen, BROWN, [[66, 700], [133, 700], [105, 766]], 0)
	pygame.draw.polygon(screen, BROWN, [[100, 600], [150, 575], [180, 605], [156, 666]], 0)
	pygame.draw.polygon(screen, BROWN, [[166, 466], [200, 468], [201, 534], [165, 530]], 0)
	pygame.draw.polygon(screen, BROWN, [[201, 366], [233, 400], [275, 350], [235, 301], [235, 352]], 0)
	pygame.draw.polygon(screen, BROWN, [[308, 235], [314, 251], [296, 267], [275, 245]], 0)	
	pygame.draw.polygon(screen, BROWN, [[366, 366], [367, 400], [416, 432], [405, 363]], 0)
	pygame.draw.circle(screen, BROWN, [317, 350], 5, 0)
	pygame.draw.polygon(screen, BROWN, [[433, 333], [466, 320], [516, 396], [490, 420], [472, 390], [450, 395]], 0)
	pygame.draw.polygon(screen, BROWN, [[550, 427], [610, 466], [572, 470]], 0)
	pygame.draw.polygon(screen, BROWN, [[632, 471], [653, 468], [670, 537], [639, 516], [626, 510]], 0)
	
	pygame.display.flip()
	
	clock.tick(60)
	
pygame.quit()