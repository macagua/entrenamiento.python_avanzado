"""Modulo de configuraciones"""

import os
from pathlib import Path
import ZODB, ZODB.FileStorage

DB_FILE = "inventario.fs"
DB_DIR = os.path.dirname(os.path.abspath(__file__)) + os.sep + "filestorage/"
Path(DB_DIR).mkdir(parents=True, exist_ok=True)
STORAGE = ZODB.FileStorage.FileStorage(DB_DIR + DB_FILE)

DB = ZODB.DB(STORAGE)

# Lista de filas a ingresar
INSERT_MULTIPLE_COLUMNS = [
    (1, "Carro"),
    (2, "Moto"),
    (3, "Bicicleta"),
]

#import pdb; pdb.set_trace()

# Lista de filas a actualizar
UPDATE_MULTIPLE_COLUMNS = [
    ("5051", 1),
    ("6303", 2),
]