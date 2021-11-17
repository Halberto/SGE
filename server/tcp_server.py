import ast
import json
import socket
import sys
import threading

from controller.Login import Login

SERVER_IP = "127.0.0.1"
SERVER_PORT = 9998
# family = Internet, type = stream socket means TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER_IP, SERVER_PORT))
server.listen(5)
try:

    print("[*] Server Listening on %s:%d" % (SERVER_IP, SERVER_PORT))

    client, addr = server.accept()
    client.send("Accepting connections...".encode())
    print("[*] Accepted connection from: %s:%d" % (addr[0], addr[1]))


    def handle_client(client_socket):
        request = client_socket.recv(1024)
        dictionary = ast.literal_eval(request.decode())
        username = dictionary['username']
        password = dictionary['password']
        client_socket.send('Bem vindo'.encode())

        if Login.login(username, password):
            print(' Enviando a mensagem de boas vindas ao cliente')
        else:
            print('Try again')

        print("[*] Received request : {0} from client {1}".format(request, client_socket.getpeername()))
        client_socket.send(bytes("ACK", "utf-8"))


    while True:
        handle_client(client)

    else:
        client_socket.close()
        server.close()
except socket.timeout as e:
    print("Timeout %s" % e)
    sys.exit(1)
except socket.gaierror as e:
    print("connection error to the server:%s" % e)
    sys.exit(1)
except socket.error as e:
    print("Connection error: %s" % e)
