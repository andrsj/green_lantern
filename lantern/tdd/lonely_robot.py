from functools import partial
import random


class Obstacles:

    def __init__(self, x: int, y: int):
        self.coordinates = x, y


class Asteroid:

    def __init__(self, x: int, y: int):
        self._obstacles = []
        self.x = x
        self.y = y
        for _ in range(x // 10 + y // 10):
            self.create_obstacles()

    def __str__(self):
        return f'Asteroid x = {self.x},\ty = {self.y}'

    def create_obstacles(self, x: int = None, y: int = None):
        if x:
            x = random.randint(2, self.x - 2)
        if y:
            y = random.randint(2, self.y - 2)
        self._obstacles.append(Obstacles(x, y))


class Robot:

    _directions = ['N', 'W', 'S', 'E']

    def __init__(self, x: int, y: int, asteroid: Asteroid, direction: str):
        self.x = x
        self.y = y
        self.asteroid = asteroid
        if direction.upper() in Robot._directions:
            self.direction = direction.upper()
        else:
            raise InvalidDirection
        if self.x > self.asteroid.x or self.y > self.asteroid.y:
            raise MissAsteroidError

    def __str__(self):
        return f'Robot x = {self.x}, y = {self.y}, direction = {self.direction}\nAsteroid: {self.asteroid}'

    def turn_left(self, times: int = 1):
        self.direction = Robot._directions[(Robot._directions.index(self.direction) - times) % len(Robot._directions)]

    def turn_right(self, times: int = 1):
        self.direction = Robot._directions[(Robot._directions.index(self.direction) + times) % len(Robot._directions)]

    def __change_coord_value(self, value: int, x_direction: bool = True):
        if x_direction:
            if self.x + value <= self.asteroid.x and self.x >= 0:
                self.x += value
            else:
                raise FallingRobot
        else:
            if self.y + value <= self.asteroid.y and self.y >= 0:
                self.y += value
            else:
                raise FallingRobot

    def move_forward(self, value: int = 1):
        moves = {
            'N': partial(self.__change_coord_value, value, False),
            'W': partial(self.__change_coord_value, value),
            'S': partial(self.__change_coord_value, -value, False),
            'E': partial(self.__change_coord_value, -value)
        }
        moves[self.direction]()

    def move_backward(self, value: int = 1):
        moves = {
            'N': partial(self.__change_coord_value, -value, False),
            'W': partial(self.__change_coord_value, -value),
            'S': partial(self.__change_coord_value, value, False),
            'E': partial(self.__change_coord_value, value)
        }
        moves[self.direction]()


class MissAsteroidError(Exception):
    pass


class InvalidDirection(Exception):
    pass


class FallingRobot(Exception):
    pass


# Agenda:
#
#     + Create Robot with position and direction
#     + Check if Robot miss asteroid while landing
#     + Create and test turn_left and turn_right functions
#     + Add move_forward, move_backward functions
#     + Check if it falls from asteroid during movement
#     + Add asteroid obstacles
#     Update robot movement to respect obstacles
