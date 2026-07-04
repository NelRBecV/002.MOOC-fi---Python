# WRITE YOUR SOLUTION HERE:
	import pygame
	 
	screen = pygame.display.set_mode((640,480))
	pygame.init()
	
	ball = pygame.image.load("ball.png")
	time = pygame.time.Clock()
	x = screen.get_width()//2
	y = screen.get_height()//2
	 
	start_bouncing = True
	bounce_x = 1
	bounce_y = 1

	while start_bouncing:
	    for event in pygame.event.get():
	        if event.type == pygame.QUIT:
	            start_bouncing = False
            
	    if x <= 0 or x >= screen.get_width() - ball.get_width():
	        bounce_x *= -1
        
	    if y <= 0 or y >= screen.get_height() - ball.get_height():
	        bounce_y *= -1
        
	    screen.fill((0,0,0))        
	    x += bounce_x 
	    y += bounce_y 
	    screen.blit(ball, (x, y))    
	    pygame.display.flip()
	    time.tick(120)
	 
	    
	pygame.QUIT



