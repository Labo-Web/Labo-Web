#coding=utf-8
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
    def frame_rate(rate=60):
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
        self.emit("voitures_json", json.dumps(self.voitures))
        
    def on_start(self, msg):
        '''
        Démarre la partie avec notre boucle d'envoi des coordonnées des voitures 
        générées par le moteur de jeu
        '''
        print "Start event | message received :", msg
        self.draw_id = 0
        
        def main_loop():
            while self.socket.connected:
                self.draw_id+=1
                print "Loop ID =", self.draw_id
                with open(PROJECT_PATH+'/static/js/voitures'+str(self.draw_id)+'.json', 'r') as voitures_json: 
                    self.voitures = json.loads(voitures_json.read())
                self.emit('frame', json.dumps(self.voitures))
                print "frame emitted !"
                if self.draw_id == 8:
                    print "stop there !"
                    self.kill_local_jobs()
                print "sleeping ..."
                gevent.sleep(GameNamespace.frame_rate())
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

