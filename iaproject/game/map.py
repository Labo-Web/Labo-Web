'''
Created on 5 Apr 2012

@author: Thibault
'''

class Map(object):

    def __init__(self, id, type, checkpoint, tiles):
        '''
        Constructor
        '''
        self.id = id
        self.type = type
        self.checkpoint = checkpoint
        self.tiles = 1 # liste de tiles
        


class Tile(object):
    
    def __init__(self, type, position):
        self.type = 1
        self.position = position
    
class Position(object):
    
    def __init__(self,x ,y):
        self.x = x
        self.y = y