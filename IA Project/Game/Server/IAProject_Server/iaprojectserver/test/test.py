'''
Created on 5 Apr 2012

@author: Thibault
'''

from iaprojectserver.voiture import Voiture
import unittest

class TestVoitureFunctions(unittest.TestCase):
    
    def setUp(self):
        position = {"x":0,"y":0}
        self.voiture = Voiture(1,position)
        
    def test_voiture_ctr(self):
        self.assertIsInstance(self.voiture, Voiture, "test instanciation voiture : echec")
        
    def test_angle_volant(self):
        self.voiture.angle_volant = 300
        self.assertEqual(self.voiture.angle_volant, Voiture.acceleration_max(), "test set angle_volant : echec")
        
        
if __name__ == '__main__':
    unittest.main()