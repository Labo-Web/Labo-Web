'''
Created on 29 mars 2012

@author: damienp
http://bytes.com/topic/python/answers/521401-threading-event-usage-causing-intermitent-exception
'''
from testdevalidation import TestDeValidation
from iaproject.test.ia import Ia

if __name__ == '__main__':
    
    code = '''
if Action['get_vision'](10,0)!=1:
    Action["accelerer_voiture"](0.1)
else :
    Action["accelerer_voiture"](1.5)
     
     
Action["tourner_volant_voiture"](0)
print "voiture tourne le volant de 5"

Action["tourner_voiture"]()
print "voiture tourne donc de 25"

print "voiture avance"'''
    
    utilisateur = Ia(1, 0, 500, code, None)
    
    dicoThread = {}
    for n in range(0,1):
        dicoThread[n] = TestDeValidation(utilisateur, utilisateur.environnement, 1)
        dicoThread[n].TTestRun()
    