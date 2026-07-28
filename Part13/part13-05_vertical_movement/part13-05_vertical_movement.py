# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()

window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

limit = window.get_height() - robot.get_height()
steps = 0
sign = "+"
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    window.blit(robot, (0, steps))
    if steps == limit:
        sign = "-"
    if steps == 0:
        sign = "+"
    exec(f"steps {sign}= 1")
    pygame.display.flip()
    clock.tick(60)
