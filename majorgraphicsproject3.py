import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (139, 69, 19)
YELLOW = (255, 215, 0)
BLUE = 	(0, 0, 205)
RED = (255, 0, 0)
VANILLA = (231, 214, 184)
REDVELVET = (102, 35, 25)
BLUE = (30, 144, 255)
ORANGE = (255, 140, 0)
GREY = (169, 169, 169)

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

	
	# main cake
	pygame.draw.circle(screen, WHITE, (400, 400), 390, 0)
	pygame.draw.circle(screen, BLACK, (400, 400), 390, 2)
	pygame.draw.polygon(screen, VANILLA, [[400, 204], [255, 340], [273, 387], [400, 271]], 0)
	pygame.draw.polygon(screen, REDVELVET, [[400, 271], [273, 387], [292, 434], [400, 332]], 0)
	pygame.draw.polygon(screen, VANILLA, [[400, 332], [292, 434], [310, 480], [400, 400]], 0)
	pygame.draw.polygon(screen, VANILLA, [[400, 204], [757, 550], [732, 600], [400, 271]], 0)
	pygame.draw.polygon(screen, REDVELVET, [[400, 271], [732, 600], [701, 645], [400, 332]], 0)
	pygame.draw.polygon(screen, VANILLA, [[400, 332], [701, 645], [668, 681], [400, 400]], 0)
	pygame.draw.polygon(screen, REDVELVET, [[400, 400], [310, 480], [325, 520], [400, 466]], 0)
	pygame.draw.polygon(screen, REDVELVET, [[400, 400], [668, 681], [633, 710], [400, 466]], 0)
	pygame.draw.polygon(screen, WHITE, [[0, 400], [237, 300], [325, 520], [400, 466], [720, 800], [0, 800]], 0)
	pygame.draw.polygon(screen, BLACK, [[237, 300], [343, 567], [200, 733], [0, 533], [0, 400], [237, 300], [0, 533]], 2)
	
	# cake slicer
	pygame.draw.polygon(screen, GREY, [[342, 567], [150, 780], [66, 733], [33, 650], [45, 580]], 0)
	pygame.draw.polygon(screen, BLACK, [[66, 733], [0, 766], [0, 666], [33, 650]], 0)
	
	# main cake 2
	pygame.draw.polygon(screen, VANILLA, [[237, 303], [2, 533], [45, 575], [263, 367]], 0)
	pygame.draw.polygon(screen, REDVELVET, [[263, 367], [45, 575], [95, 625], [290, 433]], 0)
	pygame.draw.polygon(screen, VANILLA, [[290, 433], [95, 625], [150, 680], [315, 500]], 0)
	pygame.draw.polygon(screen, REDVELVET, [[315, 500], [150, 680], [200, 731], [342, 567]], 0)
	
	
	# candles
	pygame.draw.rect(screen, BLUE, [266, 100, 33, 166], 0)
	pygame.draw.rect(screen, BLACK, [266, 100, 33, 166], 2)
	pygame.draw.circle(screen, WHITE, [282, 100], 17, 0)
	pygame.draw.circle(screen, ORANGE, [282, 60], 15, 0)
	pygame.draw.polygon(screen, ORANGE, [[266, 60], [266, 20], [276, 50]], 0)
	pygame.draw.polygon(screen, ORANGE, [[295, 60], [295, 20], [284, 50]], 0)
	pygame.draw.polygon(screen, WHITE, [[266, 150], [300, 160], [300, 178], [266, 167]], 0)
	pygame.draw.polygon(screen, WHITE, [[266, 190], [300, 205], [300, 225], [266, 210]], 0)
	pygame.draw.polygon(screen, WHITE, [[266, 236], [300, 251], [300, 266], [266, 255]], 0)
	pygame.draw.polygon(screen, WHITE, [[266, 115], [300, 125], [300, 140], [266, 130]], 0)
	pygame.draw.rect(screen, BLACK, [266, 100, 33, 166], 2)
	pygame.draw.circle(screen, WHITE, [282, 100], 17, 0)
	pygame.draw.line(screen, BLACK, [280, 100], [280, 66], 2)
	pygame.draw.circle(screen, BLACK, [282, 100], 17, 2)
	
	pygame.draw.rect(screen, BLUE, [768-266, 100, 33, 166], 0)
	pygame.draw.rect(screen, BLACK, [768-266, 100, 33, 166], 2)
	pygame.draw.circle(screen, WHITE, [800-282, 100], 17, 0)
	pygame.draw.circle(screen, ORANGE, [800-282, 60], 15, 0)
	pygame.draw.polygon(screen, ORANGE, [[798-266, 60], [798-266, 20], [798-276, 50]], 0)
	pygame.draw.polygon(screen, ORANGE, [[798-295, 60], [798-295, 20], [798-284, 50]], 0)
	pygame.draw.polygon(screen, WHITE, [[800-266, 150], [800-300, 160], [800-300, 178], [800-266, 167]], 0)
	pygame.draw.polygon(screen, WHITE, [[800-266, 190], [800-300, 205], [800-300, 225], [800-266, 210]], 0)
	pygame.draw.polygon(screen, WHITE, [[800-266, 236], [800-300, 251], [800-300, 266], [800-266, 255]], 0)
	pygame.draw.polygon(screen, WHITE, [[800-266, 115], [800-300, 125], [800-300, 140], [800-266, 130]], 0)
	pygame.draw.rect(screen, BLACK, [768-266, 100, 33, 166], 2)
	pygame.draw.circle(screen, WHITE, [800-282, 100], 17, 0)
	pygame.draw.line(screen, BLACK, [800-280, 100], [800-280, 66], 2)
	pygame.draw.circle(screen, BLACK, [800-282, 100], 17, 2)
		
	# important lines 
	pygame.draw.line(screen, BLACK, [325, 520], [400, 466], 2)
	pygame.draw.line(screen, BLACK, [633, 710], [400, 466], 2)
	pygame.draw.line(screen, BLACK, [400, 204], [400, 466], 2)
	pygame.draw.line(screen, BLACK, [400, 204], [757, 550], 2)
	pygame.draw.line(screen, BLACK, [400, 204], [255, 340], 2)
	
	pygame.display.flip()
	
	clock.tick(60)
	
pygame.quit()