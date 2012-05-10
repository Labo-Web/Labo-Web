'''
Created on 5 Apr 2012

@author: Thibault
'''

from iaproject.game.action import Action
from iaproject.game.voiture import Voiture
import unittest




class TestVoitureFunctions(unittest.TestCase):
    
    
    def setUp(self):
        position = {"x":0,"y":0}
        self.voiture = Voiture(1,position)
        self.voiture.angle_volant = 300
        
        
    def test_voiture_ctr(self):
        self.assertIsInstance(self.voiture, Voiture, "test instanciation voiture : echec")
        
        
    def test_angle_volant(self):
        self.assertEqual(self.voiture.angle_volant, Voiture.angle_volant_max(), "test angle volant : echec")
        
        
    def test_tourner_voiture(self):
        self.voiture.tourner()
        self.voiture.tourner()
        self.assertEqual(self.voiture._angle, 60, "test angle voiture : echec")
        
        
    def test_accelerer_voiture(self):
        self.test_tourner_voiture()

        self.voiture.accelerer(2.0)
        self.voiture.accelerer(1.8)
        self.voiture.accelerer(1.6)
        self.voiture.accelerer(2)
        
        self.assertAlmostEqual(self.voiture._vitesse, 11.52, None, "test vitesse voiture (acceleration) : echec", 0.0000001)
        
        
    def test_freiner_voiture(self):
        self.voiture.accelerer(2.0)
        self.voiture.accelerer(2.0)
        self.voiture.accelerer(0.6)
        
        self.assertAlmostEqual(self.voiture._vitesse, 2.4, None, "test vitesse voiture (freinage) : echec", 0.0000001)
        
        
    def test_avancer_voiture(self):
        self.voiture.accelerer(2.0)
        self.voiture.accelerer(2.0)
        self.voiture.accelerer(2.0)
        self.voiture.accelerer(2.0)
        
        self.voiture.tourner()
        self.voiture.avancer()
        
        self.assertEqual(self.voiture._position, {'y':8, 'x':14}, "test position voiture : echec")




class TestActionFonctions(unittest.TestCase):
    
    
    def setUp(self):
        self.action = Action(1)
        self.action.voiture._vitesse = 3
   
    def test_action_tourner_volant_voiture(self):
        angle_volant = self.action.tourner_volant_voiture(24)
        self.assertEqual(angle_volant, 24, "test action angle volant : echec")
    
    
    def test_action_tourner_voiture(self):
        self.action.tourner_volant_voiture(24)
        self.action.tourner_voiture()
        angle = self.action.tourner_voiture()
        
        self.assertEqual(angle, 48, "test action angle voiture : echec")
    
    
    def test_action_accelerer_voiture(self):
        self.action.accelerer_voiture(2.0)
        self.action.accelerer_voiture(1.8)
        self.action.accelerer_voiture(1.6)
        vitesse = self.action.accelerer_voiture(2.0)
        
        self.assertAlmostEqual(vitesse, 11.52, None, "test action vitesse voiture : echec", 0.0000001)
   
   
    def test_action_avancer_voiture(self):
        self.action.tourner_volant_voiture(24)
         
        self.action.accelerer_voiture(2.0)
        self.action.accelerer_voiture(1.4)
        self.action.accelerer_voiture(1.6)
        self.action.accelerer_voiture(2.0)
        
        self.action.tourner_voiture()
        self.action.tourner_voiture()
        self.action.avancer_voiture()
    
        self.assertEqual(self.voiture._position, {'y':7, 'x':6}, "test position voiture : echec")

class testBonus(unittest.TestCase):
    def setUp(self):
        self.action = Action(1)
        self.action.hasBonus()
        self.action.useBonus()


if __name__ == '__main__':
    unittest.main()