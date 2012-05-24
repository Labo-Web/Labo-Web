'''
Created on 11 mai 2012

@author: Sora
'''
from iaproject.game.map import Map, Block
import json

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Map) or isinstance(obj, Block):
            return obj.json_encode()
        else:
            return json.JSONEncoder.default(self, obj)
        return json.dumps(self.grid)

class Position(object):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y