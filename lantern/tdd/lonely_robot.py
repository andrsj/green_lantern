from functools import partial
import random


class Obstacles:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Asteroid:

    def __init__(self, x: int, y: int):
        self.obstacles = []
        self.x = x
        self.y = y
        for _ in range(x // 10 + y // 10):
            self.create_obstacles()

    def __str__(self):
        return f'Asteroid x = {self.x},\ty = {self.y}'

    def create_obstacles(self, x: int = None, y: int = None):
        if not x:
            x = random.randint(2, self.x - 2)
        if not y:
            y = random.randint(2, self.y - 2)
        self.obstacles.append(Obstacles(x, y))


class Robot:

    _directions = ['N', 'W', 'S', 'E']

    def __init__(self, x: int, y: int, asteroid: Asteroid, direction: str):
        self.x = x
        self.y = y
        self.asteroid = asteroid
        if direction.upper() in Robot._directions:
            self.direction = direction.upper()
        else:
            raise InvalidDirectionError
        if not (self.asteroid.x >= self.x >= 0 and self.asteroid.y >= self.y >= 0):
            raise MissAsteroidError
        for obstacle in self.asteroid.obstacles:
            if self.x == obstacle.x and self.y == obstacle.y:
                raise CrashRobotByObstaclesError

    def __str__(self):
        return f'Robot x = {self.x}, y = {self.y}, direction = {self.direction}\nAsteroid: {self.asteroid}'

    def turn_left(self, times: int = 1):
        self.direction = Robot._directions[(Robot._directions.index(self.direction) - times) % len(Robot._directions)]

    def turn_right(self, times: int = 1):
        self.direction = Robot._directions[(Robot._directions.index(self.direction) + times) % len(Robot._directions)]

    def __change_coord_value(self, value: int, x_direction: bool = True):
        if x_direction:
            if self.asteroid.x >= self.x + value >= 0:
                for _ in range(abs(value)):
                    self.x += 1 if value > 0 else -1
                    for obstacle in self.asteroid.obstacles:
                        if self.x == obstacle.x and self.y == obstacle.y:
                            raise CrashRobotByObstaclesError
            else:
                for obstacle in self.asteroid.obstacles:
                    if self.x == obstacle.x and self.y == obstacle.y:
                        raise CrashRobotByObstaclesError
                raise FallingRobotError
        else:
            if self.asteroid.y >= self.y + value >= 0:
                for _ in range(abs(value)):
                    self.y += 1 if value > 0 else -1
                    for obstacle in self.asteroid.obstacles:
                        if self.x == obstacle.x and self.y == obstacle.y:
                            raise CrashRobotByObstaclesError
            else:
                raise FallingRobotError

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


class InvalidDirectionError(Exception):
    pass


class FallingRobotError(Exception):
    pass


class CrashRobotByObstaclesError(Exception):
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
