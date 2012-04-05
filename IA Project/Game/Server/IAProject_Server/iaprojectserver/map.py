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
        self.tiles = tiles
        