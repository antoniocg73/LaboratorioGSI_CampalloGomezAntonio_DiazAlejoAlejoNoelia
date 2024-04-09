import sqlite3
class Login:
    def __init__(self):
        self.conn = sqlite3.connect('persistencia/UsuariosRecomendaciones.db')
        self.cursor = self.conn.cursor()

    def verificar_usuario(self, usuario, contrasena):
        try:
            # Buscar en la base de datos si las credenciales son válidas
            self.cursor.execute('SELECT * FROM Usuarios WHERE username=? AND password=?', (usuario, contrasena))
            resultado = self.cursor.fetchone()
            if resultado:
                return True
            else:
                return False
        except Exception as e:
            print("Error al verificar usuario:", e)
            return False
        finally:
            self.conn.close()
        