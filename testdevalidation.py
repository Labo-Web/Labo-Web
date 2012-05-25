'''
Created on 17 avr. 2012

@author: damienp
'''
from com.safeexecution.SafeEvalVisitor import safe_eval
import Queue
import threading
import time


class TestDeValidation(object):
    '''
    classdocs
    '''


    def __init__(self, utilisateur, environment, time_out):
        self.utilisateur = utilisateur
        self.environment = []
        self.environment = environment
        self.time_out = time_out
        self.Queue = Queue.Queue()
        self.startclock = time.clock()
        self.TTest = threading.Thread(target=safe_eval, args=(self.Queue, self.utilisateur.ia,self.environment, self.time_out, self))

    
    def TTestRun(self):
        print self.utilisateur.actionVoiture.voiture.position.x, self.utilisateur.actionVoiture.voiture.position.y
        self.TTest.start()
        
    
    def on_thread_finished_callback(self):
        time.sleep(1)
        print "callbacked"
        self.Check()
        print (time.clock() - self.startclock)
        print self.utilisateur.actionVoiture.voiture.position.x, self.utilisateur.actionVoiture.voiture.position.y
        print 'Test termine'
        
        
        
   
    def Check(self):
        print 'is checking'
    