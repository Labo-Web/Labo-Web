#coding=utf-8
from iaproject.game.map import Position
from iaproject.game.zone import Zone
from iaproject.test.ia import GameTest
from socketio import socketio_manage
from socketio.mixins import BroadcastMixin
from socketio.namespace import BaseNamespace
import gevent
import json
import os

PROJECT_PATH = os.path.dirname(__file__)

def index(request):
    """ Base view to load our template """
    return {}

class GameNamespace(BaseNamespace, BroadcastMixin):
        
    @staticmethod
    def frame_rate(rate=25):
        try:
            assert isinstance(rate, int)
            assert rate > 0
            return 1 / rate 
        except:
            raise Exception("Frame rate value error !!! Should be an Int > 0")
        
    # self.io is the Socket.IO socket
    # self.request is the request
    def on_init(self, msg):
        with open(PROJECT_PATH+'/static/js/map.json', 'r') as map_json: 
            self.map = json.loads(map_json.read())
        
        with open(PROJECT_PATH+'/static/js/voitures.json', 'r') as voitures_json: 
            self.voitures = json.loads(voitures_json.read())
        
        self.emit("map_json", json.dumps(self.map))
        
        # --- CARS
        self.players = [GameTest(1, 0, Position(200, 90)), GameTest(2, 1, Position(300, 78))]
        self.players_json = {"voiture" : [] }
        
        for player in self.players:
            self.players_json["voiture"].append(player.get_frame_value())
        
        #self.emit("voitures_json", json.dumps(self.voitures))
        self.emit("voitures_json", json.dumps(self.players_json))
        self.players_json["voiture"] = []
        
        # --- ZONES
        self.zones = [Zone(1, Position(200, 90), 90), Zone(2, Position(300,78), 45)]
        self.zones_json = {"zone" : [] }
        
        for zone in self.zones:
            self.zones_json["zone"].append(zone.get_frame_value())
        
        self.emit("zones_json", json.dumps(self.zones_json))
        self.zones_json["zone"] = []
        
    def game_run(self):
        for player in self.players:
            player.run()
            for zone in self.zones:
                if player.voiture.zoneDistance(zone.position.x, zone.position.y):
                    player.voiture.bonusDistance(zone.bonuses)
            
            self.players_json["voiture"].append(player.get_frame_value())
        print "Sent JSON=", json.dumps(self.players_json)
        self.emit('frame', json.dumps(self.players_json))
        print "frame emitted !"
        self.players_json["voiture"] = []
        
    def on_start(self, msg):
        '''
        Démarre la partie avec notre boucle d'envoi des coordonnées des voitures
        générées par le moteur de jeu
        '''
        print "Start event | message received :", msg
        gevent.sleep(seconds=3)
        def main_loop():
            while self.socket.connected:
                self.game_run()
                gevent.sleep(seconds=0.05)
        self.spawn(main_loop)
        
    def recv_initialize(self):
        print 'test init'
    
    def on_disconnect(self, data):
        print "disconnecting..."
        self.disconnect()

def socketio_service(request):
    print ('socketio_service requested !')
    retval = socketio_manage(request.environ,
        {
            '': GameNamespace,
        }, request=request
    )

    return retval

