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



----

.. _python_modulo_json:

Módulo json
-----------

.. note::
    **Propósito:** usar el módulo que incorpora Python para codificar y decodificar **JavaScript Object
    Notation** (:ref:`JSON <python_json>`).

El módulo `json`_ expone una API familiar a los usuarios de los módulos de la biblioteca estándar `marshal`_
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
con el módulo ``json`` para leer y escribir un archivo JSON basado en un tipo :ref:`diccionario <python_dict>`:


Estructura de archivos
^^^^^^^^^^^^^^^^^^^^^^

Para crear la estructura de archivos del proyecto ``JSON`` debe ejecutar los siguientes comandos:

.. tabs::

   .. group-tab:: Linux

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

    La ejecucion anterior generar la siguiente estructura:

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

Así de esta forma puede leer y escribir registros en un archivo JSON usando el módulo ``json``.

----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion3>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

..
    .. disqus::

.. _`Standard ECMA-262 3rd Edition - Diciembre 1999`: https://ecma-international.org/wp-content/uploads/ECMA-262_3rd_edition_december_1999.pdf
.. _`JavaScript`: https://es.wikipedia.org/wiki/JavaScript
.. _`marshal`: https://docs.python.org/es/3.11/library/marshal.html#
.. _`json`: https://docs.python.org/es/3.11/library/json.html
.. _`formato JSON`: https://es.wikipedia.org/wiki/JSON
.. _`API REST`: https://es.wikipedia.org/wiki/Transferencia_de_Estado_Representacional
