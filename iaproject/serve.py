from pyramid.paster import get_app
from socketio.server import SocketIOServer
import os, sys

if __name__ == '__main__':
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    app = get_app('development.ini')
    print 'Listening on port http://127.0.0.1:8080 and on port 843 (flash policy server)'
    SocketIOServer(('0.0.0.0', 8080), app, namespace="socket.io",
            policy_server=False).serve_forever()
