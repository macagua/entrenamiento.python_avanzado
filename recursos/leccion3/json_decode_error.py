"""Ejemplo de manejo de errores al decodificar un JSON roto."""

import json

json_roto = '{"nombre": "Carlos", edad: 25}'  # Falta comilla en la clave 'edad'

try:
    json.loads(json_roto)
except json.JSONDecodeError as e:
    print(f"Error de sintaxis en JSON: {e}")
