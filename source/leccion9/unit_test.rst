.. _python_test_unit_test:

Pruebas unitarias
=================

Son una técnica de depuración que se enfoca en validar el funcionamiento de unidades individuales de código, como
funciones o métodos, de forma aislada. Su objetivo es asegurarse de que cada componente del software cumpla con su
propósito específico, sin depender de otros módulos.

Al automatizar estas pruebas, los desarrolladores pueden detectar errores de manera temprana, mejorando la calidad del
código y reduciendo los costos de corrección en etapas posteriores del desarrollo. Las pruebas unitarias son esenciales
en el desarrollo ágil, ya que permiten realizar cambios rápidos y seguros en el código, garantizando que las modificaciones
no afecten negativamente el funcionamiento del sistema.

Estas pruebas verifican el funcionamiento de las unidades más pequeñas de un programa, normalmente funciones o métodos
individuales. El propósito es garantizar que cada unidad de código funcione correctamente de manera aislada antes de
integrarse en el sistema completo.


Importancia
-----------

Son fundamentales para mejorar la calidad del software. Detectan errores en una etapa temprana del desarrollo, reducen
costos de mantenimiento y proporcionan documentación sobre el comportamiento esperado del código. Además, permiten realizar
cambios en el código sin miedo a introducir nuevos errores.


Herramientas populares
----------------------

Existen varias herramientas populares para realizar pruebas unitarias:

+-------------+---------------+-----------------------------------------------------+------------------------+----------------------------------------------+
|  Nombre     | Licencia      | Forma parte de                                      | Categoría              | Categoría Especial                           |
+-------------+---------------+-----------------------------------------------------+------------------------+----------------------------------------------+
|             |               |                                                     |                        | Shell :ref:`IPython <python_modulo_ipython>` |
| `doctest`_  | Licencia MIT  | :ref:`librería estándar <python_libreria_estandar>` | Pruebas unitarias      | para el símbolo del sistema y la aplicación  |
|             |               | de Python.                                          |                        | inclusiva.                                   |
+-------------+---------------+-----------------------------------------------------+------------------------+----------------------------------------------+
| `unittest`_ | Licencia MIT  | :ref:`librería estándar <python_libreria_estandar>` | Pruebas unitarias      | Coleccción rápida de pruebas y ejecución     |
|             |               | de Python.                                          |                        | flexible de las mismas.                      |
+-------------+---------------+-----------------------------------------------------+------------------------+----------------------------------------------+
| `PyTest`_   | Licencia MIT  | Autónomo, permite suites de prueba compactas.       | Pruebas unitarias      | Clase especial y sencilla para facilitar las |
|             |               |                                                     |                        | pruebas.                                     |
+-------------+---------------+-----------------------------------------------------+------------------------+----------------------------------------------+
| `Robot`_    | Licencia ASF  | Librerías de pruebas genéricas de Python.           | Pruebas de aceptación  | Enfoque de pruebas basado en palabras clave. |
+-------------+---------------+-----------------------------------------------------+------------------------+----------------------------------------------+
| `Nose2`_    | Licencia BSD  | Lleva las características de ``unittest`` con       | Extensión de           | Un gran número de plugins.                   |
|             |               | características adicionales y plugins.              | ``unittest``           |                                              |
+-------------+---------------+-----------------------------------------------------+------------------------+----------------------------------------------+
| `Testify`_  | Licencia ASF  | Lleva las características de ``unittest`` y         | Extensión de           | Mejora del descubrimiento de pruebas.        |
|             |               | ``nose2`` con características adicionales y plugins.| ``unittest``           |                                              |
+-------------+---------------+-----------------------------------------------------+------------------------+----------------------------------------------+

En este articulo se explicará como utilizar el módulo ``unittest``, que es la :ref:`librería estándar <python_libreria_estandar>` de Python para realizar
pruebas unitarias.


----


.. _python_test_unit_test_instalar:

Instalación
-----------

El módulo ``unittest`` esta incluida en :ref:`librería estándar de Python <python_libreria_estandar>`, puede probar la
instalación existe, ejecutando el siguiente comando:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

          python3 -c "import unittest ; print(unittest.__package__)"

   .. group-tab:: Windows

      .. code-block:: console

          python3 -c "import unittest ; print(unittest.__package__)"

Si muestra el nombre del módulo ``unittest``, tiene correctamente instalado el módulo.
Con esto, ya tiene todo listo para continuar.


----


.. _python_test_unit_test_scaffolding:

Práctica - Caso real
--------------------

A continuación se presenta una práctica más real de implementar el uso de proyectos
con ``unittest``, a continuación la estructura de proyecto llamado ``unitarias``:


Estructura de archivos
^^^^^^^^^^^^^^^^^^^^^^

Para crear la estructura de archivos del proyecto ``unittest`` debe ejecutar los siguientes comandos:

.. tabs::

   .. group-tab:: Linux

      Crear y acceder al directorio ``unitarias`` en un solo comando, ejecutando el siguiente comando:

      .. code-block:: console

          mkdir -p ~/proyectos/pruebas/unitarias && cd $_

      El comando anterior crea la siguiente estructura de directorios:

      .. code-block:: console
          :class: no-copy

          proyectos/
          └── pruebas/
              └── unitarias/

      Si tiene la estructura de archivo previa, entonces puede continuar con la siguiente sección.

   .. group-tab:: Windows

      Debe crear el directorio ``unitarias``, ejecutando el siguiente comando:

      .. code-block:: console

          md .\proyectos\pruebas\unitarias

      Debe acceder al directorio , ejecutando el siguiente comando:

      .. code-block:: console

          cd .\proyectos\pruebas\unitarias

      El comando anterior crea la siguiente estructura de directorios:

      .. code-block:: console
          :class: no-copy

          proyectos/
          └── pruebas/
              └── unitarias/

      Si tiene la estructura de archivo previa, entonces puede continuar con la siguiente sección.

A continuación se presenta y explica el uso de cada archivo para este proyecto:

*Archivo* :file:`operations.py`

Módulo de funciones operativas del programa.

.. literalinclude:: ../../recursos/leccion9/unit_test/operations.py
    :language: python
    :linenos:
    :lines: 1-8

*Archivo* :file:`test_operations.py`

Módulo de pruebas unitarias funciones operativas del programa.

.. literalinclude:: ../../recursos/leccion9/unit_test/test_operations.py
    :language: python
    :linenos:
    :lines: 1-20


----


Para ejecutar el código del proyecto llamado ``unitarias`` abra una consola de comando, cree la
siguiente estructura de directorio y acceda al mismo donde se encuentra el programa:

.. code-block:: console
    :class: no-copy

    proyectos/
    └── pruebas/
        └── unitarias/
            ├── __init__.py
            ├── operations.py
            └── test_operations.py


Si tiene la estructura de archivo previa, entonces puede continuar los procesos de ejecución del
código fuente.


----


Teniendo creada la anterior estructura de proyecto, vuelva a ejecutar ahora el módulo con
el siguiente comando, el cual a continuación se presentan el correspondiente comando de tu
sistema operativo:

.. tabs::

   .. group-tab:: Linux

      .. tip::
        Para ejecutar el código fuente de esta práctica debe invocar al módulo :file:`operations.py`,
        abra una consola de comando, acceda al directorio donde se encuentra la estructura previa
        y ejecute el siguiente comando:

      .. code-block:: console

          python3 operations.py

      El anterior código al ejecutar debe mostrar el siguiente mensaje:

      .. code-block:: console
          :class: no-copy

          📜 The total sum is: 3

      Este es el funcionamiento normal del módulo :file:`operations.py`. Por defecto siempre devolvera
      el valor ``3``.

      Este código crea una prueba unitaria para la función ``total_sum``, evalúa que el valor ``3``
      sea el resultado esperado.


      .. tip::
        Para ejecutar el código fuente de esta práctica debe invocar al módulo :file:`test_operations.py`,
        abra una consola de comando, acceda al directorio donde se encuentra la estructura previa
        y ejecute el siguiente comando:

      .. code-block:: console

          python3 test_operations.py

      El anterior código al ejecutar debe mostrar el siguiente mensaje:

      .. code-block:: console
          :class: no-copy

          📜 The total sum is: 3
          ..
          ----------------------------------------------------------------------
          Ran 2 tests in 0.000s

          OK

      Si la ejecucion anterior muestra el mensaje anterior, quiere decir que la prueba unitaria fue exitosa.

   .. group-tab:: Windows

      .. tip::
        Para ejecutar el código fuente de esta práctica debe invocar al módulo :file:`operations.py`,
        abra una consola de comando, acceda al directorio donde se encuentra la estructura previa
        y ejecute el siguiente comando:

      .. code-block:: console

          python3 operations.py

      El anterior código al ejecutar debe mostrar el siguiente mensaje:

      .. code-block:: console
          :class: no-copy

          📜 The total sum is: 3

      Este es el funcionamiento normal del módulo :file:`operations.py`. Por defecto siempre devolvera
      el valor ``3``.

      Este código crea una prueba unitaria para la función ``total_sum``, evalúa que el valor ``3``
      sea el resultado esperado.


      .. tip::
        Para ejecutar el código fuente de esta práctica debe invocar al módulo :file:`test_operations.py`,
        abra una consola de comando, acceda al directorio donde se encuentra la estructura previa
        y ejecute el siguiente comando:

      .. code-block:: console

          python3 test_operations.py

      El anterior código al ejecutar debe mostrar el siguiente mensaje:

      .. code-block:: console
          :class: no-copy

          📜 The total sum is: 3
          ..
          ----------------------------------------------------------------------
          Ran 2 tests in 0.000s

          OK

      Si la ejecucion anterior muestra el mensaje anterior, quiere decir que la prueba unitaria fue exitosa.


Así de esta forma puede replicar una práctica real de un proyecto para realizar pruebas unitareas
usando ``unittest`` para el módulo :file:`operations.py`, aplicando buenas prácticas de código funcional.


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en los
    siguientes enlaces:

    - :download:`operations.py <../../recursos/leccion9/unit_test/operations.py>`.

    - :download:`test_operations.py <../../recursos/leccion9/unit_test/test_operations.py>`.


Las pruebas unitarias son una parte esencial del desarrollo de software. Implementarlas de manera adecuada
ayuda a garantizar la calidad, estabilidad y mantenibilidad del código. Con herramientas como ``unittest``
en Python, los desarrolladores pueden escribir pruebas de manera sencilla y efectiva.


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion9>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html


..
  .. disqus::

.. _`doctest`: https://docs.python.org/es/3.11/library/doctest.html
.. _`unittest`: https://docs.python.org/es/3.11/library/unittest.html
.. _`Robot`: https://pypi.org/project/robotframework/
.. _`PyTest`: https://pypi.org/project/pytest/
.. _`Nose2`: https://pypi.org/project/nose2/
.. _`Testify`: https://pypi.org/project/testify/
