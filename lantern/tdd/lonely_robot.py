class Asteroid:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Asteroid x = {self.x},\ty = {self.y}'


class Robot:

    _directions = ['N', 'W', 'S', 'E']

    def __init__(self, x:int, y:int, asteroid:Asteroid, direction:str):
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

    def turn_left(self):
        self.direction = Robot._directions[Robot._directions.index(self.direction) - 1]

    def turn_right(self):
        self.direction = Robot._directions[(Robot._directions.index(self.direction) + 1) % len(Robot._directions)]

    def __change_coord_value(self, value, x_direction=True):
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

    def move_forward(self, value=1):
        moves = {
            'N': (self.__change_coord_value, {'value': value, 'x_direction': False}),
            'W': (self.__change_coord_value, {'value': value}),
            'S': (self.__change_coord_value, {'value': -value, 'x_direction': False}),
            'E': (self.__change_coord_value, {'value': -value})
        }
        moves[self.direction][0](**moves[self.direction][1])

    def move_backward(self, value=1):
        moves = {
            'N': (self.__change_coord_value, {'value': -value, 'x_direction': False}),
            'W': (self.__change_coord_value, {'value': -value}),
            'S': (self.__change_coord_value, {'value': value, 'x_direction': False}),
            'E': (self.__change_coord_value, {'value': value})
        }
        moves[self.direction][0](**moves[self.direction][1])


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
#     Add asteroid obstacles
#     Update robot movement to respect obstacles
