.. _python_pickle:

pickle
------

.. todo::
    TODO terminar de escribir esta sección.


.. _python_pickle_serializar:

Serializar
^^^^^^^^^^

.. todo::
    TODO terminar de escribir esta sección.


.. _python_pickle_deserializar:

Deserializar
^^^^^^^^^^^^

.. todo::
    TODO terminar de escribir esta sección.


.. _python_pickle_scaffolding:

Práctica - Caso real
^^^^^^^^^^^^^^^^^^^^

A continuación se presenta una práctica más real de implementar el uso de proyectos
con ``pickle`` para operaciones CRUD en un archivo de registros serializados:

.. literalinclude:: ../../recursos/leccion2/pickle/crud/main.py
    :language: python
    :linenos:
    :lines: 1-207

.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en el
    siguiente enlace: :download:`main.py <../../recursos/leccion2/pickle/crud/main.py>`.


.. tip::
    Para ejecutar el código :file:`main.py`, abra una consola de comando,
    acceda al directorio donde se encuentra ambos programas:

    ::

        leccion2/
        └── pickle/
            └── crud/
                └── main.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    .. code-block:: console

        $ python main.py

Asi de esta forma puede ingresar, consultar, actualizar y eliminar
registro en un archivo serializado de objetos python ``pickle``.


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion2>`


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. _`pickle`: https://docs.python.org/es/3.11/library/pickle.html
