#coding=utf-8
from iaproject.game.bonus import Bonus
from iaproject.game.common.utils import Position
import math

class Zone(object):
    
    def __init__(self, id, position, angle):
        '''
        Constructor
        '''
        self.id = id
        self.position = position
        
        self.radian_angle = math.radians(angle)
        
        self.bonuses = []
        self.bonuses.append(Bonus(1, Position(self.position.x + math.cos(self.radian_angle) * - 2, self.position.y + math.sin(self.radian_angle))))
        self.bonuses.append(Bonus(2, Position(self.position.x + math.cos(self.radian_angle) * - 1, self.position.y + math.sin(self.radian_angle))))
        self.bonuses.append(Bonus(3, Position(self.position.x + math.cos(self.radian_angle) * 1, self.position.y + math.sin(self.radian_angle))))
        self.bonuses.append(Bonus(4, Position(self.position.x + math.cos(self.radian_angle) * 2, self.position.y + math.sin(self.radian_angle))))
        
    def get_frame_value(self):
        json = {"id": self.id, 
                "x": self.position.x ,
                "y": self.position.y ,
                }
        print "JSON FRAME VALUE", json
        return json