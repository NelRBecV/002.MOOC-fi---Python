import pygame
	 
	robot = pygame.image.load("robot.png")
	width, height = (640,480)
	screen = pygame.display.set_mode((width,height))

	x = 0
	y = 0
	go = True

	while go:
	    for event in pygame.event.get():
	        if event.type == pygame.QUIT:
	            go = False
	        if event.type == pygame.MOUSEMOTION:
	            x = event.pos[0] - robot.get_width() /2
	            y = event.pos[1] - robot.get_height() /2
	 
	        screen.fill((0,0,0))
	        screen.blit(robot, (x,y))
	        pygame.display.flip()
	 
	pygame.QUIT
	 
	 
