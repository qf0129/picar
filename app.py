from bottle import template, run, request, abort, Bottle ,static_file
# from gevent import monkey; monkey.patch_all()
from gevent.pywsgi import WSGIServer
# from geventwebsocket import WebSocketHandler, WebSocketError
from geventwebsocket import WebSocketError 
from geventwebsocket.handler import WebSocketHandler
from utils.car import Car

car = Car()
app = Bottle()

@app.get('/')
def index():
    return template('tpl/index')

@app.route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')

@app.route('/websocket')
def handle_websocket():
    wsock = request.environ.get('wsgi.websocket')
    if not wsock:
        abort(400, 'Expected WebSocket request.')
    while True:
        try:
            message = wsock.receive()
            up, down, left, right = 0, 0, 0, 0

            if '1' in message:
                up = 1

            if '2' in message:
                down = 1

            if '3' in message:
                left = 1

            if '4' in message:
                right = 1

            car.run(up, down, left, right)
            print('>>', message)
            wsock.send("Server: %r" % message)
        except WebSocketError:
            break

# @app.route('/<filename:path>')
# def send_html(filename):
#     return static_file(filename, root='./static', mimetype='text/html')

host = "0.0.0.0"
port = 8000

server = WSGIServer((host, port), app, handler_class=WebSocketHandler)
print("access @ http://%s:%s/websocket.html" % (host,port))
server.serve_forever()

# app.run(host='0.0.0.0', port=8000, reloader=True, server='gevent', handler_class=WebSocketHandler)
