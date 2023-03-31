import sqlite3


def main():
    crear_usuario(4, "blass", "soigei")


def main2():
    username = input("Usuario: ")
    password = input("Contraseña: ")

    if verificar_credenciales(username, password):
        print("Login correcto")
    else:
        print("Login incorrecto")


def verificar_credenciales(username, password):
    conn = sqlite3.connect("miaplicacion.db")
    cursor = conn.cursor()

    query = f"SELECT id FROM users WHERE username='{username}' AND password='{password}'"
    print("Query a ejecutar: ", query)

    rows = cursor.execute(query)
    data = rows.fetchone()

    cursor.close()
    conn.close()


def crear_usuario(identificador, usuario, clave):
    conn = sqlite3.connect("miaplicacion.db")
    cursor = conn.cursor()

    query = '''INSERT INTO users(id, username, password) VALUES(?, ?, ?)'''
    cursor.execute(query, (identificador, usuario, clave))
    conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
