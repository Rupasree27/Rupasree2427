import socket
import json
def client_program():


    client_socket = socket.socket()
    client_socket.connect((server_ip, server_port))

    message = input(" client message:  ")

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()

        print('Received from server: ' + data)

        message = input(" client message: ")

    client_socket.close()

if __name__ == '__main__':
    with open("config.json") as config_file:
        config = json.load (config_file)
        server_ip = config["server"]["host"]
        server_port = config["server"]["port"]

        start_server=(server_ip, server_port)
    client_program()


