import mysqlx

from utils.configu import connect_args


class LerUsuarion():

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
        users = schema.get_collection("usuarios")
        # Do a find on the collection - find the dog

        return users

