import socket

HOST = '10.0.0.1'
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    print('▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀')
    print('▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀   CHAT   ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀')
    print('     Para salir del chat escribe \'salir\'     ')
    print('▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀\n\n')
    
    while True:
        mensaje = input(": ")
        
        if mensaje.lower() == 'salir':
            break

        client_socket.sendall(mensaje.encode())

        # Recibir datos del servidor
        data = client_socket.recv(1024)
        print(f"			Recibido: {data.decode()}")