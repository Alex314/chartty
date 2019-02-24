import os
import psycopg2
from flask import Flask, render_template, g
from flask_socketio import SocketIO, emit
from time import sleep
import logging


app = Flask(__name__)
app.logger.setLevel(logging.INFO)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'XYZ')
socketio = SocketIO(app)


@app.route('/')
def index():
    print('/')
    app.logger.info('/ log')
    app.logger.error('/ log.error')
    return render_template('index.html')


@socketio.on('connect', namespace='/test')
def test_connect():
    # need visibility of the global thread object
    for i in range(2):
        print(i)
        socketio.emit('newnumber', {'number': 3.6}, namespace='/test')
        sleep(2)


@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app)
