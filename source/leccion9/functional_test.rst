.. _python_test_functional_test:

Pruebas funcionales
===================

Son un tipo de prueba de software que se enfoca en verificar que el sistema cumpla con los requisitos funcionales
especificados. Estas pruebas se centran en validar que las funciones y características del software se comporten
de acuerdo con las expectativas del usuario, sin tener en cuenta la estructura interna del código fuente.

Mientras se ejecutan las pruebas funcionales, se simulan escenarios de uso real para asegurarse de que el software
realice correctamente las tareas para las cuales fue diseñado. Son esenciales para garantizar que la aplicación
cumpla con los requisitos de negocio y brinde una experiencia de usuario satisfactoria.


.. tip::
    Un ejemplo de *prueba funcional*, es una aplicación web simula la ejecución de una navegador web el cual abre
    la dirección URL e interactual con la misma.


Importancia
-----------

Estas pruebas garantizan que el software cumple con su propósito, brindando una experiencia de usuario óptima y
minimizando errores en producción.


Tipos
-----

- `Pruebas de Caja Negra`_: Evalúan el sistema sin conocer su estructura interna.

- `Pruebas de Regresión`_: Aseguran que las modificaciones no afecten funcionalidades previas.

- `Pruebas de Aceptación`_: Verifican si el software cumple con los criterios establecidos por el cliente.

- `Pruebas de Sistema`_: Evaluación integral del software en su entorno real.


----


.. _python_test_functional_test_instalar:

Instalación
-----------

Al realizar pruebas funcionales pueden ser manuales o automatizadas necesita el módulo `selenium`_. Esto significa que
debe instalar ``selenium`` ejecutando los siguientes comandos correspondiente a cada sistema operativo, los cuales se
presentan a continuación:

.. tabs::

   .. group-tab:: Linux

      Para realizar pruebas funcionales en una aplicación con ``selenium`` requiere
      instalar las siguientes librerías/módulos:

      #. :ref:`Entorno de desarrollo <python_entorno_desarrollo>`.

      #. :ref:`Python package installer - pip <python_entorno_desarrollo_pip>`.

      #. :ref:`Entorno virtual Python <python_entorno_desarrollo_venv>`.

      #. Instalar el módulo ``selenium``, ejecutando el siguiente comando:

         .. code-block:: console

             pip3 install selenium

   .. group-tab:: Windows

      #. :ref:`Entorno virtual Python <python_entorno_desarrollo_venv>`.

      #. Instalar el módulo ``selenium``, ejecutando el siguiente comando:

         .. code-block:: console

             pip3 install selenium

Puede probar si la instalación se realizo correctamente, ejecutando
el siguiente comando correspondiente a tu sistema operativo:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

          python3 -c "import selenium ; print(selenium.__version__)"

   .. group-tab:: Windows

      .. code-block:: console

          python3 -c "import selenium ; print(selenium.__version__)"

Si muestra el número de la versión instalada de ``selenium``, tiene correctamente instalado
el módulo. Con esto, ya tiene todo listo para continuar.


----


.. _python_test_functional_test_scaffolding:

Práctica - Caso real
--------------------

A continuación se presenta una práctica más real de implementar el uso de proyectos
con ``selenium``, a continuación la estructura de proyecto llamado ``functionales``:


Estructura de archivos
^^^^^^^^^^^^^^^^^^^^^^

Para crear la estructura de archivos del proyecto ``selenium`` debe ejecutar los siguientes comandos:

.. tabs::

   .. group-tab:: Linux

      Crear y acceder al directorio ``functionales`` en un solo comando, ejecutando el siguiente comando:

      .. code-block:: console

          mkdir -p ~/proyectos/pruebas/functionales && cd $_

      El comando anterior crea la siguiente estructura de directorios:

      .. code-block:: console
          :class: no-copy

          proyectos/
          └── pruebas/
              └── functionales/

      Si tiene la estructura de archivo previa, entonces puede continuar con la siguiente sección.

   .. group-tab:: Windows

      Debe crear el directorio ``functionales``, ejecutando el siguiente comando:

      .. code-block:: console

          md .\proyectos\pruebas\functionales

      Debe acceder al directorio , ejecutando el siguiente comando:

      .. code-block:: console

          cd .\proyectos\pruebas\functionales

      El comando anterior crea la siguiente estructura de directorios:

      .. code-block:: console
          :class: no-copy

          proyectos/
          └── pruebas/
              └── functionales/

      Si tiene la estructura de archivo previa, entonces puede continuar con la siguiente sección.

A continuación se presenta y explica el uso de cada archivo para este proyecto:

*Archivo* :file:`functtest_navigate_url.py`

Módulo de prueba funcional para buscar el elemento HTML ``title`` y verificar el valor del título
de la página.

.. literalinclude:: ../../recursos/leccion9/functional_test/test_navigate_url.py
    :language: python
    :linenos:
    :lines: 1-18

*Archivo* :file:`test_find_element.py`

Módulo de prueba funcional para buscar el nombre del paquete en la página con expresión ``xpath``
y verificando el valor del elemento.

.. literalinclude:: ../../recursos/leccion9/functional_test/test_find_element.py
    :language: python
    :linenos:
    :lines: 1-24


----


Para ejecutar el código del proyecto llamado ``functionales`` abra una consola de comando, cree la
siguiente estructura de directorio y acceda al mismo donde se encuentra el programa:

.. code-block:: console
    :class: no-copy

    proyectos/
    └── pruebas/
        └── functionales/
            ├── __init__.py
            ├── test_navigate_url.py
            └── test_find_element.py


Si tiene la estructura de archivo previa, entonces puede continuar los procesos de ejecución del
código fuente.


----


Teniendo creada la anterior estructura de proyecto, vuelva a ejecutar ahora el módulo con
el siguiente comando, el cual a continuación se presentan el correspondiente comando de tu
sistema operativo:

.. tabs::

   .. group-tab:: Linux

      .. tip::
        Para ejecutar el código fuente de esta práctica debe invocar al módulo :file:`test_navigate_url.py`,
        abra una consola de comando, acceda al directorio donde se encuentra la estructura previa
        y ejecute el siguiente comando:

      .. code-block:: console

          python3 test_navigate_url.py

      El anterior código al ejecutar debe mostrar el siguiente mensaje:

      .. code-block:: console
          :class: no-copy

          ✅ Successed Test: selenium · PyPI page launched successfully

      Este es el funcionamiento normal del módulo :file:`test_navigate_url.py`. Por defecto siempre devolvera
      el valor ``Python 3.11+``.

      .. tip::
        Para ejecutar el código fuente de esta práctica debe invocar al módulo :file:`test_find_element.py`,
        abra una consola de comando, acceda al directorio donde se encuentra la estructura previa
        y ejecute el siguiente comando:

      .. code-block:: console

          python3 test_find_element.py

      El anterior código al ejecutar debe mostrar el siguiente mensaje:

      .. code-block:: console
          :class: no-copy

          ✅ Successed Test: selenium 4.29.0 version found

      Si la ejecución anterior muestra el mensaje anterior, quiere decir que la prueba unitaria fue exitosa.

   .. group-tab:: Windows

      .. tip::
        Para ejecutar el código fuente de esta práctica debe invocar al módulo :file:`test_navigate_url.py`,
        abra una consola de comando, acceda al directorio donde se encuentra la estructura previa
        y ejecute el siguiente comando:

      .. code-block:: console

          python3 test_navigate_url.py

      El anterior código al ejecutar debe mostrar el siguiente mensaje:

      .. code-block:: console
          :class: no-copy

          ✅ Successed Test: selenium · PyPI page launched successfully

      Este es el funcionamiento normal del módulo :file:`test_navigate_url.py`. Por defecto siempre devolvera
      el valor ``Python 3.11+``.

      .. tip::
        Para ejecutar el código fuente de esta práctica debe invocar al módulo :file:`test_find_element.py`,
        abra una consola de comando, acceda al directorio donde se encuentra la estructura previa
        y ejecute el siguiente comando:

      .. code-block:: console

          python3 test_find_element.py

      El anterior código al ejecutar debe mostrar el siguiente mensaje:

      .. code-block:: console
          :class: no-copy

          ✅ Successed Test: selenium 4.29.0 version found

      Si la ejecución anterior muestra el mensaje anterior, quiere decir que la prueba unitaria fue exitosa.


Así de esta forma puede replicar una práctica real de un proyecto para realizar *pruebas funcionales*
usando ``selenium`` para la pagina web: https://pypi.org/project/selenium/4.29.0/


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en los
    siguientes enlaces:

    - :download:`test_navigate_url.py <../../recursos/leccion9/functional_test/test_navigate_url.py>`.

    - :download:`test_find_element.py <../../recursos/leccion9/functional_test/test_find_element.py>`.


Las pruebas funcionales son fundamentales para garantizar que una aplicación funcione correctamente desde
la perspectiva del usuario. Implementarlas adecuadamente ayuda a mejorar la calidad del software y evitar
fallos en producción.


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion9>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html


..
  .. disqus::

.. _`selenium`: https://pypi.org/project/selenium/
.. _`Pruebas de Caja Negra`: https://es.wikipedia.org/wiki/Caja_negra_(sistemas)
.. _`Pruebas de Regresión`: https://es.wikipedia.org/wiki/Pruebas_de_regresi%C3%B3n
.. _`Pruebas de Aceptación`: https://es.wikipedia.org/wiki/Pruebas_de_aceptaci%C3%B3n_(inform%C3%A1tica)
.. _`Pruebas de Sistema`: https://www.zaptest.com/es/que-es-la-comprobacion-de-sistemas-una-inmersion-en-profundidad-en-enfoques-tipos-herramientas-consejos-y-trucos-y-mucho-mas
