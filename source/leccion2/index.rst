.. _python_leccion2:

pickle - Serialización de objetos
=================================

.. note::
    **Propósito:** es una libraría para implementa protocolos binarios para serializar
    y deserializar una estructura de objetos Python, es decir, convertirlos en un flujo
    de bytes que se puede almacenar o transmitir por una red.

La *serialización* es el proceso de convertir un objeto en una secuencia de bytes
para almacenarlo o transmitirlo a la memoria, a una base de datos o a un archivo.
Su propósito principal es guardar el estado de un objeto para poder volver a
crearlo cuando sea necesario. El proceso inverso se denomina *deserialización*.

Por ejemplo, guardar una :ref:`lista <python_list>` de Python en un archivo de texto o base de datos,
y luego cargarlo cuando sea necesario, para ser tratado con su tipo de datos.

Formatos comunes entre los distintos lenguajes de programación incluyen XML y JSON.

Python ofrece tres módulos diferentes en la biblioteca estándar que le permiten serializar y deserializar objetos:

CRUD con archivo pickle
-----------------------

.. literalinclude:: ../../recursos/leccion2/inventarios/main.py
    :language: python
    :linenos:
    :lines: 1-191

Asi de esta forma puede ingresar, consultar, actualizar y eliminar
registro en un archivo serializado de objetos python ``pickle``.


----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion2>`


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. _`pickle`: https://docs.python.org/es/3.11/library/pickle.html
