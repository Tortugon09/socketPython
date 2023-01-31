import socket
import threading

s = socket.socket()
s.connect(("127.0.0.1", 1234))

nombre_usuario = input("Ingresa tu nombre de usuario: ")
s.send(nombre_usuario.encode())

def recibir_mensajes():
    while True:
        datos = s.recv(1024).decode()
        print(f"{datos}")

threading.Thread(target=recibir_mensajes).start()

while True:
    mensaje = input("Mensaje a enviar: ")
    s.send(mensaje.encode())

s.close()
