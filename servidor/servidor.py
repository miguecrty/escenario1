import socket

HOST = '172.16.17.5'
PORT = 8080
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f"Servidor escuchando en {HOST}:{PORT}")
print("Esperando conexion...\n")

# Initialize salida as a global variable
salida = False

def main():
    global salida
    while not salida:
        conn, addr = server_socket.accept()
        with conn:
            print('▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀')
            print(f"Conexión establecida desde {addr}")
            print('▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀   CHAT   ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀')
            print('     Para salir del chat escribe \'salir\'     ')
            print('▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀\n\n')
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"			Recibido: {data.decode()}\n")
                if data.decode() == 'salida':
                    salida = True
                # Ahora el servidor también puede enviar mensajes al cliente
                mensaje_servidor = input(": ")
                conn.sendall(mensaje_servidor.encode())

if __name__ == "__main__":
    main()

