'''
Created on 12 Apr 2012

@author: Thibault
'''

from iaproject.common.utils import Position
from iaproject.game.voiture import Voiture
import math



class Action(object):
    
    def __init__(self, voiture_id, startposition, map):
        self.position = startposition
        self.voiture = Voiture(voiture_id, startposition)
        self.map = map
    
    def get_vision(self, x, y):
        #voiture_position = self.voiture.position()
        #position = Position(voiture_position.x + x, voiture_position.y + y)
        
        radian_angle = math.radians(self.voiture._angle)
        pos_voiture_X = self.voiture.position.x + int(round(x * math.cos(radian_angle)))
        pos_voiture_Y = self.voiture.position.y + int(round(y * math.sin(radian_angle)))
        
        posX = int(round(pos_voiture_X/10))
        posY = int(round(pos_voiture_Y/10))
        if posX >= 0 and posY >= 0 and posX < 80 and posY < 60:
            posX = str(posX)
            posY = str(posY)
            return self.map['cases'][posY][posX]
        else:
            return -1
        
    def tourner_voiture(self):
        angle = self.voiture.tourner()
        return angle
        
        
    def accelerer_voiture(self, acceleration):
        vitesse = self.voiture.accelerer(acceleration)
        return vitesse
        
        
    def tourner_volant_voiture(self, angle_volant):
        angle_volant = self.voiture.angle_volant = angle_volant
        return angle_volant
    
    def get_vitesse(self):
        return self.voiture.get_vitesse