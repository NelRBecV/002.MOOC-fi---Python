# WRITE YOUR SOLUTION HERE:
import math
import pygame


class Robot:
    COLOR = (0, 0, 0)

    def __init__(self, angle):
        self.angle: int = angle
        self.char = pygame.image.load("robot.png")

    def move_around(self):
        y_length: int = main_window.get_height() // 2
        x_length: int = main_window.get_width() // 2
        radius: int = x_length // 2  # radius is the length of X coordinate
        radians: float = (self.angle / 180) * math.pi  # converts into radians the given angle

        # "sin" and "cos" math properties work angle values as radians
        x = x_length + math.cos(radians) * radius - self.char.get_width() / 2
        y = y_length + math.sin(radians) * radius - self.char.get_height() / 2
        self.angle += 0.5
        main_window.blit(self.char, (x, y))


pygame.init()

main_window = pygame.display.set_mode((640, 480))
robots: list = [Robot(n * 36) for n in range(0, 10)]
my_clock = pygame.time.Clock()
game_on: bool = True

while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False

    main_window.fill(Robot.COLOR)
    for robot in robots:
        robot.move_around()
        
    pygame.display.flip()
    my_clock.tick(60)
