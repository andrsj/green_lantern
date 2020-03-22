class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Robot:
    def __init__(self, x, y, asteroid):
        self.x = x
        self.y = y
        self.asteroid = asteroid
        if self.x > self.asteroid.x:
            raise MissAsteroidError()


class MissAsteroidError(Exception):
    pass

# Agenda:
#
#     Create Robot with position and direction
#     Check if Robot miss asteroid while landing
#     Create and test turn_left and turn_right functions
#     Add move_forward, move_backward functions
#     Check if it falls from asteroid during movement
#     Add asteroid obstacles
#     Update robot movement to respect obstacles
