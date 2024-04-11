import sqlite3
import os
class cargarBBDDRespuestas:
    def __init__(self) -> None:
        pass
    def cargarRespuestas(self):
        # Obtener la ruta del directorio del script actual
        directorio_script = os.path.dirname(__file__)

        # Ruta completa de la base de datos
        ruta_base_datos = os.path.join(directorio_script, 'UsuariosRecomendaciones.db')

        # Conexión a la base de datos (se creará si no existe)
        conexion = sqlite3.connect(ruta_base_datos)

        # Crear un cursor para ejecutar comandos SQL
        cursor = conexion.cursor()

        # Crear la tabla "Respuestas" si no existe
        cursor.execute('''CREATE TABLE IF NOT EXISTS Respuestas (
                        dni TEXT NOT NULL,
                        pregunta1 TEXT NOT NULL,
                        pregunta2 TEXT NOT NULL,
                        pregunta3 TEXT NOT NULL,
                        pregunta4 TEXT NOT NULL,
                        pregunta5 TEXT NOT NULL,
                        pregunta6 TEXT NOT NULL,
                        pregunta7 TEXT NOT NULL,
                        pregunta8 TEXT NOT NULL,
                        pregunta9 TEXT NOT NULL,
                        FOREIGN KEY (dni) REFERENCES Usuarios(dni)
                        )''')

        # Insertar las respuestas de ejemplo para el usuario con DNI '06297500P'
        respuestas_ejemplo_06297500P = [
            ('06297500P', 'a) Desarrollo de software y sistemas.', 'b) Programación de sistemas y tiempo real.',
              'c) Análisis y manipulación de grandes volúmenes de datos.', 'd) Creación de interfaces de usuario.',
                'a) Programación orientada a objetos y desarrollo de aplicaciones.', 'a) Desarrollo de software para diferentes plataformas y aplicaciones.',
                  'b) Profundizar en el funcionamiento interno de los sistemas informáticos.', 'b) Investigación y diseño de nuevas arquitecturas de computadoras.',
                    'a) Crear soluciones intuitivas y eficientes para usuarios finales.'),
        ]

        # Insertar las respuestas de ejemplo para el usuario '06297500P'
        for respuestas in respuestas_ejemplo_06297500P:
            cursor.execute('''INSERT INTO Respuestas (dni, pregunta1, pregunta2, pregunta3, pregunta4, pregunta5, pregunta6, pregunta7, pregunta8, pregunta9)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', respuestas)

        # Insertar las respuestas de ejemplo para el usuario con DNI '05970690M'
        respuestas_ejemplo_05970690M = [
            ('05970690M', 'd) Gestión y diseño de redes de computadores.', 'd) Diseño y configuración de redes informáticas.',
              'd) Configuración y administración de redes y sistemas de información.', 'd) Creación de interfaces de usuario.',
                'd) Configuración y administración de redes y sistemas de información.', 'a) Desarrollo de software para diferentes plataformas y aplicaciones.',
                  'a) Convertirme en un desarrollador de software altamente competente.', 'b) Investigación y diseño de nuevas arquitecturas de computadoras.',
                    'c) Abordar problemas de análisis de datos para obtener información significativa.'),
        ]

        # Insertar las respuestas de ejemplo para el usuario '05970690M'
        for respuestas in respuestas_ejemplo_05970690M:
            cursor.execute('''INSERT INTO Respuestas (dni, pregunta1, pregunta2, pregunta3, pregunta4, pregunta5, pregunta6, pregunta7, pregunta8, pregunta9)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', respuestas)

        # Guardar los cambios
        conexion.commit()

        # Cerrar la conexión
        conexion.close()

        print("Las respuestas han sido insertadas correctamente.")
