#coding=utf-8
from iaproject.game.bonus import Bonus
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
        self.bonuses.append(Bonus(1, {"x":self.position.x + math.cos(self.radian_angle) * - 2, "y": self.position.y + math.sin(self.radian_angle)}))
        self.bonuses.append(Bonus(2, {"x":self.position.x + math.cos(self.radian_angle) * - 1, "y": self.position.y + math.sin(self.radian_angle)}))
        self.bonuses.append(Bonus(3, {"x":self.position.x + math.cos(self.radian_angle) * 1, "y": self.position.y + math.sin(self.radian_angle)}))
        self.bonuses.append(Bonus(4, {"x":self.position.x + math.cos(self.radian_angle) * 2, "y": self.position.y + math.sin(self.radian_angle)}))