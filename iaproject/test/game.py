'''
Created on 11 mai 2012

@author: Sora
'''
from iaproject.game.map import Map, Block, BlockType, Position
import json
import unittest

class MapTestSuite(unittest.TestCase):
    
    def setUp(self):
        self.map = Map(id=0)
        self.block = Block(BlockType.GRASS, Position(10, 20))
    
    def test_dump_map(self):
#        print self.map
        dump = self.map.json_encode()
        print dump
        assert json.loads(dump)
        
    def test_dump_block(self):
        print self.block.json_encode()