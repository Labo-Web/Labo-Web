'''
Created on 12 Apr 2012

@author: Thibault
'''

from iaprojectserver.voiture import Voiture



class Action(object):
    
    def __init__(self, voiture_id):
        position = {"x":0,"y":0}
        self.voiture = Voiture(voiture_id,position)


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