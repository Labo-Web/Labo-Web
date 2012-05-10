#coding=utf-8
import random

class BONUSTYPE:
	SPEED = 1
	WEAPON = 2

class Bonus(object):
	def _get_effect_type(self):
		return self.effect_type
	
	def _get_effect_value(self):
		return self.effect_value
	
	def __init__(self, id, position):
		'''
		Constructor
		'''
		self.id = id
		self.position = position
		
		self.effect_type = random.randint(1,2)
		
	def get_frame_value(self):
		json = {"id": self.id, 
                "x": self.position['x'],
                "y": self.position['y'],
                }
		print "JSON FRAME VALUE", json
		return json
		