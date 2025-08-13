import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host="sql5.freesqldatabase.com",
        user="sql5794797",
        password="AQUI_TU_CONTRASEÑA",
        database="sql5794797"
    )
    return connection
