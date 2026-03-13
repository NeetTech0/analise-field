import mysql.connector

def conectar():
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="1102016",
            port= 3306,
            database="decorp_field",
            use_pure=True,
            connection_timeout=2
        )
        print("Conectou.")
        return conn

    except mysql.connector.Error as err:
        print("Erro:", err)

