# WRITE YOUR SOLUTION HERE:
	import pygame
	 
	pygame.init()
	window = pygame.display.set_mode((640,480))
	robot = pygame.image.load("robot.png")
	skip = (window.get_width()-100) // 10
	limit = window.get_width() - 50
	
	while True:
	    for event in pygame.event.get():
	        for i in range(skip,limit,skip):
	            window.blit(robot, (i, 150))
	        pygame.display.flip()
	        if event.type == pygame.QUIT:
	            exit()
	 
	 
	 
