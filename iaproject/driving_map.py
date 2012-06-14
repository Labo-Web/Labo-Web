from random import randint
from sympy import Point

MAP_WIDTH = 800
MAP_HEIGHT = 600
MAP_DEVIDED_BY = 10 * 5
BORDER_DIFF = 2

CASES_WIDTH = MAP_WIDTH / MAP_DEVIDED_BY
CASES_HEIGHT = MAP_HEIGHT / MAP_DEVIDED_BY

CASE = {
    'departure' : 1,
    'straight horizontal' : 2,
    'straight vertical' : 3,
    'up right' : 4,
    'up left' : 5,
    'down right' : 6,
    'down left' : 7,
    }

class DrivingMap():
    def __init__(self):
        self.number_of_x = CASES_WIDTH
        self.number_of_y = CASES_HEIGHT

        map_matrix = []
        for line_y in xrange(1, self.number_of_y):
            list_x = []
            for line_x in xrange(1, self.number_of_x):
                list_x.append("0")

            map_matrix.append(list_x)

        self.map_matrix = map_matrix

    def get_value(self, point):
        return self.map_matrix[point.y][point.x]

    def set_value(self, point, value):
        self.map_matrix[point.y][point.x] = value

    def set_departure_point(self):
        random_case = self._get_case_randomly()
        random_point = Point(random_case['x'],random_case['y'])

        self.set_value(random_point, CASE['departure'])
        return random_point

    def set_default_route(self):
        #set square of route
        for case_x in xrange(0, self.number_of_x-1):
            self.set_value(Point(case_x, BORDER_DIFF), CASE['straight horizontal'])

        for case_y in xrange(0, self.number_of_y-1):
            self.set_value(Point(case_y, BORDER_DIFF), CASE['straight vertical'])

        #remove extra route

    def _get_case_randomly(self):
        random_x = randint(2, self.number_of_x-3)
        random_y = randint(2, self.number_of_y-3)

        return { 'x': random_x, 'y' : random_y }