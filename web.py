from bottle import get, run, template


@get('/')
def index():
	return template("index.html")

run(host='0.0.0.0', port=8001, reloader=True, debug=True)