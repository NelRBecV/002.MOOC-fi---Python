# WRITE YOUR SOLUTION HERE:
import pygame
import random
 
pygame.init()
 
window = pygame.display.set_mode((800, 600))
robot = pygame.image.load("robot.png")
n = 0
while True:   
    for event in pygame.event.get():
        for i in range(0, 1000):
            if n < 1000:
                x = random.randint(0, window.get_width()-50)
                y = random.randint(0, window.get_height()-80)
                # 50 and 80 is the robot width-height measurement set
              
                window.blit(robot, (x, y))
                n += 1
        if event.type == pygame.QUIT:
            exit()    
    pygame.display.flip()
