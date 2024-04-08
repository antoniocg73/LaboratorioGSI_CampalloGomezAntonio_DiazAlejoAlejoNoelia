from persistencia.cargaBBDDUsuarios import cargarBBDDUsuarios
from persistencia.cargarBBDDNotas import cargarBBDDNotas
from persistencia.cargarBBDDRespuestas import cargarBBDDRespuestas
from presentacion.InterfazAplicacion import InterfazAplicacion
import os

if __name__ == '__main__':

    archivoBBDD_db = "persistencia/basesDeDatos/UsuariosRecomendaciones.db"

    

    # Utiliza os.path.exists para comprobar si el archivo existe.
    def existe_archivo(archivoBBDD_db):
        if os.path.exists(archivoBBDD_db):
            return True
        else:
            return False
        
    if not (existe_archivo(archivoBBDD_db)):
        cargarBBDDUsuarios().cargaUsuarios()
        cargarBBDDNotas().cargarNotas()
        cargarBBDDRespuestas().cargarRespuestas()
    #Siempre se ejecutará la interfaz de la aplicación
    InterfazAplicacion()

    
