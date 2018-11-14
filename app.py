from bottle import get, run, template, static_file
from utils.car import Car

car = Car()

@get('/')
def index():
	return template("tpl/index.html")

@get('/static/<filename:re:.*\.*>')
def server_static(filename):
    return static_file(filename, root= './static')


@get('/car/control/<command>')
def car_control(command):
	if not hasattr(car, command):
		return {'code': -1, 'msg': 'can not find command'}
	cmd = getattr(car, command)
	cmd()

	return {'code': 0}

run(host='0.0.0.0', port=8001, reloader=True, debug=True)