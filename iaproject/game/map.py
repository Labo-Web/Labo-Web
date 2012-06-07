'''
Created on 5 Apr 2012

@author: Thibault
'''
from iaproject.common.utils import Position
import json
        
class BlockType(object):
    '''
        Enum des Types de bloc
    '''
    GRASS = 0
    ROAD = 1
    TIRE = 2
    SAND = 3

class Block(object):
    
    def __init__(self, type, position):
        if not type  in (BlockType.ROAD, BlockType.TIRE, 
                         BlockType.GRASS, BlockType.SAND):
            # MAIS OU EST BlockTypeNotExistingException
            raise 
        self.type = type
        self.position = position
        
    def __unicode__(self):
        return self.type
    
    def __str__(self):
        return str(self.__unicode__())
    
    def json_encode(self):
        return json.dumps(self.type, cls=CustomEncoder)
        
class Map(object):

    def __init__(self, id, grid=None):
        '''
        Constructor
        '''
        self.id = id
        #map par defaut avec de l'herbe
        self.grid = dict()
        if grid == None:
            for x in range(60):
                row = {}
                for y in xrange(80):
                    row[y] = Block(BlockType.GRASS, Position(x, y))
                    self.grid[x] = row
        else:
            self.grid = grid
            
    def json_encode(self):
        return json.dumps(self.grid, cls=CustomEncoder)
    
    
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Map) or isinstance(obj, Block):
            return obj.json_encode()
        else:
            return json.JSONEncoder.default(self, obj)
        return json.dumps(self.grid)