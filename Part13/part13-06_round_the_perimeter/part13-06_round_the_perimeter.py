# # WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()

window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
w_length = window.get_width() - robot.get_width()
h_length = window.get_height() - robot.get_height()
x = 0
y = 0
move_x = 0
move_y = 0

timer = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    window.blit(robot, (x, y))
    if x == 0 and y == 0:
        move_x = 1
        move_y = 0
    elif x == w_length and y == 0:
        move_x = 0
        move_y = 1
    elif x == w_length and y == h_length:
        move_x = -1
        move_y = 0
    elif x == 0 and y == h_length:
        move_x = 0
        move_y = -1

    x += move_x
    y += move_y

    pygame.display.flip()
    timer.tick(60)
