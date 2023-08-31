import socket
import json
def client_program():
    host = socket.gethostname()
    port = 5600

    client_socket = socket.socket()
    client_socket.connect((host, port))

    message = input(" client message:  ")

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()

        print('Received from server: ' + data)

        message = input(" client message: ")

    client_socket.close()

if __name__ == '__main__':
    client_program()
