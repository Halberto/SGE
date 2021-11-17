# Import the MySQL X module
import mysql
import mysqlx
# Get a session with a URI
from mysql.connector import errorcode

from controller.LerUsuario import LerUsuarion
from model.Usuarios import Usuarios
from utils.configu import connect_args
from model.Usuarios import Usuarios


class UserController():

    def get_connection(operacao):
        try:
            db = mysql.connector.connect(
                option_files=[
                    "my_shared.ini",
                    "SGE.ini"
                ],
                option_groups=[
                    "client",
                    "connector_python"
                ],
                use_pure=True
            )

            print(
                "Connectado a base de dados : {0}"
                    .format(db.database)
            )
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")


    def readUserData(self):
        db = mysqlx.get_session(**connect_args)
        # Check the connection
        if not db.is_open():
            print("Connection failed!")
            exit(1)
        # Create a schema.

        db = mysqlx.get_session(**connect_args)
        schema = db.get_schema("sge")
        # Create a new table
        # Get the collection.
        users = schema.get_table("user")
        # Do a find on the collection - find the dog

        return users

    def search_user(username):
        users = UserController.readUserData(None)
        find = users.select('username')
        res = find.fetch_one()
        while res:
            usuario = Usuarios(res['username'], res['password'], res['role'])
            if username == usuario.username:
                print('User found', end='\n')
                print(
                    "{0:12s} {1:10s} {2:10s} ".format(
                        "username", "password", "role"
                    )
                )
                print(
                    " {0:10s} {1:10s} {2:14s}".format(

                        usuario.username,
                        usuario.password,
                        usuario.role
                    )
                )
                break

        else:
            print('User not found')

    def novo_usuario(self, ):
        # Instancia a sessao
        usernameg = input('Introduza o usuario')
        passwordg = input('Introduza a senha')
        roleg = input('Introduza o papel')
        db = mysqlx.get_session(**connect_args)
        # Check the connection
        if not db.is_open():
            print("Connection failed!")
            exit(1)
        # Create a schema.
        schema = db.get_schema("sge")
        # Create a new collection
        user = schema.get_collection("usuarios", True)
        usuario = Usuarios(usernameg, passwordg, roleg)
        user.add({'username': usuario.username, 'password': usuario.password, 'role': usuario.role}).execute()

        # print(user.username, 'introduzido com sucesso')
        # Fechamos a conexao
        db.close()

    def apagar_usuario(self):
        users = LerUsuarion.readUserData(None)

        # For printing information along the way
        fmt = "{0:36s}: {1:2d}"

        # Run inside a transaction, so the
        # changes can be rolled back at the end.

        userinput = input("Deseja apagar que usuario? \nIntroduza o username... ")
        passinput = input("\nIntroduza a palavra pass do usuario...")

        row = users.find("username = '{0}' and password = '{1}'".format(userinput,
                                                                        passinput)).execute()
        user = row.fetch_one()
        while user:
            userdata = user['_id']
            usuario = Usuarios(user['username'], user['password'], user['role'])
            if userinput == usuario.username:
                if passinput == usuario.password:

                    print(
                        "{0:12s} {1:10s} {2:10s} ".format(
                            "username", "password", "role"
                        )
                    )
                    print(
                        " {0:10s} {1:10s} {2:14s}".format(

                            usuario.username,
                            usuario.password,
                            usuario.role
                        )
                    )

                    data = input("Dados confirmados. Deseja apagar o id {0}? sim ou nao...".format(userdata))
                    if data == 'sim':
                        result = users.remove_one(
                            userdata)
                        items = result.get_affected_items_count()
                        print(fmt.format(
                            "Number of rows deleted by remove_one",
                            result.get_affected_items_count()
                        ))
                    break

        else:
            print('User not found')

    def atualizar_usuario(self):
        users = LerUsuarion.readUserData(None)

        # For printing information along the way
        fmt = "{0:36s}: {1:2d}"

        # Run inside a transaction, so the
        # changes can be rolled back at the end.
        print ("Para atualizar um usuario, primeiro introduza o username e password autenticos.")
        userinput = input("\nIntroduza o username... \n")

        passinput = input("Introduza a palavra pass ...")

        row = users.find("username = '{0}' and password = '{1}'".format(userinput,
                                                                        passinput)).execute()
        user = row.fetch_one()
        while user:
            userdata = user['_id']
            usuario = Usuarios(user['username'], user['password'], user['role'])
            if userinput == usuario.username:
                if passinput == usuario.password:

                    print(
                        "{0:12s} {1:10s} {2:10s} ".format(
                            "username", "password", "role"
                        )
                    )
                    print(
                        " {0:10s} {1:10s} {2:14s}".format(

                            usuario.username,
                            usuario.password,
                            usuario.role
                        )
                    )

                    data = input("Proceder com atualizacao do id {0}? sim ou nao...".format(userdata))
                    if data == 'sim':
                        username = input("Introduza novamente o nome do usuario")
                        password = input("Introduza novamente a password")
                        role = input("Introduza o role")
                        user['username'], user['password'], user['role'] = username, password, role
                        result = users.add_or_replace_one(
                            userdata, user)
                        print("Number of affected docs: {0}"
                              .format(result.get_affected_items_count()))
                    break

        else:
            print('User not found')


UserController.search_user('Lopes')