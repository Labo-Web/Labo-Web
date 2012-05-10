'''
Created on 16 Apr 2012

@author: Thibault
'''
from iaproject.exception.game import RunNotImplementedException
from iaproject.game.voiture import Voiture


class PlayerWrapper(object):
    
    def __init__(self, voiture_id, texture_id, position):
        self.texture_id = texture_id
        #self.position = {"x":200,"y":position}
        self.position = position
        self.voiture = Voiture(voiture_id, self.position, 0, 45)
        
    
    def run(self):
        raise RunNotImplementedException("Implemente run mongolien")
    
    
    def get_frame_value(self):
        json = {"id": self.voiture.id, 
                "texture": self.texture_id, 
                "x": self.voiture.position['x'],
                "y": self.voiture.position['y'],
                "angle": self.voiture.angle 
                }
        print "JSON FRAME VALUE", json
        return json

TypeError
        
class GameTest(PlayerWrapper):
    
    def run(self):
        print "RUN !"
        if self.voiture._get_vitesse() < 50:
            self.voiture.accelerer(1.1)
        self.voiture.avancer()
        self.voiture._set_angle_volant(20)
        self.voiture.tourner()
    
    