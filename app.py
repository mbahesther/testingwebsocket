from flask import Flask, render_template, request, redirect, url_for, session
from flask_socketio import SocketIO, join_room, send, leave_room, emit
# from flask_session import Session
from flask_cors import CORS
app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret'
# app.config['SESSION_TYPE'] = 'filesystem'

# Session(app)

socketio = SocketIO(app, cors_allowed_origins="*", logger=True)
# CORS(app)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     return render_template('index.html')



@app.route('/chat', methods=['GET', 'POST'])
def chat():
    return render_template('index.html')


@socketio.on('message', namespace='/chat')
def handle(msg):
    print('message: ' + msg )
    send(msg, broadcast=True)




if __name__ == '__main__':
    socketio.run(app)
