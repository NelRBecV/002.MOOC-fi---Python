# Complete your game here
"""
Tips:
    1 - The game rules are simple: You have to get crossed to the other side of the street avoiding all
        the vehicle coming and going.

    2 - This game has a particular disvantage. You can NOT go back, so if you did a bad move, say goodbye
        to Robbie.

    3 - Unlike other games, you'll lose your earned points if Robbie get rolled over before reaching the
        upper sidewalk

    4 - Car's speed will be increased as you reaches overcoming levels

    5 - Car speed varies unlike truck's. This a vantage yo can use while passing though every level.

    6 - Every level is different to each other but, if you die in , you'll remain in the same level until you solve it

"""

import pygame
import json, time
from random import randint, choice

pygame.init()
pygame.display.set_caption("Robbie Crosses the Street")
width, height = 640, 480
window = pygame.display.set_mode((width, height))
score_font = pygame.font.SysFont("Arial", 24)
end_game = pygame.font.SysFont("Calibri Bold", 80)
bg_color_text = (0, 0, 0)
color_text = (255, 255, 255)


class Car:
    """Creates a car."""
    COLOR = ["blue", "red", "green", "yellow", "orange", "pink", "gray"]
    level = 1

    def __init__(self, row, pos):
        multiplier_x = width // 8  # It´s used to determine which row (X coord) will contains the enemy
        multiplier_y = height // 8  # It´s used to determine which column (Y coord) will contains the enemy
        # separator allows me to put a enemy (Car) away from last one
        separator = multiplier_y // 4
        self._x = (row * multiplier_x) + separator ** pos
        self._y = (row * multiplier_y) + separator
        self.color = choice(Car.COLOR)
        self.__speed = Car.level / 2
        self.car = None
        self.draw()

    def draw(self):
        """Draw a shape that acts as a car"""
        pygame.draw.rect(window, self.color, (self._x, self._y, 50, 40))
        self.car = pygame.draw.rect(window, (0, 0, 0), (self._x, self._y, 50, 40), 2)

    def hit_player(self, coords: tuple):
        """ Checks if either cabin or container hits the runner (player) """
        x, y = coords
        car_x, car_y = self.car.center
        return abs(x - car_x) <= 30 and abs(y - car_y) <= 40

    def move(self):
        self._x -= self.__speed

    def set_start(self):
        """Initialize car's position in the X axis"""
        if self._x < 0:
            self._x = width + 20


class Truck:
    """Creates a Truck"""
    COLOR = ["blue", "red", "green", "yellow", "orange", "pink", "gray"]
    fill = 80
    level = 1

    def __init__(self, row, pos) -> None:
        self.cabin_color = choice(Truck.COLOR)
        self.container_color = choice(Truck.COLOR)
        multiplier_x = width // 8  # It´s used to determine which row (X coord) will contains the enemy
        multiplier_y = height // 8  # It´s used to determine which column (Y coord) will contains the enemy
        # separator allows me to put a enemy (Truck) away from last one
        separator = multiplier_y // 4
        self._x_container = (row * multiplier_x) - separator ** pos
        self._y_container = (row * multiplier_y) + separator
        self._x_cabin = self._x_container + Truck.fill
        self._y_cabin = self._y_container + 5
        self.cabin = None
        self.container = None
        self.__speed = Truck.level / 4
        self.draw()

    def draw(self):
        """Assembles a Truck by drawing two pieces"""
        # draw cabin with black border
        pygame.draw.rect(window, self.cabin_color,
                         (self._x_cabin, self._y_cabin, 30, 30))
        self.cabin = pygame.draw.rect(window, (0, 0, 0),
                                      (self._x_cabin, self._y_cabin, 30, 30), 2)

        # draw container with black border
        pygame.draw.rect(window, self.container_color,
                         (self._x_container, self._y_container, Truck.fill, 40))
        self.container = pygame.draw.rect(window, bg_color_text, (self._x_container,
                                                                  self._y_container, Truck.fill, 40), 2)

    def hit_player(self, coords: tuple):
        """Checks if either cabin or container hits the runner (player)"""
        x, y = coords
        cabin_x, cabin_y = self.cabin.center
        cont_x, cont_y = self.container.center
        return abs(cabin_x - x) <= 20 and abs(cabin_y - y) <= 35 or abs(cont_x - x) <= 50 and abs(cont_y - y) <= 40

    def move(self):
        """Moves the truck though the street"""
        self._x_container += self.__speed
        self._x_cabin += self.__speed

    def set_start(self):
        """displace the enemy to a initial position on screen"""
        if self._x_container > width:
            self._x_container = -Truck.fill
            self._x_cabin = self._x_container + Truck.fill


class Street:
    """Draw a street. The game's scenario."""

    def __init__(self) -> None:
        self.max_h = window.get_height()
        self.max_w = window.get_width()

    def draw_street(self):
        """Draw a paved street with its respective lines"""

        pavement = (150, 150, 150)
        fill = self.max_w + 100
        stretch = -100
        pygame.draw.rect(window, pavement, (-10, 0, self.max_w + 20, 60))
        pygame.draw.rect(window, (0, 0, 0), (stretch, 0, fill + 20, 60), 2)
        pygame.draw.rect(window, pavement, (-10, self.max_h - 60, self.max_w + 20, 60))
        pygame.draw.rect(window, (0, 0, 0), (stretch, self.max_h - 60, fill + 20, 60), 2)
        for line in range(self.max_h - 120, 60, -60):
            strip = -20
            if not line == self.max_h / 2:
                while strip <= self.max_w + 20:
                    pygame.draw.rect(window, color_text, (strip, line, 100, 10))
                    pygame.draw.rect(window, bg_color_text, (strip, line, 100, 10), 2)
                    strip += 110
            else:
                pygame.draw.rect(window, color_text, (strip, self.max_h / 2, self.max_w + 100, 10))
                pygame.draw.rect(window, bg_color_text, (strip, self.max_h / 2, self.max_w + 100, 10), 2)


class Player:
    """Creates the game's playable character"""

    def __init__(self) -> None:
        self.char = pygame.image.load("robot.png")
        self.robot = pygame.transform.scale(self.char, (30, 50))
        self._initial_x = width // 2
        self._initial_y = height - self.robot.get_height()
        self.x = self._initial_x
        self.y = self._initial_y

    @property
    def player_location(self):
        """brings information about character's current location"""
        x = self.x + self.robot.get_width() // 2
        y = self.y + self.robot.get_height() // 2
        return x, y

    def move_forward(self):
        """moves the character ahead"""
        if self.y > 0:
            self.y -= 5
        self.update_char()

    def move_left(self):
        """moves the character to the left"""
        if self.x > 0:
            self.x -= 5
        self.update_char()

    def move_right(self):
        """moves the character to the right"""
        if self.x < width - self.robot.get_width():
            self.x += 5
        self.update_char()

    def reach_other_side(self):
        """verifies if player have succeeded crosing the street"""
        return self.y <= 10

    def update_char(self):
        """redraw player's character"""
        window.blit(self.robot, (self.x, self.y))

    def set_start(self):
        """returns the robot to its initial position"""
        self.x = self._initial_x
        self.y = self._initial_y
        self.update_char()


class Scores:
    """shows all information board"""

    def __init__(self) -> None:
        self.score = 0
        self.points = {}
        self.level_points = 0

    def increment_score(self):
        """keep a track of players's progress"""
        self.score += 0.5
        self.level_points += 0.5

    def update_board(self):
        """update player progress through levels"""
        bg_score = score_font.render(
            f"Score: {int(self.score)}", True, bg_color_text)
        score = score_font.render(f"Score: {int(self.score)}", True, color_text)
        window.blits([(bg_score, (2, 0)), (score, (0, 1))])

    def failed_attempt(self):
        """reset everything done by the player before crashing"""

        self.score -= self.level_points
        self.reset_level_points()

    def reset_level_points(self):
        """restart points counter"""
        self.level_points = 0

    def save_points(self):
        """saves player's achievements into a JSON file"""
        new_board = {}
        if len(self.points) > 1:
            for key, value in self.points.items():
                if self.score > value:
                    new_board[key] = self.score
                    self.score = value
                else:
                    new_board[key] = value
        else:
            new_board['player_1'] = self.score
            new_board['player_2'] = 0
            new_board['player_3'] = 0
            new_board['player_4'] = 0
            new_board['player_5'] = 0

        print(new_board)
        with open(".\scores.json", "w") as scores:
            json.dump(new_board, scores)

    def get_scores(self):
        """retrieves high scores from a JSON file"""
        try:
            with open(".\scores.json", "r") as score_board:
                data_file = json.load(score_board)
                self.points.update(data_file)
        except FileNotFoundError:
            self.points['player_1'] = 0


    def show_hi_scores(self):
        """shows the highest score any player has gotten so far"""

        self.get_scores()
        points = self.points['player_1']
        points = int(self.score) if points < self.score else int(points)
        bg_hi_score = score_font.render(f"Hi-score: {points}", True, bg_color_text)
        hi_score = score_font.render(f"Hi-score: {points}", True, color_text)
        score_width = (width / 2) - hi_score.get_width() / 2
        window.blits([(bg_hi_score, (score_width, 1)), (hi_score, (score_width - 2, 0))])


    def show_level(self, level):
        """shows the current play level"""

        bg_lvl_board = score_font.render(f"Level: {level}", True, bg_color_text)
        lvl_board = score_font.render(f"Level: {level}", True, color_text)
        level_width = width - bg_lvl_board.get_width()
        window.blits([(bg_lvl_board, (level_width - 2, height - 32)), (lvl_board, (level_width - 4, height - 30))])

    def show_remaining_lives(self, lives):
        """shows how many chances left to the player"""

        bg_lives = score_font.render(f"Lives: {lives}", True, bg_color_text)
        lives = score_font.render(f"Lives: {lives}", True, color_text)
        lives_width = width - lives.get_width() / 2
        window.blits([(bg_lives, (lives_width - 40, 0)), (lives, (lives_width - 42, 1))])

    def start_game(self):
        """indicates the pleyer to be ready before the game starts"""
        x = width // 2
        y = height // 2
        messages = pygame.font.SysFont("Arial", 30)

        window.fill((120, 120, 120))
        bg_msg = messages.render(f"Level {level}", True, bg_color_text)
        msg = messages.render(f"Level {level}", True, color_text)
        window.blits([(bg_msg, (x + 3, y + 3)), (msg, (x, y))])
        update_screen()
        time.sleep(1)

        window.fill((120, 120, 120))
        bg_msg = messages.render("Set", True, bg_color_text)
        msg = messages.render("Set", True, color_text)
        window.blits([(bg_msg, (x + 3, y + 3)), (msg, (x, y))])
        update_screen()
        time.sleep(1)

        window.fill((120, 120, 120))
        bg_msg = end_game.render("GO", True, bg_color_text)
        msg = end_game.render("GO", True, color_text)
        window.blits([(bg_msg, (x + 4, y + 4)), (msg, (x, y))])
        update_screen()
        time.sleep(0.5)


def update_screen():
    """update play screen"""
    pygame.display.flip()


def update_screen_items():
    """update game elements"""
    player1.update_char()
    player_score.update_board()
    player_score.show_hi_scores()
    player_score.show_level(level)
    player_score.show_remaining_lives(lives)


def generate_enemies():
    """creates the correspondant enemies to the current level"""
    enemies = []
    for m in range(1, 7):
        coin = randint(1, 2)
        times = randint(1, 3)
        for n in range(1, times + 1):
            if coin == 1:
                enemies.append(Car(m, n))
            else:
                enemies.append(Truck(m, n))
    return enemies


timer = pygame.time.Clock()
cars = generate_enemies()

player1 = Player()
street = Street()
fwrd = False
lives = 3
level = 1
sides = 0
player_score = Scores()
while True:
    window.fill((120, 120, 120))
    player_score.start_game()
    update_screen()
    player1.set_start()
    start = True
    while start:
        timer.tick(60)
        window.fill((120, 120, 120))
        street.draw_street()
        update_screen_items()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            # setting anction keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    fwrd = True
                if event.key == pygame.K_a:
                    sides = 1
                if event.key == pygame.K_d:
                    sides = 2
            if event.type == pygame.KEYUP:
                fwrd = False
                sides = 0

            if fwrd:
                if player1.player_location[1] > 20:
                    player_score.increment_score()
                player1.move_forward()
            if sides == 1:
                player1.move_left()
            elif sides == 2:
                player1.move_right()

        crash = False
        for car in cars:

            # checking if some vehicle rolled over Robbie
            if car.hit_player(player1.player_location):
                crash = True

            car.set_start()
            car.move()
            car.draw()

            # Robbie was hit while trying to cross
            if crash:
                sign_x = width // 2 - 150
                sign_y = height // 2 - 50
                start = False
                player_score.failed_attempt()
                bg_lose = end_game.render("CRASHED", True, bg_color_text)
                lose = end_game.render("CRASHED", True, color_text)
                player1.update_char()
                window.blits([(bg_lose, (sign_x + 4, sign_y + 4)), (lose, (sign_x, sign_y))])
                lives -= 1
                update_screen()
                time.sleep(1)
                break
        update_screen()

        # The player has won
        if player1.reach_other_side():
            sign_width = width // 2 - 200
            sign_height = height // 2 - 50
            bg_won = end_game.render("YOU CROSSED", True, bg_color_text)
            won = end_game.render("YOU CROSSED", True, color_text)
            player_score.reset_level_points()
            window.blits([(bg_won, (sign_width, sign_height)), (won, (sign_width - 4, sign_height - 4))])
            update_screen()
            time.sleep(3)
            level += 1
            Car.level = level
            Truck.level = level
            cars = generate_enemies()
            break

    # The player has lost
    if lives == 0:
        x = width // 2 - 150
        y = height // 2 - 50
        window.fill((120, 120, 120))
        street.draw_street()
        bg_end = end_game.render("GAME OVER", True, (0, 0, 0))
        end = end_game.render("GAME OVER", True, (255, 255, 255))
        window.blits([(bg_end, (x + 4, y + 4)), (end, (x, y))])
        update_screen()
        player_score.save_points()
        time.sleep(3)
        break
