.. _python_leccion3:

Serialización en la web
=======================

.. note::
    **Propósito:** es una libraría para codificar y decodificar JSON (JavaScript Object Notation).

Codifique objetos de Python como cadenas JSON y decodifique cadenas JSON en objetos de
Python. El módulo json proporciona una API similar a la de pickle convertir objetos de
Python en memoria a una representación serializada conocida como notación de objetos de
JavaScript (JSON).

A diferencia de :ref:`pickle <python_modulo_pickle>`, JSON tiene la ventaja de tener
implementaciones en muchos lenguajes (especialmente JavaScript). Se usa más ampliamente para
la comunicación entre el servidor web y el cliente en una API REST, pero también es útil
para otras necesidades de comunicación entre aplicaciones.

json
----

.. todo::
    TODO terminar de escribir esta sección.


.. _python_json_serializar:

Serializar
^^^^^^^^^^

.. todo::
    TODO terminar de escribir esta sección.


.. _python_json_deserializar:

Deserializar
^^^^^^^^^^^^

.. todo::
    TODO terminar de escribir esta sección.


.. _python_json_scaffolding:

Práctica - Caso real
^^^^^^^^^^^^^^^^^^^^

A continuación se presenta una práctica más real de implementar el uso de proyectos
con ``pickle`` para leer y escribir un archivo JSON basado en un tipo :ref:`diccionario <python_dict>`:

.. literalinclude:: ../../recursos/leccion3/json_reading_writing.py
    :language: python
    :linenos:
    :lines: 1-54


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en los
    siguientes enlaces: :download:`json_reading_writing.json <../../recursos/leccion3/json_reading_writing.json>`
    y :download:`json_reading_writing.py <../../recursos/leccion3/json_reading_writing.py>`.


.. tip::
    Para ejecutar el código :file:`json_reading_writing.json` y :file:`json_reading_writing.py`,
    abra una consola de comando, acceda al directorio donde se encuentra ambos programas:

    ::

        leccion3/
        ├── json_reading_writing.json
        └── json_reading_writing.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    .. code-block:: console

        $ python json_reading_writing.py

El anterior código al ejecutar debe mostrar el siguiente mensaje:

.. code-block:: console

    {'clientes': [{'nombre': 'Leonardo', 'apellido': 'Caballero', 'codigo_postal': '5001', 'telefono': '+58-412-4734567'}, {'nombre': 'Ana', 'apellido': 'Poleo', 'codigo_postal': '6302', 'telefono': '+58-426-5831297'}, {'nombre': 'Pedro', 'apellido': 'Lopez', 'codigo_postal': '4001', 'telefono': '+58-414-2360943'}]} <class 'dict'>

    INFO:root:Se escribió un tipo diccionario en archivo JSON

    INFO:root:Se leyó desde archivo JSON

    Nombre: Leonardo
    Apellido: Caballero
    Código postal: 5001
    Teléfono: +58-412-4734567
    Datos detallados: {'nombre': 'Leonardo', 'apellido': 'Caballero', 'codigo_postal': '5001', 'telefono': '+58-412-4734567'}

    Nombre: Ana
    Apellido: Poleo
    Código postal: 6302
    Teléfono: +58-426-5831297
    Datos detallados: {'nombre': 'Ana', 'apellido': 'Poleo', 'codigo_postal': '6302', 'telefono': '+58-426-5831297'}

    Nombre: Pedro
    Apellido: Lopez
    Código postal: 4001
    Teléfono: +58-414-2360943
    Datos detallados: {'nombre': 'Pedro', 'apellido': 'Lopez', 'codigo_postal': '4001', 'telefono': '+58-414-2360943'}


El archivo JSON creado que incluye la información de los empleados:

.. literalinclude:: ../../recursos/leccion3/json_reading_writing.json
    :language: json
    :linenos:
    :lines: 1

De esta forma se escribí y lee un archivo JSON.

----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion3>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::

.. _`json`: https://docs.python.org/es/3.11/library/json.html
