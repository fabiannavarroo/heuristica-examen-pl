"""Normaliza los tests revisados y une su procedencia al banco existente.
El manifiesto explicita cada aparición, incluso duplicados y numeración reiniciada.
No requiere distribuir los PDF originales.
"""
import json,hashlib,html
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
# A:20, B:20+17, C:60, D:30. C se revisó completo en la primera lectura;
# el PDF ya no está en la carpeta local, por lo que se conserva su inventario leído.
FILES={
 'A':{'file':'wuolah-free-TEST-1 (1).pdf','count':20,'section':'principal'},
 'B':{'file':'wuolah-free-Test-1.pdf','count':37,'section':'principal y extras'},
 'C':{'file':'wuolah-free-TEST1.pdf','count':60,'section':'principal','reviewNote':'Inventario de la lectura completa inicial; el archivo no se encuentra en la carpeta local actual.','sha256Prefix':'be77b834793e71f7'},
 'D':{'file':'wuolah-free-tipotest1.pdf','count':30,'section':'principal','numberingNote':'Tras las primeras diez preguntas se reinicia la numeración. Se identifica cada pregunta por su orden global y su número impreso.'}}
A_PROMPTS='''Aplicando el modelo de ramificación y acotación en profundidad para resolver problemas de programación lineal entera
Un problema de transporte se caracteriza porque
Si no ha sido preciso añadir variables artificiales a una tarea de Programación Lineal para iniciar la aplicación del Simplex con una base igual a la matriz identidad
A la hora de resolver un problema de programación lineal con el uso del Simplex con n variables y m restricciones, con m<=n
En un problema de programación lineal
Un problema de programación lineal es no acotado si
Un problema de programación lineal puede describirse de varias formas
Las variables de holgura sirven para
Las soluciones óptimas del problema dual sirven para
Cualquier problema de programación lineal
Cada vez que se añade una variable artificial y una variable de holgura a una restricción de un problema de maximización es preciso
En programación lineal, la regla de entrada establece que
Una vez que se ha resuelto un problema de Programación Lineal, las variables de holgura deben interpretarse puesto que tienen un significado específico
El modelo de resolución gráfica de problemas de programación lineal
La programación lineal sirve para
Un problema de programación lineal consta de
Marca la frase correcta (primal y dual)
En programación lineal, la regla de salida establece que
Las variables de decisión de un problema de programación lineal
Un problema de programación lineal es infactible si'''.splitlines()
EXTRAS='''La programación lineal sirve para
En programación lineal, la regla de salida establece que
Se denomina región factible de un problema de programación lineal
A la hora de resolver un problema de programación lineal con el uso del Simplex con n variables y m restricciones, con m<=n
Aplicando el modelo de ramificación y acotación en profundidad para resolver problemas de programación lineal entera
Las variables artificiales sirven para
Marca la frase correcta: un problema de programación lineal tiene una región infinitamente grande de soluciones pero la solución óptima debe buscarse en un conjunto restringido finito
Una vez que se ha resuelto un problema de Programación Lineal, las variables de holgura deben interpretarse puesto que tienen un significado específico
Las soluciones óptimas del problema dual sirven para
Las variables de decisión de un problema de programación lineal
Si un problema de programación lineal tiene más restricciones que variables de decisión
Un problema de programación lineal es infactible si
Cada vez que se añade una variable artificial y una variable de holgura a una restricción de un problema de maximización es preciso
La programación entera se divide en las clases
Un problema de transporte se caracteriza porque
La ramificación en el algoritmo de Ramificación y Acotación consiste en dividir la región factible actual en otras dos
¿Cuál de las siguientes restricciones es lineal?'''.splitlines()
C_PROMPTS='''¿Qué característica define a un problema de programación lineal en forma canónica?
Para resolver un problema de programación lineal gráficamente, ¿qué se debe hacer primero?
¿Cuál de las siguientes afirmaciones es verdadera respecto a las soluciones óptimas alternativas?
¿Cómo se detecta que un problema es infactible?
¿Qué método de solución para programación lineal permite trabajar con más de tres variables y es computacionalmente eficiente?
¿Qué variable entra en la base en el Método del Simplex?
En un problema primal-dual, ¿qué relación existe entre el primal y el dual en su forma estándar?
En programación entera, ¿qué método se utiliza para resolver problemas que requieren que algunas o todas las variables sean enteras?
¿Qué sucede si en el Método del Simplex no se puede mejorar la función objetivo?
¿Qué representa el costo reducido zj−cj en la tabla del Simplex?
¿Cuál de las siguientes afirmaciones describe un problema en forma estándar?
¿Qué permite hacer la transformación canónica en un problema de minimización?
¿Qué es un punto extremo en el conjunto factible de un problema de programación lineal?
¿Qué define a una solución básica en el método del Simplex?
¿Cómo se puede identificar una solución no acotada en el Método del Simplex?
En el Método del Simplex, ¿qué indica el valor de la columna zj−cj?
¿Qué sucede si en un problema de programación lineal se introduce una variable de holgura?
¿Qué característica tiene un problema primal en comparación con su dual?
¿Cuál es la principal utilidad de la tabla del Simplex en la solución de problemas de programación lineal?
¿Qué representa la variable artificial introducida en el Método del Simplex para asegurar una solución inicial factible?
¿Cuál es la regla de la variable de entrada en el Método del Simplex?
¿Qué es una base factible en el Método del Simplex?
¿Qué asegura el teorema de los puntos extremos en un problema de programación lineal?
¿Qué ocurre si en el Método del Simplex todas las variables no básicas tienen un zj−cj ≥ 0?
¿Qué indica que un problema de programación lineal tiene soluciones óptimas alternativas?
¿Cuál es la función principal de las restricciones duales en un problema dual?
En un problema de programación entera con variables binarias (0-1), ¿qué representa el Algoritmo de Ramificación y Acotación?
¿Qué asegura el Teorema de Dualidad Fuerte en la programación lineal?
¿Qué significa que un problema tenga una base degenerada en el Método del Simplex?
¿Cuál es el principal objetivo de las transformaciones algebraicas en el Método del Simplex?
En un problema de programación lineal en forma canónica, ¿qué condiciones deben cumplirse?
¿Qué tipo de restricciones tiene un problema en forma estándar?
Si una variable de decisión no está restringida en signo, se puede representar como
En el método del Simplex, una base factible debe cumplir que
¿Qué relación hay entre una solución básica factible y un punto extremo?
Si en el método del Simplex todos los valores zj−cj ≥ 0, entonces
¿Qué condición indica que un problema es no acotado?
¿Qué indica una variable artificial en el método del Simplex?
En la forma tabular del Simplex, la columna cB contiene
En la regla de la variable de salida, ¿qué cociente determina qué variable abandona la base?
Si el problema primal es de maximización con restricciones ≤, el dual será
En la interpretación económica del dual, las variables duales representan
Si el primal tiene una solución óptima, el teorema de dualidad fuerte asegura que
En un problema de transporte, ¿qué representan las variables xij?
En un problema de asignación, ¿qué valor toma xij si el recurso i se asigna a la tarea j?
En el modelo de camino de longitud mínima, la variable xij vale 1 si
En el método de la M grande, la constante M debe ser
¿Qué tipo de problemas puede resolver el algoritmo de Ramificación y Acotación?
En la programación entera mixta, ¿qué ocurre?
En una base degenerada del Simplex
En el Método del Simplex, si dos variables tienen el mismo valor mínimo en la razón xBi/yij, ¿qué puede ocurrir si se elige cualquiera de ellas?
Si en un problema del Simplex se detecta que zj−cj<0 pero todos los coeficientes de la columna de entrada son negativos o cero, entonces
En el método de la M grande, ¿cuál es el objetivo de asignar un valor muy grande a M?
En el contexto de la dualidad, si el problema primal es infactible, entonces el dual
En un problema dual, ¿qué significa que una variable dual sea igual a cero en la solución óptima?
Si el dual tiene una solución óptima infinita, ¿qué se puede concluir sobre el problema primal?
En un problema de programación entera binaria, si se añade la restricción x1+x2≤1, ¿qué se está modelando?
En el algoritmo de Ramificación y Acotación, ¿qué ocurre cuando se obtiene una solución entera con valor mejor que la mejor cota actual?
¿Cuál es el propósito principal de la relajación lineal en programación entera?
En un problema con una condición if a>b then c=1 else c=0, ¿qué garantiza el uso del método de la M grande?'''.splitlines()
assert len(A_PROMPTS)==20 and len(EXTRAS)==17 and len(C_PROMPTS)==60
A_IDS=['entera-009','redes-001','artificiales-019','bases-001','anterior-001','artificiales-011','anterior-002','formas-007','dualidad-008','anterior-003','artificiales-003','simplex-001','formas-009','grafica-019','fundamentos-019','anterior-004','dualidad-004','simplex-005','formas-003','artificiales-006']
EXTRA_IDS=['fundamentos-019','simplex-005','grafica-003','bases-001','entera-009','artificiales-001','grafica-020','formas-009','dualidad-008','formas-003','bases-018','artificiales-006','artificiales-003','anterior-005','redes-001','entera-008','fundamentos-002']
C_IDS=['formas-001','grafica-001','grafica-008','fundamentos-009','anterior-006','simplex-001','anterior-007','anterior-008','artificiales-010','simplex-004','formas-002','formas-005','anterior-009','bases-003','artificiales-011','simplex-004','formas-007','anterior-007','anterior-010','artificiales-001','simplex-001','bases-001','grafica-020','artificiales-010','grafica-008','anterior-011','entera-009','dualidad-006','bases-008','formas-007','formas-001','formas-002','formas-011','bases-001','bases-013','artificiales-010','artificiales-011','artificiales-001','bases-014','simplex-005','anterior-007','dualidad-008','dualidad-006','redes-001','redes-008','redes-014','artificiales-018','anterior-008','entera-002','bases-008','simplex-019','artificiales-011','anterior-012','dualidad-014','dualidad-012','dualidad-013','entera-016','entera-012','entera-004','entera-019']
assert len(C_IDS)==60
# Enunciados y opciones corregidos. Se mantienen IDs y correctId para conservar el historial.
# Separador |: id, tema, apartado, pregunta, correcta, distractor A, distractor B, explicación, nota de revisión.
ROWS='''
redes-001|redes|13|En un problema de transporte entre orígenes y destinos, ¿qué representan las variables xij?|La cantidad enviada del origen i al destino j|Solo una decisión binaria sobre si existe movimiento, sin indicar cantidad|El coste unitario cij de transportar una unidad|El transporte decide cantidades sobre una estructura bipartita de orígenes y destinos. El coste cij es un dato; xij no tiene por qué ser una variable binaria ni necesariamente entera en toda formulación.|Se agrupan las variantes sobre la caracterización del transporte y el significado de sus variables, evitando atribuir integridad automática a cualquier modelo.
grafica-019|grafica|06|¿Qué limitación principal tiene la resolución gráfica habitual en un plano?|Se aplica directamente a problemas con pocas variables, normalmente dos|Solo admite problemas con pocas restricciones, aunque tengan cien variables|Es un método gráfico plano apropiado para cualquier dimensión|El número de variables determina la dimensión que habría que representar. Pueden dibujarse muchas restricciones de dos variables; pocas restricciones no reducen automáticamente cien variables a un plano.|Se conserva la distinción entre pocas variables y pocas restricciones del test original.
entera-004|entera|15|¿Cuál es el propósito de la relajación lineal de un modelo entero en ramificación y acotación?|Resolver una versión continua retirando la integridad para obtener cotas y guiar la búsqueda|Eliminar todas las restricciones del modelo|Redondear directamente cualquier solución fraccionaria y declararla óptima|La relajación conserva restricciones y cotas y amplía los dominios enteros a continuos. Su óptimo da cota superior en máximo e inferior en mínimo; redondear no garantiza factibilidad ni optimalidad.|Se incluyen tanto la operación de retirar integridad como su finalidad de obtener cotas, presentes en las variantes del material.
anterior-001|fundamentos|03|En la formulación habitual de una PL, ¿qué relaciones pueden usarse en las restricciones lineales?|≤, ≥ o =|Solo desigualdades estrictas < y >|Cualquier relación no lineal|La formulación habitual utiliza igualdades y desigualdades no estrictas. Productos, cuadrados o desigualdades estrictas no se incorporan sin tratar sus particularidades.|Se explicita «formulación habitual» y se eliminan erratas de símbolos del original.
anterior-002|formas|05|Según la terminología de los apuntes, ¿qué formas se estudian para representar una PL?|Canónica, estándar y simétrica|Singular, estándar y simétrica|Canónica, multivaluada y estándar|Los materiales denominan estas formas canónica, estándar y simétrica; «singular» describe una matriz sin inversa, no una forma de PL.|Se conserva la terminología concreta de clase.
anterior-003|fundamentos|03|¿Qué resultados puede presentar una PL continua al analizar su factibilidad y su objetivo?|Óptimo finito único o múltiple, infactibilidad, o un objetivo no acotado|Siempre un único óptimo finito|Siempre una solución factible|Primero se distingue si hay puntos factibles; si los hay, el objetivo puede ser no acotado o alcanzar un óptimo finito, único o con múltiples soluciones.|«Una o más soluciones» del original se precisa como resultados de optimización, sin confundir factibles con óptimas.
anterior-004|fundamentos|03|En el modelo matricial de PL con objetivo cᵀx y restricciones Ax≤b, ¿qué representan A, c y b?|A: coeficientes tecnológicos; c: costes o beneficios; b: recursos o términos independientes|A: costes; c: recursos; b: coeficientes tecnológicos|A: soluciones; c: restricciones; b: decisiones binarias|A tiene los coeficientes de las restricciones, c los del objetivo y b sus términos independientes. x contiene las decisiones.|Se añaden los símbolos para que la identificación sea inequívoca.
anterior-005|entera|15|¿Qué clases de programación entera se distinguen en los apuntes?|Entera pura, entera mixta y binaria 0–1|Canónica, estándar y simétrica|Factible, degenerada y singular|Pura impone integridad a todas las decisiones; mixta combina enteras y continuas; binaria restringe decisiones a 0 y 1. Las otras listas no clasifican los dominios enteros.|La binaria se presenta como el caso 0–1, sin afirmar que estas categorías sean conjuntos disjuntos.
anterior-006|simplex|08|¿Qué método estudiado permite resolver una PL con más de tres variables sin recurrir a una representación gráfica en el plano?|El método del Simplex|El método gráfico plano|El método de mínimos cuadrados como algoritmo general de PL|Simplex opera con bases y tablas de cualquier dimensión compatible. Un dibujo plano no representa directamente más de dos variables; mínimos cuadrados resuelve otro tipo de problema.|Se elimina la afirmación imprecisa «computacionalmente eficiente» como garantía general: Simplex no tiene complejidad polinómica de peor caso.
anterior-007|dualidad|11|Para un primal max cᵀx con Ax≤b y x≥0, ¿qué sentido y desigualdades tiene su dual simétrico?|Minimiza, con Aᵀy≥c e y≥0|También maximiza, con Aᵀy≤c|Minimiza, pero tiene siempre el mismo número de variables y restricciones que el primal|La pareja simétrica es max con ≤ frente a min con ≥. El dual tiene una variable por restricción primal y una restricción por variable primal; las dimensiones no coinciden necesariamente.|Se fijan el sentido del primal y la forma simétrica. Un primal general también puede minimizar, por lo que el original sin hipótesis era ambiguo.
anterior-008|entera|15|¿Qué algoritmo estudiado resuelve modelos lineales con exigencias de integridad, incluidas variables binarias?|Ramificación y acotación|Simplex continuo por sí solo garantiza siempre la integridad|La transformación a forma canónica por sí sola|Ramificación y acotación usa relajaciones y divide regiones para encontrar y certificar soluciones enteras. Simplex puede resolver las relajaciones, pero no impone por sí solo integridad general.|Se unen las variantes que preguntan el nombre del algoritmo y qué clase de problemas resuelve.
anterior-010|simplex|09|¿Cuál es la utilidad principal de la tabla del Simplex?|Organizar las columnas transformadas, los valores básicos y los costes reducidos para realizar los pivotes|Garantizar que siempre se necesita menos de un pivote|Sustituir las restricciones por un dibujo de dos dimensiones|La tabla representa B⁻¹A, B⁻¹b y los costes reducidos. Facilita cálculo y lectura de pivotes, sin garantizar un número fijo menor de iteraciones.|Se precisa el contenido tabular; organizar datos no constituye una garantía de reducir iteraciones.
anterior-011|dualidad|11|En el dual de max cᵀx con Ax≤b y x≥0, ¿qué expresan las restricciones Aᵀy≥c?|Que la valoración dual de los recursos consumidos por cada actividad no sea menor que su beneficio unitario|Que las variables primales dejen de cumplir sus restricciones originales|Que las holguras primales valgan todas cero|Cada columna aj exige ajᵀy≥cj: la valoración de los recursos de una unidad de actividad cubre su beneficio. Esto permite construir una cota dual del máximo primal.|Se reemplaza la explicación ambigua de «coste marginal» por la desigualdad y su interpretación correcta.
anterior-012|artificiales|10|¿Para qué se asigna una penalización M suficientemente grande a las variables artificiales?|Para favorecer su eliminación de la solución auxiliar cuando el modelo original es factible|Para convertirlas en recursos disponibles reales|Para imponer que todas las variables originales sean binarias|La penalización evita conservar artificiales por conveniencia del objetivo. En máximo sus coeficientes son −M y en mínimo +M; si no pueden eliminarse, hay que comprobar la infactibilidad original.|Se especifica que se trata de M en el tratamiento de artificiales, distinto del uso de cotas M en condiciones lógicas.
fundamentos-002|fundamentos|03|¿Cuál de las siguientes restricciones es lineal?|2x₁+x₂+1 = 3|x₁x₂+1 = 3|x₁²+x₂ = 3|Una suma de variables con coeficientes constantes y un término independiente es lineal o afín. El 1 puede pasarse al otro lado; productos y cuadrados de variables no son expresiones lineales.|La lista de extras solo daba la correcta; se añaden dos distractores originales para practicar con tres opciones.
artificiales-019|artificiales|10|En forma estándar con b≥0, si se inicia Simplex con una base identidad sin artificiales y no básicas a cero, ¿qué se sabe del modelo original?|Que ya se dispone de una solución factible|Que el óptimo es necesariamente único|Que el objetivo es necesariamente no acotado|Con B=I se obtiene xB=b≥0; junto a xN=0 satisface el sistema y el dominio. Esto certifica factibilidad, pero no optimalidad ni acotación del objetivo.|Se explicitan b≥0 y las no básicas a cero: la mera aparición de una identidad sin esas condiciones no bastaría.
bases-001|bases|07|Para iniciar Simplex primal con m ecuaciones independientes y n variables totales, ¿qué base inicial se necesita?|Una B de tamaño m×m, invertible, con B⁻¹b≥0|Una B de tamaño n×n en todos los casos|Cualquier B de tamaño m×m, aunque su solución básica tenga componentes negativas|Se eligen m columnas independientes; la inversa determina los valores básicos. Para Simplex primal se requiere una solución básica factible, no solo cumplir las igualdades.|Se explicitan el rango, las dimensiones tras transformar el modelo y la no negatividad omitida en algunas respuestas de base factible.
formas-007|formas|05|¿Para qué se añaden variables de holgura o de exceso al pasar una PL a forma estándar?|Para convertir restricciones ≤ o ≥ en igualdades con auxiliares no negativas|Para garantizar siempre una base identidad sin importar el signo ni b|Para imponer integridad a todas las decisiones|En ax≤b se suma s; en ax≥b se resta s. Las artificiales, no las holguras por sí solas, ayudan a formar una base inicial cuando hace falta.|Se agrupan las formulaciones equivalentes sobre conversión a igualdad. La pregunta sobre «todas las transformaciones» se restringe a esta operación concreta.
formas-003|formas|05|En la forma estándar utilizada en clase, ¿qué dominio tienen las variables de decisión?|Son no negativas|Son estrictamente positivas|Son todas no positivas|La forma estándar exige x≥0 y permite el cero. En una formulación general puede haber variables libres, que se transforman como diferencia de no negativas.|Se añade el contexto «forma estándar»: en una PL general también son posibles variables libres, así que el original sin contexto era ambiguo.
artificiales-003|artificiales|10|En una maximización con gran M, ¿qué coeficientes corresponden a una artificial t y a una holgura s en el objetivo?|−M para t y 0 para s, con M>0 suficientemente grande|−M para s y 0 para t|+M para t y +M para s|La artificial se penaliza en un máximo; la holgura conserva coste cero. Un signo positivo premiaría la artificial y no expulsaría su uso.|Se usa −M en lugar de tratar −∞ como un coeficiente real sobre el que operar aritméticamente.
simplex-005|simplex|08|En Simplex primal, ¿qué regla determina la variable básica de salida para una columna entrante yj?|El menor cociente xBi/yij entre los denominadores yij>0|El menor valor básico xBi, sin mirar yij|El mayor coeficiente de la variable en el objetivo|Solo yij>0 hace disminuir una básica; el menor cociente indica cuál llega a cero primero. Denominadores nulos o negativos no limitan el paso por ese criterio.|Se corrigen índices y se explicita que el denominador debe ser estrictamente positivo.
artificiales-011|artificiales|10|En maximización desde una base factible del original, ¿qué permite certificar que el objetivo no está acotado?|Una no básica con rj=zj−cj<0 y columna transformada yj≤0|Que quede una artificial positiva en el óptimo de fase I|Que una base elegida arbitrariamente tenga una componente negativa|El coste negativo da una dirección de mejora y yj≤0 permite aumentar la entrante sin agotar ninguna básica. La artificial positiva al finalizar fase I señala infactibilidad; una mala base no clasifica todo el modelo.|Se añaden la dirección de mejora y la factibilidad original. En el criterio se usa B⁻¹aj, no los coeficientes originales aj sin transformar.
artificiales-006|artificiales|10|¿Qué resultado de una fase I correctamente terminada certifica que el modelo original es infactible?|Un mínimo estrictamente positivo de la suma de artificiales|Una artificial positiva en cualquier iteración intermedia|Una artificial básica con valor cero|Si el mínimo auxiliar es positivo no existe una solución que elimine todas las artificiales. Su presencia intermedia o su pertenencia a la base con valor cero no demuestran infactibilidad.|Se precisa «al acabar» como óptimo del auxiliar correctamente resuelto, no cualquier interrupción del algoritmo.
fundamentos-019|fundamentos|03|¿Para qué sirve resolver una PL mediante un método exacto hasta su terminación correcta?|Para encontrar y certificar un óptimo cuando existe, o identificar el estado correspondiente del problema|Solo para obtener una solución aproximadamente buena|Para aceptar siempre soluciones que incumplen alguna restricción|La PL busca el mejor objetivo entre las soluciones admisibles. Un método exacto puede certificar óptimo, infactibilidad o no acotación; no necesita aceptar soluciones inadmisibles.|«Encontrar óptimos si existe alguno» se mantiene, haciendo explícitos los otros estados posibles.
grafica-020|grafica|06|Para una PL en forma estándar factible con óptimo finito, ¿qué permite el teorema de los puntos extremos?|Buscar un óptimo entre los vértices o soluciones básicas factibles|Afirmar que todo punto factible es un vértice|Afirmar que cualquier PL tiene siempre infinitos puntos factibles|Existe al menos un óptimo en un vértice. Hay un número finito de bases candidatas, aunque F pueda tener infinitos puntos; F también puede ser vacío o un único punto en otros modelos.|La frase de los extras que afirmaba una región «infinitamente grande» para cualquier PL es falsa en general. Se añaden las hipótesis del teorema y se distingue un óptimo en vértice de todos los óptimos en vértices.
formas-001|formas|05|Según los apuntes, ¿qué condiciones definen la forma canónica de maximización?|Maximizar, restricciones ≤ y variables no negativas|Minimizar, todas las restricciones iguales y variables libres|Maximizar con restricciones estrictas < y variables libres|La convención docente utiliza max cᵀx, Ax≤b y x≥0. Las tres condiciones deben conservarse al identificar la forma.|Se completa la respuesta de la recopilación que omitía no negatividad; se usa la convención de los apuntes.
grafica-008|grafica|06|¿Qué condición permite concluir que una PL tiene soluciones óptimas alternativas?|Dos puntos factibles distintos alcanzan el mismo valor óptimo, y su segmento también es óptimo|La recta objetivo es paralela a cualquier restricción, aunque no forme una cara óptima factible|Una restricción es redundante, sin más información|Por convexidad y linealidad, el segmento de dos óptimos distintos es óptimo. El paralelismo debe sostener una cara óptima factible; cualquier paralelismo aislado no basta.|Se corrige el criterio insuficiente de paralelismo con una restricción cualquiera.
fundamentos-009|fundamentos|03|¿Qué significa que una PL sea infactible?|Que su región factible sea vacía|Que no hayamos encontrado todavía una solución|Que el objetivo puede crecer sin límite desde puntos factibles|Infactibilidad es una propiedad del modelo: ningún punto cumple todo. No haber encontrado una solución no prueba su inexistencia; no acotación supone puntos factibles.|Se elimina «todas las anteriores»: no encontrar una solución por sí solo no certifica que no exista.
artificiales-010|artificiales|10|En maximización, con base factible del original y artificiales a cero, ¿qué certifica rj=zj−cj≥0 para todas las no básicas?|Que la solución actual es óptima|Que el modelo es necesariamente infactible|Que el objetivo es no acotado|No existe una dirección básica de mejora con esos signos y la solución ya es válida para el original. Sin factibilidad original y sin eliminar artificiales positivas no bastaría el criterio de costes.|Se añaden las hipótesis omitidas en las variantes «no se puede mejorar» y «todos los costes son no negativos».
simplex-004|simplex|08|Con rj=zj−cj, ¿cómo varía el objetivo al aumentar xj en un paso factible θ manteniendo la base?|Δz=(cj−zj)θ=−rjθ|Δz=(zj−cj)θ=rjθ|Δz=cjθ sin ajustar las básicas|El aumento de la entrante obliga a ajustar las básicas: zj mide esa pérdida. La mejora por unidad es cj−zj, el opuesto de rj, y la variación total multiplica por θ.|Se corrige el signo de las respuestas marcadas: zj−cj no es el incremento positivo del objetivo. Se distingue tasa marginal de mejora total.
anterior-009|grafica|06|¿Qué define a un punto extremo de una región factible convexa?|Un punto factible que no puede expresarse como combinación convexa no trivial de dos puntos factibles distintos|Cualquier intersección de dos rectas, aunque incumpla otras restricciones|Un punto que siempre minimiza cualquier objetivo|Se exige una combinación de puntos distintos con peso entre 0 y 1. Una intersección puede ser infactible y un vértice no optimiza todos los objetivos.|Se añaden «no trivial» y «distintos» a la definición original.
redes-008|redes|13|En la formulación binaria de asignación, ¿cuánto vale xij cuando el individuo i se asigna a la tarea j?|1|0|El coste cij de la asignación|La decisión binaria indica seleccionar la pareja con 1 y no seleccionarla con 0; cij es un dato económico distinto.|Se explicita que se usa la formulación binaria; no se confunde con su posible relajación lineal.
artificiales-018|artificiales|10|En el método de la gran M para artificiales, ¿cómo se elige la constante M?|Positiva y suficientemente grande para la penalización requerida|Siempre M=1, independientemente de la escala del modelo|Negativa, sin cambiar ningún otro signo del objetivo|M se define positiva; la penalización aparece como −M al maximizar y +M al minimizar. Un valor numérico arbitrario puede ser insuficiente; puede tratarse simbólicamente.|Se distingue el signo de M del signo de su coeficiente en el objetivo.
simplex-019|simplex|08|En una base factible, ¿qué puede ocurrir si empatan dos cocientes mínimos de salida con denominadores positivos?|La nueva solución básica puede ser degenerada; con reglas inadecuadas la degeneración puede permitir ciclado|El modelo se vuelve necesariamente infactible|Se garantiza que ya se alcanzó el óptimo|Dos básicas llegan simultáneamente a cero; al salir una, la otra puede quedar básica cero. No todo empate produce un ciclo: el ciclado es una posibilidad con reglas inadecuadas, no una equivalencia.|Se separan degeneración y ciclado: el original los confundía como si fueran lo mismo.
dualidad-012|dualidad|12|Si una variable dual óptima vale cero, ¿qué puede afirmarse de la restricción primal correspondiente?|Puede estar activa o tener holgura; el cero no distingue ambos casos|Está necesariamente inactiva|Es necesariamente redundante|Complementariedad permite holgura positiva ⇒ precio cero, pero no la implicación inversa. Por ejemplo max x con x≤1 e y≤1 admite el óptimo (1,1), con la segunda restricción activa y precio cero.|Se corrige expresamente la opción marcada que deducía inactividad de precio sombra cero.
dualidad-013|dualidad|11|Si el objetivo del dual es no acotado en su sentido de mejora, ¿qué se concluye del primal?|Que es infactible|Que tiene infinitos óptimos de valor finito necesariamente|Que es degenerado necesariamente|Por dualidad débil, un primal factible impondría una cota al dual en el sentido correspondiente. La no acotación dual obliga a infactibilidad primal; el mismo razonamiento funciona intercambiando papeles.|Se sustituye «solución óptima infinita» por «objetivo no acotado». Tener infinitos óptimos finitos es otro fenómeno y no implica infactibilidad del otro problema.
entera-008|entera|15|Al ramificar una relajación de un modelo entero, ¿qué variable se elige y cómo se divide su dominio?|Una variable exigida entera con valor v fraccionario, creando ramas xi≤suelo(v) y xi≥techo(v)|Cualquier variable continua, aunque no deba ser entera|Una variable ya entera, conservando la misma fracción en ambas ramas|Una variable que debe ser entera y vale, por ejemplo, 3,4 se divide en xi≤3 y xi≥4. Así se cubren todos sus valores enteros y se excluye la fracción actual.|La lista adicional solo daba una respuesta corta; se incorporan las restricciones de suelo y techo y dos distractores.
entera-012|entera|15|En una maximización entera, si el óptimo relajado de un nodo es entero y mejora al incumbente, ¿qué se hace?|Actualizar el incumbente y su cota inferior, cerrar ese nodo y podar otros cuyas cotas no puedan mejorarla|Reiniciar todo el árbol desde cero|Conservar el incumbente anterior aunque sea peor|El punto es entero y factible, por lo que da un valor alcanzable mejor. La relajación ya certifica el óptimo de ese nodo; los demás se podan solo si sus propias cotas lo justifican.|Se explicita maximización: en minimización el incumbente es cota superior. No se eliminan indiscriminadamente todas las ramas.
entera-019|entera|14|Con variables acotadas y una binaria de activación, ¿para qué se usa una constante M válida en restricciones condicionales?|Para activar o desactivar restricciones lineales de acuerdo con la lógica de la binaria|Para garantizar por sí sola que cualquier variable continua sea entera|Para representar cualquier comparación estricta continua exacta sin condiciones adicionales|Una M obtenida de cotas válidas puede relajar una condición cuando la binaria no la activa. La integridad debe declararse y los umbrales estrictos continuos requieren hipótesis explícitas.|Se corrige la promesa demasiado general del if a>b: no basta mencionar M para representar exactamente todo umbral estricto continuo; se añaden cotas y binaria.
'''
# Una definición editorial por pregunta; las repeticiones se agrupan en el inventario.
UPDATES={}
for line in ROWS.strip().splitlines():
 fields=line.split('|');assert len(fields)==9,(fields[0],len(fields))
 qid,topic,section,prompt,c,a,b,explanation,note=fields
 assert qid not in UPDATES,qid
 UPDATES[qid]={'id':qid,'topic':topic,'difficulty':2,'prompt':prompt,
 'options':[{'id':'c','text':c},{'id':'a','text':a},{'id':'b','text':b}], 'correctId':'c',
 'explanation':explanation,'rationales':{k:('Correcta. ' if k=='c' else 'Incorrecta. ')+explanation for k in ['c','a','b']},
 'reference':f'Guía, apartado {section}','kind':'concepto','revisionNote':note}

def page_for(doc,n,section='principal'):
 if doc=='A':return 2 if n<=4 else 3 if n<=10 else 4 if n<=15 else 5
 if doc=='B':
  if section=='extras':return 5 if n<=9 else 6
  return 2 if n<=5 else 3 if n<=11 else 4 if n<=17 else 5
 if doc=='D':return 2 if n<=7 else 3 if n<=14 else 4 if n<=21 else 5 if n<=28 else 6
 for lo,hi,p in [(1,5,2),(6,11,3),(12,16,4),(17,22,5),(23,27,6),(28,33,8),(34,39,9),(40,45,10),(46,50,11),(51,56,12),(57,60,13)]:
  if lo<=n<=hi:return p

def inventory():
 entries=[]
 for doc in ['A','B','C','D']:
  prompts=A_PROMPTS if doc in ['A','B'] else C_PROMPTS if doc=='C' else C_PROMPTS[:30]
  ids=A_IDS if doc in ['A','B'] else C_IDS if doc=='C' else C_IDS[:30]
  for n,(prompt,qid) in enumerate(zip(prompts,ids),1):
   entries.append({'key':f'{doc}:principal:{n}','document':doc,'file':FILES[doc]['file'],'section':'principal','number':n,'printedNumber':n if doc!='D' or n<=10 else n-10,'page':page_for(doc,n),'originalPrompt':prompt,'questionId':qid})
  if doc=='B':
   for n,(prompt,qid) in enumerate(zip(EXTRAS,EXTRA_IDS),1):entries.append({'key':f'B:extras:{n}','document':'B','file':FILES['B']['file'],'section':'extras','number':n,'printedNumber':n,'page':page_for('B',n,'extras'),'originalPrompt':prompt,'questionId':qid})
 assert len(entries)==147
 assert len({e['key'] for e in entries})==147
 return entries

def apply_to_bank(bank):
 entries=inventory();lookup={q['id']:q for q in bank['questions']}
 all_ids={e['questionId'] for e in entries}
 for qid in sorted(all_ids):
  if qid in UPDATES:
   if qid in lookup:lookup[qid].update(UPDATES[qid])
   else:
    bank['questions'].append(UPDATES[qid].copy());lookup[qid]=bank['questions'][-1]
  q=lookup[qid];q['pastExam']=True
  q['sources']=[{k:v for k,v in e.items() if k!='questionId'} for e in entries if e['questionId']==qid]
  q.setdefault('revisionNote','Enunciado revisado y adaptado a tres opciones con una única correcta. Se conserva el concepto preguntado y se agrupan sus variantes repetidas.')
 # Algunas respuestas cortas en los extras no traían distractores.
 for q in bank['questions']:
  if not q.get('pastExam'):continue
  if any(s['section']=='extras' for s in q['sources']):q['revisionNote']+=' Las entradas del apartado de extras solo daban la respuesta: se completan con distractores para poder practicarlas.'
 bank['pastExams']={'documents':FILES,'occurrences':len(entries),'uniqueQuestions':len(all_ids),'coverage':entries,
  'note':'Todas las apariciones de los cuatro documentos aportados se asocian a una pregunta corregida. La deduplicación agrupa enunciados equivalentes, no todos los ejercicios de un mismo tema. No se atribuye año ni carácter oficial que no conste en los documentos.'}
 assert len({q['prompt'] for q in bank['questions']})==len(bank['questions'])
 return bank

def write_outputs(bank):
 coverage=bank['pastExams']
 (ROOT/'study/past-exam-coverage.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2))
 (ROOT/'web/past-exam-coverage.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2))
 esc=html.escape
 lookup={q['id']:q for q in bank['questions']}
 parts=['<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Exámenes anteriores · Cobertura y correcciones</title><link rel="stylesheet" href="./styles.css"></head><body><main class="coverage"><a class="button secondary" href="./">← Volver a practicar</a><p class="eyebrow" style="margin-top:32px">Exámenes anteriores · revisión completa</p><h1>Cobertura y correcciones</h1>',
 f'<p><strong>{coverage["occurrences"]} apariciones revisadas → {coverage["uniqueQuestions"]} preguntas únicas.</strong> Se incluyen todas las preguntas principales y los 17 extras, agrupando las repetidas entre archivos y dentro de cada recopilación.</p><p>Las preguntas se han adaptado a tres opciones y se han corregido errores e hipótesis omitidas. No se presuponen solucionarios oficiales ni años que no consten. Los originales se conservan fuera del repositorio.</p>']
 for doc,meta in FILES.items():
  parts.append(f'<details><summary><strong>{esc(meta["file"])}</strong> · {meta["count"]} apariciones</summary>')
  if meta.get('reviewNote'):parts.append('<p>'+esc(meta['reviewNote'])+'</p>')
  if meta.get('numberingNote'):parts.append('<p>'+esc(meta['numberingNote'])+'</p>')
  parts.append('<ol>')
  for e in coverage['coverage']:
   if e['document']!=doc:continue
   label=f'{"Extra " if e["section"]=="extras" else "Pregunta "}{e["number"]} · pág. {e["page"]}'
   if doc=='D' and e['number']>10:label+=f' · impresa como {e["printedNumber"]}'
   parts.append(f'<li><a href="#{e["questionId"]}"><strong>{label}</strong>: {esc(e["originalPrompt"])}</a></li>')
  parts.append('</ol></details>')
 parts.append('<h2>Preguntas unificadas y revisión</h2>')
 for n,qid in enumerate(dict.fromkeys(e['questionId'] for e in coverage['coverage']),1):
  q=lookup[qid];correct=next(o['text'] for o in q['options'] if o['id']==q['correctId'])
  sources='; '.join(f'{s["document"]} {"extra " if s["section"]=="extras" else ""}{s["number"]}' for s in q['sources'])
  parts.append(f'<article class="sheet review-card" id="{qid}"><span class="badge">{n} · Referencias: {esc(sources)}</span><h3>{esc(q["prompt"])}</h3><details><summary>Ver respuesta y corrección</summary><p><strong>Respuesta:</strong> {esc(correct)}</p><p>{esc(q["explanation"])}</p><p><strong>Revisión:</strong> {esc(q["revisionNote"])}</p></details></article>')
 parts.append('</main></body></html>')
 (ROOT/'web/examenes-anteriores.html').write_text('\n'.join(parts))

if __name__=='__main__':
 bank=json.loads((ROOT/'study/questions.json').read_text())
 # La ejecución directa parte del banco fresco para no acumular notas.
 from subprocess import run
 import sys
 run([sys.executable,str(ROOT/'scripts/build_bank.py')],check=True)
