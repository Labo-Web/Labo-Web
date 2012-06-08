'''
Created on 16 Apr 2012

@author: Thibault & modified by Damien
'''
from iaproject.common.utils import Position
from iaproject.game.action import Action


class Ia(object):
    
    def __init__(self, ia_id, texture_id, y_position, stringed_ia, map):
        self.texture_id = texture_id
        self.startposition = Position(300, y_position)
        self.ia_id = ia_id
        self.ia = stringed_ia
        self.actionVoiture = Action(ia_id, self.startposition, map)
        JsonActionEnvironnement = {'tourner_voiture':self.actionVoiture.tourner_voiture, 'get_vitesse':self.actionVoiture.get_vitesse,
                                'accelerer_voiture':self.actionVoiture.accelerer_voiture, 'tourner_volant_voiture':self.actionVoiture.tourner_volant_voiture, 'get_vision':self.actionVoiture.get_vision}
    
        self.environnement = {'Action':JsonActionEnvironnement}
        
    
    def run(self):
        try:
            exec self.ia in self.environnement
            
        except Exception:
            print Exception
            raise NotImplementedError("explosion du code dans run de Ia")
    
    def get_frame_value(self):
        json = {"id": self.actionVoiture.voiture.id, 
                "texture": self.texture_id, 
                "x": self.actionVoiture.voiture.position.x,
                "y": self.actionVoiture.voiture.position.y,
                "angle": self.actionVoiture.voiture.angle 
                }
        print "JSON FRAME VALUE", json
        return json
