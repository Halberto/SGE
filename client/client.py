# Import socket module
import pickle
import socket
import sys

from controller.ControllerTable import ControllerTable


def Main():
    # local host IP '127.0.0.1'
    host = '127.0.0.1'

    # Define the port on which you want to connect
    port = 12345

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to server on local computer
    s.connect((host, port))

    # message you send to server
    # message = "shaurya says geeksforgeeks"

    while True:
        # message sent to server
        # s.send(message.encode('ascii'))
        if login(s):
            print('Entrando no login')
            while True:
                print('Entrando no loop')
                menut = menu()
                if menut == '1':
                    inserir(menut, s)
                elif menut == '2':
                    ler(menut, s)
                elif menut == '3':
                    atualizar(menut, s)
                elif menut == '4':
                    apagar(menut, s)

                ans = input('\nVoltar novamente ao menu?(y/n) :')
                if ans == 'y':
                    s.send('continuar'.encode())
                    continue
                else:
                    s.send('parar'.encode())
                    print('Fazendo logoff da applicacao')
                    break

        # messaga received from server
        # data = s.recv(1024)

        # print the received message
        # here it would be a reverse of sent message
        # print('Received from the server :', str(data.decode('ascii')))

        # ask the client whether he wants to continue
        ans = input('\nDeseja continuar no programa? (y/n):')
        if ans == 'y':
            continue
        else:
            break
    # close the connection
    s.close()


def printresult(myresult):
    print(
        "{0:5s} {1:10s} {2:10s} {3:15s}".format(
            "id", "username", "password", "role"
        )
    )
    for user in myresult:
        print(
            "{0:5s} {1:10s} {2:10s} {3:14s}".format(str(user[0]), user[1], user[2], user[3])
        )


def inserir(menu, s):
    if menu == '1':
        s.send('1'.encode())
        _username = input('Introduza o username: ')
        _password = input('Introduza a password: ')
        _role = input('Introduza o role: ')
        userdata = str({'username': _username, 'password': _password, 'role': _role, 'opcao': '1'}).encode('utf-8')
        s.send(bytes(userdata))
        data = s.recv(1024)
        print(data.decode())


def ler(menu, s):
    if menu == '2':
        s.send('2'.encode())
        data = s.recv(4096)

        data_variable = pickle.loads(data)

        printresult(data_variable)


def atualizar(menu, s):
    if menu == '3':
        s.send('3'.encode())
        print('\nPara atualizar o usuario devera primeiro identificar e introduzir o id.\n')
        id = input('Introduza o id: ')
        print('\nIntroduza os campos a atualizar.\n')
        _username = input('Introduza o username: ')
        _password = input('Introduza a password: ')
        _role = input('Introduza o role: ')
        userdata = str({'username': _username, 'password': _password, 'role': _role, 'id': id}).encode('utf-8')
        s.send(bytes(userdata))



def apagar(menu, s):
    if menu == '4':
        s.send('4'.encode())
        print('\nPara apagar um utilizador devera antes introduzir o id')
        iduser = input('Introduza o username: ')
        question = input('Deseja apagar o utilizador {0}?(y/n)'.format(iduser))
        if question == 'y':
            s.send(iduser.encode())
        else:
            pass



def menu():
    menu = input('Para realizar operacoes no sistema escolha as seguintes opcoes.'
                 '\n1: Para adicionar um novo usuario.'
                 '\n2: Para ler o usuario.'
                 '\n3: Para atualizar um usuario'
                 '\n4: Para apagar um usuario.'
                 '\n:>')

    if menu == '1':
        return '1'
    elif menu == '2':
        return '2'
    elif menu == '3':
        return '3'
    elif menu == '4':
        return '4'
    elif menu == 'q':
        sys.exit()


def login(s):
    while True:
        authentication = None
        loginaut = None
        print("Bem vindo ao SGE")
        message = input("Gostaria de entrar no sistema?\n> ")
        if message == '1' or message == 's':
            credential_username = input('Introduza o username: ')
            credential_password = input('Introduza a password: ')
            credentials = str({'username': credential_username, 'password': credential_password}).encode('utf-8')
            s.send(bytes(credentials))
            data = s.recv(1024)

            authentication = data.decode()

        if authentication == 'True':
            print('Boas vindas usuario {0}'.format(credential_username))
            loginaut = True
            return loginaut
            break
        else:
            print('You missed your credential')
            loginaut = False
            return loginaut
            continue


if __name__ == '__main__':
    Main()
