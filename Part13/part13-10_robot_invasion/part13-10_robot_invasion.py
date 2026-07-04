# WRITE YOUR SOLUTION HERE:
import	pygame
from random import randint


class Robot:
    '''Creates a robot on screen'''
  
    def __init__(self) -> None:
        self.invader = pygame.image.load("robot.png")
        distance_x = window.get_width()-self.invader.get_width()
        self.distance_y = window.get_height()-self.invader.get_height()        
        self._x = randint(0, distance_x)
        self._y = randint(0, window.get_height())*-1
 
    def falling(self):
        '''moves a robot down to the ground'''
      
        if self._y < self.distance_y:
            self._y +=1        
 
    def move_to_sides(self):
        '''moves a robot to aside depending its Y coordinate value'''

        if self.y_coord == self.distance_y:
            if self._x <= window.get_width()//2:
                self._x -= 1
            else:
                self._x += 1        
 
    def show_robot(self):        
        window.blit(self.invader,(self._x,self._y))
        pygame.display.flip()    
 
    @property
    def x_coord(self):
        return self._x
 
    @property
    def y_coord(self):
        return self._y
 
    @property
    def width(self):
        return self.invader.get_width()
 
window = pygame.display.set_mode((640,480))
pygame.init()
fall_time = pygame.time.Clock()
 
robot_troops = []
invade = True
while invade:
    robots = len(robot_troops)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            invade = False
    
    # adds a new robot invader when random value is equal to 50
    if randint(0, 100) == 50:
        robot_troops.append(Robot())
 
    for robot in robot_troops:
        robot.falling()
        robot.move_to_sides()
        robot.show_robot()
 
    for robot in robot_troops:
        x_robot: int = robot.x_coord        
      
        # checks if a robot goes beyond XY coordinates limit
        if x_robot <= 0 - robot.width or x_robot >= window.get_width() + robot.width:
            # if that's so, the robot is removed from platoon
            robot_troops.remove(robot)          
    
    fall_time.tick(60)
pygame.QUIT
