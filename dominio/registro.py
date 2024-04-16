import sqlite3

class Registro:
    def __init__(self):
        self.conn = sqlite3.connect("persistencia/UsuariosRecomendaciones.db")
        self.cursor = self.conn.cursor()

    def registrar_usuario(self, dni, username, password, nombre, apellido, telefono):
        try:
            # Verificar si el usuario ya existe
            self.cursor.execute('SELECT * FROM Usuarios WHERE username=?', (username,))
            if self.cursor.fetchone() is not None:
                return False, "El usuario ya existe"

            # Verificar si el DNI ya está registrado
            self.cursor.execute('SELECT * FROM Usuarios WHERE dni=?', (dni,))
            if self.cursor.fetchone() is not None:
                return False, "El DNI ya está registrado"    
            
            #Verificar si el telefono ya está registrado
            self.cursor.execute('SELECT * FROM Usuarios WHERE telefono=?', (telefono,))
            if self.cursor.fetchone() is not None:
                return False, "El telefono ya está registrado"

            # Verificar la longitud de la contraseña
            if len(password) < 4:
                return False, "La contraseña debe tener al menos 4 caracteres"

            # Insertar nuevo usuario en la base de datos
            self.cursor.execute('INSERT INTO Usuarios (dni, username, password, nombre, apellido, telefono) VALUES (?, ?, ?, ?, ?, ?)',
                                (dni, username, password, nombre, apellido, telefono))
            self.conn.commit()
            return True, "Usuario registrado exitosamente"
        except Exception as e:
            return False, str(e)
        finally:
            self.conn.close()
