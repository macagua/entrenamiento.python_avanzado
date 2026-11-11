.. _python_test_pytest:

PyTest
======

En este articulo se explicará como utilizar el módulo ``PyTest``.

`PyTest`_, es el framework de pruebas más popular de Python. Permite escribir funciones de test pequeñas
y legibles usando sentencias assert simples — sin necesidad de clases repetitivas — y a la vez escala
hacia suites complejas con fixtures compartidos, parametrización y plugins.

Este capítulo cubre todo lo que necesitas para probar código Python con ``PyTest``: instalación, tu primer
test, assertions y excepciones esperadas, fixtures, parametrize, organización de tests con :file:`conftest.py`,
opciones útiles de línea de comandos y los errores más comunes.


----


.. _python_test_pytest_por_que:

¿Por qué PyTest?
----------------

Python incluye el módulo :ref:`unittest <python_test_unit_test>`, entonces ¿por qué usar ``PyTest`` en su lugar?

+-----------------------------+-------------------------+-----------------------------------------------+
|  Característica             |          unittest       |                   pytest                      |
+-----------------------------+-------------------------+-----------------------------------------------+
|  Sintaxis de test           |     Clase + método      |  Función simple                               |
+-----------------------------+-------------------------+-----------------------------------------------+
|  Assertions                 |  self.assertEqual(a, b) |  assert a == b                                |
+-----------------------------+-------------------------+-----------------------------------------------+
|  Fixtures                   |    setUp / tearDown     |  @pytest.fixture (componible)                 |
+-----------------------------+-------------------------+-----------------------------------------------+
|  Parametrizar               |	     Bucle manual       |  @pytest.mark.parametrize                     |
+-----------------------------+-------------------------+-----------------------------------------------+
|  Ecosistema de plugins      |          Mínimo         |  Más de 1 000 plugins (coverage, mock, etc.)  |
+-----------------------------+-------------------------+-----------------------------------------------+

``PyTest`` también ejecuta tests estilo :ref:`unittest <python_test_unit_test>` sin cambios, por lo que
puedes adoptarlo de forma gradual.


----


.. _python_test_pytest_instalar:

Instalación
-----------

El módulo ``PyTest`` puede instalarse utilizando el administrador de paquetes de Python :ref:`pip <python_pip>`,
ejecutando el siguiente comando:

.. code-block:: console

    pip install pytest

Una vez instalado, puede probar la instalación existe, ejecutando el siguiente comando:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

          python3 -c "import pytest ; print(pytest.__version__)"

   .. group-tab:: Windows

      .. code-block:: console

          python3 -c "import pytest ; print(pytest.__version__)"

Si muestra el numero de la versión del módulo ``pytest``, tiene correctamente instalado el módulo.
Con esto, ya tiene todo listo para continuar.


----


.. _python_test_pytest_assertions:

Assertions
----------

.. todo::
    TODO Terminar de escribir esta sección.


----


.. _python_test_pytest_fixtures:

Fixtures
--------

.. todo::
    TODO Terminar de escribir esta sección.


----


.. _python_test_pytest_scaffolding:

Práctica - Caso real
--------------------

A continuación, se presenta la estructura de proyecto llamado ``unitarias_pytest`` de
una práctica más real de implementar el uso de proyectos con ``PyTest``:


Estructura de archivos
^^^^^^^^^^^^^^^^^^^^^^

Para crear la estructura de archivos del proyecto ``pytest`` debe ejecutar los siguientes comandos:

.. tabs::

   .. group-tab:: Linux

      Crear y acceder al directorio ``unitarias_pytest`` en un solo comando, ejecutando el siguiente comando:

      .. code-block:: console

          mkdir -p ~/proyectos/pruebas/unitarias_pytest && cd $_

      El comando anterior crea la siguiente estructura de directorios:

      .. code-block:: console
          :class: no-copy

          proyectos/
          └── pruebas/
              └── unitarias_pytest/

      Si tiene la estructura de archivo previa, entonces puede continuar con la siguiente sección.

   .. group-tab:: Windows

      Debe crear el directorio ``unitarias_pytest``, ejecutando el siguiente comando:

      .. code-block:: console

          md .\proyectos\pruebas\unitarias_pytest

      Debe acceder al directorio , ejecutando el siguiente comando:

      .. code-block:: console

          cd .\proyectos\pruebas\unitarias_pytest

      El comando anterior crea la siguiente estructura de directorios:

      .. code-block:: console
          :class: no-copy

          proyectos/
          └── pruebas/
              └── unitarias_pytest/

      Si tiene la estructura de archivo previa, entonces puede continuar con la siguiente sección.

A continuación, se presenta y explica el uso de cada archivo para este proyecto:

*Archivo* :file:`operations.py`

Módulo de funciones operativas del programa.

.. literalinclude:: ../../recursos/leccion9/unit_test_pytest/operations.py
    :language: python
    :linenos:
    :lines: 1-8

*Archivo* :file:`tests/test_operations.py`

Módulo de pruebas unitarias funciones operativas del programa.

.. literalinclude:: ../../recursos/leccion9/unit_test_pytest/tests/test_operations.py
    :language: python
    :linenos:
    :lines: 1-13

*Archivo* :file:`pytest.ini`

Archivo de configuración global para ``PyTest``.

Se coloca normalmente en la raíz del proyecto y permite definir opciones que afectan a
todas las ejecuciones de ``PyTest``.

**Usos principales:**

- Configurar opciones por defecto (sin tener que pasarlas por línea de comandos).

- Definir markers personalizados para clasificar tests.

- Ignorar directorios o archivos durante la búsqueda de tests.

- Cambiar el patrón de descubrimiento de tests (por ejemplo, nombres de archivos o funciones).

- Configurar plugins.

.. literalinclude:: ../../recursos/leccion9/unit_test_pytest/pytest.ini
    :language: ini
    :linenos:
    :lines: 1-11

*Archivo* :file:`conftest.py`

Es un archivo especial para compartir ``fixtures`` y ``hooks`` entre múltiples archivos de
test sin necesidad de importarlos explícitamente. ``PyTest`` lo detecta automáticamente si
está en el mismo directorio o en un directorio padre.

**Usos principales:**

- Definir fixtures reutilizables para todo el paquete o subpaquete.

- Implementar hooks de pytest (por ejemplo, modificar el comportamiento antes/después de ejecutar tests).

- Configurar datos comunes para varios tests.


.. literalinclude:: ../../recursos/leccion9/unit_test_pytest/conftest.py
    :language: python
    :linenos:
    :lines: 1-27


----


Para ejecutar el código del proyecto llamado ``unitarias_pytest`` abra una consola de comando, cree la
siguiente estructura de directorio y acceda al mismo donde se encuentra el programa:

.. code-block:: console
    :class: no-copy

    proyectos/
    └── pruebas/
        └── unitarias_pytest/
            ├── __init__.py
            ├── conftest.py
            ├── operations.py
            ├── pytest.ini
            └── tests/
                ├── __init__.py
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
        Para ejecutar las pruebas unitarias con ``pytest``, abra una consola de comando, acceda
        al directorio donde se encuentra la estructura previa y ejecute el siguiente comando:

      .. code-block:: console

          pytest

      El anterior código al ejecutar debe mostrar el siguiente mensaje:

      .. code-block:: console
          :class: no-copy

          ============================= test session starts ==============================
          platform linux -- Python 3.11.x, pytest-7.x.x, pluggy-1.x.x -- /usr/bin/python3
          cachedir: .pytest_cache
          rootdir: .../unitarias_pytest
          configfile: pytest.ini
          testpaths: tests
          collected 2 items
          collecting ... collected 2 items

          tests/test_operations.py::test_total_sum_positive PASSED                 [ 50%]
          tests/test_operations.py::test_total_sum_negative PASSED                 [100%]

          ============================== 2 passed in 0.02s ===============================

      Si la ejecución anterior muestra el mensaje anterior, quiere decir que la prueba unitaria fue exitosa.

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
        Para ejecutar las pruebas unitarias con ``pytest``, abra una consola de comando, acceda
        al directorio donde se encuentra la estructura previa y ejecute el siguiente comando:

      .. code-block:: console

          pytest

      El anterior código al ejecutar debe mostrar el siguiente mensaje:

      .. code-block:: console
          :class: no-copy

          ============================= test session starts ==============================
          platform linux -- Python 3.11.2, pytest-9.2.0, pluggy-1.7.0 -- python3
          cachedir: .pytest_cache
          rootdir: .../unitarias_pytest
          configfile: pytest.ini
          testpaths: tests
          collected 2 items

          tests/test_operations.py::test_total_sum_positive PASSED                 [ 50%]
          tests/test_operations.py::test_total_sum_negative PASSED                 [100%]

          ============================== 2 passed in 0.02s ===============================

      Si la ejecución anterior muestra el mensaje anterior, quiere decir que la prueba unitaria fue exitosa.


Así de esta forma puede replicar una práctica real de un proyecto para realizar pruebas unitareas
usando ``pytest`` para el módulo :file:`operations.py`, aplicando buenas prácticas de código funcional.


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en los
    siguientes enlaces:

    - :download:`operations.py <../../recursos/leccion9/unit_test_pytest/operations.py>`.

    - :download:`test_operations.py <../../recursos/leccion9/unit_test_pytest/tests/test_operations.py>`.

    - :download:`pytest.ini <../../recursos/leccion9/unit_test_pytest/pytest.ini>`.

    - :download:`conftest.py <../../recursos/leccion9/unit_test_pytest/conftest.py>`.


Las pruebas unitarias son una parte esencial del desarrollo de software. Implementarlas de manera adecuada
ayuda a garantizar la calidad, estabilidad y mantenibilidad del código. Con herramientas como ``pytest``
en Python, los desarrolladores pueden escribir pruebas de manera sencilla y efectiva.


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion9>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html


..
  .. disqus::

.. _`PyTest`: https://pytest.org/
