import mysql.connector
import pprint

from mysql.connector import errorcode
from mysql.connector.conversion import MySQLConverter

from model.Usuarios import Usuarios


class TableExample():

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

            if (operacao == 'criar_tabela'):
                sql = {}
                sql['nwtable'] = ()
                cursor = db.cursor()
                for sq_ in sql:
                    table_description = sql[sq_]
                    try:
                        print("Creating table {}: ".format(sq_), end='')
                        cursor.execute(table_description)
                    except mysql.connector.Error as err:
                        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                            print("already exists.")
                        else:
                            print(err.msg)
                    else:
                        print("OK")
            elif (operacao == 'inserir'):
                usernameg = input('Introduza o usuario')
                passwordg = input('Introduza a senha')
                roleg = input('Introduza o papel')
                sql_code = ('''INSERT INTO user (username,password,Role) 
                            VALUES (%s, %s, %s)''')
                udata = (usernameg, passwordg, roleg)
                mycursor = db.cursor()
                try:
                    # Execute SQL Query to insert record
                    mycursor.execute(sql_code, udata)
                    db.commit()  # Commit is used for your changes in the database
                    print('Record inserted successfully...')
                except:
                    # rollback used for if any error
                    db.rollback()
                db.close()  # Connection Close
            elif (operacao == 'ler'):
                mycursor = db.cursor()

                mycursor.execute("SELECT * FROM user")

                myresult = mycursor.fetchall()

                print(
                    "{0:5s} {1:10s} {2:10s} {3:15s}".format(
                      "id", "username", "password", "role"
                    )
                )
                for user in myresult:
                    print(
                        "{0:5s} {1:10s} {2:10s} {3:14s}".format(
                            str(user[0]),
                            user[1],
                            user[2],
                            user[3]
                        )
                    )
            elif (operacao == 'atualizar'):
                # Cursor do metodo
                mycursor = db.cursor()
                id =int(input("Introduza o ID"))
                username = input("Introduza o nome do usuario")
                password = input("Introduza a password")
                role = input("Introduza o role")
                sql = "UPDATE user SET username='{0}', password='{1}', role ='{2}' WHERE iduser = {3}".format(username,password,role,id)
                mycursor.execute(sql)
                db.commit()
                print(mycursor.rowcount, "record(s) affected")
            elif operacao == 'apagar':
                mycursor = db.cursor()
                id = int(input("Introduza o ID"))

                desejaapgar= input("Deseja apagar o id {0}? Responda sim ou nao. ".format(id))
                if desejaapgar == 'sim':
                    sql = "DELETE FROM user WHERE iduser = {0}".format(id)
                    mycursor.execute(sql)
                    db.commit()
                    print(mycursor.rowcount, "record(s) deleted")

                else:
                    print("")

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)




