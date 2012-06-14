#coding=utf-8
from iaproject.server.gamesocket import GameNamespace
from iaproject.test.ia import Ia
from pyramid.response import Response
from pyramid.view import view_config
from socketio import socketio_manage
from testdevalidation import TestDeValidation

def index(request):
    """ Base view to load our template """
    
    return {}

def socketio_service(request):
    print ('socketio_service requested !')
    retval = socketio_manage(request.environ,
        {
            '': GameNamespace,
        }, request=request
    )

    return retval

@view_config(route_name='ia',request_method='GET')
def ia(request):
    return Response('damien')

@view_config(route_name='ia',request_method='OPTIONS')
@view_config(route_name='ia',request_method='POST')
def ia_post(request):
    
    print "IA CODE: ", request.POST['ia[code]']
    
    utilisateur = Ia(1, 0, 500, request.POST['ia[code]'])
    
    currentTest = TestDeValidation(utilisateur, utilisateur.environnement, 1)
    currentTest.TTestRun()
    
    while currentTest.TTest.isAlive() == True:
        print "running : ", "ia id :", request.POST['ia[key]'], "ia name : ", request.POST['ia[name]']
        pass
    
    return Response(str(currentTest.ErrorTable))

#HTTPFound(location='http://google.com')