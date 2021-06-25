from flask import Flask, render_template
from flask_socketio import SocketIO, emit


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('status')
def handle_message(data):
    print(data) 

@socketio.on('enviarmsg')
def send_handle_message(msg):
    emit('enviarmsg', msg)


if __name__ == '__main__':
    socketio.run(app, debug=True)