from flask import Flask
from flask_socketio import SocketIO


app = Flask(__name__)
sio = SocketIO(app, async_mode='eventlet', cors_allowed_origins='*')





@sio.on('connect')
def connect(sid):
    print(f"Conexión establecida {sid}.")

@sio.on('enviar_mensaje')
def message( datos):
    print(f"Mensaje recibido desde: {datos}")
    sio.emit('mensaje_recibido', datos)

@sio.on('disconnect')
def disconnect(sid):
    print(f"Conexión desde {sid} finalizada.")


if __name__ == '__main__':
    sio.run(app, host='192.168.137.1', port=1234)

    