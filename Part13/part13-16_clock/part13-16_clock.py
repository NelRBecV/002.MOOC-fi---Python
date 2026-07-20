import pygame
from math import *
from datetime import datetime

BLUE_COLOR: tuple = (0, 0, 255)
RED_COLOR: tuple = (255, 0, 0)

width: int = 800
height: int = 400
center_x: int = window.get_width() // 2
center_y: int = window.get_height() // 2
center: tuple = (center_x, center_y)

window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
timer = pygame.time.Clock()


def get_radius(width_value: int) -> int:
    """Returns an integer represinting the radius value from center"""
    return width_value - int(10 + width_value // 2)


def draw_clock_circles():
    """Shows clock circles"""
  
    pygame.draw.circle(window, RED_COLOR, center, get_radius(center_x), 7)
    pygame.draw.circle(window, RED_COLOR, center, get_radius(center_x // 10))


def create_clock_hand(value: int, max_value: int, line_thickness: int, hand_length: int = 0):
    """Draws a clock hand to the corresponding circle position related to the value given"""
  
    leap: int = 360 // max_value # calculates the hand's leap on clock
    angle: int = 360 + (leap * value) - 90 # calculates the angle depending on the value given    
    x_circle_radius: int = get_radius(center_x)# gets the circle diameter

    x = center_x + cos(radians(angle)) * (x_circle_radius - hand_length)
    y = center_y + sin(radians(angle)) * (x_circle_radius - hand_length)

    pygame.draw.line(window, BLUE_COLOR, (x, y), (circle_width, circle_height), line_thickness)

pygame.init()

stop: bool = False

while not stop:
    hour: int = datetime.now().hour
    minute: int = datetime.now().minute
    second: int = datetime.now().second

    pygame.display.set_caption(f"{hour:0>2}:{minute:0>2}:{second:0>2}")
    window.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True

    create_clock_hand(second, 60, 1, 5)
    create_clock_hand(minute, 60, 3, 5)
    create_clock_hand(hour, 12, 3, 30)

    draw_clock_circles()

    pygame.display.flip()
    timer.tick(60)
