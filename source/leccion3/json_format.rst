.. _python_json:

JavaScript Object Notation - JSON
---------------------------------

El JavaScript Object Notation - JSON (o en español *Notación de Objetos de JavaScript*) es
un formato ligero de intercambio de datos. Leerlo y escribirlo es simple para humanos, mientras
que para las máquinas es simple interpretarlo y generarlo. Está basado en un subconjunto del
Lenguaje de Programación `JavaScript`_, `Standard ECMA-262 3rd Edition - Diciembre 1999`_.

**JSON** es un formato de texto que es completamente independiente del lenguaje pero utiliza
convenciones que son ampliamente conocidos por los programadores de la familia de lenguajes C,
incluyendo C, C++, C#, Java, JavaScript, Perl, :ref:`Python <python_modulo_json>`, y muchos otros.
Estas propiedades hacen que **JSON** sea un lenguaje ideal para el intercambio de datos.


**JSON** ha trascendido sus orígenes para convertirse en un lenguaje agnóstico y ahora es
reconocido como el estándar para el intercambio de datos.

.. figure:: ../_static/images/json_logo.png
    :align: center
    :width: 100%

    Logotipo de JavaScript Object Notation (JSON)

La popularidad de **JSON** puede atribuirse al soporte nativo por parte del lenguaje JavaScript,
lo que se traduce en un excelente rendimiento de análisis sintáctico en los navegadores web.
Además, la sencilla sintaxis de **JSON** permite tanto a humanos como a ordenadores leer y escribir
datos **JSON** sin esfuerzo.

A diferencia del módulo :ref:`pickle <python_modulo_pickle>`, el formato :ref:`JSON <python_json>`
tiene la ventaja de tener implementaciones en muchos lenguajes (especialmente *JavaScript*). Se usa
más ampliamente para la comunicación entre el servidor web y el cliente en una `API REST`_, pero
también es útil para otras necesidades de comunicación entre aplicaciones.


Estructura y formato JSON
^^^^^^^^^^^^^^^^^^^^^^^^^^

JSON está constituído por dos estructuras:

- Una colección de pares de nombre/valor. En varios lenguajes esto es conocido como un objeto,
  registro, estructura, :ref:`diccionario <python_dict>`, tabla hash, :ref:`lista <python_list>` de claves o un arreglo asociativo.

- Una lista ordenada de valores. En la mayoría de los lenguajes, esto se implementa como arreglos,
  vectores, :ref:`listas <python_list>` o sequencias.

Estas son estructuras universales; virtualmente todos los lenguajes de programación las soportan de una
forma u otra. Es razonable que un formato de intercambio de datos que es independiente del lenguaje de
programación se base en estas estructuras.

En JSON, se presentan de estas formas:

#. Un ``objeto`` es un conjunto desordenado de pares nombre/valor. Un objeto comienza con ``{`` *llave de apertura*
   y *termine con llave de cierre* ``}``. Cada nombre es seguido por ``:`` *dos puntos* y los pares nombre/valor están
   separados por ``,`` *coma*.

#. Un ``arreglo`` es una colección de valores. Un arreglo comienza con ``[`` *corchete izquierdo* y termina con
   *corchete derecho* ``]``. Los valores se separan por ``,`` *coma*.

#. Un ``valor`` puede ser una :ref:`cadena de caracteres<python_str>` con comillas dobles, o un :ref:`número <python_int>`,
   o ``true`` o ``false`` o ``null``, o un objeto o un arreglo. Estas estructuras pueden anidarse.

#. Una ``cadena de caracteres`` es una colección de cero o más caracteres Unicode, encerrados entre comillas
   dobles, usando barras divisorias invertidas como escape. Un carácter está representado por una cadena
   de caracteres de un único carácter. Una ``cadena de carateres`` es parecida a una cadena de caracteres C
   o Java.

#. Un ``número`` es similar a un número C o Java, excepto que no se usan los formatos octales y hexadecimales.

#. Los ``espacios`` en blanco pueden insertarse entre cualquier par de símbolos. Exceptuando pequeños detalles
   de encoding, esto describe completamente el lenguaje.


Veamos su estructura básica con un ejemplo que representa un ficha basica de un cliente. A continuación
se muestra un ejemplo de un archivo **JSON**:

.. code-block:: json
    :linenos:
    :caption: Ejemplo de archivo JSON

    {
        "nombre": "Leonardo",
        "apellido": "Caballero",
        "codigo_postal": "5001",
        "telefono": "+58-412-4734567"
    }


Estas son las características principales del `formato JSON`_:

- Posee una secuencia de pares clave-valor rodeados por un par de llaves ``{}``.

- Cada clave se asocia a un valor con este formato:

  .. code-block:: console
      :class: no-copy

      "clave": <valor>

  .. tip:: Los valores que incluyen comillas simples deben estar rodeados por comillas dobles.

  Los pares clave-valor deben estar separados por una coma. Solo el último par no debe estar seguido de
  una coma.

  .. code-block:: console
      :class: no-copy

      {
          "nombre": "Manuel",
          "apellido": "Matos",
          "codigo_postal": "4001", # ¡Coma!
          "telefono": "+58-414-2360943"
      }

  .. warning:: Los comentarios no están permitidos en JSON.

  .. tip::
    Generalmente estructuramos los archivos JSON con distintos niveles de indentación para que la
    información sea más fácil de leer. De forma automática con Python puedes controlar la indentación
    a usar.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. _`Standard ECMA-262 3rd Edition - Diciembre 1999`: https://ecma-international.org/wp-content/uploads/ECMA-262_3rd_edition_december_1999.pdf
.. _`JavaScript`: https://es.wikipedia.org/wiki/JavaScript
.. _`formato JSON`: https://es.wikipedia.org/wiki/JSON
.. _`API REST`: https://es.wikipedia.org/wiki/Transferencia_de_Estado_Representacional
