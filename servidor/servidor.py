import socket

HOST = '172.16.17.5'
PORT = 8080
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f"Servidor escuchando en {HOST}:{PORT}\n\n")

while True:
    conn, addr = server_socket.accept()
    with conn:
        print('▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀')
        print(f"Conexión establecida desde {addr}")
        print('▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀   CHAT   ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀')
        print('     Para salir del chat escribe \'salir\'     ')
        print('▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀\n\n')
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"			Recibido: {data.decode()}\n")

            # Ahora el servidor también puede enviar mensajes al cliente
            mensaje_servidor = input(": ")
            conn.sendall(mensaje_servidor.encode())
