'''
Created on 12 Apr 2012

@author: Thibault
'''

from iaproject.game.voiture import Voiture



class Action(object):
    
    def __init__(self, voiture_id, startposition):
        self.position = startposition
        self.voiture = Voiture(voiture_id, startposition)


    def avancer_voiture(self):
        position = self.voiture.avancer()
        
        return position
        
        
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