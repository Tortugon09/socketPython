import socket
import threading

def manejar_cliente(conexion, direccion, nombre_usuario):
    while True:
        datos = conexion.recv(1024).decode()
        if not datos:
            desconectar_cliente(conexion)
            break
        print(f"Mensaje recibido de {nombre_usuario}: {datos}")
        for cliente in clientes:
            if cliente != conexion:
                cliente.send(f"{nombre_usuario}: {datos}".encode())

def desconectar_cliente(conexion):
    nombre_usuario = clientes[conexion]
    print(f"{nombre_usuario} se ha desconectado.")
    del clientes[conexion]
    conexion.close()

s = socket.socket()
s.bind(("", 1234))
s.listen(5)

clientes = []
while True:
    conexion, direccion = s.accept()
    nombre_usuario = conexion.recv(1024).decode()
    print(f"Conexión desde {direccion} ha sido establecida con el nombre de usuario {nombre_usuario}.")
    clientes.append(conexion)
    threading.Thread(target=manejar_cliente, args=(conexion, direccion, nombre_usuario)).start()

s.close()




