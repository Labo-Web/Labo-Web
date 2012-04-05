#coding=utf-8

'''
Created on 5 Apr 2012

@author: Thibault
'''
import math

class Voiture(object):
    
    '''
    Avec @property, je crée des getters public + des champs privés !
    '''
    
    @property
    def id(self):
        return self._id
    
    @property
    def position(self):
        return self._position
    
    @property
    def vitesse(self):
        return self._vitesse
    
    @property
    def angle(self):
        return self._angle
    
    
    

    '''
    Avec @x.setter, je crée des setters
    L'utilisateur n'a accès qu'à l'angle du volant en public
    On check la valeur entré
    '''
   
    def _get_angle_volant(self):
        return self._angle_volant
   
    def _set_angle_volant(self, value):
        if value > self.angle_volant_max():
            print("valeur supérieure autorisé : %s" % value )
            print("valeur max : %s" % Voiture.angle_volant_max() )
            self._angle_volant = Voiture.angle_volant_max()
        elif value < self.angle_volant_min():
            print("valeur inférieure autorisé : %s" % value )
            self._angle_volant = Voiture.acceleration_min()
        else :
            print("valeur autorisé : %s" % value )
            self._angle_volant = value
    

    angle_volant = property(_get_angle_volant, _set_angle_volant)

    '''
    Ici on défini les valeur max et min de tous nos champs
    '''

    @staticmethod
    def vitesse_max():
        return 100
    
    @staticmethod
    def vitesse_min():
        return 0
    
    @staticmethod
    def angle_volant_max():
        return 30
    
    @staticmethod
    def angle_volant_min():
        return -30
    
    @staticmethod
    def acceleration_min():
        return 0
    
    @staticmethod
    def acceleration_max():
        return 2
        
    
    
    def __init__(self, id, position, vitesse=0, angle=0, angle_volant=0):
        '''
        Constructor
        ''' 
        self._id = id
        self._position = position
        self._vitesse = vitesse
        self._angle = angle
        self._angle_volant = angle_volant
    
    
        
    def accelerer(self, acceleration):
        '''
        vitesse * acceleration avec acceleration compris entre 0 et 2
        '''
        if acceleration > self.acceleration_max():
            acceleration = self.acceleration_max()
        if acceleration < self.acceleration_min():
            acceleration = self.acceleration_min()
        
        self.vitesse = self.vitesse * acceleration
        
        if self.vitesse > self.vitesse_max():
            self.vitesse = self.vitesse_max()
        if self.vitesse < self.vitesse_min():
            self.vitesse = self.vitesse_min()
        
        return self.vitesse
            
            
            
    def tourner(self):
        '''
        ajout de l'angle du volant à l'angle de la voiture
        '''
        self.angle = self.angle + self.angle_volant
        if self.angle > 360:
            self.angle = self.angle % 360
            
        return self.angle
        
           
            
    def avancer(self):
        '''
        calcul et retour de la position sur les axes x ete y
        '''
        radian_angle = math.radians(self.angle)
        
        self.position["x"] = self.vitesse * math.cos(radian_angle)
        self.position["y"] = self.vitesse * math.sin(radian_angle)
        
        return self.position
    
    

    
    
        
        
        
    
        
        
        