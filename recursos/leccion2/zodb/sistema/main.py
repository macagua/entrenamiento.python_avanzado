"""Modulo de Clase ZODB"""

import logging
import transaction

from settings import *
from classes.producto import Producto
from ZODB.POSException import StorageError

def crear_conexion(ruta):
    """Crear conexión con un servidor SQLite

    Args:
        ruta (str): La ruta completa usada para leer la base de datos

    Returns:
        root (Connection): Representación conexión a la base de datos SQLite
    """
    try:
        connection = DB.open()
        root = connection.root()
        logging.info(
            f"¡Conexión a la base de datos '{os.path.basename(ruta)}' fue exitosa!\n"
        )
    except StorageError as e:
        print(f"ERROR: ¡Se produjo una falla al almacenar: '{e}'!")

    return root


#def insertar_registro(bd, registros):
def insertar_registro(bd, raiz, registros):
    """Función para la inserción de registro de la tabla

    Args:
        bd (Connection): Representación conexión a la base de datos ZODB
        registros (list): Lista de filas a ingresar
    """

    try:
        print("Listado de productos\n")
        for registro in registros:
            producto = Producto(registro[0], registro[1])
            #raiz['productos'] = producto
            raiz['productos'].append(producto)
            transaction.commit()
            print(raiz['productos'])
            print("Tipo de dato: {} ({})\n".format(
                Producto.__name__, type(raiz['productos'])
                )
            )
        logging.info(
            "¡Fueron insertado(s) {} registro(s) correctamente en la tabla!\n".format(
                len(registros)
            )
        )
        bd.close()
    except StorageError as error:
        print("¡Fallo la inserción de registro(s) en la tabla!", error)

def consultar_registro(bd, raiz):
    print(raiz.items())
    print(f"Total de productos en Inventario: {raiz.__len__()}")

def actualizar_registro(raiz, registros):
    print(raiz['productos'].descripcion)
    raiz['productos'].descripcion='Camioneta'
    transaction.commit()

def eliminar_registro(raiz):
    pass


# connection = DB.open()
# root = connection.root()

# producto1 = Producto(1, "Carro")
# root['producto1'] = producto1

# producto2 = Producto(2, "Moto")
# root['producto2'] = producto2

# producto3 = Producto(3, "Bicicleta")
# root['producto3'] = producto3

# root['productos'] = [producto1, producto2, producto3]
# transaction.commit()

# print(root.items())
# root['producto1'].descripcion='Camioneta'
# transaction.commit()

# print(root['producto1'])
# print(root['producto1'].descripcion)

# connection.close()


if __name__ == "__main__":
    conexion = DB.open()
    root = conexion.root()
    import pdb ; pdb.set_trace()
    #conexion = crear_conexion(DB)
    #insertar_registro(conexion, INSERT_MULTIPLE_COLUMNS)
    insertar_registro(conexion, root, INSERT_MULTIPLE_COLUMNS)
    consultar_registro(conexion, root)
    #actualizar_registro(conexion, UPDATE_MULTIPLE_COLUMNS, UPDATE_SQL_SCRIPTS)
    #eliminar_registro(conexion, DELETE_SQL_SCRIPTS)
    #connection.close()