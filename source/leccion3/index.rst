.. _python_leccion3:

Serialización en la web
=======================

La serialización es un proceso mediante el cual podemos convertir objetos de un programa
en ejecución en flujos de bytes capaces de ser almacenados en dispositivos, bases de datos
o de ser enviados a través de la red y, posteriormente, ser capaces de reconstruirlos en
los equipos donde sea necesario.

Hoy en día, los desarrolladores de aplicaciones web enfrentan el reto de incluir en sus
programas algoritmos de serialización/deserialización y transmisión de datos que permitan
convertir objetos de diferentes tipos a texto, transportarlos y finalmente volver a ser el
objeto que eran antes.

La serialización es un proceso para convertir datos en grandes cantidades de bits llamados
en inglés Stream, que luego pueden ser enviados por la red o almacenados en bases de datos.
Lo opuesto a esto se conoce como deserialización, que sería volver un objeto a su estado
natural. Este proceso lo utilizan la mayoría de aplicaciones en internet.

Existen dos tipos de serialización/deserialización:

1) El que tiene formato de texto para poder ser interpretado por el ser humado y las
   computadoras.

   .. note::
       El presente artículo se enfoca en el formato de texto que puede ser interpretado por
       el ser humano, por medio de formato :ref:`JSON <python_json>`.

2) La binaria, que solo es interpretada por las computadoras.

   .. note::
       En el artículo referente al módulo :ref:`pickle <python_modulo_pickle>` se enfoca en
       la serialización/deserialización binaria.


.. toctree::
   :maxdepth: 2

   json_format
   json

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion3>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

..
    .. disqus::
