# import socket programming library
import ast
import pickle
import socket

# import thread module
from _thread import *
import threading
from urllib import request

from controller.ControllerTable import ControllerTable
from controller.Login import Login

print_lock = threading.Lock()


def login(client_socket):
    while True:

        while True:
            data = client_socket.recv(1024)
            dictionary = ast.literal_eval(data.decode())
            username = dictionary['username']
            password = dictionary['password']
            authentication = None

            if Login.login(username, password):
                print(' Enviando a mensagem de boas vindas ao cliente')
                client_socket.send('True'.encode())
                authentication = True
            else:
                client_socket.send('False'.encode())
                print('Try again')
                authentication = False

            print("[*] Received request : {0} from client {1}".format(request, client_socket.getpeername()))
            while True:
                if authentication:
                    opcao = client_socket.recv(1024)
                    data = opcao.decode()
                    print(data)
                    if data == '1':
                        inserir(authentication, client_socket)
                    elif data == '2':
                        ler(authentication, client_socket)
                    elif data == '3':
                        atualizar(authentication,client_socket)
                    elif data == '4':
                        apagar(authentication,client_socket)
                    elif data == 'parar':
                        print('Bye')

                        # lock released on exit
                        print_lock.release()
                        return 'bye'
                        break


def inserir(authentication, client_socket):
    if authentication:
        while True:
            print('Invocando inserir')
            data = client_socket.recv(1024)
            pure = data.decode()

            if not pure == 'continuar':

                if pure == 'continuar':
                    print(pure)
                    data = client_socket.recv(1024)
                print(pure)
                userdata = ast.literal_eval(data.decode())
                username = userdata['username']
                password = userdata['password']
                role = userdata['role']
                ControllerTable.inserir(username, password, role)
                client_socket.send('voltando ao menu principal\n'.encode())
                return 'awaiting'
            else:
                break
    else:
                print('O usuario nao esta autenticado')

def ler(authentication, client_socket):
    if authentication:
        query = ControllerTable.ler(None)
        print(type(query))
        data = pickle.dumps(query)
        client_socket.send(data)
        print(type(query))
    else:
        print('O usuario nao esta autenticado')

def atualizar(authentication, client_socket):
    if authentication:

        print('Invocando atualizar')
        data = client_socket.recv(1024)
        pure = data.decode()

        if not pure == 'continuar':

            if pure == 'continuar':
                print(pure)
                data = client_socket.recv(1024)
            print(pure)
            userdata = ast.literal_eval(data.decode())
            userid = userdata['id']
            username = userdata['username']
            password = userdata['password']
            role = userdata['role']
            ControllerTable.atualizar(userid,username, password, role)
            client_socket.send('voltando ao menu principal\n'.encode())
    else:
        print('O usuario nao esta autenticado')

def apagar(authentication, client_socket):
    if authentication:

        print('Invocando apagar')
        data = client_socket.recv(1024)
        pure = data.decode()

        if not pure == 'continuar':

            if pure == 'continuar':
                print(pure)
                data = client_socket.recv(1024)
            print(pure)
            _id = int(pure)
            ControllerTable.apagar(_id)
            client_socket.send('voltando ao menu principal\n'.encode())
    else:
        print('O usuario nao esta autenticado')

def Main():
    host = ""

    # reverse a port on your computer
    # in our case it is 12345 but it
    # can be anything
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)

    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")

    # a forever loop until client wants to exit
    while True:
        # establish connection with client
        c, addr = s.accept()

        # lock acquired by client
        print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])

        # Start a new thread and return its identifier
        start_new_thread(login, (c,))
    s.close()


if __name__ == '__main__':
    Main()
