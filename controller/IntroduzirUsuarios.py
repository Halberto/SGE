# Create a schema.
# Import the MySQL X module
import mysqlx
# Get a session with a URI
from model.Usuarios import Usuarios
from utils.configu import connect_args
from model.Usuarios import Usuarios


class IntroduzirUsuarios():



    def novo_usuario(self,):
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

        #print(user.username, 'introduzido com sucesso')
        # Fechamos a conexao
        db.close()
