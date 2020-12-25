from flask import Flask, render_template
from flask_socketio import SocketIO
from models import TikTok
import os

app = Flask(__name__)
socketio = SocketIO(app)
tiktok = TikTok(os.getenv('ACC_HANDLE'))


def emit_data():
    data = {
        'followers': tiktok.followers,
        'likes': tiktok.likes
    }
    socketio.emit('data', data)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@socketio.on('connect')
def on_connect():
    emit_data()

@socketio.on('refresh_data')
def on_refresh_data():
    tiktok.refresh_data()
    emit_data()

if __name__ == '__main__':
    socketio.run(app)
