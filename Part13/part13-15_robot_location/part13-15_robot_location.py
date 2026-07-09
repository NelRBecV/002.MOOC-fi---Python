# WRITE YOUR SOLUTION HERE:
	import pygame
	from random import randint
	 
	robot = pygame.image.load("robot.png")
	width, height = 640, 480
	window = pygame.display.set_mode((width, height))
	pygame.init()

	x = window.get_width()/2
	y = window.get_height()/2
	start_clicking = True
	limit_x = window.get_width() - robot.get_width()
	limit_y = window.get_height() - robot.get_height()

	while start_clicking:
	    new_x = randint(0, limit_x)
	    new_y = randint(0, limit_y)
	    for event in pygame.event.get():
	        if event.type == pygame.QUIT:
	            start_clicking = False
	        if event.type == pygame.MOUSEBUTTONDOWN:
	            x = new_x
	            y = new_y
	            window.fill((0,0,0))
	        window.blit(robot,(x,y))
	        pygame.display.flip()

