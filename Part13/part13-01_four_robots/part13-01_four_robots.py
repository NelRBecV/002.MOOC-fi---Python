# The exercises in this part of the course have no automated tests, as the results as visually verified.
# The tests grant points automatically as you submit your solution to the server, no matter what your implementation.
# Only submit your solution when you are ready, and your solution matches the exercise description.
# The exercises may not have automatic tests, but the course staff will still see your solution.
# If your solution clearly does not match the exercise description, you may lose the points granted for the exercises in this part.
 
# WRITE YOUR SOLUTION HERE:
import pygame
def create_robot():	    
    robot = pygame.image.load("robot.png")
    return robot
 
pygame.init()
 
window = pygame.display.set_mode((1024,800))
height = window.get_height()-90
width = window.get_width()-50
coords = [(0,0),(0,height),(width,0),(width,height)]
robot = create_robot()
window.fill((0,0,0))
while True:
    for event in pygame.event.get():
        for c in coords:
            window.blit(robot, c)
        if event.type == pygame.QUIT:
            exit()
    pygame.display.flip()
        
 
