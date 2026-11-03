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

.. todo::
    TODO terminar de escribir esta sección.


.. _python_modulo_json_codificar:

Codificación
^^^^^^^^^^^^


..
    .. code-block:: python
        :linenos:

        import json

        hello_world = {"greeting": "Hello, world!"}

        print(hello_world["greeting"])

        print(type(hello_world))

        json.dumps(hello_world)

        type(json.dumps(hello_world))

        str(hello_world)


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


.. todo::
    TODO terminar de escribir esta sección.


.. _python_modulo_json_decodificar:

Decodificación
^^^^^^^^^^^^^^



.. code-block:: python
    :linenos:

    import json

    # Abrir el archivo en modo lectura
    with open("clientes.json", encoding="utf-8") as json_leido:
        # Leyendo desde archivo JSON
        data = json.load(json_leido)
        for cliente in data["clientes"]:
            print(f"📜 Nombre:", cliente["nombre"])
            print(f"📜 Apellido:", cliente["apellido"])
            print(f"📜 Código postal:", cliente["codigo_postal"])
            print(f"📜 Teléfono:", cliente["telefono"])
            print(f"📜 Datos detallados: {cliente}\n")
        # Cerrar el archivo después de leerlo
        json_leido.close()
        print("✅ Se leyó el archivo JSON 'clientes.json'.")


.. todo::
    TODO terminar de escribir esta sección.


.. _python_modulo_json_scaffolding:

Práctica - Caso real
^^^^^^^^^^^^^^^^^^^^

A continuación se presenta una práctica más real de implementar el uso de proyectos
con el módulo :mod:`json` para leer y escribir un archivo JSON basado en un tipo :ref:`diccionario <python_dict>`:


Estructura de archivos
^^^^^^^^^^^^^^^^^^^^^^

Para crear la estructura de archivos del proyecto ``JSON`` debe ejecutar los siguientes comandos:

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

Así de esta forma puede leer y escribir registros en un archivo JSON usando el módulo :mod:`json`.


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_leccion10_json>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

..
    .. disqus::

.. _`Standard ECMA-262 3rd Edition - Diciembre 1999`: https://ecma-international.org/wp-content/uploads/ECMA-262_3rd_edition_december_1999.pdf
.. _`JavaScript`: https://es.wikipedia.org/wiki/JavaScript
.. _`formato JSON`: https://es.wikipedia.org/wiki/JSON
.. _`API REST`: https://es.wikipedia.org/wiki/Transferencia_de_Estado_Representacional
