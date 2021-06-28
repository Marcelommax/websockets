from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('status')
def statusConexao(data):
    print('status', data) 

@socketio.on('enviarmsg')
def postmsg(msg):
    emit('enviarmsg', msg, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, debug=True)