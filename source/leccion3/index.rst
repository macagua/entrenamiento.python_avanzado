.. _python_leccion3:

Serialización en la web
=======================

.. note::
    **Propósito:** es una libraría para codificar y decodificar *JavaScript Object Notation (JSON)*.

El módulo `json`_ le permite codificar objetos de Python como cadenas en `formato JSON`_ y decodifiquelas
en objetos de Python. El módulo ``json`` proporciona una API similar a la del módulo :ref:`pickle <python_modulo_pickle>`
para convertir objetos de Python en memoria a una representación serializada conocida como
*JavaScript Object Notation (JSON)*.

Como su nombre indica, JSON tiene su origen en JavaScript. Sin embargo, JSON ha trascendido sus orígenes para
convertirse en un lenguaje agnóstico y ahora es reconocido como el estándar para el intercambio de datos.

.. figure:: ../_static/images/json_logo.png
    :align: center
    :width: 100%

    Logotipo de JavaScript Object Notation (JSON)

La popularidad de JSON puede atribuirse al soporte nativo por parte del lenguaje JavaScript, lo que se traduce
en un excelente rendimiento de análisis sintáctico en los navegadores web. Además, la sencilla sintaxis de JSON
permite tanto a humanos como a ordenadores leer y escribir datos JSON sin esfuerzo.

A diferencia de :ref:`pickle <python_modulo_pickle>`, JSON tiene la ventaja de tener
implementaciones en muchos lenguajes (especialmente JavaScript). Se usa más ampliamente para
la comunicación entre el servidor web y el cliente en una API REST, pero también es útil
para otras necesidades de comunicación entre aplicaciones.

Para tener una primera impresión de JSON, eche un vistazo a este código de ejemplo:

.. code-block:: json
    :linenos:

    {
        "greeting": "Hello, world!"
    }



.. _python_modulo_json:

Módulo json
-----------

El módulo `json`_ expone una API familiar a los usuarios de los módulos de la biblioteca estándar `marshal`_
y :ref:`pickle <python_modulo_pickle>`.

.. todo::
    TODO terminar de escribir esta sección.


.. _python_modulo_json_codificar:

Codificación
^^^^^^^^^^^^



.. code-block:: python
    :linenos:

    import json

    hello_world = {"greeting": "Hello, world!"}

    print(hello_world["greeting"])

    print(type(hello_world))

    json.dumps(hello_world)

    type(json.dumps(hello_world))

    str(hello_world)



.. todo::
    TODO terminar de escribir esta sección.


.. _python_modulo_json_decodificar:

Decodificación
^^^^^^^^^^^^^^



.. code-block:: python
    :linenos:


    import json

.. todo::
    TODO terminar de escribir esta sección.


.. _python_modulo_json_scaffolding:

Práctica - Caso real
^^^^^^^^^^^^^^^^^^^^

A continuación se presenta una práctica más real de implementar el uso de proyectos
con el módulo ``json`` para leer y escribir un archivo JSON basado en un tipo :ref:`diccionario <python_dict>`:

A continuación se presenta y explica el uso de cada archivo para este proyecto:

*Archivo* :file:`json_reading_writing.py`

Módulo de principal del programa.

.. literalinclude:: ../../recursos/leccion3/json_reading_writing.py
    :language: python
    :linenos:
    :lines: 1-64


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

        INFO:root:✅ Se escribió un tipo diccionario dentro de un archivo JSON 'clientes.json'.

        INFO:root:✅ Se leyó el archivo JSON 'clientes.json'.

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

        INFO:root:✅ Se cerro el archivo JSON 'clientes.json'.

    La ejecucion anterior generar la siguiente estructura:

    .. code-block:: console
        :class: no-copy

        proyectos/
        └── json/
            ├── clientes.json
            └── json_reading_writing.py

    *Archivo* :file:`clientes.json`

    Archivo en `formato JSON`_ llamado :file:`clientes.json`
    la cual no se incluye ya que cada vez que se inicia el programa :file:`json_reading_writing.py` se sustituye y crea
    nuevamente, para cuidar la creación de los datos iniciales.

Asi de esta forma puede leer y escribir registros en un archivo JSON usando la librería ``json``.

----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion3>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

..
    .. disqus::

.. _`marshal`: https://docs.python.org/es/3.11/library/marshal.html#
.. _`json`: https://docs.python.org/es/3.11/library/json.html
.. _`formato JSON`: https://es.wikipedia.org/wiki/JSON
