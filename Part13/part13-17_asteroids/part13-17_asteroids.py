# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint
 
def random_width():
    return randint(10, width - 100)
 
def random_height():
    return randint(10, height * 4)
 
def add_asteriods(rocks:int):
    return [[rock, random_width(),-random_height()] for _ in range (rocks)]
 
width: int = 640
height: int = 480
window = pygame.display.set_mode((width, height))
timer = pygame.time.Clock()
robot = pygame.image.load("robot.png")
rock = pygame.image.load("rock.png")
asteroids: list = add_asteriods(20)

pygame.init()

robot_ready: bool = True
points: int = 0
x: int = window.get_width() // 2
y: int = window.get_height() - robot.get_height()
score = pygame.font.SysFont("Arial", 20)
score_points = score.render(str(points),True,(255,0,0))
pressed: bool = False
move: bool = 0

while robot_ready:
    score_points = score.render(f"Points: {str(points)}", True, (255, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                move = -10
                pressed = True
            if event.key == pygame.K_d:
                move = 10
                pressed = True
        if event.type == pygame.KEYUP:
            pressed = False
    
    if pressed:
        x += move
        if x < 0:
            x += 10
        elif x > width - robot.get_width():
            x -= 10
          
    window.fill((0,0,0))
  
    for stone in asteroids:
        stone[2] += 1
        #if robot catches rock before touching gronud
        if abs(stone[1] - x) < 40 and abs(stone[2] - y) < 40:            
            stone[1] = random_width()
            stone[2] = -random_height()
            points += 1
        #if rock reaches to impact on the ground
        if stone[2] >= height - robot.get_height()//2:            
            points = 0
            y = window.get_height() - robot.get_height()
            x = 0
            asteroids = add_asteriods(20)
            break
        window.blit(stone[0], (stone[1], stone[2]))
    
    timer.tick(60)   
    window.blit(robot,(x,y))
    window.blit(score_points,(width-100,0))
    pygame.display.flip()



