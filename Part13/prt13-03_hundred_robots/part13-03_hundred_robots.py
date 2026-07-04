# WRITE YOUR SOLUTION HERE:
	import pygame
	 
	pygame.init()
	window = pygame.display.set_mode((640,480))
	path = "robot.png"
	robot = pygame.image.load(path)
	while True:
	    n = 0
	    for c in range(40, 240, 20):
	        for r in range(50, 450,40):
	            window.blit(robot, (r+n,c))
	            n +=1       
	    for event in pygame.event.get():
	        if event.type == pygame.QUIT:
	            exit()
	 
	    pygame.display.flip()
	 
