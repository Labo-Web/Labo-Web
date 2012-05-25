'''
Created on 29 mars 2012

@author: damienp
http://bytes.com/topic/python/answers/521401-threading-event-usage-causing-intermitent-exception
'''
from testdevalidation import TestDeValidation
from iaproject.test.ia import Ia

if __name__ == '__main__':
    
    code = '''
if Action['get_vitesse']() < 50:
     Action["accelerer_voiture"](2)
     print "voiture accelere a 2 car < 50"
     
Action["tourner_volant_voiture"](20)
print "voiture tourne le volant de 20"

Action["tourner_voiture"]()
print "voiture tourne donc de 20"
Action["avancer_voiture"]()
print "voiture avance"

Action["avancer_voiture"]()
print "voiture avance"

Action["avancer_voiture"]()
print "voiture avance"

Action["avancer_voiture"]()

print "voiture avance"'''
    
    utilisateur = Ia(1, 0, 500, code)
    
    dicoThread = {}
    for n in range(0,1):
        dicoThread[n] = TestDeValidation(utilisateur, utilisateur.environnement, 1)
        dicoThread[n].TTestRun()
    