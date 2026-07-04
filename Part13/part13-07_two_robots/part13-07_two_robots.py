# WRITE YOUR SOLUTION HERE:
	import pygame
	class Robot:
      '''Creates a moving robot'''
	    def __init__(self, x,y):
	        self.x = x
	        self.y = y
	        self.image = pygame.image.load("robot.png")
	        self.step = 1      
	        
	    def move_forward(self, speed):
          '''Define orientation and movement from robot'''
	        if self.x <= 0:
	            self.step = 1        
	        
	        if self.x >= window.get_width()-self.image.get_width():
	            self.step = -1
	 
	        self.x += (speed * self.step)	        
	        
	        window.blit(self.image,(self.x, self.y))
	    
	window = pygame.display.set_mode((640, 480),pygame.RESIZABLE)
	 
	pygame.init()
	timer = pygame.time.Clock()
	 
	robot1 = Robot(0,window.get_height()//4)
	robot2 = Robot(0,window.get_height()//2)	 
	 
	while True:
	    for event in pygame.event.get():
	        if event.type == pygame.QUIT:
	            exit()
	 
	    window.fill((0, 0, 0))
	    robot1.move_forward(1)
	    robot2.move_forward(15)
	    pygame.display.flip()
	 
	    timer.tick(60)
	    
