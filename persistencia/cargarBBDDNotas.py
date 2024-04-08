import sqlite3
import os

class cargarBBDDNotas:
    def __init__(self) -> None:
        pass
    def cargarNotas(self):
        # Obtener la ruta del directorio del script actual
        directorio_script = os.path.dirname(__file__)

        # Ruta completa de la base de datos
        ruta_base_datos = os.path.join(directorio_script, 'UsuariosRecomendaciones.db')

        # Conexión a la base de datos (se creará si no existe)
        conexion = sqlite3.connect(ruta_base_datos)

        # Crear un cursor para ejecutar comandos SQL
        cursor = conexion.cursor()

        # Crear la tabla "Notas" si no existe
        cursor.execute('''CREATE TABLE IF NOT EXISTS Notas (
                        dni TEXT NOT NULL,
                        asignatura TEXT NOT NULL,
                        nota DOUBLE NOT NULL,
                        FOREIGN KEY (dni) REFERENCES Usuarios(dni)
                        )''')

        # Insertar algunas notas de ejemplo para el usuario con DNI '06297500P'
        notas_ejemplo_06297500P = [
            # Notas de la rama de Computadores
            ('06297500P', 'Sistemas Operativos', 7.5),
            ('06297500P', 'Programación Concurrente y Tiempo Real', 8.2),
            ('06297500P', 'Tecnología de Computadores', 6.9),
            ('06297500P', 'Estructura de Computadores', 7.8),
            ('06297500P', 'Organización de Computadores', 8.1),
            ('06297500P', 'Arquitectura de Computadores', 7.3),
            ('06297500P', 'Sistemas Distribuidos', 7.0),
            # Notas de la rama de Ingeniería del Software
            ('06297500P', 'Ingeniería del Software I', 6.8),
            ('06297500P', 'Ingeniería del Software II', 7.6),
            ('06297500P', 'Bases de Datos', 8.4),
            ('06297500P', 'Fundamentos de la Programación I', 7.9),
            ('06297500P', 'Fundamentos de la Programación II', 8.0),
            # Notas de la rama de Computación
            ('06297500P', 'Estructura de Datos', 8.3),
            ('06297500P', 'Metodología de la Programación', 7.7),
            ('06297500P', 'Sistemas Inteligentes', 8.6),
            ('06297500P', 'Lógica', 7.2),
            ('06297500P', 'Álgebra y Matemática Discreta', 8.5),
            # Notas de la rama de Tecnología de la Información
            ('06297500P', 'Interacción Persona-Ordenador I', 7.1),
            ('06297500P', 'Redes de Computadores I', 8.7),
            ('06297500P', 'Redes de Computadores II', 8.9),
            ('06297500P', 'Sistemas de la Información', 7.4),
            ('06297500P', 'Bases de Datos', 8.8)
        ]

        # Insertar las notas de ejemplo para el usuario '06297500P'
        for nota in notas_ejemplo_06297500P:
            cursor.execute('''INSERT INTO Notas (dni, asignatura, nota)
                            VALUES (?, ?, ?)''', nota)

        # Insertar algunas notas de ejemplo para el usuario con DNI '05970690M'
        notas_ejemplo_05970690M = [
            # Notas de la rama de Computadores
            ('05970690M', 'Sistemas Operativos', 8.0),
            ('05970690M', 'Programación Concurrente y Tiempo Real', 8.5),
            ('05970690M', 'Tecnología de Computadores', 7.8),
            ('05970690M', 'Estructura de Computadores', 7.7),
            ('05970690M', 'Organización de Computadores', 8.2),
            ('05970690M', 'Arquitectura de Computadores', 8.4),
            ('05970690M', 'Sistemas Distribuidos', 8.1),
            # Notas de la rama de Ingeniería del Software
            ('05970690M', 'Ingeniería del Software I', 7.6),
            ('05970690M', 'Ingeniería del Software II', 8.0),
            ('05970690M', 'Bases de Datos', 7.9),
            ('05970690M', 'Fundamentos de la Programación I', 8.3),
            ('05970690M', 'Fundamentos de la Programación II', 8.2),
            # Notas de la rama de Computación
            ('05970690M', 'Estructura de Datos', 7.8),
            ('05970690M', 'Metodología de la Programación', 8.1),
            ('05970690M', 'Sistemas Inteligentes', 7.9),
            ('05970690M', 'Lógica', 8.0),
            ('05970690M', 'Álgebra y Matemática Discreta', 8.4),
            # Notas de la rama de Tecnología de la Información
            ('05970690M', 'Interacción Persona-Ordenador I', 7.5),
            ('05970690M', 'Redes de Computadores I', 8.2),
            ('05970690M', 'Redes de Computadores II', 8.3),
            ('05970690M', 'Sistemas de la Información', 7.8),
            ('05970690M', 'Bases de Datos', 8.1)
        ]

        # Insertar las notas de ejemplo para el usuario '05970690M'
        for nota in notas_ejemplo_05970690M:
            cursor.execute('''INSERT INTO Notas (dni, asignatura, nota)
                            VALUES (?, ?, ?)''', nota)

        # Guardar los cambios
        conexion.commit()

        # Cerrar la conexión
        conexion.close()

        print("Las notas han sido insertadas correctamente.")
