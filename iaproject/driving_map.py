from random import randint
from sympy import Point

MAP_WIDTH = 800
MAP_HEIGHT = 600
MAP_DEVIDED_BY = 10 * 4
BORDER_DIFF = 1

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

        self.map_matrix = []
        
        for line_y in xrange(0, self.number_of_y):
            list_x = []
            for line_x in xrange(0, self.number_of_x):
                list_x.append(0)
            
            self.map_matrix.append(list_x)

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
#        for case_x in xrange(BORDER_DIFF, self.number_of_x-BORDER_DIFF):
#              
#            self.set_value(Point(case_x, BORDER_DIFF), CASE['straight horizontal'])   
#            self.set_value(Point(case_x, self.number_of_y-BORDER_DIFF-1), CASE['straight horizontal'])
#
#        for case_y in xrange(BORDER_DIFF, self.number_of_y-BORDER_DIFF):
#            self.set_value(Point(BORDER_DIFF, case_y), CASE['straight vertical'])
#            self.set_value(Point(self.number_of_x-BORDER_DIFF-1, case_y), CASE['straight vertical'])
#        
#        


        for case_y in xrange(BORDER_DIFF, self.number_of_y-BORDER_DIFF):
            
            for case_x in xrange(BORDER_DIFF, self.number_of_x-BORDER_DIFF):

                if case_y == BORDER_DIFF:
                    self.set_value(Point(case_x, BORDER_DIFF), CASE['straight horizontal'])
                
                elif case_x == BORDER_DIFF:
                    self.set_value(Point(BORDER_DIFF, case_y), CASE['straight vertical'])
                
                elif case_x == self.number_of_y-BORDER_DIFF-1:
                    self.set_value(Point(self.number_of_x-BORDER_DIFF-1, case_y), CASE['straight vertical'])
                
                elif case_y ==  self.number_of_y-BORDER_DIFF-1:   
                    self.set_value(Point(case_x, self.number_of_y-BORDER_DIFF-1), CASE['straight horizontal'])
                    
                if case_x == BORDER_DIFF and case_y == BORDER_DIFF:
                    self.set_value(Point(case_x, case_y), CASE['up right'])
                
                if case_x == self.number_of_x-BORDER_DIFF-1 and case_y == BORDER_DIFF:
                    self.set_value(Point(case_x, case_y), CASE['up left'])
                    
                if case_x == BORDER_DIFF and case_y == self.number_of_y-BORDER_DIFF-1:
                    self.set_value(Point(case_x, case_y), CASE['down right'])
                
                if case_x == self.number_of_x-BORDER_DIFF-1 and case_y == self.number_of_y-BORDER_DIFF-1:
                    self.set_value(Point(case_x, case_y), CASE['down left'])
        
        #set 

    def _get_case_randomly(self):
        random_x = randint(2, self.number_of_x-3)
        random_y = randint(2, self.number_of_y-3)

        return { 'x': random_x, 'y' : random_y }