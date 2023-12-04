.. _python_leccion4:

Base de datos relacional
========================

Una `base de datos`_ es un conjunto de datos pertenecientes a un mismo
contexto y almacenados sistemáticamente para su posterior uso.

Una base de datos relacional, es un tipo de bases de datos (BD) que
cumple con el modelo relacional (el modelo más utilizado actualmente
para implementar las BD ya planificadas).

El sistema de gestión de bases de datos relacionales o Relational
Database Management System (RDBMS), es el software utilizado para
mantener las bases de datos relacionales.

Structured Query Language
-------------------------

Por defecto todos los sistemas de bases de datos relacionales utilizan
el *Structured Query Language* (`SQL <https://es.wikipedia.org/wiki/SQL>`_)
para consultar y mantener la base de datos.


.. _python_base_crear_tabla:

Crear tablas
^^^^^^^^^^^^

Si requiere crear una tabla, a continuación tiene un ejemplo:

.. literalinclude:: ../../recursos/leccion4/sistema/sistema.sql
    :language: sql
    :linenos:
    :lines: 47-58


.. _python_base_ingresar_registro:

Insertar registros
^^^^^^^^^^^^^^^^^^

Si requiere insertar registro en una tabla, a continuación tiene un ejemplo:

.. literalinclude:: ../../recursos/leccion4/sistema/sistema_data.sql
    :language: sql
    :linenos:
    :lines: 2-7


.. _python_base_consultar_registro:

Consultar registros
^^^^^^^^^^^^^^^^^^^

Si requiere consultar registros de tabla, a continuación tiene un ejemplo:

.. literalinclude:: ../../recursos/leccion4/sistema/sistema_data.sql
    :language: sql
    :linenos:
    :lines: 10-11


.. _python_base_actualizar_registro:

Actualizar registros
^^^^^^^^^^^^^^^^^^^^

Si requiere actualizar registro de tabla, a continuación tiene un ejemplo:

.. literalinclude:: ../../recursos/leccion4/sistema/sistema_data.sql
    :language: sql
    :linenos:
    :lines: 14-15


.. _python_base_eliminar_registro:

Eliminar registros
^^^^^^^^^^^^^^^^^^

Si requiere eliminar registro de tabla, a continuación tiene un ejemplo:

.. literalinclude:: ../../recursos/leccion4/sistema/sistema_data.sql
    :language: sql
    :linenos:
    :lines: 18


Asi de esta forma puede crear una tabla, ingresar, consultar, actualizar y eliminar
registro a dicha tabla.

----


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic
    :download:`aquí <../../recursos/leccion4/sistema/sistema_data.sql>`.


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion4>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::

.. _`base de datos`: https://es.wikipedia.org/wiki/Base_de_datos