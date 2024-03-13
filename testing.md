# PRUEBAS

### PREGUNTAS EXAMEN

1. **¿Qué se entiende por término prueba?**<br>
El término "prueba" se refiere a procesos sistemáticos para evaluar un sistema o componente con el objetivo de detectar errores y verificar su funcionamiento correcto.
Las pruebas de software son investigaciones cuyo objetivo es proporcionar información objetiva e independeiente
sobre la calidad del producto.<br>


2. **¿Qué son validación y verificación?**

**VERIFCACIÓN:**
Proceso de evaluación de un sistema o componente para determinar
si un producto de una **determinada fase** de desarrollo satisface las condiciones
impuestas al inicio de la fase.*¿Estamos elaborando correctamente el producto?*
- **Propósito**: Asegurar que los productos internos seleccionados cumplen con su especificación de requerimientos. Los métodos
pueden ser: inspecciones, revisiones por pares, auditorias, recorridas, análisis, demostraciones, simulaciones..<br>

**VALIDACIÓN:** 
Proceso de evaluación de un sistema o componente **durante o al final** del proceso
de desarrollo para determinar cuando se satisfacen los requerimientos especificados.*¿Estamos
elaborando el producto correcto?*
- **Propósito**: Es demostrar que un producto o componente de un producto cumple
su uso previsto cuando es puesto en su ambiente previsto. Deben ser seleccionados los productos internos
que mejor indican cuanto de bien el producto y los productos internos deben satisfacer las
necesidades del usuario.<br>

3. **¿Por qué se realizan las pruebas?**
- Evitar pérdidas económicas
- Evitar incumplir plazos y presupuestos
- Evitar mala calidad del producto
- Evitar insatisfacción a los interesados
- Evitar perder confianza del cliente

4. **¿Recuerdas algún principio de los mencionados?**

- **Pruebas muestran la presencia de defectoss**: Significa que las pruebas demuestran que EXISTEN problemas, pero no
que los problemas NO EXISTEN. El objetivo es detectar defectos.
- **Las pruebas exhaustivas son imposibles**: Las ruebas exhaustivas tratan de cubrir todas las combinaciones
posibles de datos en el software, para garantizar que ninguna situación puede surgir. En aplicaciones muy simples
sí es posible.
- **Pruebas tempranas**: Un producto se puede probar tan pronto como se haya creado. Es lo recomendable. Al final son más difíciles de resolver.
- **Agrupamiento de defectos**: Estudios dicen que los problemas tienden a agruparse en torno a un conjunto limitado
de módulos o áreas. Una vez que hayan sido identificadas, se puede enfocar las pruebas en esas zonas sensibles, mientras
se sigue buscando errores en los módulos restantes.
- **Paradoja del Pesticida**: Si las pruebas se repiten una y otra vez, ya no se encuentran nuevos errores. Si los programadores
responden a las pruebas reduciendo o eliminando los errores, se deduce que como el software mejora, la eficacia de las pruebas anteriores se
daña, se desgastan las pruebas y hay que crear y aprender y usar nuevas. Estas deben ser escritas.

5. **¿Qué son los casos de prueba?**<br>
Estos casos se utilizan para probar diferentes escenarios y asegurarse de que el software funcione correctamente en diversas situaciones.
Se recomienda **mínimo 2** casos de prueba para cada requisito del sistema.

### PUNTOS IMPORTANTES
- Las pruebas nos demuestran la presencia de errores en un programa. No pueden demostrar que no existen más defectos.
- Se diseñan pruebas según el sistema a desarrollar.
- Todo el proceso de pruebas puede ser demasiado extenso para un grupo pequeño, por eso se ajustan las pruebas o se contratan terceras empresas.
- La automatización de las pruebas puede reducir el tiempo, pero puede elevar el coste

### DEFINICIONES
**Pruebas**: Es una actividad realizada para evaluar la calidad del producto y mejorarla
identificando defectos y problemas. <br>
**Pruebas(IEEE)**: Es el proceso de operar un sistema o componente bajo condiciones
específicas, observar o registrar los resultados y realizar una evaluación 
de algún aspecto del sistema.<br>
**Pruebas de software**: Verificación dinámica del comportamiento de un programa
contra el comportamiento esperado, usando un conjunto finito de casos
de prueba, seleccionados de manera adecuada desde el dominio infinito
de ejecución(SWEBOK):
- Dinámica: Implica que para realizar las pruebas hay que ejecutar el programa
para los datos de entrada.
- Comportamiento esperado: Debe ser posible decidir cuando la salida observada
de la ejecución del programa es aceptable o no, de otra forma el esfuerzo
de la prueba es inútil.


## Causa del mal funcionamiento
- **Error**: Equivocación realizada por una persona(Ej.: escribir mal una instrucción de código)
- **Defecto o falta**: Error al realizar alguna actividad concerniente al software. Lo que debería hacer y lo que hace(Debido a un error
de programación, un botón en una app no hace lo que se supone que debería)
- **Falla**: Desvío respecto al comportamiento requerido del sistema.(Ej.: Si hago clic en un enlace de página web, la página no se carga como se espera)<br>
*La prueba puede revelar fallas, pero son las faltas las que pueden y deber ser removidas*

## INTRODUCCIÓN(definición)
Las pruebas de software son investigaciones cuyo objetivo es proporcionar información objetiva e independiente
sobre la calidad del producto.<br>
Es una actividad más en el proceso de control de calidad.<br>
Dependiendo del tipo, pueden ser implementas en cualquier momento del proceso.<br>

### ¿POR QUÉ REALIZAR PRUEBAS?
- Evitar pérdidas económicas
- Evitar incumplir plazos y presupuestos
- Evitar mala calidad del producto
- Evitar insatisfacciones a los interesados
- Evitar perder confianza del cliente

## OBJETIVOS
- Demostrar al desarrollador y cliente que el software satisface sus requerimientos
- Descubrir defectos en software, en el que comportamiento esté incorrecto,
no deseable o no cumple la especificación. (caídas del sistema, cálculos incorrectos y corrupción de datos "x" por ejemplo)
### CONCLUSIÓN OBJETIVOS
- Prueba es un proceso que intenta proporcionar confianza en software
- La salida de las pruebas, solo pueden predecirse por personas que comprenden
el funcionamiento del sistema
- Las pruebas deben basarse en un subconjunto de posibles casos de prueba

## PRINCIPIOS
- **Pruebas muestran a presencia de defectoss**: Significa que las pruebas demuestran que EXISTEN problemas, pero no
que los problemas NO EXISTEN. El objetivo es detectar defectos.
- **Las pruebas exhaustivas son imposibles**: Las pruebas exhaustivas tratan de cubrir todas las combinaciones
posibles de datos en el software, para garantir que ninguna situación puede surgir. En aplicaciones muy simples
sí es posible.
- **Pruebas tempranas**: Un producto se puede probar tan pronto como se haya creado. Es lo recomendable. Al final son más difíciles de resolver.
- **Agrupamiento de defectos**: Estudios dicen que los problemas tienden a agruparse en torno a un conjunto limitado
de módulos o áreas. Una vez que hayan sido identificadas, se puede enfocar las pruebas en etas zonas sensibles, mientras
se sigue buscando errores en los módulos restantes.
- **Paradoja del Pesticida**: Si las pruebas se repiten una y otra vez, ya no se encuentran nuevos errores. Si los programadores
responden a las pruebas reduciendo o eliminando los errores, se deduce que como el software mejora, la eficacia de las pruebas anteriores se
daña, se desgastan las pruebas y hay que crear y aprender y usar nuevas. Estas deben ser escritas.
## CONSIDERACIONES RESPECTO A LAS PRUEBA
- El problema principal es que no se puede probar completamente el sistema por lo que se diseñarán **casos de prueba**
- La actitud de la persona frente a la prueba es muy importante.
## CASOS DE PRUEBA
Son un conjunto de condiciones bajo las cuales un analista determinará si un app, software es parcial o completamente satisfactoria.
Se recomienda **mínimo 2** casos de prueba para cada requisito del sistema.
## ESTRUCTURA DE CASOS DE PRUEBA
1. **Introducción**: Contiene info general sobre los casos de prueba (identificador, creador, versión, nombre, propósito, etc.)
2. **Actividades**: Se describen y documentan las acciones a realizar en los casos de prueba (ambiente de prueba, inicialización, finalización...)
3. **Resultados**: Se describen y documentan los resultados de las pruebas realizadas sobre el sistema (salida esperada, salida obtenida, resultados, severidad, estado...)
## ACTITUD FRENTE A LA PRUEBA
- Prueba debe verse como forma de encontrar errores
- La persona que la hace no puede tener el propósito de verificar que el sistema
funciona correctamente, sino el de buscar fallas, teniendo por seguro que existen.

-------------------------------------------------

## PROCESO ESTÁNDAR
**HAY CINCO ETAPAS**:
1. **Planificación de pruebas**: Se definen el plan, estrategias... Qué recursos se usarán, cuanto tiempo va a tardar, esfuerzos queridos,
riesgos... Debe actualizarse este plan según se avanza el proyecto.
2. **Análisis y diseño de pruebas**: Se diseña cómo se va a probar el sistema, se determinan las pruebas a ejecutarse,
la metodología... *No se necesita un producto finalizado. Se generan aquí los casos de prueba.*
3. **Ejecución de pruebas:** Aquí se hace uso de todos los diseños generados anteriormente. Se registran las incidencias detectadas documentando
en un reporte. *Se necesita producto para realizar la ejecución*
4. **Reporte de pruebas**: Se analizan los resultados de la etapa anterior y de las incidencias
y su impacto en el proyecto. Se busca hacer análisis para corregir errores/fallas, etc.
5. **Cierre de pruebas**: Se toman las lecciones aprendidas de las fases anteriores. Se deja documentado los errores, incidencias que afectaron,
para ser más preventivo en el futuro.

## TIPOS DE PRUEBAS POR SU EJECUCIÓN
- **Pruebas manuales**: Las hace un tester como si fuese un usuario pero siguiendo unos pasos establecidos. Realiza las acciones
indicadas en cada paso del caso de prueba comprobando que se cumpla el resultado. Si es distinto al esperado, se reportan con todo detalle.
- **Pruebas automáticas**: Uso de software especial para controlar la ejecución de pruebas y comparar resultados obtenidos
y los esperados.
- **Pruebas específicas**: Se hacen de forma independiente y se hacen informes detallados de los resultados. Este equipo trabaja a partir de documentos
de requerimientos del sistema y del usuario para desarollar los planes de prueba del sistema

## TRATAMIENTO DE PRUEBAS
Normalmente se empieza con pruebas de componentes y luego las del sistema, aunque también se ha invertido esto, ya que implica
integrar componentes reutilizables ya adaptar el software.

## PRUEBAS DEL SISTEMA
- Implica integrar dos o más componentes que realicen funciones del sistema y luego se prueba esto.
- Es un proceso interactivo con el cliente, esta prueba buscan probar un incremento que se va enterar al cliente.
- Es un proceso en cascada, se ocupan de probar el sistema por completo.

# STUBS
Componentes de "mentira" que imitan comportamiento de componentes todavía no implementados.

##  PRUEBAS DE INTEGRACIÓN
Hay dos fases:
1. **PRUEBAS DE INTEGRACIÓN:** Aquí el tipo de pruebas tiene acceso al código fuente del sistema.
Se construye a partir de sus componentes y probar el sistema resultante para encontrar problemas surgidos a partir de estos. Se comprueba
que los componentes funcionan juntos correctamente.<br>
**Integración descendente**: Se desarrolla el esqueleto del sistema y se añaden los componentes. Desde programa
principal hasta abajo por jerarquía.<br>
**Integración descendente profunda**: Se hace por ramas. Cada una implementa una funcionalidad específica.
Hay componentes comerciales, reutilizables adaptados, nuevos.
**Integración ascendente**: Se integran primero los componentes de infraestructura que proporcionan servicios comunes como acceso a la BD y luego las funcionales.<br>
*Una buena opción es usar mezcla de ambas. Descendente para niveles superiores de la estructura y ascendente para los subordinados.*


## RESUMEN INTEGRACIÓN
- Hay que decidir al principio el orden de integración de los componentes
- Buena práctica e integrar primero los componentes que se usan con frecuencia
- Los componentes más usados reciben la mayoría de pruebas
- Integrar un nuevo componente puede cambiar el patrón de interacción de las demás
- **PRUEBAS DE REGRESIÓN**: es cuando se vuelve a ejecutar pruebas existentes de pruebas.

## **PRUEBAS DE ENTREGAS**: 
- Proceso de probar una entrega del sistema que distribuirá a los clientes.
- Objetivo es incrementar la confianza. Si se cumplen requisitos, se entrega al cliente. Esto se sabe si se muestra
que se ha entregado la funcionalidad especificada, el rendimiento OK, confiabilidad OK y no falla durante uso normal.

## TÉCNICA DE LA CAJA NEGRA
Estas pruebas permiten obtener un conjunto de condiciones de entrada que ejerciten completamente los requisitos funcionales de un programa. Se ignora
la estructura de control, concentrándose en la funcionalidad del sistema.<br>
Se centran en asegurarse de que todas las diferentes formas en que alguien podría usar el software estén probadas.
(Ejemplo biblioteca¿?)
## PRUEBAS GENERADAS:
- Probar el login usando logins correctos e incorrectos para ver que los que pueden pueden y los que no no.
- Probar respuestas correo electrónico

## PRUEBAS DE RENDIMIENTO
- Se diseñan para asegurar que el sistema pueda procesar su carga de forma esperada
- Se debe construir perfil operacional: conjunto de pruebas que reflejan la combinación real del trabajo que debería ser manejada 
por el sistema
## PRUEBAS DE COMPONENTES
- Comprueba los componentes individuales del sistema
- Hay tres tipos de componentes:
  - Funciones o individudales: Más simples. Se usan rutinas.
  - Clases de objetos con varios atributos y métodos
  - Componentes compuestos formados por diferentes objetos o funciones(tienen interfaz)
  
## PRUEBAS DE INTERFACES
- Objeto probar que la interfaz se comporta de acuerdo a la especificación
- Son importantes para desarrollados orientados a objetos
- Hay interfaces de parámetros, de memoria compartida, procedurales(un componente encapsula un conjunto
de procedimientos que pueden ser llamados por otros componentes), interfaces de paso de mensajes(un componente solicita un servicio a otro componente mediante paso de un mensaje)

## ERRORES DE INTERFACES
- Mal uso de la interfaz: Un componente llama a otro y va mal. Por parámetros mal pasados, número erróneos de parámetros.
- No compresión de interfaz: el componente que hace llamada no comprende la interfaz del componente al que llama y hace suposiciones
- Errores temporales: esto pasa los que comparten memoria o en la interfaz de paso de mensajes.

## PRUEBAS BASADAS EN REQUERIMIENTOS
Son pruebas de validación en lugar de por decto. El uso intenta demostrar que el sistema
se ha ejecutado bien haciendo un conjunto de pruebas.

## PRUEBAS DE PARTICIONES
Son conjuntos de datos en donde todos los miembros de los conjuntos deberían ser procesados de la misma forma.

## PRUEBAS ESTRUCTURALES
- Estas se derivan a partir del conocimiento a le estructura e implementación del software. Son de **CAJA BLANCA**.
- Su diseño está ligado al código fuente

## PRUEBAS DE CAMINOS
- Son una estrategia de pruebas estructurales cuyo objetivo es probar cada camino de ejecución de un problema.
- El número de caminos del programa es proporcional al tamaño del mismo
- Se usan sobre todo en pruebas de componentes
- Cada camino debe ejecutarse al menos una vez

## GLOSARIO
1. Gestor de prueba: gestiona la ejecución de las pruebas del programa, mantiene registros de los datos
2. Generador de datos: usa datos de la base de datos o genera patrones aleatorios para probar el sistema
3. Oráculo: Genera predicciones de resultados esperados
4. Comparador de ficheros: compara los resultados de pruebas al programa con resultados
anteriores
5. Generado de informes: Proporciona la definición de informes y calidades de generación 
para los resultados de las pruebas.
6. Analizados dinámico: Añade código de un programa para contar números de veces que se ha ejecutado
cada sentencia, para generar un informe.
7. Simulador: simulan donde se ejecuta el programa.