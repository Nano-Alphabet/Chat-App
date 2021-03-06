from flask import Flask 
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

@socketio.on('message')
def handleMessage(msg):
	send(msg, broadcast=True)

@app.route('/')
def Homepage():
	return 'Hello, World!'

if __name__ == '__main__':
	socketio.run(app)
	app.run()
