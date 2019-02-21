"""
Demo Flask application to test the operation of Flask with socket.io

Based on tutorials from Miguel Grinberg
https://github.com/miguelgrinberg/Flask-SocketIO
and Shane Lynn
https://www.shanelynn.ie/asynchronous-updates-to-a-webpage-with-flask-and-socket-io/

Aim is to create a webpage that is updating content based on output from another application.

15th Feb 2019

===================

Updated 20th Feb 2019

+ Upgraded with eventlet
+ Added async_mode
+ Added HTTP POST request handler

"""

# Start with a basic flask app webpage.
import eventlet
eventlet.monkey_patch()
from flask_socketio import SocketIO, emit
from flask import Flask, render_template, url_for, copy_current_request_context, request
from random import random
from time import sleep
from threading import Thread, Event
import json

#original author 'slynn'
__author__ = 'aerfurt'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

#turn the flask app into a socketio app
async_mode = 'eventlet'
socketio = SocketIO(app, async_mode=async_mode)

#random number Generator Thread
thread = Thread()
thread_stop_event = Event()

global_state = {
'product_name': 'Undefined',
'confidence': 1.0
}

def update_state(product_name, confidence):
    defined = confidence and confidence > 0.7
    if defined:
        global_state['product_name'] = product_name
        global_state['confidence'] = confidence
    return defined

@app.route('/')
def index():
    #only by sending this page first will the client be connected to the socketio instance
    return render_template('index.html')

@app.route('/newstate', methods=['POST'])
def fetch_label():
    #only by sending this page first will the client be connected to the socketio instance
    payload = request.get_json() # payload is {'product_name': str, 'confidence': float}
    should_notify = update_state(payload.get('product_name', None),
                                 payload.get('confidence', None))
    if should_notify:
        msg = {
            'product_name': global_state['product_name'],
        }
        print(msg)
        socketio.emit('newfact', msg, namespace='/test')
    return 'OK'

@socketio.on('connect', namespace='/test')
def test_connect():
    # need visibility of the global thread object
    print('Client connected')


@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app)
