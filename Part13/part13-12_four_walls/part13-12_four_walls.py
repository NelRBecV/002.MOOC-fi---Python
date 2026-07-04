# WRITE YOUR SOLUTION HERE:
	import pygame
	 
	robot = pygame.image.load("robot.png")
	screen = pygame.display.set_mode((640,480))
	timer = pygame.time.Clock()
	x: int = 0
	y: int = 0
	x_move:int = 0
	y_move: int = 0
	vertical: bool = False
	horizontal: bool = False	
	game_on: bool = True

  pygame.init()
	 
	while game_on:    
	    limit_x = screen.get_width() - robot.get_width()
	    limit_y = screen.get_height() - robot.get_height()
    
	    for event in pygame.event.get():
	        if event.type == pygame.KEYDOWN:
	            if event.key == pygame.K_w:                              
	                vertical = True
	                y_move = -1
	            if event.key == pygame.K_s:                
	                vertical = True
	                y_move = 1
	            if event.key == pygame.K_a:                
	                horizontal = True
	                x_move = -1
	            if event.key == pygame.K_d:                
	                horizontal = True
	                x_move = 1
	 
	        if event.type == pygame.KEYUP:
	            vertical = False
	            horizontal = False
	            
	        if event.type == pygame.QUIT:
	            game_on = False
	    
	    if vertical:        
	        y += y_move * 10
	        if y < 0:
	            y += 10
            
	        if y > limit_y:
	            y -= 10
	 
	    if horizontal:        
	        x += x_move * 10
	        if x < 0:
	            x += 10
            
	        if x > limit_x:
	            x -= 10
	    
	    screen.fill((0,0,0))
	    screen.blit(robot,(x,y))
	    pygame.display.flip()
	    timer.tick(60)
	



