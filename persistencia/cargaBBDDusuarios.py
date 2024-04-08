# Instalar sqlite3 de la pagina oficial: https://www.sqlite.org/download.html
#Instalar sqlitebrowser de la página oficial: https://sqlitebrowser.org/dl/ para poder ver las bases de datos
import sqlite3
import os

# Obtener la ruta del directorio del script actual
directorio_script = os.path.dirname(__file__)

# Ruta completa de la base de datos
ruta_base_datos = os.path.join(directorio_script, 'UsuariosRecomendaciones.db')

# Conexión a la base de datos (se creará si no existe)
conexion = sqlite3.connect(ruta_base_datos)

# Crear un cursor para ejecutar comandos SQL
cursor = conexion.cursor()

# Crear la tabla "Usuarios" si no existe
cursor.execute('''CREATE TABLE IF NOT EXISTS Usuarios (
                dni TEXT PRIMARY KEY,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL,
                telefono TEXT UNIQUE NOT NULL
                )''')

# Insertar los usuarios de ejemplo
def insertar_usuario(username, dni, password, nombre, apellido, telefono):
    try:
        cursor.execute('''INSERT INTO Usuarios (username, dni, password, nombre, apellido, telefono)
                          VALUES (?, ?, ?, ?, ?, ?)''', (username, dni, password, nombre, apellido, telefono))
        conexion.commit()
        print("Usuario insertado correctamente.")
    except sqlite3.Error as error:
        print("Error al insertar usuario:", error)

# Insertar los usuarios de ejemplo
insertar_usuario('NoeliaDA', '06297500P', 'patata2', 'Noelia', 'Diaz-Alejo', '686543211')
insertar_usuario('AntonioCG', '05970690M', 'manzana3', 'Antonio', 'Campallo', '675454565')

# Cerrar la conexión
conexion.close()

print("La base de datos 'UsuariosRecomendaciones' ha sido creada correctamente.")
