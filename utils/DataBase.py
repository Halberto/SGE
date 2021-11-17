import mysql.connector
import pprint
from mysql.connector.conversion import MySQLConverter

printer = pprint.PrettyPrinter(indent=1)
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
print(__file__ + " - two configu.py files:")
print(
    "MySQL connection ID for db: {0}"
        .format(db.connection_id)
)
result = db.cmd_query(
    """SELECT *
    FROM user
    """
)

# Fetch the rows
(users, eof) = db.get_rows(5)
converter = MySQLConverter(
    db.charset, True)
# Print the rows found
print(__file__ + " – Using decode:")
print("")
print(
    "{0:10s} {1:10s} {2:15s}".format(
        "username", "password", "role"
    )
)
for city in users:
    values = converter.row_to_python(
        city, result["columns"])
    print(
        "{0:10s} {1:10s} {2:4s}".format(
            values[1],
            values[2],
            values[3]

        )
    )
# Print the eof package
print("\nEnd-of-file:")

if eof is None:
    (cities, eof) = db.get_rows(count=4)
else:
    cities = []

db.close()
