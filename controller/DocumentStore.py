# Create a schema.
# Import the MySQL X module
import mysqlx
# Get a session with a URI
from utils.configu import connect_args

db = mysqlx.get_session(**connect_args)
# Check the connection
if not db.is_open():
    print("Connection failed!")
    exit(1)
# Create a schema.
schema = db.get_schema("sge")
# Create a new collection
# user = schema.get_collection("usuarios", True)

# schema.drop_collection('usuarios')

user = schema.create_collection("usuarios", True)
# Insert some documents
user.add({'username': 'Lopes', 'password': 'aek136', 'role': 'admin'}).execute()
user.add({'username': 'zangao', 'password': '1kkq6', 'role': 'estudante'}).execute()
user.add({'username': 'Rita', 'password': 'aqk46', 'role': 'professor'}).execute()
user.add({'username': 'Soqk', 'password': 'qj16q', 'role': 'admin'}).execute()
user.add({'username': 'Violet', 'password': '6alq', 'role': 'estudante'}).execute()
# Close the connection

# Get the collection.
users = schema.get_collection("usuarios")
# Do a find on the collection - find the dog
find = users.find("username = 'Lopes'").execute()
res = find.fetch_one()
while res:
    print("Get the data item as a string: {0}".format(res))
    print("Get the data elements: {0}, {1}, {2}".format(res['username'], res['password'],
                                                        res['role']))
    res = find.fetch_one()

db.close()
