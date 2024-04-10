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
                        eda DOUBLE NOT NULL,
                        si DOUBLE NOT NULL,
                        logica DOUBLE NOT NULL,
                        algebra DOUBLE NOT NULL,
                        metodologia DOUBLE NOT NULL,
                        ipoi DOUBLE NOT NULL,
                        bbdd DOUBLE NOT NULL,
                        sisinf DOUBLE NOT NULL,
                        redesi DOUBLE NOT NULL,
                        redesii DOUBLE NOT NULL,
                        ssoo DOUBLE NOT NULL,
                        pctr DOUBLE NOT NULL,
                        teco DOUBLE NOT NULL,
                        eco DOUBLE NOT NULL,
                        arco DOUBLE NOT NULL,
                        orco DOUBLE NOT NULL,
                        ssdd DOUBLE NOT NULL,
                        isoi DOUBLE NOT NULL,
                        isoii DOUBLE NOT NULL,
                        progi DOUBLE NOT NULL,
                        progii DOUBLE NOT NULL,
                        FOREIGN KEY (dni) REFERENCES Usuarios(dni)
                        )''')

        # Insertar algunas notas de ejemplo para el usuario con DNI '06297500P'
        notas_ejemplo = [
            # Notas de la rama de Computadores
            ('06297500P', 5.0, 6.2, 9.2, 4.5, 6.5, 7.5, 8.7, 7.0, 7.7, 7.6, 7.3, 8.0, 5.0, 5.5, 5.9, 3.5, 7.6, 4.9, 6.6, 9.8, 7.5),
            ('05970690M', 8.1, 5.0, 8.0, 6.5, 7.0, 6.5, 7.5, 8.0, 7.5, 7.0, 7.5, 8.0, 6.5, 7.0, 7.5, 8.0, 7.5, 7.0, 7.5, 8.0, 7.5)
        ]

        # Insertar las notas de ejemplo para el usuario '05970690M'
        for nota in notas_ejemplo:
            cursor.execute('''INSERT INTO Notas (dni, eda, si, logica, algebra, metodologia, ipoi, bbdd, sisinf, redesi, redesii, ssoo, pctr, teco, eco, arco, orco, ssdd, isoi, isoii, progi, progii) 
                            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', nota)

        # Guardar los cambios
        conexion.commit()

        # Cerrar la conexión
        conexion.close()

        print("Las notas han sido insertadas correctamente.")
