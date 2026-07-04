# WRITE YOUR SOLUTION HERE:
import pygame, random
 
pygame.init()
 
window = pygame.display.set_mode((1024,800))
robot = pygame.image.load("robot.png")
n = 0
while True:   
    for event in pygame.event.get():
        for i in range(0, 1000):
            if n < 1000:
                x = random.randint(0, window.get_width()-50)
                y = random.randint(0, window.get_height()-80)
                # 50 and 80 is the robot width-height set meassurement
              
                window.blit(robot,(x,y))
                n += 1
        if event.type == pygame.QUIT:
            exit()    
    pygame.display.flip()
 
