import socket
import pickle
import sys

host = "127.0.0.1"
port = 9998
try:
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.connect((host, port))
    print('Connected to host ' + str(host) + ' in port:' + str(port))
    servermessage = mysocket.recv(1024)

    print("Message received from the server", servermessage.decode())
    message = input("> ")
    if message == '1':
        welcome = mysocket.recv(1024)
        welcome.decode()
        credential_username = input('Introduza o username: ')
        credential_password = input('Introduza a password: ')
        credentials = str({'username': credential_username, 'password': credential_password}).encode('utf-8')
        mysocket.send(bytes(credentials))
        welcome = mysocket.recv(1024)
        welcome.decode()

    elif message == "quit":
        sys.exit(1)

except socket.errno as error:
    print("Socket error ", error)
finally:
    mysocket.close()
