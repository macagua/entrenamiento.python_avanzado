"""Modulo de eliminar registros en la ZODB"""

import logging
import os
import transaction
import ZODB, ZODB.FileStorage
from ZODB.POSException import StorageError
from pathlib import Path

logging.basicConfig(level=logging.INFO)

DB_PATH = os.path.dirname(os.path.abspath(__file__)) + os.sep + "filestorage/"
Path(DB_PATH).mkdir(parents=True, exist_ok=True)
DB_FILE = ZODB.FileStorage.FileStorage(DB_PATH + "productos.fs")
DB = ZODB.DB(DB_FILE)


def eliminar_registro():
    """Función para la eliminación de registro de la ZODB"""

    try:
        # Crear la instancia de DB y pasar el nombre del archivo
        conexion = DB.open()

        # Crear la instancia de conexion y llamar al método open de db
        nodo = conexion.root()
        logging.info(f"¡Conectado a la base de datos {os.path.basename(DB_FILE.getName())}!\n")

        # Mostrar el objeto a eliminar
        print(nodo['producto1'].descripcion)

        if 'producto1' in nodo.items():
            # Eliminar el objeto de la raíz
            nodo.pop("producto1")
            # Guardar los cambios en la base de datos
            transaction.commit()
            logging.info("¡Registro eliminado correctamente!\n")
        else:
            logging.info("¡No tiene ningún registro en la ZODB!\n")

    except StorageError as error:
        print("¡Fallo la eliminación de registro(s) en la ZODB!", error)
    finally:
        if conexion:
            # Cerrar la conexión a la base de datos
            conexion.close()
            logging.info(
                "¡La conexión ZODB a la base de datos {} fue cerrada!\n".format(
                    os.path.basename(DB_FILE.getName())
                )
            )


if __name__ == "__main__":
    eliminar_registro()
