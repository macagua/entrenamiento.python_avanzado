"""Ejemplo de escritura/lectura de un archivo JSON usando el módulo json."""

import json
import os

JSON_PATH = os.path.dirname(os.path.abspath(__file__)) + os.sep
JSON_FILE = JSON_PATH + ("config.json")

# Datos a escribir en el archivo JSON
datos_app = {"tema": "oscuro", "notificaciones": True, "intentos_maximos": 3}

# 1. Escribir (guardar) en un archivo JSON
with open(JSON_FILE, "w", encoding="utf-8") as archivo:
    json.dump(datos_app, archivo, indent=4, ensure_ascii=False)

# 2. Leer (cargar) desde un archivo JSON
with open(JSON_FILE, encoding="utf-8") as archivo:
    config_leida = json.load(archivo)

print(f"Color del tema: {config_leida['tema']}")  # Salida: oscuro
