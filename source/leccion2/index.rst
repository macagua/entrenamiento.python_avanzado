.. _python_leccion2:

Serialización de objetos
========================

La *serialización* es el proceso de convertir un objeto en una secuencia de bytes
para almacenarlo o transmitirlo a la memoria, a una base de datos o a un archivo.
Su propósito principal es guardar el estado de un objeto para poder volver a
crearlo cuando sea necesario. El proceso inverso se denomina *deserialización*.

Por ejemplo, guardar una :ref:`lista <python_list>` de Python en un :ref:`archivo de texto <python_cls_file>`
o base de datos, y luego cargarlo cuando sea necesario, para ser tratado con su tipo
de datos.

Formatos comunes entre los distintos lenguajes de programación incluyen XML y :ref:`JSON <python_json>`.

Python ofrece varios módulos diferentes en la biblioteca estándar que le permiten
serializar y deserializar objetos:

.. toctree::
   :maxdepth: 2

   pickle
   zodb


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion2>`


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html


..
  .. disqus::

.. _`pickle`: https://docs.python.org/es/3.11/library/pickle.html
