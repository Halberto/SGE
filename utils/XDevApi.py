import mysqlx

# Connect to server on localhost
from utils.configu import connect_args

db = mysqlx.get_session(schema='sge', **connect_args)
schema = db.get_default_schema()

print("Schema name: {0}"
      .format(schema.name)
      )


db.close()
