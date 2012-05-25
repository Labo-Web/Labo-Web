#coding=utf-8
from iaproject.server.gamesocket import GameNamespace
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