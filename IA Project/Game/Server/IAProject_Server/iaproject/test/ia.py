'''
Created on 16 Apr 2012

@author: Thibault
'''
from iaproject.exception.game import RunNotImplementedException
from iaproject.game.voiture import Voiture


class PlayerWrapper(object):
    
    def __init__(self, voiture_id, y_position):
        position = {"x":0,"y":y_position}
        self.voiture = Voiture(voiture_id, position)
        
    
    def run(self):
        raise RunNotImplementedException("Implemente run mongolien")
    
    
    def get_frame_value(self, texture=0, id=0 ):
        return {"id" : id , "texture"  : texture , "x" : self.voiture.position['x'] ,"y" : self.voiture.position['y'] ,"angle" : self.voiture.angle }
    
        
class GameTest(PlayerWrapper):
    
    def run(self):
        self.voiture.accelerer(1.6)
    
    
    


    
    
    