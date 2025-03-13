.. _python_serializacion_objetos:

Serialización de objetos
========================

La *serialización* es el proceso de convertir un objeto en una secuencia de bytes
para almacenarlo o transmitirlo a la memoria, a una base de datos o a un archivo.
Su propósito principal es guardar el estado de un objeto para poder volver a
crearlo cuando sea necesario. El proceso inverso se denomina *deserialización*.

Por ejemplo, guardar una :ref:`lista <python_list>` de Python en un archivo de texto o
base de datos, y luego cargarlo cuando sea necesario, para ser tratado con su tipo de datos.

Formatos comunes entre los distintos lenguajes de programación incluyen XML y JSON.

Python ofrece tres módulos diferentes en la biblioteca estándar que le permiten
**serializar** y **deserializar** objetos:

.. _python_modulo_pickle:

Módulo pickle
-------------

.. note::
    **Propósito:** es una libraría para implementa protocolos binarios para **serializar**
    y **deserializar** una estructura de objetos Python, es decir, convertirlos en un flujo
    de bytes que se puede almacenar o transmitir por una red.

El módulo `pickle`_ implementa protocolos binarios para **serializar** y **deserializar**
una estructura de objetos Python.

El módulo ``pickle`` nos permite **serializar** y **deserializar** datos en archivos binarios.
Podemos usarlo para guardar y cargar registros como si fuera una base de datos simple.

En lugar de una base de datos real, usaremos un archivo ``.pkl`` para almacenar los
datos en una lista de diccionarios.

📌 **Ventajas de pickle**:

- ✅ Fácil de usar, sin necesidad de instalar bases de datos.

- ✅ Útil para almacenar estructuras de datos complejas (listas, diccionarios, objetos).

📌 **Desventajas**:

- ❌ No es ideal para grandes volúmenes de datos.

- ❌ No permite consultas avanzadas como SQL.

..
    .. todo::
        TODO Terminar de escribir esta sección.


    .. _python_modulo_pickle_codificar:

    Codificación
    ^^^^^^^^^^^^

    .. todo::
        TODO terminar de escribir esta sección.


    .. _python_modulo_pickle_decodificar:

    Decodificación
    ^^^^^^^^^^^^^^

    .. todo::
        TODO terminar de escribir esta sección.


.. _python_modulo_pickle_scaffolding:

Práctica - Caso real
^^^^^^^^^^^^^^^^^^^^

A continuación se presenta una práctica más real de implementar el uso de proyectos
con ``pickle`` para operaciones CRUD en un archivo de registros serializados:

.. literalinclude:: ../../recursos/leccion2/pickle/sistema/main.py
    :language: python
    :linenos:
    :lines: 1-203

.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en el
    siguiente enlace:

    - :download:`main.py <../../recursos/leccion2/pickle/sistema/main.py>`.


.. tip::
    Para ejecutar el código :file:`main.py`, abra una consola de comando,
    acceda al directorio donde se encuentra el programa:

    .. code-block:: pycon
        :class: no-copy

        proyectos/
        └── pickle/
            └── sistema/
                └── main.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    .. code-block:: console

        python3 main.py

    El anterior código al ejecutar debe mostrar el siguiente mensaje:

    .. code-block:: console
        :class: no-copy

        ==============
        MENÚ PRINCIPAL
        ==============

        1) Crear
        2) Consultar
        3) Actualizar
        4) Eliminar
        5) Salir

        Elija uno:

    Luego de crear un registro, el archivo :file:`inventario.pkl` debe ser
    creado en el directorio :file:`filestorage/` como se muestra a continuación:

    .. code-block:: pycon
        :class: no-copy

        proyectos/
        └── pickle/
            └── sistema/
                ├── filestorage/
                │   └── inventario.pkl
                └── main.py

.. tip::
    En lugar de una base de datos real, usaremos un archivo :file:`inventario.pkl`` para almacenar los
    datos en una lista de diccionarios.

Asi de esta forma puede ingresar, consultar, actualizar y eliminar
registro en un archivo serializado de objetos python ``pickle``.


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion2>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html


..
  .. disqus::

.. _`pickle`: https://docs.python.org/es/3/library/pickle.html
