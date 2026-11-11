.. _python_modulo_json:

Módulo json
-----------

.. note::
    **Propósito:** usar el módulo que incorpora Python para codificar y decodificar **JavaScript Object
    Notation** (:ref:`JSON <python_json>`).

El módulo :mod:`json` expone una API familiar a los usuarios de los módulos de la biblioteca estándar :mod:`marshal`
y :ref:`pickle <python_modulo_pickle>`. Este le permite codificar objetos de Python como cadenas en formato
:ref:`JSON <python_json>` y decodifiquelas en objetos de Python.

Además proporciona una API similar al módulo :ref:`pickle <python_modulo_pickle>` para convertir objetos de
Python en memoria a una representación serializada conocida como **JavaScript Object Notation (JSON)**.

.. _python_modulo_json_codificar:

Codificación
^^^^^^^^^^^^

La codificación *(Serialización)* convierte objetos de Python (como
:ref:`diccionarios <python_dict>` y :ref:`listas <python_list>`)
en texto estructurado en :ref:`formato JSON <python_json>`.

- ``json.dumps()``: Convierte un objeto Python y devuelve una cadena
  de texto.

- ``json.dump()``: Convierte un objeto Python y lo escribe directamente
  en un archivo.

Parámetros de Formato Clave:

- ``indent``: Permite tabular la salida con espacios para que sea legible
  por humanos (pretty print).

- ``ensure_ascii=False``: Permite conservar caracteres especiales (como
  tildes o eñes) en texto plano en lugar de convertirlos a códigos de
  escape ASCII (\u00e1).

- ``sort_keys=True``: Ordena alfabéticamente las claves del :ref:`diccionario <python_dict>`
  resultante.

Ejemplo práctico de ``json.dumps()``:

.. code-block:: python

    import json

    configuracion = {
        "servidor": "localhost",
        "puerto": 5432,
        "depuracion": True,
        "modulos": ["auth", "base_datos"],
    }

    # Codificamos a una cadena JSON legible con indentación y soporte para acentos
    json_bonito = json.dumps(configuracion, indent=4, ensure_ascii=False, sort_keys=True)

    print(json_bonito)

Salida generada:

.. code-block:: json

    {
        "depuracion": true,
        "modulos": [
            "auth",
            "base_datos"
        ],
        "puerto": 5432,
        "servidor": "localhost"
    }

De esta forma, puede codificar objetos de Python a texto en formato
:ref:`JSON <python_json>` usando el módulo :mod:`json`.

----

Ejemplo práctico de ``json.dump()``:

.. code-block:: python
    :linenos:

    import json

    # Data a escribir
    clientes_data = {
        "clientes": [
            {
                "nombre": "Leonardo",
                "apellido": "Caballero",
                "codigo_postal": "5001",
                "telefono": "+58-412-4734567",
            }
        ]
    }
    # Abriendo archivo para escribir un tipo diccionario 'clientes_data'
    with open("clientes.json", mode="w", encoding="utf-8") as json_nuevo:
        json.dump(clientes_data, json_nuevo)
        # Cerrar el archivo después de escribirlo
        json_nuevo.close()
        print("✅ Se escribió el archivo JSON 'clientes.json'.")


De esta forma, puede escribir registros en un archivo :ref:`JSON <python_json>`
usando el módulo :mod:`json`.

----

.. _python_modulo_json_decodificar:

Decodificación
^^^^^^^^^^^^^^

La deserialización *(Deserialización)* consiste en transformar texto o archivos
en :ref:`formato JSON <python_json>` a estructuras de datos nativas de Python
(principalmente :ref:`diccionarios <python_dict>` y :ref:`listas <python_list>`).

- ``json.loads()``: Carga :ref:`JSON <python_json>` desde un ``string`` o
  :ref:`cadena de caracteres <python_str>`.

- ``json.load()``: Carga :ref:`JSON <python_json>` desde un :ref:`archivo <python_cls_file>`
  o ``stream`` abierto.

Ejemplo práctico de ``json.loads()``:

.. code-block:: python
    :linenos:

    import json

    # Cadena de texto con formato JSON (nótese el uso de comillas dobles)
    datos_json = (
        '{"nombre": "Ana", "edad": 30, "activo": true, "skills": ["Python", "FastAPI"]}'
    )

    # Decodificamos la cadena a un diccionario de Python
    usuario = json.loads(datos_json)

    print(type(usuario))  # Salida: <class 'dict'>
    print(usuario["nombre"])  # Salida: Ana
    print(usuario["skills"][0])  # Salida: Python


De esta forma, puede decodificar texto en formato :ref:`JSON <python_json>`
a estructuras de datos nativas de Python usando el módulo :mod:`json`.


----


Ejemplo práctico de ``json.load()``:

.. literalinclude:: ../../recursos/leccion3/json_reading.py
    :language: python
    :linenos:
    :lines: 1-21


De esta forma, puede leer registros desde un archivo :ref:`JSON <python_json>`
usando el módulo :mod:`json`.


----


Trabajo con archivos
^^^^^^^^^^^^^^^^^^^^

En aplicaciones reales, los datos :ref:`JSON <python_json>` suelen
almacenarse en archivos de configuración o persistencia, usando los
metodos ``json.load`` y ``json.dump``.

.. literalinclude:: ../../recursos/leccion3/json_file.py
    :language: python
    :linenos:
    :lines: 1-20


De esta forma, puede trabajar con archivos :ref:`JSON <python_json>` para guardar y
cargar configuraciones o datos persistentes usando el módulo :mod:`json`.


----


Manejo de errores y Tipos no serializables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Manipular datos :ref:`JSON <python_json>` puede generar errores si el contenido
no es válido o si se intenta serializar tipos de datos que no son compatibles
con el formato :ref:`JSON <python_json>`.

A continuación se presentan algunas consideraciones importantes:

Gestión de errores de decodificación
`````````````````````````````````````

Si intentas procesar un :ref:`JSON <python_json>` mal formado (por ejemplo,
con comas finales sobrantes o comillas simples), Python lanzará una
:ref:`excepción <python_errores>` del tipo ``json.JSONDecodeError``.

.. literalinclude:: ../../recursos/leccion3/json_decode_error.py
    :language: python
    :linenos:
    :lines: 1-10


De esta forma, puede manejar errores de decodificación al procesar datos en formato
:ref:`JSON <python_json>` usando el módulo :mod:`json`.


----


Serialización de tipos complejos
`````````````````````````````````

Por defecto, tipos como  :ref:`datetime.datetime <python_modulo_datetime>` o
instancias de clases personalizadas no son serializables directamente por
``json.dumps()``, lo que genera una excepción :ref:`TypeError <python_exception_typeerror>`.

Para solucionarlo, puedes pasar una función personalizada al parámetro default:

.. literalinclude:: ../../recursos/leccion3/json_encoder_datetime.py
    :language: python
    :linenos:
    :lines: 1-28


De esta forma, puede serializar tipos complejos como el módulo :ref:`datetime <python_modulo_datetime>`
usando una función personalizada con el módulo :mod:`json`.


----


.. _python_modulo_json_scaffolding:

Práctica - Caso real
^^^^^^^^^^^^^^^^^^^^

A continuación se presenta una práctica más real de implementar el uso de proyectos
con el módulo :mod:`json` para leer y escribir un archivo :ref:`JSON <python_json>`
basado en un tipo :ref:`diccionario <python_dict>`:


Estructura de archivos
```````````````````````

Para crear la estructura de archivos del proyecto debe ejecutar los siguientes comandos:

.. tabs::

   .. group-tab:: macOS, Linux, y WSL

      Crear y acceder al directorio ``json`` en un solo comando, ejecutando el siguiente comando:

      .. code-block:: console

          mkdir -p ~/proyectos/json && cd $_

      El comando anterior crea la siguiente estructura de directorios:

      .. code-block:: console
          :class: no-copy

          proyectos/
          └── json/

      Si tiene la estructura de archivo previa, entonces puede continuar con la siguiente sección.

   .. group-tab:: Windows

      Debe crear el directorio ``json``, ejecutando el siguiente comando:

      .. code-block:: console

          md .\proyectos\json

      Debe acceder al directorio , ejecutando el siguiente comando:

      .. code-block:: console

          cd .\proyectos\json

      El comando anterior crea la siguiente estructura de directorios:

      .. code-block:: console
          :class: no-copy

          proyectos/
          └── json/

      Si tiene la estructura de archivo previa, entonces puede continuar con la siguiente sección.

A continuación se presenta y explica el uso de cada archivo para este proyecto:

*Archivo* :file:`json_reading_writing.py`

Módulo de principal del programa.

.. literalinclude:: ../../recursos/leccion3/json_reading_writing.py
    :language: python
    :linenos:
    :lines: 1-63


----


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en el
    siguiente enlace:

    - :download:`json_reading_writing.py <../../recursos/leccion3/json_reading_writing.py>`.


.. tip::
    Para ejecutar el código :file:`json_reading_writing.py`, abra una consola de comando,
    acceda al directorio donde se encuentra el programa:

    .. code-block:: console
        :class: no-copy

        proyectos/
        └── json/
            └── json_reading_writing.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    .. code-block:: console

        python3 json_reading_writing.py

    El anterior código al ejecutar debe mostrar el siguiente mensaje:

    .. code-block:: console

        INFO:root:✅ Se escribió el archivo JSON 'clientes.json'.

        📜 Nombre: Leonardo
        📜 Apellido: Caballero
        📜 Código postal: 5001
        📜 Teléfono: +58-412-4734567
        📜 Datos detallados: {'nombre': 'Leonardo', 'apellido': 'Caballero', 'codigo_postal': '5001', 'telefono': '+58-412-4734567'}

        📜 Nombre: Ana
        📜 Apellido: Poleo
        📜 Código postal: 6302
        📜 Teléfono: +58-426-5831297
        📜 Datos detallados: {'nombre': 'Ana', 'apellido': 'Poleo', 'codigo_postal': '6302', 'telefono': '+58-426-5831297'}

        📜 Nombre: Manuel
        📜 Apellido: Matos
        📜 Código postal: 4001
        📜 Teléfono: +58-414-2360943
        📜 Datos detallados: {'nombre': 'Manuel', 'apellido': 'Matos', 'codigo_postal': '4001', 'telefono': '+58-414-2360943'}

        INFO:root:✅ Se leyó el archivo JSON 'clientes.json'.

    La ejecución anterior generar la siguiente estructura:

    .. code-block:: console
        :class: no-copy

        proyectos/
        └── json/
            ├── clientes.json
            └── json_reading_writing.py

    *Archivo* :file:`clientes.json`

    Archivo en formato :ref:`JSON <python_json>` llamado :file:`clientes.json`
    la cual no se incluye ya que cada vez que se inicia el programa :file:`json_reading_writing.py` se sustituye y crea
    nuevamente, para cuidar la creación de los datos iniciales.

Así de esta forma puede leer y escribir registros en un archivo :ref:`JSON <python_json>`,
usando el módulo :mod:`json`.


----


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en los
    siguientes enlaces:

    - :download:`json_decode_error.py <../../recursos/leccion3/json_decode_error.py>`.

    - :download:`json_encoder_datetime.py <../../recursos/leccion3/json_encoder_datetime.py>`

    - :download:`json_file.py <../../recursos/leccion3/json_file.py>`

    - :download:`json_reading.py <../../recursos/leccion3/json_reading.py>`

    - :download:`json_reading.py <../../recursos/leccion3/json_reading.py>`.


.. tip::
    Para ejecutar el código :file:`json_decode_error.py`, :file:`json_encoder_datetime.py`,
    :file:`json_file.py`, :file:`json_reading.py`, y :file:`json_reading.py`, abra una
    consola de comando, acceda al directorio donde se encuentra los programas:

    ::

        leccion2/
        ├── json_decode_error.py
        ├── json_encoder_datetime.py
        ├── json_file.py
        └── json_reading.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    .. code-block:: console

        python3 json_decode_error.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    .. code-block:: console

        python3 json_encoder_datetime.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    .. code-block:: console

        python3 json_file.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    .. code-block:: console

        python3 json_reading.py


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion3>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

..
    .. disqus::
