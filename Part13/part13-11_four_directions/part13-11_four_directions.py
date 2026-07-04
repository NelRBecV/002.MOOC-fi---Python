# WRITE YOUR SOLUTION HERE:
import pygame
 
screen = pygame.display.set_mode((640,480))
robot = pygame.image.load("robot.png")
timer = pygame.time.Clock()
 
pygame.init()
x: int = 0
y: int = 0
game_on: bool = True
vertical: bool = False
horizontal: bool = False
y_move: int = 0
x_move: int = 0

while game_on:
    screen.fill((0,0,0))
    for event in pygame.event.get():        
        if event.type == pygame.KEYDOWN:            
            if event.key == pygame.K_UP:
                vertical = True
                y_move = -1
            if event.key == pygame.K_DOWN:
                vertical = True
                y_move = 1
            if event.key == pygame.K_LEFT:
                horizontal = True
                x_move = -1
            if event.key == pygame.K_RIGHT:
                horizontal = True
                x_move = 1
              
        if event.type == pygame.KEYUP:
            vertical = False
            horizontal = False
 
        if event.type == pygame.QUIT:
            game_on = False
 
    if vertical:
        y += y_move*10
    if horizontal:
        x += x_move*10
    
    screen.blit(robot, (x,y))
    pygame.display.flip()
    timer.tick(60)
pygame.QUIT



