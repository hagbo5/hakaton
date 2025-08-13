import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',  # Cambia si tienes contraseña en XAMPP
        database='solaris'
    )
