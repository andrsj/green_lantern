import pytest
import lonely_robot


class TestAsteroidAndRobotCreation:
    def test_parameters(self):
        x, y = 10, 15
        asteroid = lonely_robot.Asteroid(x, y)
        assert len(asteroid._obstacles) == 2

        robot = lonely_robot.Robot(x, y, asteroid, 'N')
        assert robot.x == 10
        assert robot.y == 15
        assert robot.asteroid == asteroid
        assert robot.direction == 'N'

    @pytest.mark.parametrize(
        'asteroid_size, count_of_obstacles',
        (
            ((21, 11), 3),
            ((11, 11), 2),
            ((31, 35), 6),
            ((9, 11), 1),
            ((101, 101), 20)
        )
    )
    def test_to_many_obstacles(self, asteroid_size: tuple, count_of_obstacles: int):
        asteroid = lonely_robot.Asteroid(*asteroid_size)
        assert len(asteroid._obstacles) == count_of_obstacles

    @pytest.mark.parametrize(
        'direction',
        ('', 'M', 'I', 'Xla', 'L', '2')
    )
    def test_check_wrong_direction(self, direction: str):
        asteroid = lonely_robot.Asteroid(10, 10)
        with pytest.raises(lonely_robot.InvalidDirection):
            lonely_robot.Robot(5, 5, asteroid, direction)

    @pytest.mark.parametrize(
        "asteroid_size,robot_coordinates",
        (
            ((15, 25), (26, 30)),
            ((15, 25), (26, 24)),
            ((15, 25), (15, 27)),
        )
    )
    def test_check_if_robot_on_asteroid(self, asteroid_size: tuple, robot_coordinates: tuple):
        with pytest.raises(lonely_robot.MissAsteroidError):
            asteroid = lonely_robot.Asteroid(*asteroid_size)
            lonely_robot.Robot(*robot_coordinates, asteroid, 'N')


@pytest.fixture()
def create_asteroid_and_robot():
    asteroid = lonely_robot.Asteroid(30, 25)
    robot = lonely_robot.Robot(15, 15, asteroid, 'N')
    return asteroid, robot


class TestMovingRobot:

    @pytest.fixture(autouse=True)
    def _create_asteroid_and_robot(self, create_asteroid_and_robot):
        self._asteroid, self._robot = create_asteroid_and_robot

    def test_turn_left_one_time(self):
        robot = self._robot
        for direction in ['E', 'S', 'W', 'N']:
            robot.turn_left()
            assert robot.direction == direction

    @pytest.mark.parametrize(
        'input_times, excepted_direction',
        (
            (2, 'S'),
            (3, 'W'),
            (15, 'W')
        )
    )
    def test_turn_left_no_one_time(self, input_times: int, excepted_direction: str):
        robot = self._robot
        robot.turn_left(input_times)
        assert robot.direction == excepted_direction

    def test_turn_right_one_time(self):
        robot = self._robot
        for direction in ['W', 'S', 'E', 'N']:
            robot.turn_right()
            assert robot.direction == direction

    @pytest.mark.parametrize(
        'input_times, excepted_direction',
        (
            (2, 'S'),
            (3, 'E'),
            (13, 'W')
        )
    )
    def test_turn_right_no_one_time(self, input_times: int, excepted_direction: str):
        robot = self._robot
        robot.turn_right(input_times)
        assert robot.direction == excepted_direction

    def test_move_forward(self):
        robot = self._robot
        coordinates = [
            (14, 15),
            (14, 14),
            (15, 14),
            (15, 15)
        ]
        for coord in coordinates:
            robot.turn_left()
            robot.move_forward()
            assert (robot.x, robot.y) == coord

    def test_move_backward(self):
        robot = self._robot
        coordinates = [
            (16, 15),
            (16, 16),
            (15, 16),
            (15, 15)
        ]
        for coord in coordinates:
            robot.turn_left()
            robot.move_backward()
            assert (robot.x, robot.y) == coord

    def test_falls_after_moving(self):
        robot = self._robot

        with pytest.raises(lonely_robot.FallingRobot):
            robot.move_forward(16)

        robot.turn_left()
        with pytest.raises(lonely_robot.FallingRobot):
            robot.move_backward(16)
