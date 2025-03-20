.. _python_test_integration_test:

Pruebas de integración
======================

Son fundamentales para asegurar que diferentes módulos o componentes de un sistema funcionen correctamente
cuando se combinan. A diferencia de las pruebas unitarias, que verifican el funcionamiento de componentes
individuales, las pruebas de integración se centran en la interacción entre esos componentes.

Estas ayudan a identificar problemas en las interfaces entre módulos y aseguran que el sistema completo
opere como se espera. Son esenciales en entornos de desarrollo ágiles y en aplicaciones grandes y complejas,
donde la integración de servicios, bases de datos y APIs externas debe funcionar sin problemas para garantizar
un rendimiento adecuado y una experiencia de usuario sin fallos.

Además verifican la interacción entre diferentes módulos o componentes de un software. Su objetivo es
garantizar que las unidades individuales de código trabajen correctamente cuando se combinan, previniendo
fallos en la comunicación entre ellas.


Importancia
-----------

Estas permiten identificar errores que pueden surgir cuando diferentes módulos trabajan juntos. Son
esenciales para garantizar la estabilidad del software y evitar problemas en etapas avanzadas del desarrollo.


Tipos
-----

- `Big Bang`_: Se prueban todos los módulos en conjunto después del desarrollo.

- `Top-Down`_: Se prueban los módulos superiores primero, integrando gradualmente los módulos inferiores.

- `Bottom-Up`_: Se prueban primero los módulos más básicos, integrando progresivamente los módulos superiores.

- `Sandwich`_: Combinación de los enfoques de pruebas ``Top-Down`` y de pruebas ``Bottom-Up``.


----


.. _python_test_integration_test_instalar:

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


.. _python_test_integration_test_scaffolding:

Práctica - Caso real
--------------------

A continuación se presenta una práctica más real de implementar el uso de proyectos
con ``unittest``, a continuación la estructura de proyecto llamado ``integracion``:


Estructura de archivos
^^^^^^^^^^^^^^^^^^^^^^

Para crear la estructura de archivos del proyecto ``unittest`` debe ejecutar los siguientes comandos:

.. tabs::

   .. group-tab:: Linux

      Crear y acceder al directorio ``integracion`` en un solo comando, ejecutando el siguiente comando:

      .. code-block:: console

          mkdir -p ~/proyectos/pruebas/integracion && cd $_

      El comando anterior crea la siguiente estructura de directorios:

      .. code-block:: console
          :class: no-copy

          proyectos/
          └── pruebas/
              └── integracion/

      Si tiene la estructura de archivo previa, entonces puede continuar con la siguiente sección.

   .. group-tab:: Windows

      Debe crear el directorio ``integracion``, ejecutando el siguiente comando:

      .. code-block:: console

          md .\proyectos\pruebas\integracion

      Debe acceder al directorio , ejecutando el siguiente comando:

      .. code-block:: console

          cd .\proyectos\pruebas\integracion

      El comando anterior crea la siguiente estructura de directorios:

      .. code-block:: console
          :class: no-copy

          proyectos/
          └── pruebas/
              └── integracion/

      Si tiene la estructura de archivo previa, entonces puede continuar con la siguiente sección.

A continuación se presenta y explica el uso de cada archivo para este proyecto:

*Archivo* :file:`instagram.py`

Módulo de funciones para el componente API de Instagram.

.. literalinclude:: ../../recursos/leccion9/integration_test/instagram.py
    :language: python
    :linenos:
    :lines: 1-10

*Archivo* :file:`whatsapp.py`

Módulo de funciones para el componente API de WhatsApp.

.. literalinclude:: ../../recursos/leccion9/integration_test/whatsapp.py
    :language: python
    :linenos:
    :lines: 1-10

*Archivo* :file:`installation.py`

Módulo de integración de componentes de redes sociales.

.. literalinclude:: ../../recursos/leccion9/integration_test/installation.py
    :language: python
    :linenos:
    :lines: 1-31

*Archivo* :file:`test_installation.py`

Módulo de pruebas unitarias para la integración de componentes de redes sociales.

.. literalinclude:: ../../recursos/leccion9/integration_test/test_installation.py
    :language: python
    :linenos:
    :lines: 1-26


----


Para ejecutar el código del proyecto llamado ``integracion`` abra una consola de comando, cree la
siguiente estructura de directorio y acceda al mismo donde se encuentra el programa:

.. code-block:: console
    :class: no-copy

    proyectos/
    └── pruebas/
        └── integracion/
            ├── __init__.py
            ├── instagram.py
            ├── installation.py
            ├── test_installation.py
            └── whatsapp.py


Si tiene la estructura de archivo previa, entonces puede continuar los procesos de ejecución del
código fuente.


----


Teniendo creada la anterior estructura de proyecto, vuelva a ejecutar ahora el módulo con
el siguiente comando, el cual a continuación se presentan el correspondiente comando de tu
sistema operativo:

.. tabs::

   .. group-tab:: Linux

      .. tip::
        Para ejecutar el código fuente de esta práctica debe invocar al módulo :file:`installation.py`,
        abra una consola de comando, acceda al directorio donde se encuentra la estructura previa
        y ejecute el siguiente comando:

      .. code-block:: console

          python3 installation.py

      El anterior código al ejecutar debe mostrar el siguiente mensaje:

      .. code-block:: console
          :class: no-copy

          📜 The Instagram message is: 'Hi, from Instagram API'.
          📜 The Whatapp message is: 'Hello, from WhatsApp API'.

      Este es el funcionamiento normal del módulo :file:`installation.py`. Por defecto, la *API de Instagram* siempre
      devolvera el valor ``Hi, from Instagram API`` y la *API de WhatsApp* siempre devolvera el valor
      ``Hello, from WhatsApp API``.

      Este código evalúa la integración entre la función ``sent_message()`` en el módulo :file:`installation.py`
      y la función ``greetings()`` en cada módulo como :file:`instagram.py` y :file:`whatsapp.py`, verificando que
      funcionen correctamente juntas.


      .. tip::
        Para ejecutar el código fuente de esta práctica debe invocar al módulo :file:`test_installation.py`,
        abra una consola de comando, acceda al directorio donde se encuentra la estructura previa
        y ejecute el siguiente comando:

      .. code-block:: console

          python3 test_installation.py

      El anterior código al ejecutar debe mostrar el siguiente mensaje:

      .. code-block:: console
          :class: no-copy

          ..
          ----------------------------------------------------------------------
          Ran 4 tests in 0.000s

          OK

      Si la ejecución anterior muestra el mensaje anterior, quiere decir que la prueba unitaria fue exitosa.

   .. group-tab:: Windows

      .. tip::
        Para ejecutar el código fuente de esta práctica debe invocar al módulo :file:`installation.py`,
        abra una consola de comando, acceda al directorio donde se encuentra la estructura previa
        y ejecute el siguiente comando:

      .. code-block:: console

          python3 installation.py

      El anterior código al ejecutar debe mostrar el siguiente mensaje:

      .. code-block:: console
          :class: no-copy

          📜 The Instagram message is: 'Hi, from Instagram API'.
          📜 The Whatapp message is: 'Hello, from WhatsApp API'.

      Este es el funcionamiento normal del módulo :file:`installation.py`. Por defecto, la *API de Instagram* siempre
      devolvera el valor ``Hi, from Instagram API`` y la *API de WhatsApp* siempre devolvera el valor
      ``Hello, from WhatsApp API``.

      Este código evalúa la integración entre la función ``sent_message()`` en el módulo :file:`installation.py`
      y la función ``greetings()`` en cada módulo como :file:`instagram.py` y :file:`whatsapp.py`, verificando que
      funcionen correctamente juntas.

      .. tip::
        Para ejecutar el código fuente de esta práctica debe invocar al módulo :file:`test_installation.py`,
        abra una consola de comando, acceda al directorio donde se encuentra la estructura previa
        y ejecute el siguiente comando:

      .. code-block:: console

          python3 test_installation.py

      El anterior código al ejecutar debe mostrar el siguiente mensaje:

      .. code-block:: console
          :class: no-copy

          ..
          ----------------------------------------------------------------------
          Ran 4 tests in 0.000s

          OK

      Si la ejecución anterior muestra el mensaje anterior, quiere decir que la prueba unitaria fue exitosa.


Así de esta forma puede replicar una práctica real de un proyecto para realizar *pruebas de integración*
usando ``unittest`` para el módulo :file:`installation.py`, aplicando buenas prácticas de código funcional.


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en los
    siguientes enlaces:

    - :download:`instagram.py <../../recursos/leccion9/integration_test/instagram.py>`.

    - :download:`installation.py <../../recursos/leccion9/integration_test/installation.py>`.

    - :download:`test_installation.py <../../recursos/leccion9/integration_test/test_installation.py>`.

    - :download:`whatsapp.py <../../recursos/leccion9/integration_test/whatsapp.py>`.


Las pruebas de integración son una parte crucial del desarrollo de software. Implementarlas correctamente ayuda
a garantizar que los módulos trabajen juntos sin problemas, reduciendo errores en la etapa de producción.


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion9>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html


..
  .. disqus::

.. _`Big Bang`: https://www.geeksforgeeks.org/big-bang-integration-testing/
.. _`Top-Down`: https://www.geeksforgeeks.org/steps-in-top-down-integration-testing/
.. _`Bottom-Up`: https://www.geeksforgeeks.org/steps-in-bottom-up-integration-testing/
.. _`Sandwich`: https://www.geeksforgeeks.org/sandwich-testing-software-testing/
