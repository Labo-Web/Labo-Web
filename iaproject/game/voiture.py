#coding=utf-8

'''
Created on 5 Apr 2012

@author: Thibault
'''
import math

class Voiture(object):
    
    '''
    Avec @property, je crée des getters public + des champs privés ! -> AH NON !
    '''
    
    @property
    def id(self):
        return self._id
    
    @property
    def position(self):
        return self._position
    
    
    def _get_vitesse(self):
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
            self._angle_volant = Voiture.angle_volant_max()
        elif value < self.angle_volant_min():
            self._angle_volant = Voiture.acceleration_min()
        else :
            self._angle_volant = value

    angle_volant = property(_get_angle_volant, _set_angle_volant)
    get_vitesse = property(_get_vitesse)



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
        return 0.0
    
    @staticmethod
    def acceleration_max():
        return 2.0
        
         
    def __init__(self, id, position, vitesse=0, angle=0, angle_volant=0):
        '''
        Constructor
        ''' 
        self._id = id
        self._position = position
        self._vitesse = vitesse
        self._angle = angle
        self._angle_volant = angle_volant
        self._hasBonus = False
    
    
        
    def accelerer(self, acceleration):
        '''
        vitesse * acceleration avec acceleration compris entre 0 et 2
        '''
        if acceleration > self.acceleration_max():
            acceleration = self.acceleration_max()
        if acceleration < self.acceleration_min():
            acceleration = self.acceleration_min()
        
        if self._vitesse == 0 and acceleration >= 1.0:
            self._vitesse = acceleration
        elif self._vitesse == 0 and acceleration <= 1.0:
            self._vitesse = 0
        else: 
            self._vitesse = self._vitesse * acceleration
        
        if self._vitesse > self.vitesse_max():
            self._vitesse = self.vitesse_max()
        if self._vitesse < self.vitesse_min():
            self._vitesse = self.vitesse_min()
            
        return self._vitesse
            
            
            
    def tourner(self):
        '''
        ajout de l'angle du volant à l'angle de la voiture
        '''
        self._angle = self._angle + self.angle_volant
        if self._angle > 360:
            self._angle = self._angle % 360
        return self._angle
    
    def zoneDistance(self, posX, posY):
        zoneDist = math.sqrt( pow(self._position.x - posX, 2) + pow(self._position.y - posY, 2) )
        
        if zoneDist < 2:
            return True
        
        return False
    
    def bonusDistance(self, bonuses):
        for bonus in bonuses:
            bonusDist = math.sqrt( pow(self._position.x - bonus.position.x, 2) + pow(self._position.y - bonus.position.y, 2) )
        
            if bonusDist < 2:
                self.bindBonus(bonus)
                
    def bindBonus(self, bonus):
        self.bonus = bonus
        self.hasBonus = True
        
    def useBonus(self):
        self.hasBonus = False
        # TODO : FINISH !
           
    def avancer(self):
        '''
        calcul et retour de la position sur les axes x et y
        '''
        radian_angle = math.radians(self._angle)
        self.position.x = self.position.x + int(round(self._vitesse * math.cos(radian_angle)))
        self.position.y = self.position.y + int(round(self._vitesse * math.sin(radian_angle)))
        
        return self.position
    
    

    
    
        
        
        
    
        
        
        