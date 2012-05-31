'''
Created on 10 mai 2012

@author: damienp
'''

from iaproject.game.zone import Zone
from iaproject.test.ia import Ia
from socketio.namespace import BaseNamespace
import gevent
import json
import os
from iaproject.common.utils import Position


PROJECT_PATH = os.path.dirname(__file__)

class GameNamespace(BaseNamespace):
        
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
        
        #msg TOKEN d'appel a la base pour la partie
        
        self.mapcustom = None
        
        #IA D'arrive, ici non presente DON la suite avec 1 user
        self.IAscustom = None
        
        code = '''
if Action['get_vitesse']() < 10:
     Action["accelerer_voiture"](1.5)
     print "voiture accelere a 1.5 car < 10"
     
Action["tourner_volant_voiture"](25)
print "voiture tourne le volant de 25"

Action["tourner_voiture"]()
print "voiture tourne donc de 25"

for n in range(0,5):
     Action["avancer_voiture"]()
     print "voiture avance"'''
    
        self.User1 = Ia(ia_id=1, texture_id=0, y_position=300, stringed_ia=code)
        print 'USER TEST :', self.User1
        
        
        # --- MAP
        self.map = None
        
        if self.map == None:
            self.map = self.get_static_map()
        else:
            self.map = self.mapcustom
         
        print 'MAPS :', json.dumps(self.map) 
        
        self.emit("map_json", json.dumps(self.map))
        
                # --- CARS
        self.players = [self.User1]
        
        self.players_json = {"voiture" : [] }
        
        for player in self.players:
            self.players_json["voiture"].append(player.get_frame_value())
        
        print 'VOITURES :', self.players_json["voiture"]
        
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
        
         
            
    def get_static_map(self):
        with open(PROJECT_PATH+'/static/js/map.json', 'r') as map_json: 
            return json.loads(map_json.read())
        gevent.sleep(seconds=3)
        
        
    def game_run(self):
        for player in self.players:
            player.run()
            posX = str(int(round(player.actionVoiture.voiture.position.x/10)))
            posY = str(int(round(player.actionVoiture.voiture.position.y/10)))
            case = self.map['cases'][posY][posX]
            if case == 3 or (posX == '24') :
                player.actionVoiture.voiture._vitesse = 0
            
            for zone in self.zones:
                if player.actionVoiture.voiture.zoneDistance(zone.position.x, zone.position.y):
                    player.actionVoiture.voiture.bonusDistance(zone.bonuses)
            
            self.players_json["voiture"].append(player.get_frame_value())
        print "Sent JSON=", json.dumps(self.players_json)
        self.emit('frame', json.dumps(self.players_json))
        print "frame emitted !"
        self.players_json["voiture"] = []
        
    def on_start(self, msg):
        '''
        Demarre la partie avec notre boucle d'envoi des coordonnees des voitures
        generees par le moteur de jeu
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