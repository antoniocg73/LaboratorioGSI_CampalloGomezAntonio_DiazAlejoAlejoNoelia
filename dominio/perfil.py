import sqlite3

class Perfil:
    def __init__(self):
        self.conn = sqlite3.connect('persistencia/UsuariosRecomendaciones.db')
        self.cursor = self.conn.cursor()

    def obtener_datos(self, usuario):
        try:
            # Buscar en la base de datos los datos del usuario
            self.cursor.execute('SELECT nombre, apellido, telefono, dni FROM Usuarios WHERE username=?', (usuario,))
            resultado = self.cursor.fetchone()
            return resultado
        except Exception as e:
            print("Error al obtener datos del usuario:", e)
            return None
        finally:
            self.conn.close()

    def cambiar_contrasena(self, usuario, contrasena_antigua, contrasena_nueva):
        try:
            # Verificar si la contraseña antigua es correcta para el usuario
            self.cursor.execute('SELECT * FROM Usuarios WHERE username=? AND password=?', (usuario, contrasena_antigua))
            resultado = self.cursor.fetchone()
            if resultado:
                # Actualizar la contraseña del usuario en la base de datos
                self.cursor.execute('UPDATE Usuarios SET password=? WHERE username=?', (contrasena_nueva, usuario))
                self.conn.commit()
                return True, "Contraseña cambiada exitosamente."
            else:
                return False, "La contraseña antigua es incorrecta."
        except Exception as e:
            return False, f"No se pudo cambiar la contraseña: {e}"
        finally:
            self.conn.close()
    '''    
    def cambiar_contrasena(self, usuario, contrasena):
        try:
            # Actualizar en la base de datos la contraseña del usuario
            self.cursor.execute('UPDATE Usuarios SET password=? WHERE username=?', (contrasena, usuario))
            self.conn.commit()
            return True
        except Exception as e:
            return False
        finally:
            self.conn.close()
        
    def obtener_calificaciones(self, usuario):
        try:
            # Buscar en la base de datos las calificaciones del usuario
            self.cursor.execute('SELECT * FROM Calificaciones WHERE username=?', (usuario,))
            resultado = self.cursor.fetchall()
            return resultado
        except Exception as e:
            print("Error al obtener calificaciones del usuario:", e)
            return None
        finally:
            self.conn.close()
        
    def obtener_gustos(self, usuario):
        try:
            # Buscar en la base de datos los gustos del usuario
            self.cursor.execute('SELECT * FROM Gustos WHERE username=?', (usuario,))
            resultado = self.cursor.fetchall()
            return resultado
        except Exception as e:
            print("Error al obtener gustos del usuario:", e)
            return None
        finally:
            self.conn.close()
        
    def obtener_formulario(self, usuario):
        try:
            # Buscar en la base de datos el formulario del usuario
            self.cursor.execute('SELECT * FROM Formulario WHERE username=?', (usuario,))
            resultado = self.cursor.fetchone()
            return resultado
        except Exception as e:
            print("Error al obtener formulario del usuario:", e)
            return None
        finally:
            self.conn.close()
        
    def actualizar_formulario(self, usuario, genero, edad, estado_civil, hijos, mascotas, fumador, estudios, trabajo, ingresos):
        try:
            # Actualizar en
            '''