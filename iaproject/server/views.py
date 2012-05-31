#coding=utf-8
from iaproject.server.gamesocket import GameNamespace
from pyramid.response import Response
from pyramid.view import view_config
from socketio import socketio_manage

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

@view_config(route_name='ia',request_method='POST')
def test_ia(request):
    print request.POST['id']
    return Response(str(request.GET['id']))