# WRITE YOUR SOLUTION HERE:
	import pygame
	class Robot:   
	    def __init__(self, y: int) -> None:
	        self.x: int = 0
	        self.y: int = y
	        self.char = pygame.image.load("robot.png")
	 
	    def go_up(self):
	        self.y += -10 if self.y > 0 else 0        
	 
	    def go_down(self):
	        limit_y: int = window.get_height() - (self.char.get_height()+10)
	        self.y += 10 if self.y < limit_y else 0
	    
	    def go_left(self):
	        self.x += -10 if self.x > 0 else 0        
	    
	    def go_right(self):
	        limit_x = window.get_width() - self.char.get_width()
	        self.x += 10 if self.x < limit_x else 0       
	 
	width, height = (640,480)
	window = pygame.display.set_mode((width,height))
	player1 = Robot(0)
	player2 = Robot(height-90)
	pressed_1: str = ""
	pressed_2: str = ""
	time_game = pygame.time.Clock() 
	pygame.init()
	start_game: bool = True

	while start_game:
	    for event in pygame.event.get():
	        if event.type == pygame.QUIT:
	            start_game = False
	        if event.type == pygame.KEYDOWN:           
	            if event.key == pygame.K_UP:
	                pressed_1 = "up"
	            if event.key == pygame.K_DOWN:
	                pressed_1 = "down"
	            if event.key == pygame.K_LEFT:
	                pressed_1 = "left"
	            if event.key == pygame.K_RIGHT:
	                pressed_1 = "right"
	            if event.key == pygame.K_w:
	                pressed_2 = "up"
	            if event.key == pygame.K_s:
	                pressed_2 = "down"
	            if event.key == pygame.K_a:
	                pressed_2 = "left"
	            if event.key == pygame.K_d:
	                pressed_2 = "right"
                
	        if event.type == pygame.KEYUP:            
	            pressed_1 = ""
	            pressed_2 = ""
	    
	    window.fill((0,0,0))    
	    if pressed_1 != "":        
	        if pressed_1 == "up":
	            player1.go_up()
	        if pressed_1 == "down":
	            player1.go_down()
	        if pressed_1 == "left":
	            player1.go_left()
	        if pressed_1 == "right":
	            player1.go_right()
	    
	    if pressed_2 != "":
	        if pressed_2 == "up":
	            player2.go_up()
	        if pressed_2 == "down":
	            player2.go_down()
	        if pressed_2 == "left":
	            player2.go_left()
	        if pressed_2 == "right":
	            player2.go_right() 
	    
	    window.blit(player1.char,(player1.x,player1.y))
	    window.blit(player2.char,(player2.x,player2.y))
	    pygame.display.flip()
	    time_game.tick(60)
    
