import socket
import json
def server_program():
    server_socket = socket.socket()

    server_socket.bind((server_ip, server_port))

    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))
    while True:

        data = conn.recv(1024).decode()
        if not data:

            break
        print("from connected client: " + str(data))
        data = input(' server Message:  ')
        conn.send(data.encode())
    conn.close()(config_file)
if __name__ == '__main__':
    with open("config.json") as config_file:
        config = json.load(config_file)
        server_ip = config["server"]["host"]
        server_port = config["server"]["port"]

        start_server=(server_ip, server_port)
    server_program()
