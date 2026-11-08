"""Ejemplo de codificación personalizada."""

from datetime import datetime
import json


def codificador_personalizado(objeto):
    """Codificador personalizado para objetos no serializables por defecto.

    Args:
        objeto (datetime): El objeto que se desea codificar a JSON.

    Raises:
        TypeError: Si el objeto no es serializable.

    Returns:
        datetime: La representación en cadena del objeto datetime.
    """
    if isinstance(objeto, datetime):
        return objeto.isoformat()
    raise TypeError(f"El objeto de tipo {type(objeto)} no es serializable")


registro = {"evento": "inicio_sesion", "timestamp": datetime.now()}

# Usamos el parámetro default para manejar el objeto datetime
json_texto = json.dumps(registro, default=codificador_personalizado, indent=4)
print(json_texto)
