"""Banco original; cada línea conceptual contiene pregunta, opciones y explicación."""
import json, random
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
TOPICS={
'fundamentos':('Fundamentos','03'), 'modelos':('Modelización','04'),
'formas':('Formas y transformaciones','05'), 'grafica':('Resolución gráfica','06'),
'bases':('Bases y degeneración','07'), 'simplex':('Simplex','08'),
'artificiales':('Artificiales y terminación','10'), 'dualidad':('Dualidad','11'),
'redes':('Transporte, asignación y redes','13'), 'entera':('Entera y condiciones','14')}
DATA={
'fundamentos': '''
¿Qué debe ser lineal en un programa lineal?|La función objetivo y las expresiones de las restricciones|Solo la función objetivo|Solo las restricciones|La linealidad se exige tanto al objetivo como a las restricciones; imponerla solo a una parte no basta.
¿Cuál de estas expresiones es afín y puede aparecer en una restricción lineal?|3x + 2y + 7|xy + 7|x² + y|Se permiten sumas con coeficientes constantes y un término independiente; productos de variables y cuadrados no son lineales.
¿Qué representa una variable de decisión?|Una cantidad que debe determinar el modelo|Siempre una disponibilidad fija|Siempre el beneficio unitario|Las decisiones son incógnitas; disponibilidades y beneficios unitarios suelen ser datos del problema.
¿Qué representa c en z = cᵀx?|Los coeficientes del objetivo|Las disponibilidades de recursos|La solución óptima|c contiene costes o beneficios unitarios; b representa los términos independientes y x representa las decisiones.
¿Qué representa b en Ax ≤ b?|Los términos independientes de las restricciones|El vector de costes reducidos|La matriz de restricciones|b contiene límites o recursos; los costes reducidos se calculan con la base y A es la matriz de coeficientes.
¿Qué contiene A en Ax ≤ b?|Los coeficientes de las variables en las restricciones|Solo los beneficios unitarios|Solo las soluciones factibles|A es la matriz tecnológica, c contiene los coeficientes del objetivo y las soluciones no son datos de A.
¿Qué es una solución factible?|Un vector que cumple todas las restricciones y dominios|Cualquier vector que mejora el objetivo|Cualquier vector de componentes positivas|Mejorar el objetivo o ser positivo no garantiza satisfacer las restricciones del modelo.
¿Qué es una solución óptima de maximización?|Una factible cuyo objetivo no es superado por ninguna otra factible|Cualquier solución factible|Un punto con todas las variables positivas|Optimalidad exige factibilidad y comparación con todas las soluciones factibles; positividad estricta no es necesaria.
¿Qué significa que un problema sea infactible?|Que su conjunto factible es vacío|Que el objetivo puede crecer sin límite|Que hay más de una solución óptima|Infactibilidad es ausencia de soluciones factibles; no acotación y multiplicidad son conceptos distintos.
¿Qué significa no acotación del objetivo al maximizar?|Existen valores factibles del objetivo arbitrariamente grandes|No existe ningún punto factible|La región factible tiene necesariamente área finita|La no acotación del objetivo requiere factibilidad y ausencia de cota superior; no significa región vacía.
¿Una región factible no acotada obliga a que el objetivo no esté acotado?|No, puede existir un óptimo finito|Sí, para cualquier objetivo|Sí, salvo que haya variables de holgura|El sentido y los coeficientes del objetivo importan; la presencia de holguras no determina su acotación.
¿Qué ocurre al añadir restricciones a un modelo manteniendo sus variables y dominios?|El conjunto factible no puede aumentar|El conjunto factible siempre aumenta|El conjunto factible siempre queda vacío|Una restricción adicional conserva o elimina puntos; no tiene por qué eliminar todos.
¿Qué ocurre al eliminar una restricción manteniendo el resto?|El conjunto factible no puede reducirse|El conjunto factible siempre se reduce|El objetivo cambia de maximización a minimización|Eliminar una condición conserva todos los puntos anteriores; no modifica por sí mismo el sentido del objetivo.
¿Una restricción redundante cambia el conjunto factible al retirarla?|No|Siempre lo aumenta estrictamente|Siempre cambia el valor óptimo|Una restricción redundante ya está implicada por las restantes, de modo que ni región ni óptimo cambian.
¿Qué es un parámetro del modelo?|Un dato conocido al formular el problema|Una variable que Simplex debe elegir|Una variable artificial necesariamente|Un parámetro es fijo para una instancia; decisiones y artificiales son variables.
¿Qué describe la función objetivo?|El criterio cuantitativo que se quiere maximizar o minimizar|Todas las condiciones de admisibilidad|La matriz inversa de cualquier base|Las restricciones describen admisibilidad; el objetivo expresa qué soluciones se prefieren.
¿Puede una solución óptima de PL continua tener valores fraccionarios?|Sí|No, Simplex siempre da enteros|Solo si el problema es infactible|La PL continua admite fracciones; la integridad requiere condiciones adicionales y un problema infactible no tiene óptimo.
¿Qué distingue principalmente optimización de factibilidad?|Optimización compara soluciones mediante un objetivo|Factibilidad exige siempre maximizar|Optimización permite incumplir restricciones|La factibilidad busca satisfacer condiciones; optimización busca además el mejor valor entre soluciones admisibles.
¿Qué caracteriza un método exacto aplicado correctamente hasta terminar?|Certifica un óptimo o el estado correspondiente del problema|Devuelve siempre un óptimo aunque no exista|Solo promete una solución aproximadamente buena|Un método exacto distingue también infactibilidad y no acotación; no promete óptimos inexistentes ni solo aproximaciones.
¿Pueden existir variables libres en una formulación general de PL?|Sí, y se transforman si se exige no negatividad|No, en ninguna formulación|Sí, pero convierten siempre el problema en no lineal|Una variable libre sigue siendo compatible con linealidad y puede representarse como diferencia de no negativas.
''',
'modelos': '''
¿Cómo se calcula el beneficio unitario si se conocen venta y coste unitarios?|Venta menos coste|Venta más coste|Solo el precio de venta|El beneficio descuenta el coste; sumar ambos o ignorar el coste no calcula el margen.
¿Qué desigualdad representa al menos L unidades de x?|x ≥ L|x ≤ L|x = 0|Al menos impone un límite inferior, no superior ni producción nula.
¿Qué desigualdad representa como máximo U unidades de x?|x ≤ U|x ≥ U|x > U|Como máximo impone una cota superior inclusiva; no exige superar U.
¿Cómo modelar exactamente D unidades producidas entre x e y?|x + y = D|x + y ≤ D|x + y ≥ D|Exactamente exige igualdad; los dos sentidos por separado permiten cantidades distintas de D.
¿Cómo modelar al menos dos unidades de y por cada unidad de x?|y ≥ 2x|x ≥ 2y|y ≥ x + 2|La proporción multiplica a x; invertirla o añadir una constante cambia el requisito.
¿Cómo modelar que no se produzca más de B que de A?|xB ≤ xA|xB ≥ xA|xB ≤ 1|Comparar producciones exige xB ≤ xA; no es una cuota fija de una unidad.
¿Cómo modelar que x sea al menos el 30 % del total x + y?|x ≥ 0,3(x + y)|x ≥ 0,3y|x ≥ 30|La base porcentual es el total; el 30 % de y o una cifra fija expresan requisitos diferentes.
¿Qué se debe hacer con kg y g en una misma restricción de material?|Convertirlos a una unidad común|Sumarlos directamente sin conversión|Eliminar el límite de material|Las unidades deben ser compatibles; ni ignorar la conversión ni quitar la restricción es válido.
¿Dos operarios con 40 horas cada uno aportan cuántas horas si son intercambiables?|80 horas|40 horas|160 horas|Las capacidades suman 40 + 40 cuando el trabajo puede repartirse entre ambos.
¿Si cada bicicleta usa dos ruedas, qué restricción limita 100 ruedas?|2x + 2y ≤ 100|x + y ≤ 100|2x + 2y ≥ 100|La disponibilidad es un máximo y cada unidad consume dos ruedas, no una.
¿Un recurso disponible que no aparece en el objetivo puede limitar el óptimo?|Sí, mediante sus restricciones|No, solo importan los coeficientes del objetivo|Solo si su precio es negativo|Las restricciones determinan qué combinaciones pueden producirse aunque el recurso no tenga término directo en el objetivo.
¿Es lineal una restricción con coeficientes constantes y variables sumadas?|Sí|Solo si todos los coeficientes son positivos|Solo si no hay término independiente|La linealidad no exige coeficientes positivos ni término independiente nulo.
¿Es lineal x + y ≤ 10 aunque x sea entera?|Sí; el dominio añade integridad|No; cualquier variable entera genera un producto|Solo cuando x vale cero|La expresión sigue siendo lineal; la integridad distingue PL entera de continua, sin crear productos.
¿Qué debe indicar una buena definición de variable?|Qué mide y sus unidades|Solo una letra|Solo el valor óptimo esperado|Significado y unidades permiten construir e interpretar el modelo; no se presupone la solución.
¿Si x mide litros, qué unidades debe tener c para que cx mida euros?|Euros por litro|Litros por euro|Euros por litro cuadrado|Al multiplicar euros/litro por litros se obtienen euros; las otras unidades no se cancelan correctamente.
¿Puede cambiarse la unidad de x sin modificar los coeficientes asociados?|En general no, deben ajustarse los coeficientes|Sí, siempre sin ningún cambio|Sí, pero solo en restricciones de igualdad|Cambiar escala requiere adaptar objetivo y restricciones; el signo de la restricción no evita esa necesidad.
¿Si un coste fijo solo se paga al abrir una fábrica, cómo representarlo naturalmente?|Con una binaria de apertura y su coste fijo|Añadiendo ese coste a cada unidad producida|Obligando a producir una unidad siempre|Un coste fijo depende de activar la instalación; no es proporcional a cada unidad ni exige abrir siempre.
¿Qué modelo representa x no superior a tres veces y?|x ≤ 3y|3x ≤ y|x ≤ y + 3|La comparación es multiplicativa; las alternativas invierten el factor o usan una diferencia fija.
¿Qué significa una solución numérica sin interpretar las unidades?|No basta para explicar la decisión real|Siempre determina beneficios en euros|Siempre representa unidades enteras de producto|Los números deben vincularse al significado de las variables; ni moneda ni integridad se deducen sin el modelo.
¿Se puede redondear cualquier óptimo continuo para resolver exactamente un modelo entero?|No, puede perder factibilidad u optimalidad|Sí, redondeando siempre hacia arriba|Sí, redondeando siempre hacia abajo|Redondear no controla simultáneamente restricciones y objetivo, en ninguno de los dos sentidos.
''',
'formas': '''
Según los apuntes, ¿qué caracteriza la forma canónica de maximización?|max, restricciones ≤ y variables no negativas|min, restricciones = y variables libres|max, restricciones estrictas <|La convención docente usa max, ≤ y no negatividad; ni igualdades con libres ni desigualdades estrictas la describen.
¿Qué restricciones aparecen en forma estándar en los apuntes?|Igualdades|Solo desigualdades ≤|Solo desigualdades ≥|La forma estándar exige igualdades; las desigualdades se transforman con variables auxiliares.
¿Qué dominio tienen las variables de la forma estándar utilizada en clase?|No negativas|Todas estrictamente positivas|Todas libres|Se admite cero; la no negatividad no equivale a positividad estricta ni a libertad de signo.
¿Qué condición se exige a b en la forma estándar de los apuntes?|b ≥ 0 componente a componente|b < 0 componente a componente|b = c necesariamente|Los términos independientes se normalizan no negativos; no tienen que coincidir con el vector del objetivo.
¿Cómo convertir min cᵀx en maximización equivalente?|max −cᵀx, recuperando después el signo del valor|max cᵀx sin cambiar nada más|max cᵀx multiplicando solo b por −1|Se niega el objetivo; conservarlo o alterar únicamente recursos no representa la misma optimización.
¿Qué ocurre al multiplicar una desigualdad por −1?|Se invierte el sentido|Se conserva el sentido|Se convierte automáticamente en igualdad|El orden se invierte al multiplicar por un número negativo; no aparece una igualdad.
¿Cómo convertir ax ≤ b en igualdad con s ≥ 0?|ax + s = b|ax − s = b|ax + s = 0 siempre|La holgura es b − ax, por eso se suma; restarla corresponde al exceso de una restricción ≥.
¿Cómo convertir ax ≥ b en igualdad con s ≥ 0?|ax − s = b|ax + s = b|ax − s ≤ b|El exceso es ax − b y se resta; conservar desigualdad no produce forma estándar.
¿Qué representa una holgura añadida con signo positivo?|La diferencia entre el límite y el uso|El precio sombra del recurso|Una penalización infinita|La holgura mide recurso sobrante; precio sombra es una variable dual y penalización pertenece al tratamiento de artificiales.
¿Qué representa un exceso en ax − s = b?|Cuánto supera ax el mínimo b|Cuánto recurso máximo sobra siempre|Una variable obligatoriamente negativa|s = ax − b es no negativa y mide superación de un mínimo, no sobrante de un máximo.
¿Cómo representar una variable libre x?|x = u − v, con u,v ≥ 0|x = u + v, con u,v ≥ 0|x = uv, con u,v ≥ 0|La diferencia puede ser positiva o negativa; la suma no y el producto introduce no linealidad.
¿Cómo transformar una variable x ≤ 0 a no negativa?|Usar x = −u, u ≥ 0|Usar x = u, u ≥ 0|Usar x = u²|Negar una no negativa produce una no positiva; las otras opciones cambian el dominio o la linealidad.
¿Cómo expresar ax = b usando solo restricciones ≤?|ax ≤ b y −ax ≤ −b|Solo ax ≤ b|ax ≤ b y ax ≤ −b|Se necesitan ambos sentidos de la igualdad; las otras formulaciones no son equivalentes.
¿Qué restricción expresa x ≥ L con una variable desplazada no negativa?|x = L + u, u ≥ 0|x = L − u, u ≥ 0|x = Lu con u libre|El desplazamiento suma una cantidad no negativa a L; restarla impone una cota superior.
¿Pasar a forma estándar obliga por sí mismo a añadir artificiales?|No; las artificiales ayudan a iniciar Simplex cuando hace falta|Sí, una por cada variable de decisión|Sí, una por cada coeficiente no nulo|Igualdades y no negatividad definen la forma; las artificiales son una herramienta de inicialización.
¿La forma estándar docente permite minimizar directamente?|Sí|No, solo permite maximizar|Solo si todas las variables son binarias|La definición de los apuntes admite max o min; las reglas de costes reducidos deben adaptarse al sentido.
¿Qué caracteriza la forma simétrica de minimización?|min, restricciones ≥ y variables no negativas|min, restricciones ≤ y variables libres|max, restricciones = y variables binarias|La pareja simétrica usa min con ≥ y no negatividad; las otras no corresponden a esa convención.
¿Al añadir holguras, cambia el valor del objetivo original para una misma decisión x?|No, si tienen coeficiente cero|Sí, aumenta en una unidad por holgura|Sí, pasa a ser siempre cero|Las holguras se añaden con coste cero; no alteran el valor económico de x.
¿Una igualdad necesita siempre una holgura para ser igualdad?|No|Sí, una positiva|Sí, una negativa|Ya es una igualdad; puede necesitar artificial para iniciar una base, que es una cuestión distinta.
¿Cambiar correctamente a forma estándar conserva las decisiones factibles originales?|Sí, al proyectar sobre las variables originales|No, elimina siempre soluciones|No, obliga a que todas las decisiones sean enteras|Las auxiliares representan las desigualdades sin alterar las decisiones originales ni imponer integridad.
''',
'grafica': '''
¿Cuál es el primer paso geométrico para resolver una PL con dos variables?|Representar las fronteras y los semiplanos de las restricciones|Evaluar todos los puntos del plano|Invertir siempre una matriz de todas las restricciones|Se dibujan rectas y lados admisibles; no se enumeran infinitos puntos ni se requiere una matriz cuadrada global.
¿Cómo elegir el semiplano de ax + by ≤ d?|Comprobar un punto de prueba que no esté en la recta|Elegir siempre el lado superior|Elegir siempre el lado que excluye el origen|El sentido depende de coeficientes y término independiente; un punto de prueba evita reglas visuales falsas.
¿Qué es la región factible geométricamente?|La intersección de todos los conjuntos admisibles|La unión de todos los semiplanos|Solo la recta del objetivo|Un punto debe cumplir simultáneamente todas las restricciones; la unión exige solo alguna.
¿Qué representa una recta de isobeneficio?|Puntos con el mismo valor del objetivo|Puntos con el mismo consumo de todos los recursos|Puntos necesariamente óptimos|La igualdad cᵀx = k fija el objetivo; no garantiza igual consumo ni optimalidad.
¿Puede un punto de intersección de dos rectas ser infactible?|Sí, si incumple otra restricción|No, toda intersección es factible|Solo si su objetivo es negativo|Ser intersección no verifica las demás restricciones y el signo del objetivo no determina factibilidad.
¿Dónde basta buscar al resolver una PL con región poligonal no vacía y acotada?|En sus vértices|Solo en el origen|Solo en puntos con coordenadas enteras|Una función lineal alcanza un óptimo en algún vértice; el origen puede no ser factible y la PL continua admite fracciones.
¿Qué significa una restricción activa en un punto?|Que se satisface con igualdad|Que tiene precio sombra estrictamente positivo siempre|Que es la única restricción del problema|Actividad expresa saturación geométrica; no garantiza precio sombra positivo ni exclusividad.
¿Qué puede producir infinitos óptimos en una región poligonal?|Un segmento factible completo sobre una recta de objetivo óptimo|Cualquier paralelismo con una recta lejana|La mera existencia de dos variables|El paralelismo debe sostener una cara óptima factible; no basta una restricción cualquiera.
¿Si dos puntos factibles distintos son óptimos de una PL, qué ocurre con su segmento?|Todos sus puntos son factibles y óptimos|Solo el punto medio es factible|Su interior mejora estrictamente el objetivo|Convexidad conserva factibilidad y linealidad conserva el mismo valor objetivo en el segmento.
¿Una región factible vacía tiene vértices óptimos?|No|Sí, al menos el origen|Sí, todos los cruces de rectas|Sin puntos factibles no hay óptimo; el origen o los cruces pueden incumplir restricciones.
¿Una restricción redundante puede dibujarse sin formar un lado de la región?|Sí|No, toda recta dibujada delimita un lado|Solo si su coeficiente del objetivo es cero|Una restricción puede estar implicada por otras y no formar una frontera efectiva; no tiene un coeficiente propio en el objetivo.
¿Qué describe x ≥ 0 en un gráfico de ejes x horizontal e y vertical?|El semiplano a la derecha del eje vertical, incluido el eje|Solo la parte por encima del eje horizontal|Solo la recta horizontal|La no negatividad de x limita la coordenada horizontal; y ≥ 0 limita la vertical.
¿Para comprobar un candidato a óptimo, qué debe verificarse antes de comparar su objetivo?|Su factibilidad|Que ambas coordenadas sean máximas por separado|Que tenga coordenadas estrictamente positivas|Un objetivo alto en un punto prohibido no es una solución; no se maximizan coordenadas independientemente.
¿Al minimizar x sobre x ≥ 2 e y ≥ 0, cuál es el valor óptimo?|2|No existe porque la región es no acotada|0|Todos los puntos con x = 2 son óptimos; la región ilimitada no impide un mínimo finito.
¿Al maximizar x sobre x ≥ 0 e y ≥ 0, qué ocurre?|El objetivo no está acotado|El óptimo es el origen|El problema es infactible|Se puede aumentar x indefinidamente manteniendo factibilidad; el origen no maximiza.
¿Si x ≥ 3 y x ≤ 1, cómo es la región?|Vacía|No acotada y no vacía|Un segmento entre 1 y 3|Ningún valor cumple ambas condiciones simultáneamente.
¿Qué información da la pendiente de una restricción si se despeja y?|La inclinación de su recta frontera|Por sí sola, qué lado es factible|El valor óptimo sin usar el objetivo|La pendiente describe dirección; el signo de la desigualdad determina el lado y el objetivo es necesario para optimizar.
¿Una función objetivo constante sobre toda la región factible no vacía tiene qué soluciones óptimas?|Todos los puntos factibles|Ninguna|Solo el origen|Si no varía el objetivo, todos empatan; el origen ni siquiera tiene que ser factible.
¿El método gráfico habitual en el plano resulta apropiado para cien variables?|No, se utiliza principalmente con dos variables|Sí, dibujando cien ejes en el plano|Sí, si solo hay dos restricciones|La limitación principal del dibujo plano es la dimensión de las variables, no únicamente el número de restricciones.
¿Para una PL en forma estándar con óptimo finito y región no vacía, existe una solución básica factible óptima?|Sí|No, debe ser un punto interior|Solo si todos los recursos sobran|En forma estándar existe un óptimo en un punto extremo; no exige interior ni recursos sobrantes.
''',
'bases': '''
Si A tiene m filas independientes, ¿cuál es el tamaño de una base B?|m × m|n × n siempre|m × n siempre|Se eligen m columnas independientes para formar una matriz cuadrada; A completa no es necesariamente una base.
¿Qué propiedad debe tener B para calcular B⁻¹?|Ser no singular|Tener todas sus entradas positivas|Ser siempre la identidad|La independencia de columnas garantiza inversa; ni positividad de entradas ni identidad son requisitos generales.
¿Cómo se obtiene una solución básica asociada a B?|Fijando no básicas a cero y resolviendo BxB = b|Fijando básicas a cero y eligiendo libres las demás|Maximizando cada variable por separado|La definición fija n − m no básicas a cero y determina las m básicas por el sistema.
¿Qué fórmula calcula los valores básicos?|xB = B⁻¹b|xB = Bᵀc|xB = Ab siempre|Resolver BxB = b da B⁻¹b; las alternativas usan objetos distintos o pueden tener dimensiones incompatibles.
¿Cuándo una solución básica es factible en forma estándar?|Cuando xB ≥ 0|Cuando xB tiene algún componente negativo|Cuando z es positivo|Las igualdades ya se satisfacen; falta verificar no negatividad, no el signo del objetivo.
¿Las variables no básicas valen cuánto en una solución básica?|Cero|Uno necesariamente|El término independiente correspondiente|Fijarlas a cero define la solución básica; no se les asignan recursos ni unos.
¿Toda variable básica tiene que ser estrictamente positiva?|No, puede ser cero|Sí, por definición de base|Solo si la base no es identidad|Una básica cero produce degeneración; la estructura de B no obliga a positividad estricta.
¿Qué es una solución básica factible degenerada?|Una con alguna variable básica igual a cero|Una con alguna variable no básica igual a cero|Una cuya base carece de inversa|Las no básicas ya son cero siempre; singularidad impide que las columnas formen una base.
¿Una base singular define una solución básica mediante B⁻¹b?|No, esa inversa no existe|Sí, si b es positivo|Sí, si el objetivo es cero|La singularidad no se resuelve por elegir b o c especiales; se necesitan columnas independientes.
¿Si hay n columnas y rango m, cuántos subconjuntos de m columnas hay como máximo para intentar bases?|El número combinatorio n sobre m|Exactamente n + m bases válidas|Exactamente n·m bases válidas|El combinatorio cuenta candidatos; algunos pueden ser dependientes y no ser bases válidas.
¿Puede un mismo vértice corresponder a varias bases?|Sí, especialmente con degeneración|No, nunca|Solo si el modelo es infactible|La representación básica puede no ser única aunque el punto geométrico sea el mismo.
¿Una solución básica no factible satisface Ax = b?|Sí, pero viola no negatividad en alguna componente básica|No satisface necesariamente ninguna igualdad|Sí y por eso siempre es óptima|Es básica por construcción del sistema; cumplir igualdades no basta para factibilidad ni optimalidad.
¿Qué relación existe en forma estándar entre vértices y soluciones básicas factibles?|Representan los mismos puntos|Todo punto interior es una solución básica factible|Toda solución factible es un vértice|La equivalencia se refiere a puntos extremos; hay puntos factibles que son combinaciones convexas y no vértices.
¿Qué contiene cB?|Coeficientes del objetivo de las variables básicas, en el orden de B|Valores actuales de las básicas|Costes de todas las restricciones|cB se extrae de c según las columnas de B; xB contiene valores y las restricciones no tienen costes propios en ese vector.
¿Cómo calcular el objetivo en una solución básica?|z = cBᵀxB|z = suma de todas las entradas de B|z = bᵀb siempre|Las no básicas son cero; solo contribuyen sus coeficientes básicos por sus valores.
¿Cambiar el orden de las columnas de B exige qué?|Reordenar coherentemente xB y cB|Cambiar las restricciones del modelo|Cambiar los beneficios originales|El orden es una convención de representación; debe mantenerse consistente sin alterar el problema.
¿Qué problema surge si hay restricciones de igualdad linealmente dependientes y se pretende una base con todas las filas?|No hay m columnas independientes si el rango es menor que m|Las bases se hacen automáticamente más grandes|Toda solución se vuelve necesariamente infactible|Se deben tratar redundancias y rango; la dependencia no implica contradicción ni aumenta el rango.
¿Puede haber más restricciones originales que variables originales y aún aplicarse Simplex?|Sí, tras las transformaciones y el tratamiento del rango|No, cualquier caso así es infactible|Solo si se elimina la función objetivo|Las auxiliares y la independencia efectiva importan; comparar solo cantidades originales no decide factibilidad.
¿Qué significa que B = I al iniciar Simplex?|Que xB = b|Que xB = c siempre|Que el óptimo ya se ha alcanzado|La identidad simplifica los cálculos iniciales, pero no certifica optimalidad.
¿Un punto factible que no es óptimo puede ser básico?|Sí|No, básico significa óptimo|Solo si alguna restricción es no lineal|Simplex recorre soluciones básicas factibles y mejora el objetivo; no todas son óptimas.
''',
'simplex': '''
En maximización con rj = zj − cj, ¿qué variable elige la regla de entrada de clase?|La no básica con rj más negativo|La básica con rj más positivo|La no básica con rj más próximo a cero sin importar el signo|La regla busca la mayor mejora marginal, equivalente al coste reducido más negativo entre no básicas.
¿Qué es yj en el Simplex matricial?|B⁻¹aj|Baj siempre|aj⁻¹b|La columna original aj se transforma con la inversa de la base; una columna no tiene inversa matricial ordinaria.
¿Qué es zj en la convención docente?|cBᵀyj|cj − cBᵀyj|La suma de los recursos|zj mide el efecto sobre contribuciones básicas; el coste reducido es zj − cj, no zj solo.
¿Qué tasa de cambio tiene z al aumentar una no básica xj una unidad manteniendo la base?|cj − zj|zj − cj|Siempre cj sin otro efecto|Las básicas se ajustan; el aumento neto es el opuesto de rj = zj − cj.
¿Qué cocientes se consideran en la regla de salida?|xBi / yij solo cuando yij > 0|Todos, incluidos denominadores negativos|Solo los de denominador cero|Solo las componentes positivas de yj hacen disminuir básicas y limitan el paso.
¿Qué variable sale según el mínimo cociente?|La básica que alcanza cero primero|La no básica con mayor valor|La básica con mayor coste unitario|La salida mantiene factibilidad al aumentar la entrante; no depende directamente del coste de la saliente.
¿Qué expresa θ en un pivote?|El incremento permitido de la variable entrante|El coste reducido de la saliente|El número total de variables|θ es un paso en unidades de la variable, no un coste ni una dimensión.
¿Cómo se actualizan las antiguas variables básicas al aumentar xj en θ?|xB nuevo = xB − yjθ|xB nuevo = xB + bθ|xB nuevo = cB − yjθ|El sistema transformado exige xB = B⁻¹b − B⁻¹aj xj; cB no contiene cantidades.
¿Un pivote puede tener θ = 0?|Sí, en un paso degenerado|No, Simplex exige siempre θ > 0|Solo si B es singular|Una básica cero puede limitar el paso; la base puede seguir siendo invertible.
¿Con θ = 0 y una entrante de mejora, cuánto mejora z en ese pivote?|Nada|Siempre una unidad|Siempre disminuye|La variación es (cj − zj)θ; con paso cero el punto y objetivo no avanzan.
¿Qué se hace tras elegir entrada y salida?|Sustituir una columna de la base y recalcular coherentemente|Eliminar para siempre una restricción del problema|Modificar los beneficios de todos los productos|Un pivote cambia representación básica, no las restricciones ni los datos económicos originales.
¿En una tabla canónica, cuánto valen las columnas de las variables básicas?|Forman la identidad|Son todas cero|Coinciden necesariamente con c|La multiplicación B⁻¹B produce I; las columnas básicas no desaparecen.
¿Cuál es el coste reducido de una variable básica en una tabla coherente?|Cero|Siempre negativo|Siempre uno|Su columna transformada es un vector de la identidad y zj coincide con cj.
¿Simplex primal conserva qué durante sus pivotes factibles?|La factibilidad de las soluciones básicas|La positividad estricta de todas las variables|El mismo conjunto de variables básicas siempre|La regla del cociente mantiene no negatividad; puede haber ceros y la base cambia.
¿Puede la degeneración permitir ciclado con reglas inadecuadas?|Sí|No, cualquier pivote mejora estrictamente|Sí, pero obliga a que el objetivo sea no lineal|Los pasos nulos pueden repetir bases; no requieren no linealidad ni mejora estricta.
¿Qué ayuda a evitar el ciclado en Simplex?|Una regla anticiclado como Bland|Permitir básicas negativas sin control|Escoger denominadores nulos para salir|Una regla anticiclado resuelve empates coherentemente; violar factibilidad o dividir por cero no es válido.
¿Para minimizar directamente con rj = zj − cj, qué signo puede indicar mejora?|rj > 0|rj < 0 como única posibilidad|rj = 0 siempre mejora estrictamente|La variación del objetivo es −rjθ; para disminuirlo se necesita rj positivo y paso positivo.
¿La regla de entrada elige necesariamente la mayor mejora total tras el pivote?|No, compara mejora marginal y el paso puede variar|Sí, porque todos los pasos son iguales|Sí, aunque el paso sea cero|El coste reducido mide mejora por unidad; la mejora total también depende de θ.
¿Un empate en el mínimo cociente obliga a declarar infactibilidad?|No, se aplica una regla de desempate|Sí|Sí, salvo que el objetivo sea cero|El empate puede originar degeneración y no demuestra ausencia de soluciones.
¿Qué efecto tiene un denominador yij < 0 sobre esa básica al aumentar xj?|La básica aumenta|La básica disminuye siempre|La básica se hace inmediatamente negativa|En xBi nuevo = xBi − yijθ, restar una cantidad negativa hace aumentar la básica.
''',
'artificiales': '''
¿Cuál es el propósito de una variable artificial?|Construir una base inicial adecuada para el problema auxiliar|Medir un recurso sobrante real|Imponer integridad a una decisión|La artificial es una herramienta algorítmica; no es recurso físico ni restricción de dominio entero.
¿Toda variable de holgura es una variable artificial?|No|Sí, ambas tienen siempre el mismo coste|Sí, ambas deben valer uno al final|Holguras representan desigualdades y tienen coste cero; artificiales permiten inicializar y se penalizan.
¿Qué coeficiente se asigna a una artificial en maximización con gran M?|−M, con M positivo suficientemente grande|+M|Cero necesariamente|Se penaliza aumentar artificiales en un máximo; +M las premiaría y cero no las penaliza.
¿Qué coeficiente se asigna a una artificial en minimización con gran M?|+M, con M positivo suficientemente grande|−M|El mismo de cualquier holgura, siempre cero|En un mínimo se penaliza con coste positivo; un coste negativo favorecería artificiales.
¿Tener una artificial positiva en una solución intermedia demuestra infactibilidad original?|No|Sí, inmediatamente|Solo si es la primera iteración|Durante la búsqueda pueden quedar artificiales positivas; el diagnóstico requiere terminar correctamente la fase auxiliar.
¿Qué indica un óptimo auxiliar con suma de artificiales estrictamente positiva?|Que el modelo original es infactible|Que el modelo original tiene óptimos alternativos|Que basta redondear las artificiales a cero|No se puede satisfacer el original sin ayuda artificial; redondear no conserva igualdades.
¿Una artificial básica con valor cero demuestra infactibilidad?|No|Sí, por seguir siendo básica|Sí, si el objetivo original es positivo|Importa su valor positivo, no solo pertenecer a la base; una artificial cero puede quedar por degeneración.
¿Introducir artificiales garantiza que el modelo original sea factible?|No; hace factible una formulación auxiliar adecuada|Sí, siempre|Sí, si se usa una M grande numérica|El auxiliar admite soluciones que usan artificiales; estas no son soluciones del original mientras sean positivas.
¿Si ya existe una base factible formada por columnas originales o auxiliares válidas, hace falta identidad para empezar?|No|Sí, B debe ser siempre I|Sí, hay que añadir una artificial por fila|Puede iniciarse con cualquier B invertible cuya solución básica sea no negativa.
¿En una maximización factible sin artificiales positivas, qué certifica rj ≥ 0 para todas las no básicas?|Optimalidad|No acotación|Infactibilidad|No hay dirección básica de mejora; las condiciones de factibilidad y ausencia de artificiales positivas son necesarias.
¿En maximización, qué certifica una entrante con rj < 0 e yj ≤ 0 en una base factible del original?|Objetivo no acotado|Región factible vacía|Solución única|La variable puede crecer sin agotar básicas y mejora el objetivo sin límite.
¿Basta encontrar yj ≤ 0 para cualquier columna y declarar no acotación del objetivo?|No, debe además ser una dirección de mejora|Sí, aunque rj sea positivo|Sí, aunque no haya base factible|Una dirección sin límite de paso debe mejorar el objetivo y partir de factibilidad para certificar no acotación.
¿Si todos los costes reducidos no básicos son estrictamente positivos en un óptimo de maximización factible, qué puede afirmarse?|La solución es única|El problema es infactible|Hay infinitos óptimos necesariamente|Cualquier aumento de no básicas empeora el objetivo; no existe otra solución óptima distinta.
¿Un coste reducido no básico cero prueba siempre otro punto óptimo distinto, incluso con degeneración?|No; puede no permitir desplazamiento positivo|Sí, sin ninguna condición|Sí, y el objetivo mejora estrictamente|Un pivote degenerado puede cambiar base sin cambiar punto; hace falta una dirección factible de paso positivo para otro punto.
¿Si una no básica tiene coste reducido cero y admite paso factible positivo desde un óptimo, qué existe?|Otro punto óptimo|Una mejora estricta|Infactibilidad|El desplazamiento es factible y la variación del objetivo es cero, por tanto hay óptimos distintos.
¿Qué diferencia hay entre base inicial factible y base óptima?|La inicial puede admitir mejoras|Ninguna; toda base factible es óptima|La óptima siempre es identidad|Factibilidad permite empezar, optimalidad exige además el criterio del objetivo; identidad no es condición de optimalidad.
¿Una componente básica negativa en una supuesta iteración de Simplex primal implica por sí sola que el modelo sea infactible?|No, indica que esa base no es factible|Sí, siempre|Sí, salvo que haya holguras|Una elección de base inválida no descarta que otra produzca una solución factible.
¿Debe interpretarse M como permiso para escoger cualquier número pequeño?|No, debe justificar la penalización suficiente o tratarse simbólicamente|Sí, M = 1 siempre sirve|Sí, su signo es irrelevante|Un valor inadecuado puede no expulsar artificiales; sentido del objetivo y escala importan.
¿En un modelo con todas las restricciones ≤, b ≥ 0 y x ≥ 0, qué proporciona la base de holguras?|Una solución inicial factible con x = 0|Una prueba de optimalidad inmediata|Una prueba de infactibilidad|Las holguras valen b ≥ 0; todavía se debe estudiar el objetivo para decidir optimalidad.
¿Que Simplex termine sin costes reducidos de mejora basta para el original si queda una artificial positiva?|No|Sí, siempre|Sí, si hay pocas restricciones|El criterio debe combinarse con eliminación de artificiales; el auxiliar no equivale al original si las necesita positivas.
''',
'dualidad': '''
¿Cuál es el dual de max cᵀx sujeto a Ax ≤ b, x ≥ 0?|min bᵀy sujeto a Aᵀy ≥ c, y ≥ 0|min cᵀy sujeto a Ay ≤ b, y ≥ 0|max bᵀy sujeto a Aᵀy ≤ c, y ≥ 0|Se intercambian b y c, se transpone A y se pasa a minimización con desigualdades ≥.
¿Si el primal tiene n variables y m restricciones, cuántas variables tiene su dual?|m|n siempre|m + n siempre|Cada restricción primal origina una variable dual; cada variable primal origina una restricción dual.
¿Qué matriz aparece en las restricciones duales de la pareja simétrica?|Aᵀ|A⁻¹ siempre|La identidad siempre|La correspondencia entre filas y columnas produce la transpuesta; A puede no ser cuadrada ni invertible.
¿Qué ocurre al dualizar dos veces bajo las convenciones correspondientes?|Se recupera el primal|Se obtiene siempre el opuesto del objetivo primal|Se obtiene un problema sin restricciones|La construcción dual es involutiva; no elimina restricciones ni niega permanentemente el problema.
¿Qué afirma la dualidad débil para primal máximo y dual mínimo factibles?|cᵀx ≤ bᵀy|cᵀx > bᵀy siempre|cᵀx = bᵀy para cualquier par factible|Un dual factible da cota superior al máximo primal; la igualdad no se da en cualquier par.
¿Qué afirma dualidad fuerte si el primal tiene óptimo finito?|El dual tiene óptimo finito con igual valor|El dual es necesariamente infactible|El dual tiene el mismo vector de decisiones|Se igualan valores óptimos, no dimensiones ni necesariamente vectores de soluciones.
¿Si un par primal-dual factible tiene el mismo objetivo, qué se concluye?|Ambas soluciones son óptimas|Solo una es óptima y no puede saberse cuál|Ambas son infactibles|La dualidad débil impide mejorar cualquiera sin romper la cota común.
¿Qué representa económicamente una variable dual óptima de un recurso?|Su precio sombra o valor marginal bajo condiciones de validez|La cantidad sobrante del recurso|El beneficio total de la empresa|El sobrante es holgura y el beneficio total es el valor objetivo; el precio sombra mide sensibilidad marginal.
¿El precio sombra permite predecir cualquier cambio arbitrariamente grande en b?|No, su interpretación requiere el rango de validez pertinente|Sí, sin límite|Sí, si el recurso es activo|La base o estructura óptima puede cambiar; actividad no garantiza validez global de una pendiente local.
¿Cómo calcular una solución dual desde una base primal óptima adecuada?|yᵀ = cBᵀB⁻¹|y = Bc siempre|y = b siempre|La fórmula combina costes básicos y la inversa; ni disponibilidades ni Bc dan en general los precios sombra.
¿En la pareja simétrica, una restricción primal con holgura positiva puede tener precio sombra óptimo positivo?|No, por complementariedad|Sí, necesariamente|Solo si el primal es un máximo|La complementariedad impone yi·si = 0; una holgura positiva obliga a yi = 0.
¿Un precio sombra cero obliga a que su restricción primal tenga holgura positiva?|No, puede estar activa|Sí, siempre|Sí, y además ser redundante|Complementariedad no permite invertir esa implicación; puede haber restricciones activas con multiplicador cero.
¿Si el primal es no acotado, qué ocurre con su dual?|Es infactible|Tiene siempre óptimo cero|Es siempre no acotado también|Un dual factible daría una cota por dualidad débil y contradice la no acotación primal.
¿Si el primal es infactible, qué puede ocurrir con el dual?|Puede ser infactible o no acotado|Debe ser siempre no acotado|Debe tener siempre óptimo finito|La infactibilidad de uno no determina un único estado del otro; ambos pueden ser infactibles.
¿Un dual infactible demuestra siempre que el primal sea no acotado?|No, el primal también puede ser infactible|Sí|Sí, y además factible por definición|Sin conocer factibilidad primal no puede concluirse no acotación a partir de infactibilidad dual.
¿En un primal de máximo con variable libre, qué tipo de restricción dual corresponde a esa variable?|Igualdad|Siempre ≤ estricta|Ninguna restricción|La libertad de signo exige igualdad de la combinación dual correspondiente; no elimina la condición.
¿En un primal de máximo, qué dominio dual corresponde a una restricción de igualdad?|Variable dual libre|Variable dual necesariamente positiva|Variable dual necesariamente binaria|Una igualdad no fija sentido de desigualdad y su multiplicador es libre; no impone integridad.
¿Qué dominio dual corresponde a una restricción ≥ de un primal máximo con la convención general?|Variable dual no positiva|Variable dual binaria|Variable dual estrictamente positiva|En un máximo, ≤ corresponde a y ≥ 0 y ≥ corresponde a y ≤ 0; se puede normalizar cambiando signo.
¿Las soluciones óptimas de primal y dual tienen siempre el mismo número de componentes?|No|Sí|Solo si ambos objetivos son iguales|Las dimensiones dependen de variables y restricciones; igualdad de valores no implica igualdad de dimensiones.
¿Qué debe especificar un cálculo de sensibilidad con un precio sombra?|El recurso, las unidades y la validez de la variación|Solo la letra de la opción correcta|Que el cambio siempre es ilimitado|La interpretación requiere significado económico y rango de validez; no es una fórmula global sin hipótesis.
''',
'redes': '''
¿Qué representa xij en un modelo de transporte típico?|Cantidad enviada del origen i al destino j|Precio unitario de ese envío|Capacidad total del destino|Las cantidades son decisiones; cij es coste y demanda o capacidad son datos.
¿Cuál es el objetivo habitual del transporte de coste mínimo?|Minimizar Σ cij·xij|Minimizar Σ xij²|Maximizar siempre cada envío|El coste lineal suma coste unitario por cantidad; el cuadrado no corresponde al modelo lineal descrito.
¿Qué limita la suma de envíos desde un origen con capacidad ai?|Σj xij ≤ ai|Σj xij ≥ ai necesariamente|Cada xij = ai necesariamente|Una capacidad máxima limita el total de salida; no obliga a agotarla salvo condición adicional.
¿Cómo modelar demanda mínima bj en un destino?|Σi xij ≥ bj|Σi xij ≤ bj|Σj xij ≥ ai|Se suman entradas de todos los orígenes a un destino; un máximo permitiría no satisfacer demanda.
¿Qué caracteriza una red de transporte origen-destino?|Una estructura bipartita de orígenes y destinos|Un único ciclo obligatorio|Una variable binaria por cada litro necesariamente|Las decisiones típicas son cantidades entre ambos grupos; no requieren ciclo ni binariedad por unidad.
¿Qué significa transporte equilibrado con satisfacción exacta?|Oferta total igual a demanda total|Cada origen tiene un único destino|Todos los costes son iguales|El equilibrio compara totales, no obliga a una única conexión ni a igualdad de costes.
¿Si la demanda total mínima supera toda la capacidad disponible sin otras fuentes, qué ocurre?|El modelo de transporte es infactible|El coste óptimo es cero|Se arregla cambiando solo la función objetivo|No hay suficiente cantidad para satisfacer demandas; optimizar otro objetivo no crea capacidad.
¿La variable de asignación xij indica normalmente qué?|Si el individuo i recibe la tarea j|Cuántos litros transporta el individuo i|El precio sombra del individuo|Es una decisión 0-1 de emparejamiento; no una cantidad de fluido ni un multiplicador dual.
¿Qué dominio tiene la formulación binaria habitual de asignación?|xij ∈ {0,1}|xij ≤ 0 siempre|xij libre sin límites|La binaria representa elegir o no una pareja; los otros dominios no expresan esa decisión.
¿Qué restricción asigna exactamente una tarea al individuo i?|Σj xij = 1|Σj xij ≤ 0|Σi xij = 0 para todo destino|La suma de las decisiones de ese individuo sobre tareas debe ser uno.
¿Qué restricción garantiza un individuo por tarea j?|Σi xij = 1|Σj xij = 0|Σi xij ≥ 0 únicamente|Se suman individuos para una tarea fija y se exige exactamente uno; no basta no negatividad.
¿Si hay tres personas y cuatro tareas y cada persona y tarea exige exactamente una asignación sin auxiliares, qué ocurre?|Es infactible|Siempre hay asignación perfecta|Se resuelve dejando una tarea sin asignar aunque la igualdad lo prohíba|Las sumas de ambas familias exigirían simultáneamente tres y cuatro asignaciones.
¿Asignar con coste mínimo significa escoger para cada persona su tarea más barata independientemente?|No, las elecciones compiten por tareas|Sí, siempre|Sí, aunque dos personas elijan la misma tarea|Las restricciones de unicidad acoplan las decisiones y pueden impedir preferencias individuales simultáneas.
¿En un camino mínimo binario, qué significa xij = 1?|Que el arco i→j se selecciona|Que su coste es una unidad|Que el arco no existe|La selección es una decisión y no describe el coste ni crea arcos ausentes.
¿Qué es un arco dirigido?|Una conexión con origen y destino ordenados|Una conexión que siempre puede recorrerse en ambos sentidos|Un recurso necesariamente entero|i→j y j→i son arcos diferentes; la dirección no determina dominios de recursos.
¿En balance salidas menos entradas, qué valor corresponde a un origen de una unidad de flujo?|1|−1|0 en todos los nodos|El origen genera una unidad neta; el destino consume una y los intermedios conservan flujo.
¿En ese mismo balance, qué valor corresponde al destino final?|−1|1|El coste del camino|El destino recibe una unidad neta, así que salidas menos entradas vale −1.
¿Qué balance debe cumplir un nodo intermedio de un camino de flujo unitario?|Salidas menos entradas = 0|Salidas menos entradas = 1|Todas sus salidas son obligatoriamente seleccionadas|El nodo no crea ni consume flujo; no obliga a seleccionar todos sus arcos.
¿En un camino mínimo con costes no negativos, añadir un ciclo de coste positivo mejora el objetivo?|No|Sí, siempre|Solo si hay más de dos nodos|El ciclo añade coste sin ayudar a conectar origen y destino; número de nodos no cambia ese hecho.
¿Qué distingue transporte de asignación en sus variables habituales?|Transporte decide cantidades y asignación decide parejas 0-1|Ambos exigen siempre exactamente una unidad en cada arco|Transporte nunca usa restricciones de capacidad|La estructura y dominio cambian; el transporte admite cantidades y capacidades.
''',
'entera': '''
¿Qué caracteriza la programación entera pura?|Todas las variables de decisión están sujetas a integridad|Todas las variables son libres|Solo una variable es entera y todas las demás continuas|Pura impone integridad a todas las decisiones; no describe un modelo mixto.
¿Qué caracteriza la programación entera mixta?|Hay variables enteras y variables continuas|Todas las variables son binarias|No hay ninguna variable entera|El modelo mixto combina dominios; no es binario puro ni continuo puro.
¿Qué dominio tiene una variable binaria?|{0,1}|Todos los reales entre 0 y 1 necesariamente enteros por sí mismos|Todos los enteros no negativos|Una binaria solo tiene dos valores; el intervalo continuo y los enteros no negativos son conjuntos mayores.
¿Qué hace la relajación lineal de un modelo entero?|Retira la integridad conservando restricciones lineales y cotas|Elimina todas las restricciones|Redondea las variables|La relajación amplía dominios; no borra el modelo ni redondea soluciones.
¿En maximización entera, el óptimo relajado finito da qué cota?|Superior al óptimo entero|Inferior necesariamente|Ninguna relación|El conjunto relajado contiene al entero, por lo que su máximo no es menor.
¿En minimización entera, el óptimo relajado finito da qué cota?|Inferior al óptimo entero|Superior necesariamente|Siempre igual a cero|Al ampliar el conjunto, el mínimo puede bajar; no tiene un valor fijo universal.
¿Una solución entera factible de un máximo proporciona qué?|Una cota inferior y un candidato incumbente|Una cota superior garantizada|Una prueba automática de óptimo global|Su valor es alcanzable, pero otros candidatos podrían mejorarla.
¿Cómo ramificar una variable entera con valor relajado 3,4?|x ≤ 3 y x ≥ 4 en ramas distintas|x ≤ 3,4 y x ≥ 3,4|x = 3,4 en ambas ramas|Suelo y techo separan todos los valores enteros posibles y excluyen la fracción actual.
¿Qué ocurre al ramificar añadiendo restricciones?|Se crean subregiones del conjunto actual|Se cambia necesariamente el objetivo|Se eliminan todas las restricciones previas|Las ramas mantienen el objetivo y las condiciones previas y añaden límites.
¿Cuándo se puede podar un nodo de maximización por cota?|Si su cota superior no supera al incumbente|Si su cota superior es mayor que el incumbente|Siempre que su solución tenga una fracción|Una cota que no mejora elimina la posibilidad de superar el mejor valor conocido; una fracción suele motivar ramificación.
¿Qué se hace con un nodo cuya relajación es infactible?|Se poda|Se redondea su solución|Se declara siempre infactible todo el árbol|El nodo no contiene solución entera, pero otros nodos aún pueden contenerla.
¿Si una relajación de nodo tiene óptimo entero, qué se hace normalmente?|Se considera como candidato y se cierra ese nodo|Se ramifica obligatoriamente en una variable fraccionaria|Se descarta siempre como infactible|El óptimo relajado entero es válido para el nodo y no hay fracción en la que ramificar.
¿Qué significa explorar en profundidad?|Continuar por descendientes antes de otras ramas pendientes|Elegir siempre el nodo de menor profundidad|Cambiar el objetivo en cada nivel|Profundidad es una estrategia de selección de nodos, no una modificación del modelo.
¿La primera solución entera encontrada es necesariamente óptima global?|No|Sí, siempre en profundidad|Sí, si sus variables son binarias|Hace falta cerrar o acotar los restantes nodos; ni profundidad ni binariedad bastan.
¿Con binaria y y producción 0 ≤ x ≤ U, qué modela x ≤ Uy?|Si y = 0, x = 0|Si y = 1, x debe ser U|Si x = 0, y debe ser 0|La restricción desactiva producción cuando y = 0; no fuerza capacidad plena ni la implicación inversa.
¿Qué modela x1 + x2 ≤ 1 con ambas binarias?|A lo sumo una decisión activa|Exactamente una activa|Al menos una activa|También se permite (0,0); igualdad modelaría exactamente una y ≥ modelaría al menos una.
¿Qué modela x1 + x2 = 1 con ambas binarias?|Exactamente una decisión activa|Ambas activas|Ninguna activa|Las únicas combinaciones son (1,0) y (0,1); ni suma dos ni suma cero son válidas.
¿Qué modela x1 ≤ x2 con ambas binarias?|Si x1 = 1, entonces x2 = 1|Si x2 = 1, entonces x1 = 1|Ambas deben ser cero|Se excluye (1,0), pero se permite (0,1), de modo que la implicación inversa no vale.
¿Una M en una condición lógica debería elegirse cómo?|A partir de cotas válidas de las variables|Siempre como un millón sin justificar|Como una variable binaria adicional|Una cota suficiente mantiene equivalencia; una cifra arbitraria puede ser insuficiente o empeorar el cálculo.
¿Para modelar exactamente un umbral estricto en una cantidad continua basta sustituir > por ≥ sin más?|No, hay que tratar explícitamente el umbral y sus hipótesis|Sí, ambas relaciones son idénticas|Sí, añadir una holgura lo resuelve siempre|La igualdad pertenece a ≥ y no a >; para cantidades enteras se usa separación de una unidad, no así para continuas sin hipótesis.
'''
}
questions=[]
for topic,block in DATA.items():
 rows=[l.split('|') for l in block.strip().splitlines()]
 assert len(rows)==20,(topic,len(rows))
 for i,(prompt,correct,w1,w2,explanation) in enumerate(rows,1):
  questions.append({'id':f'{topic}-{i:03}','topic':topic,'difficulty':1 if i<=10 else 2,'prompt':prompt,
  'options':[{'id':'c','text':correct},{'id':'a','text':w1},{'id':'b','text':w2}], 'correctId':'c',
  'explanation':explanation,'rationales':{'c':'Correcta. '+explanation,'a':'Incorrecta. '+explanation,'b':'Incorrecta. '+explanation},
  'reference':f'Guía, apartado {TOPICS[topic][1]}','kind':'concepto'})

def add(topic,i,prompt,answer,w1,w2,explanation):
 assert len({str(answer),str(w1),str(w2)})==3,(prompt,answer,w1,w2)
 questions.append({'id':f'calculo-{topic}-{i:03}','topic':topic,'difficulty':2 if i%4 else 3,'prompt':prompt,
 'options':[{'id':'c','text':str(answer)},{'id':'a','text':str(w1)},{'id':'b','text':str(w2)}], 'correctId':'c',
 'explanation':explanation,'rationales':{k:('Correcta. ' if k=='c' else 'Incorrecta. ')+explanation for k in ['c','a','b']},
 'reference':f'Guía, apartado {TOPICS[topic][1]}','kind':'calculo'})
# Diez familias, cuatro tareas diferentes por familia, cuatro instancias por tarea.
for k in range(1,17):
 mode=(k-1)%4; a=k+2; b=k+4
 if mode==0:
  add('fundamentos',k,f'Si z = {a}x + {b}y y (x,y) = (2,3), ¿cuánto vale z?',2*a+3*b,a+b,3*a+2*b,f'Sustituir: z = {a}·2 + {b}·3 = {2*a+3*b}. No se suman solo los coeficientes ni se intercambian las cantidades.')
 elif mode==1:
  add('fundamentos',k,f'La venta por unidad es {10+a} € y el coste {a} €. Si se venden {b} unidades, ¿qué beneficio se obtiene?',10*b,(10+a)*b,(10+2*a)*b,f'El margen es (10 + {a}) − {a} = 10 €/unidad; el beneficio es 10·{b} = {10*b} €, no ingresos ni venta más coste.')
 elif mode==2:
  add('fundamentos',k,f'Para (x,y) = (1,2), ¿cuánta holgura tiene {a}x + y ≤ {a+7}?',5,7,a+7,f'El uso es {a}+2 y el límite {a+7}; la diferencia es 5. El término independiente no es la holgura.')
 else:
  add('fundamentos',k,f'¿Cuál es el mayor valor de z = {a}x sobre 0 ≤ x ≤ {b}?',a*b,b,0,f'El coeficiente {a} es positivo: conviene x = {b}, y z = {a*b}; x y z son magnitudes diferentes.')
 if mode==0:
  add('modelos',k,f'Cada producto consume {a} kg y hay {a*b} kg disponibles. ¿Cuál es la capacidad máxima continua?',f'{b} unidades',f'{a*b} unidades',f'{a} unidades',f'{a}x ≤ {a*b} implica x ≤ {b}; no se confunde consumo por unidad con disponibilidad.')
 elif mode==1:
  add('modelos',k,f'Cada trabajador aporta {a} horas y hay {b} trabajadores intercambiables. ¿Cuál es la capacidad total?',f'{a*b} horas',f'{a+b} horas',f'{a} horas',f'Se suman {b} aportaciones de {a} horas: {a*b}; ni sumar los dos números ni contar solo uno calcula el total.')
 elif mode==2:
  add('modelos',k,f'Se exige que y sea al menos {a} veces x. Si x = {b}, ¿cuál es el mínimo y?',a*b,a+b,b,f'y ≥ {a}x y x = {b} implican y ≥ {a*b}; se multiplica, no se suma.')
 else:
  add('modelos',k,f'Se desea que x sea al menos el 25 % de x + y. Si y = {3*b}, ¿cuál es el mínimo x continuo?',b,3*b,4*b,f'x ≥ 0,25(x+{3*b}) lleva a 0,75x ≥ {0.75*b:g}; por tanto x ≥ {b}. El porcentaje se aplica al total.')
 if mode==0:
  add('formas',k,f'¿Cómo estandarizar {a}x ≤ {b} con s ≥ 0?',f'{a}x + s = {b}',f'{a}x − s = {b}',f'{a}x + s ≥ {b}',f'Una cota superior se convierte sumando s no negativa y usando igualdad; restar s expresaría una cota inferior.')
 elif mode==1:
  add('formas',k,f'Al multiplicar −{a}x ≥ −{a*b} por −1, ¿qué se obtiene?',f'{a}x ≤ {a*b}',f'{a}x ≥ {a*b}',f'{a}x = {a*b}',f'Se cambian todos los signos y se invierte ≥ a ≤; no se crea una igualdad.')
 elif mode==2:
  add('formas',k,f'Se resuelve min f con max g = −f y se obtiene g* = −{a*b}. ¿Cuál es f*?',a*b,-a*b,0,f'Como g = −f, al recuperar el objetivo original f* = −g* = {a*b}.')
 else:
  add('formas',k,f'¿Cómo expresar x ≥ {b} con una nueva variable u ≥ 0?',f'x = {b} + u',f'x = {b} − u',f'x = u − {b}',f'La cantidad adicional sobre el mínimo {b} debe sumarse; las otras expresiones no garantizan esa cota inferior.')
 if mode==0:
  add('grafica',k,f'Max z = {a}x + y, con x + y ≤ {b}, x,y ≥ 0. ¿Qué punto es óptimo?',f'({b},0)',f'(0,{b})','(0,0)',f'En los vértices los objetivos son {a*b}, {b} y 0. Como {a}>1, conviene dedicar todo a x.')
 elif mode==1:
  add('grafica',k,f'Se maximiza z = x + y sobre x + y ≤ {b}, x,y ≥ 0. ¿Dónde se alcanza el óptimo?',f'En todo el segmento x+y={b} del primer cuadrante','Solo en el origen',f'Solo en ({b},0)',f'El máximo es {b}; todos los puntos no negativos de esa recta tienen ese mismo valor, incluidos ambos extremos.')
 elif mode==2:
  add('grafica',k,f'Con x ≥ {b} y x ≤ {a}, siendo {b}>{a}, ¿cómo se clasifica el problema?', 'Infactible','Siempre óptimo único','Objetivo necesariamente no acotado',f'Los límites son incompatibles: no hay x entre un mínimo {b} y un máximo {a}.')
 else:
  add('grafica',k,f'Min z = x, con x ≥ {a}, y ≥ {b}. ¿Qué describe su óptimo?',f'z*={a}, con infinitos óptimos', 'No tiene óptimo por región no acotada',f'z*={b}, único',f'La mínima x es {a}; cualquier y ≥ {b} conserva el objetivo. La región no acotada admite óptimo finito.')
 if mode==0:
  add('bases',k,f'En forma estándar hay {a} ecuaciones independientes y {a+b} variables totales. ¿Cuántas no básicas tiene una base?',b,a,a+b,f'Hay m={a} básicas y n−m=({a+b})−{a}={b} no básicas. Se cuentan las variables totales tras transformar.')
 elif mode==1:
  add('bases',k,f'B es diagonal con entradas (2,3) y b = ({2*a},{3*b}). ¿Cuál es xB?',f'({a},{b})',f'({2*a},{3*b})',f'({4*a},{9*b})',f'Se resuelve 2xB1={2*a} y 3xB2={3*b}: xB=({a},{b}). No se usa b sin invertir ni se multiplica por B.')
 elif mode==2:
  add('bases',k,f'Una solución básica tiene xB = (0,{a},{b}). ¿Cómo se clasifica en forma estándar?', 'Factible y degenerada','Infactible por el cero','No degenerada por tener dos positivos',f'Todas las básicas son no negativas y una es cero: factible y degenerada. Una sola básica cero basta.')
 else:
  add('bases',k,f'Una base invertible da xB = ({a},−{b}). ¿Qué puede afirmarse de esa solución básica?', 'No es factible','Es factible porque B tiene inversa','El modelo completo es necesariamente infactible',f'La segunda básica es negativa: esta base no es factible. La invertibilidad no asegura no negatividad y otra base podría ser factible.')
 if mode==0:
  add('simplex',k,f'Maximización, costes r = z−c de no básicas: x1: −{a}, x2: −{b}, x3: 0. ¿Quién entra por la regla de clase?','x2','x1','x3',f'Como −{b} < −{a} < 0, x2 tiene el coste reducido más negativo; cero no mejora marginalmente.')
 elif mode==1:
  add('simplex',k,f'xB = ({2*a},{3*b}), yj = (2,3). ¿Qué paso máximo permite la regla de salida?',a,b,a+b,f'Los cocientes son {2*a}/2={a} y {3*b}/3={b}. Se elige el menor, {a}, para preservar no negatividad.')
 elif mode==2:
  add('simplex',k,f'En max, rj = −{a} y el paso es θ = {b}. ¿Cuánto aumenta z?',a*b,-a*b,a,f'Δz = −rj·θ = {a}·{b} = {a*b}. El signo del aumento es opuesto al coste reducido y se multiplica por el paso.')
 else:
  add('simplex',k,f'Una básica vale {a}, su yij = −2 y la entrante aumenta {b}. ¿Cuál es el nuevo valor de esa básica?',a+2*b,a-2*b,a+b,f'xBi nuevo = {a} − (−2)·{b} = {a+2*b}. Una componente negativa en y hace aumentar la básica.')
 if mode==0:
  add('artificiales',k,f'Max, base factible del original, rj = −{a}, yj = (0,−{b}). ¿Qué se detecta?','Objetivo no acotado','Infactibilidad','Óptimo único',f'Hay mejora porque rj<0 y ninguna componente positiva de yj limita el paso. Se puede crecer indefinidamente.')
 elif mode==1:
  add('artificiales',k,f'Una fase I correctamente resuelta termina con mínimo de suma de artificiales igual a {a}. ¿Qué se concluye?','Original infactible','Original óptimo con beneficio '+str(a),'Hay que aceptar las artificiales como recursos',f'El mínimo {a}>0 significa que no se pueden hacer cero todas las artificiales: el original es infactible.')
 elif mode==2:
  add('artificiales',k,f'En un óptimo de max, factible para el original, todas las no básicas tienen rj ≥ {a}>0. ¿Qué se certifica?','Óptimo único','Infinitos óptimos necesariamente','Objetivo no acotado',f'Los costes reducidos son estrictamente positivos, así que todo cambio con no básicas positivas empeora el objetivo.')
 else:
  add('artificiales',k,f'Una artificial básica vale 0 y otras básicas valen {a} y {b}. ¿La artificial demuestra infactibilidad?','No, su valor cero no la demuestra','Sí, por estar en la base','Sí, porque las otras básicas son positivas',f'El criterio de infactibilidad exige artificial positiva en el óptimo auxiliar, no la mera presencia de una artificial básica cero.')
 if mode==0:
  add('dualidad',k,f'Un primal tiene {a} variables y {b} restricciones. ¿Qué dimensiones tendrá el dual?',f'{b} variables y {a} restricciones',f'{a} variables y {b} restricciones',f'{a+b} variables y {b} restricciones',f'Cada restricción primal da una variable dual y cada variable primal una restricción dual; se intercambian los recuentos.')
 elif mode==1:
  add('dualidad',k,f'Un precio sombra es {a} €/unidad. Aumenta un recurso {b} unidades dentro del rango de validez. ¿Cuál es el cambio previsto en z?',f'{a*b} €',f'{a+b} €',f'{a} €',f'Δz = yi·Δbi = {a}·{b} = {a*b} €. Se multiplica el valor unitario por la variación, bajo la hipótesis del rango.')
 elif mode==2:
  add('dualidad',k,f'Una solución primal de máximo factible vale {a} y una dual de mínimo factible vale {a}. ¿Qué se sabe?','Ambas son óptimas','El primal aún debe mejorar estrictamente','El dual es infactible',f'La igualdad de los valores factibles cierra la brecha de dualidad: ningún primal puede superar la cota dual {a}.')
 else:
  add('dualidad',k,f'En un óptimo primal-dual simétrico, una holgura primal vale {b}>0. ¿Cuánto vale su variable dual?',0,b,a,f'Complementariedad exige yi·{b}=0; como la holgura es positiva, yi=0. No se iguala el multiplicador a la holgura.')
 if mode==0:
  add('redes',k,f'Un transporte tiene {a} orígenes y {b} destinos, todos conectados. ¿Cuántas variables xij necesita?',a*b,a+b,a,f'Hay una cantidad por pareja origen-destino, {a}·{b}={a*b}; no solo una por origen ni por nodo.')
 elif mode==1:
  add('redes',k,f'Un origen de capacidad {a+b} ya envía {a} unidades a un destino. ¿Cuánto puede enviar como máximo a otro?',b,a+b,a,f'La suma no puede superar {a+b}; restan {a+b}−{a}={b} unidades de capacidad.')
 elif mode==2:
  add('redes',k,f'Los costes de asignar dos personas a dos tareas son [[{a},1],[2,{b}]]. ¿Qué coste mínimo tiene la asignación perfecta?',3,a+b,1,f'Hay dos permutaciones: diagonal cuesta {a+b} y cruzada 1+2=3. Como {a+b}>3, la cruzada es óptima; elegir un único arco no asigna ambas personas.')
 else:
  add('redes',k,f'Un nodo intermedio recibe {a} unidades de flujo y ya envía {a-1}. ¿Cuánto debe enviar por su único arco de salida restante?',1,0,a,f'Conservación: entradas = salidas. Faltan {a}−{a-1}=1; no puede acumular una unidad ni volver a enviar todas.')
 if mode==0:
  add('entera',k,f'En un máximo entero, incumbente = {a} y cota superior de un nodo = {a-1}. ¿Qué procede?','Podar por cota','Actualizar incumbente a '+str(a-1),'Ramificar siempre',f'Ni el mejor punto del nodo superaría {a}; se poda sin empeorar el incumbente a {a-1}.')
 elif mode==1:
  add('entera',k,f'Una variable entera toma {a},6 en el óptimo relajado. ¿Qué ramas la separan correctamente?',f'x ≤ {a} y x ≥ {a+1}',f'x ≤ {a} y x ≥ {a+2}',f'x = {a},6 en ambas',f'Suelo={a}, techo={a+1}; excluir {a+1} perdería posibles soluciones enteras y mantener la fracción no ramifica correctamente.')
 elif mode==2:
  add('entera',k,f'Con producción entera 0 ≤ x ≤ {a+b} y binaria y, se exige y=1 si y solo si x≥{a}. ¿Qué límite superior fuerza x≤{a-1} cuando y=0?',f'x ≤ {a-1} + {b+1}y',f'x ≤ {a} + {b}y',f'x ≤ {a+b} siempre',f'Con y=0 debe quedar x≤{a-1}; con y=1 se permite hasta {a+b}. Se combina además con x≥{a}y para el si y solo si.')
 else:
  add('entera',k,f'Un mínimo entero tiene una solución entera factible de valor {b} y cota inferior de un nodo {b+1}. ¿Qué procede?','Podar el nodo','Actualizar la mejor solución a '+str(b+1),'Declarar todo el problema infactible',f'El nodo no puede bajar de {b+1}, que ya es peor que {b}; se poda, sin sustituir una solución mejor ni descartar otros nodos.')
assert len(questions)==360,len(questions)
assert len({q['prompt'] for q in questions})==360
# Los simulacros tienen dos preguntas de cada tema, sin repetir preguntas.
exam=[]
for e in range(3):
 ids=[]
 for ti,topic in enumerate(TOPICS):
  pool=[q for q in questions if q['topic']==topic and q['kind']=='concepto']
  ids.append(pool[e*2]['id'])
  if (ti+e)%5<3:
   ids.append([q for q in questions if q['topic']==topic and q['kind']=='calculo'][e]['id'])
  else:
   ids.append(pool[e*2+1]['id'])
 random.Random(920+e).shuffle(ids)
 exam.append(ids)
(ROOT/'study/questions.json').write_text(json.dumps({'topics':{k:v[0] for k,v in TOPICS.items()},'questions':questions,'pdfExams':exam},ensure_ascii=False,indent=2))
print('Banco:',len(questions),'preguntas; conceptos: 200; cálculos: 160; simulacros: 3 × 20')
