import mysqlx

from controller.ControllerTable import ControllerTable


from model.Usuarios import Usuarios
from utils.TableData import TableExample

from utils.configu import connect_args
from model.DadosEstudantes import estudante


class Login():


    def login(username, password):

        users = ControllerTable.ler(None)

        for user in users:
            usuario = Usuarios(user[1], user[2], user[3])
            if username == usuario.username:
                print('User found', end='\n')
                if password == usuario.password:
                    print('O usuario ',username , end=' entrou no sistema')
                    users
                    return True
                    break
                else:
                    print('Password doesnt match')
                    return False
                break
        else:
            print('User not found')
            return False




