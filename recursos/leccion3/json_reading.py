"""Ejemplo de lectura de un archivo JSON usando el módulo json."""

import json
import os

JSON_PATH = os.path.dirname(os.path.abspath(__file__)) + os.sep
JSON_FILE = JSON_PATH + ("clientes.json")

# Abrir el archivo en modo lectura
with open(JSON_FILE, encoding="utf-8") as json_leido:
    # Leyendo desde archivo JSON
    data = json.load(json_leido)
    for cliente in data["clientes"]:
        print(f"📜 Nombre:, {cliente['nombre']}")
        print(f"📜 Apellido:, {cliente['apellido']}")
        print(f"📜 Código postal:, {cliente['codigo_postal']}")
        print(f"📜 Teléfono:, {cliente['telefono']}")
        print(f"📜 Datos detallados: {cliente}\n")
    # Cerrar el archivo después de leerlo
    json_leido.close()
    print("✅ Se leyó el archivo JSON 'clientes.json'.")
