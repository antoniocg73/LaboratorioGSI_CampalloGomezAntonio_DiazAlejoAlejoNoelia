import sqlite3
from unittest import result

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
        
    def obtener_calificaciones(self, usuario):
        try:
            #Buscar el dni del usuario
            dni = self.obtener_dni(usuario)
            # Buscar en la base de datos las calificaciones del usuario
            self.cursor.execute('SELECT  eda, si, logica, algebra, metodologia, ipoi, bbdd, sisinf, redesi, redesii, ssoo, pctr, teco, eco, arco, orco, ssdd, isoi, isoii, progi, progii FROM Notas WHERE dni=?', (dni[0],))
            resultado = self.cursor.fetchall()
            if resultado:
                resultado = list(resultado[0])
            return resultado
        except Exception as e:
            print("Error al obtener calificaciones del usuario:", e)
            return None
        finally:
            self.conn.close()
    
    def actualizar_calificaciones(self, usuario, notas):
        try:
            # Buscar el dni del usuario
            dni = self.obtener_dni(usuario)
            
            # Convertir las notas de formato string a float y reemplazar comas por puntos
            notas_float = [float(nota.replace(',', '.')) for nota in notas]
            
            # Verificar si el usuario tiene un registro en la tabla Notas
            self.cursor.execute('SELECT * FROM Notas WHERE dni=?', [dni[0]])
            registro_existente = self.cursor.fetchone()
            
            if registro_existente:
                # Actualizar las calificaciones del usuario en la base de datos
                self.cursor.execute('UPDATE Notas SET eda=?, si=?, logica=?, algebra=?, metodologia=?, ipoi=?, bbdd=?, sisinf=?, redesi=?, redesii=?, ssoo=?, pctr=?, teco=?, eco=?, arco=?, orco=?, ssdd=?, isoi=?, isoii=?, progi=?, progii=? WHERE dni=?', notas_float + [dni[0],])
            else:
                # Insertar las calificaciones del usuario en la base de datos
                self.cursor.execute('INSERT INTO Notas (eda, si, logica, algebra, metodologia, ipoi, bbdd, sisinf, redesi, redesii, ssoo, pctr, teco, eco, arco, orco, ssdd, isoi, isoii, progi, progii, dni) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', notas_float + [dni[0],])
            
            self.conn.commit()
            return True, "Calificaciones actualizadas exitosamente."
        except Exception as e:
            return False, f"No se pudieron actualizar las calificaciones: {e}"
        finally:
            self.conn.close()

    def obtener_gustos(self, usuario):
        try:
            # Buscar el dni del usuario
            dni = self.obtener_dni(usuario)
            # Buscar en la base de datos los gustos del usuario
            self.cursor.execute('SELECT pregunta1, pregunta2, pregunta3, pregunta4, pregunta5, pregunta6, pregunta7, pregunta8, pregunta9 FROM Respuestas WHERE dni=?', (dni[0],))
            resultado = self.cursor.fetchall()
            if resultado:
                resultado = list(resultado[0])
            return resultado
        except Exception as e:
            print("Error al obtener los gustos del usuario:", e)
            return None
        finally:
            self.conn.close()
    
    def obtener_dni(self, usuario):
            # Buscar el dni del usuario
            self.cursor.execute('SELECT dni FROM Usuarios WHERE username=?', (usuario,))
            dni = self.cursor.fetchone()
            return dni
    
    def actualizar_formulario(self, usuario, respuestas):
        try:
            # Buscar el dni del usuario
            dni = self.obtener_dni(usuario)
            
            # Verificar si el usuario tiene un registro en la tabla Respuestas
            self.cursor.execute('SELECT * FROM Respuestas WHERE dni=?', [dni[0]])
            registro_existente = self.cursor.fetchone()
            
            if registro_existente:
                # Actualizar las respuestas del usuario en la base de datos
                self.cursor.execute('UPDATE Respuestas SET pregunta1=?, pregunta2=?, pregunta3=?, pregunta4=?, pregunta5=?, pregunta6=?, pregunta7=?, pregunta8=?, pregunta9=? WHERE dni=?', respuestas + [dni[0],])
            else:
                # Insertar las respuestas del usuario en la base de datos
                self.cursor.execute('INSERT INTO Respuestas (pregunta1, pregunta2, pregunta3, pregunta4, pregunta5, pregunta6, pregunta7, pregunta8, pregunta9, dni) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', respuestas + [dni[0],])
            
            self.conn.commit()
            return True, "Formulario realizado exitosamente."
        except Exception as e:
            return False, f"No se pudo realizar el formulario: {e}"
        finally:
            self.conn.close()

    def obtener_recomendaciones(self, usuario, notasComputacion, notasComputadores, notasISO, notasTI):
        try:
            # Buscar el dni del usuario
            dni = self.obtener_dni(usuario)
            # Buscar en la base de datos las recomendaciones del usuario
            gustos = self.obtener_gustos(usuario)
            opciones_gustos = self.obtener_opciones_gustos(gustos)
            puntajes_notas = self.obtener_puntajes_notas(notasComputacion, notasComputadores, notasISO, notasTI)
            puntajes_gustos = self.obtener_puntajes_gustos(opciones_gustos)

            puntaje_final = {}
            for key in puntajes_notas:
                puntaje_final[key] = puntajes_notas[key]*0.4 + puntajes_gustos[key]*0.6

            return puntaje_final
        except Exception as e:
            print("Error al obtener las recomendaciones del usuario:", e)
            return None
        finally:
            self.conn.close()

    def obtener_opciones_gustos(self, gustos):
        opciones = []
        for respuesta in gustos:
            # Extraer la opción seleccionada (a, b, c, d)
            opcion = respuesta.split(')')[0].strip().lower()[-1]
            opciones.append(opcion)
        return opciones
    
    def obtener_puntajes_gustos(self, opciones_gustos):
        puntajes = {}
        puntajes["Computacion"] = 0
        puntajes["Computadores"] = 0
        puntajes["ISO"] = 0
        puntajes["TI"] = 0

        for opcion in opciones_gustos:
            if opcion == 'a':
                puntajes["ISO"] += 0.1
            elif opcion == 'b':
                puntajes["Computadores"] += 0.1
            elif opcion == 'c':
                puntajes["Computacion"] += 0.1
            elif opcion == 'd':
                puntajes["TI"] += 0.1

        return puntajes

    def obtener_puntajes_notas(self, notasComputacion, notasComputadores, notasISO, notasTI):
        puntajes = {}
        puntajes["Computacion"] = self.calcular_puntaje_intensificacion(notasComputacion)
        puntajes["Computadores"] = self.calcular_puntaje_intensificacion(notasComputadores)
        puntajes["ISO"] = self.calcular_puntaje_intensificacion(notasISO)
        puntajes["TI"] = self.calcular_puntaje_intensificacion(notasTI)
        return puntajes

    def calcular_puntaje_intensificacion(self, notas_intensificacion):
        puntaje_asignatura = 0
        num_asignaturas = len(notas_intensificacion)
        for nota in notas_intensificacion:    
            # Calcular el puntaje de la asignatura
            puntaje_asignatura += nota
            # Guardar el puntaje de la asignatura
        puntaje_asignatura = puntaje_asignatura/(num_asignaturas*10)
        return puntaje_asignatura