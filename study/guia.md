# Programación lineal
## Guía de estudio para Heurística y Optimización
Teoría desde cero · ejercicios resueltos · práctica autónoma · tres simulacros

Preparada a partir del material de la asignatura y de los parciales y recopilaciones de test aportados. Curso 2026–2027.

Objetivo: que puedas explicar por qué una respuesta es correcta, reconocer las trampas y resolver los cálculos que se esconden detrás de las opciones.

**Cómo usarla.** Sigue la ruta de tres o seis días. Estudia cada procedimiento con lápiz, tapa la solución e intenta reproducirlo. Después pasa a los ejercicios propuestos y a los simulacros. Una respuesta acertada por descarte sin entender la razón cuenta como pendiente de repaso.

**Convención principal.** En maximización se usa rⱼ = zⱼ − cⱼ. Una rⱼ negativa indica mejora marginal. No mezcles esta convención con libros que llaman coste reducido a cⱼ − zⱼ.

**Lectura matemática.** xᵀ significa transpuesta; B⁻¹, inversa; ≥ incluye la igualdad; x ∈ ℤ significa entero; x ∈ {0,1}, binario. Un asterisco identifica un óptimo: x*, z*. Los subíndices i y j numeran filas y columnas; B identifica las variables básicas. Así, rⱼ se lee «coste reducido de la variable j» y xB es el vector de valores básicos.

La guía no presupone duración ni penalización del examen. La ruta distingue el tiempo de aprendizaje del tiempo que después conviene dedicar a practicar bajo las condiciones reales.

Documento de estudio personal. Las preguntas nuevas se han redactado para comprobar comprensión, sin dar por oficiales las respuestas marcadas en recopilaciones de terceros.
---PAGE---
# Índice
[[CONTENTS]]
---PAGE---
# 01. Ruta intensiva de tres o seis días
## Tres días: entender, practicar, comprobar
**Día 1.** Fundamentos, modelización, formas y gráfica: apartados 03–06. Resuelve los cuatro parciales R01–R04 sin mirar el resultado. Debes distinguir ingresos de beneficios, traducir «al menos» y porcentajes, dibujar semiplanos y descartar intersecciones infactibles.

**Día 2.** Bases, Simplex, artificiales y dualidad: apartados 07–12. Trabaja R05–R09 y R15–R16. Repite una iteración calculando B, B⁻¹b, yⱼ, rⱼ, cocientes y objetivo. Después explica qué certifica cada caso de terminación.

**Día 3.** Redes, binarias y programación entera: apartados 13–15. Haz R10–R14. Revisa las confusiones del apartado 16, resuelve al menos ocho propuestos y realiza los tres simulacros separados por sesiones de corrección. Para cada fallo escribe la regla que faltaba, no solo la letra correcta.

## Seis días: repartir el esfuerzo
Día 1: 03–05 y R01–R02. Día 2: 06–07 y R03–R05. Día 3: 08–10 y R06–R07, R15–R16. Día 4: 11–12 y R08–R09. Día 5: 13–15 y R10–R14. Día 6: propuestos pendientes, simulacros y formulario.

**Prioridad alta.** Formas, básicas frente a no básicas, holgura frente a artificial, entrada y salida, signos de rⱼ, factibilidad frente a optimalidad, dualidad y cotas de ramificación. Aparecen reiteradamente en las recopilaciones; esa repetición no demuestra por sí sola que vayan a salir.

**Prioridad práctica.** Modelización, gráfica y estándar aparecen en los cuatro parciales de problemas aportados. En un test pueden preguntarse como un cálculo de vértice, una restricción correcta o el valor objetivo, sin pedir el desarrollo completo.
---PAGE---
# 02. Cómo estudiar y responder un test
## Un protocolo de cuatro preguntas
Antes de operar: ¿es máximo o mínimo?, ¿qué variables y dominios hay?, ¿qué convención de coste reducido se usa?, ¿se presupone factibilidad? Muchas opciones solo son ciertas si se cumplen esas condiciones.

**Lee cuantificadores.** «Siempre», «necesariamente», «solo» y «si y solo si» son fuertes. Un contraejemplo basta para refutar una afirmación universal. «Puede ocurrir» exige un ejemplo, no que ocurra siempre.

**Comprueba dimensiones y unidades.** Si B tiene m filas independientes, B es m × m; b es m × 1 y c tiene una entrada por variable. Un beneficio marginal tiene unidades monetarias por recurso, no unidades sobrantes.

**No memorices letras.** Formula primero la regla y luego busca la opción. Si al barajar las respuestas dudas, probablemente recuerdas la posición en lugar del concepto.

## ¿Responder o dejar en blanco?
Sean A los puntos por acierto, P > 0 la pérdida por fallo y cero por blanco. Si estimas una probabilidad p de acertar, el valor esperado de responder es pA − (1−p)P. Es positivo si:

> p > P / (A + P)

Con tres opciones al azar, p = 1/3. Si A = 1 y P = 0,5, el valor esperado es cero; con dos opciones plausibles y p = 1/2 es positivo. Es un análisis condicionado a esas reglas, no la norma confirmada de tu examen. Si no hay penalización y no existe otro coste, conviene responder todo.

**Al corregir.** Clasifica el fallo como definición, signo, modelización, cálculo o lectura. Repite una pregunta equivalente cambiando datos. Un acierto por suerte también necesita revisión.

**Comprobación rápida.** Sustituye opciones numéricas en las restricciones, descarta dimensiones imposibles y verifica el signo de la mejora. En un máximo, una solución factible da un valor alcanzable, no una cota superior global por sí sola.
---PAGE---
# 03. Fundamentos: qué problema estamos resolviendo
## Datos, decisiones y preferencias
Un problema de optimización elige decisiones x dentro de un conjunto factible F y busca el mejor valor de una función z(x). En programación lineal continua el objetivo y las expresiones de las restricciones son lineales o afines, y las variables pueden tomar valores reales de su dominio.

> max/min z = cᵀx, sujeto a restricciones lineales y dominios

**Ejemplo mínimo.** x son mesas e y son sillas; cada mesa deja 30 € y cada silla 10 €. Si consumen 3 y 1 horas y hay 12 horas: max z = 30x + 10y; 3x + y ≤ 12; x,y ≥ 0. Sin integridad, se permiten fracciones. Si exiges unidades completas, debes imponerla expresamente.

**Linealidad.** 2x + 3y ≤ 8 y 2x + y + 1 = 3 son restricciones lineales. xy ≤ 8, x² + y ≤ 8 y x/y ≤ 2 con denominador variable no son expresiones lineales tal como están escritas. Multiplicar una variable por una constante sí es lineal. Una constante puede trasladarse al término independiente.

**Notación matricial.** A contiene coeficientes tecnológicos; b, términos independientes o recursos; c, costes o beneficios unitarios; x, decisiones. Con m restricciones y n variables, A tiene dimensión m × n. El producto cᵀx es un escalar.

**Factible** significa cumplir todas las restricciones y dominios. **Óptima** significa además que ninguna otra factible mejora el objetivo. Un punto con objetivo muy alto pero que consume más recursos de los disponibles no es una solución admisible.

## No confundas
El objetivo dice qué se desea; las restricciones, qué se permite. Una solución positiva no tiene por qué ser factible. Una solución factible no tiene por qué ser óptima. La programación lineal no promete un óptimo si el problema es infactible o tiene objetivo no acotado.

**Autocomprobación.** ¿3x − 2y + 5 = 0 es lineal? Sí. ¿x ≥ 0 implica que x es entero? No. ¿Qué componente almacena los beneficios? c.
---PAGE---
# 04. Modelización: del texto a las ecuaciones
## Procedimiento reutilizable
1. Define qué representa cada variable, sus unidades y su dominio. No elijas «beneficio» como variable de producción si necesitas decidir cantidades de producto.
2. Escribe el objetivo en unidades coherentes. Beneficio unitario = precio de venta − coste unitario, si ambos datos se proporcionan.
3. Construye una restricción por condición: suma de consumos, disponibilidad, mínimos, proporciones o relaciones entre productos.
4. Verifica el modelo con una decisión sencilla. ¿Permite producir cero cuando se exige un mínimo? ¿La cantidad total consume las unidades correctas?

**Diccionario.** «Al menos L» → ≥ L. «Como máximo U» → ≤ U. «Exactamente D» → = D. «No más B que A» → xB ≤ xA. «Al menos dos B por cada A» → xB ≥ 2xA.

**Porcentajes.** «Al menos el 30 % del tiempo total debe ser eléctrico»: xE ≥ 0,3(xE + xG), equivalente a 0,7xE − 0,3xG ≥ 0. Es distinto de xE ≥ 0,3xG. La palabra «total» identifica el denominador.

**Unidades.** Si se consumen 27 gramos por botella y hay 270 gramos, 27x ≤ 270. Con 0,27 kg disponibles debes convertir: 27x ≤ 270 g o 0,027x ≤ 0,27 kg. Nunca 27x ≤ 0,27 mezclando unidades.

**Capacidades acumuladas.** Dos operarios intercambiables de 40 horas aportan 80 horas. Si realizan tareas diferentes y no intercambiables, se requieren restricciones separadas, no necesariamente una bolsa de 80 horas.

**Redundancia.** Si x+y ≤ 50, x+y ≤ 120 no añade limitación. Puede conservarse para explicar el enunciado, pero no aporta una frontera nueva. No toda restricción escrita tiene que estar activa en el óptimo.

## No confundas
Producir objetos contables no convierte automáticamente la PL resuelta por Simplex en un modelo entero. Los parciales aportados trabajan con la relajación lineal; comenta el dominio cuando corresponda, sin redondear a ciegas.

**Autocomprobación.** Venta 500 €, coste 300 €: coeficiente de beneficio 200 €, no 500 €. Si cada unidad usa dos ruedas, 100 ruedas permiten como máximo 50 unidades.
---PAGE---
# 05. Formas y transformaciones equivalentes
## La convención de estos apuntes
**Canónica de maximización:** max cᵀx; Ax ≤ b; x ≥ 0. **Estándar:** max o min cᵀx; Ax = b; x ≥ 0; b ≥ 0. **Simétrica:** máximo con ≤, o mínimo con ≥, y variables no negativas. En los materiales, canónica y simétrica de maximización comparten la estructura indicada; no inventes diferencias que la definición no establece.

> ax ≤ b → ax + s = b, s ≥ 0
> ax ≥ b → ax − s = b, s ≥ 0
> x libre → x = u − v, u,v ≥ 0
> min f(x) → max g(x) = −f(x), con f* = −g*

**Normalizar b.** Si una fila tiene término independiente negativo, multiplica toda la fila por −1; si había desigualdad, invierte su sentido. Ejemplo: −2x + y ≥ −6 equivale a 2x − y ≤ 6; después se añade +s.

**Holgura y exceso.** La holgura positiva en una ≤ es el recurso sobrante: s = b − ax. En una ≥, el exceso es s = ax − b y aparece restado. Ambos son no negativos y tienen coeficiente cero en el objetivo original.

**Igualdad y variables libres.** Una igualdad puede expresarse como ax ≤ b y −ax ≤ −b si se requieren solo desigualdades. Una variable x ≤ 0 puede sustituirse por x = −u, u ≥ 0. Una cota x ≥ L se transforma con x = L + u.

## Ejemplo completo
Min 3x − y, sujeto a −x + y ≥ −2; x libre, y ≥ 0. Primero: x − y ≤ 2. Sustituye x = u − v. Forma estándar de minimización: min 3u − 3v − y; u − v − y + s = 2; u,v,y,s ≥ 0. Si maximizas el opuesto, los coeficientes del objetivo son −3, +3, +1 y 0.

**Autocomprobación.** La artificial no es necesaria para definir la forma estándar: se introduce cuando interesa construir una base inicial. Una igualdad ya es una igualdad y no necesita holgura para convertirse en ella.
---PAGE---
# 06. Resolución gráfica y tipos de resultado
## Procedimiento para dos variables
Dibuja la recta frontera de cada desigualdad. Para ax + by = d, los cortes son d/a y d/b cuando esos coeficientes no son cero. Si la recta pasa por el origen, prueba otro punto. Marca el semiplano permitido y conserva la intersección de todos, incluyendo no negatividad.

Encuentra los vértices candidatos mediante intersecciones. **Verifica cada candidato en todas las restricciones.** Evalúa el objetivo en los vértices factibles. Para una región poligonal no vacía y acotada, basta esa comparación para hallar un óptimo lineal.

[[GRAPH:basic]]

Ejemplo: max 2x+y, x+y≤4, x≤3, x,y≥0. Vértices: (0,0), (3,0), (3,1), (0,4). Objetivos: 0, 6, 7 y 4. Óptimo único: (3,1), z*=7. La recta 2x+y=7 toca el vértice de mayor valor.

**Isobeneficio.** Las rectas c₁x+c₂y=k son paralelas para distintos k. El vector c señala crecimiento del objetivo; minimizando se busca el sentido opuesto. La pendiente es −c₁/c₂ si c₂≠0.

**Autocomprobación.** El cruce de dos restricciones no garantiza factibilidad. La región se obtiene por intersección, no por unión. El método gráfico plano depende de tener pocas variables, no de que haya exactamente dos restricciones.
---PAGE---
# 06B. Óptimo único, alternativo, infactible o no acotado
**Único:** solo un punto factible alcanza el mejor valor. Ejemplo anterior: (3,1). No significa que solo exista un punto factible.

**Alternativos:** dos puntos factibles distintos tienen el mismo valor óptimo. Por convexidad y linealidad, todo su segmento también es óptimo. Ejemplo: max x+y, x+y≤4, x,y≥0. Todos los puntos del segmento entre (4,0) y (0,4) son óptimos con z*=4.

**Infactible:** F=∅. Ejemplo: x≥3 y x≤1. No existe decisión admisible; no se trata de un objetivo muy malo ni de un número infinito de soluciones.

**Objetivo no acotado:** existe una dirección factible que permite mejorar sin límite. Max x con x≥0 e y≥0 tiene z→+∞. En minimización, el objetivo debe poder disminuir hacia −∞.

[[GRAPH:unbounded]]

**La trampa central.** Región no acotada no implica objetivo no acotado. Min x sobre x≥2, y≥0 tiene mínimo 2 aunque la región sea ilimitada. Tiene infinitos óptimos: (2,y) para cualquier y≥0.

**Teorema con sus hipótesis.** En forma estándar, si hay solución factible y óptimo finito, existe una solución básica factible óptima. No afirma que cualquier PL tenga siempre óptimo ni que todo óptimo deba ser un vértice: con óptimos alternativos también hay puntos óptimos interiores de una cara.

**Autocomprobación.** Ser paralelo a una restricción cualquiera no demuestra óptimos múltiples: debe haber un desplazamiento factible distinto con valor óptimo constante. Dos óptimos distintos sí generan un segmento de óptimos.
---PAGE---
# 07. Bases, soluciones básicas y degeneración
## Del sistema a los vértices
En forma estándar Ax=b, x≥0, supón m filas independientes y n variables totales. Elige m columnas independientes de A: forman B, una matriz m×m invertible. Sus variables son básicas; las restantes n−m son no básicas y se fijan a cero.

> BxB = b → xB = B⁻¹b
> xN = 0; factibilidad si xB ≥ 0; z = cBᵀxB

**Ejemplo.** x₁+x₂+s₁=4; x₁+s₂=3. Con B=(a₁,a₃), las básicas son x₁,s₁. Las no básicas x₂,s₂ valen cero. La segunda ecuación da x₁=3; la primera, s₁=1. Es factible. Para max 2x₁+x₂, z=6.

Con B=(a₁,a₄), x₂=s₁=0. La primera da x₁=4 y la segunda s₂=−1. Es solución básica pero **no factible**. No demuestra que el problema original sea infactible: la otra base ya dio una solución admisible.

**Degeneración.** Una solución básica factible es degenerada si alguna básica es cero. No confundas con no básicas cero, que siempre ocurre. Una base degenerada puede corresponder al mismo punto que otra base. B debe seguir siendo invertible; «degenerada» no significa «singular».

**Cuántas bases.** Hay como máximo C(n,m) subconjuntos de m columnas; no todos tienen por qué ser independientes. Es un límite de candidatos, no el número garantizado de bases factibles. Bajo degeneración varias bases pueden dar el mismo vértice.

**Rango.** Si las m filas no son independientes, no existen m columnas independientes. Hay que tratar las igualdades redundantes o contradictorias antes de usar esa dimensión de base. Contar solo restricciones y variables originales tampoco basta: las holguras aumentan el número de variables.

**Autocomprobación.** Si B=I, xB=b; eso simplifica el inicio, pero no certifica optimalidad. cB sigue el mismo orden que las columnas elegidas para B.
---PAGE---
# 08. Simplex matricial: una iteración con sentido
Partimos de una base factible. Al aumentar una no básica xⱼ, las básicas deben ajustarse para seguir satisfaciendo las igualdades. La dirección transformada es yⱼ=B⁻¹aⱼ.

> xB(θ) = B⁻¹b − yⱼθ
> z(θ) = z(0) + (cⱼ − cBᵀyⱼ)θ
> zⱼ = cBᵀyⱼ; rⱼ = zⱼ − cⱼ; Δz = −rⱼθ

**Entrada, máximo.** Si rⱼ<0, aumentar xⱼ mejora marginalmente. La regla de clase escoge el rⱼ más negativo entre no básicas. Es mejora por unidad de xⱼ, no necesariamente la mayor mejora total después del paso.

**Salida.** Para mantener xB≥0, considera solo componentes yᵢⱼ>0. Son las básicas que disminuyen. Calcula θᵢ=xBᵢ/yᵢⱼ y elige el mínimo. Si yᵢⱼ=0 la básica no cambia; si es negativo aumenta. No dividas por cero ni uses cocientes negativos.

> θ* = min {xBᵢ/yᵢⱼ : yᵢⱼ>0}

**Actualizar.** La básica que llega primero a cero sale y xⱼ entra en su lugar. Cambia la columna correspondiente en B; conserva el orden coherente en xB y cB. Recalcula y repite.

**Ejemplo.** xB=(8,6), yⱼ=(2,1), rⱼ=−3. Cocientes 4 y 6: θ=4. Viejas básicas: (0,2). Entrante: 4. Mejora: 3·4=12. La primera básica sale, no la de menor valor inicial.

**Minimización directa.** Con la misma definición r=z−c, una mejora disminuyendo z requiere r>0. En clase puedes convertir a máximo negando el objetivo para mantener una sola regla. Recupera después el signo del valor original.

**Autocomprobación.** Con r=−5 y θ=0, la mejora es cero. Una dirección marginalmente buena no garantiza un paso positivo cuando hay degeneración.
---PAGE---
# 09. Tabla del Simplex y cálculo del pivote
Una tabla organiza el mismo cálculo matricial: las columnas de restricciones son B⁻¹A y el término independiente es B⁻¹b. Las columnas básicas forman I. La columna cB contiene sus coeficientes en el objetivo, no sus valores actuales.

## Cómo leerla
Para cada columna j, zⱼ se calcula multiplicando la columna transformada por cBᵀ. El coste reducido es zⱼ−cⱼ. Las básicas tienen coste reducido cero. El objetivo actual se calcula como cBᵀxB.

**Ejemplo inicial:** max 2x+y; x+y+s₁=4; x+s₂=3. B=(s₁,s₂), cB=(0,0).

|Base|cB|x|y|s₁|s₂|b|
|s₁|0|1|1|1|0|4|
|s₂|0|1|0|0|1|3|
|r=z−c||−2|−1|0|0|0|

Entra x (−2). Cocientes 4 y 3: sale s₂, pivote en su fila y columna x. Divide la fila pivote por el pivote y elimina la columna x del resto de filas. Aquí el pivote ya es 1.

|Base|cB|x|y|s₁|s₂|b|
|s₁|0|0|1|1|−1|1|
|x|2|1|0|0|1|3|
|r=z−c||0|−1|0|2|6|

Entra y; solo su primera componente es positiva, θ=1 y sale s₁. Resultado: x=3, y=1 y z=7. Los siguientes costes reducidos son (0,0,1,1), todos no negativos.

**Control del pivote.** La columna entrante debe quedar como una columna de I. Las básicas deben seguir no negativas. Recalcular r desde cB y la tabla evita arrastrar errores de signo. Si actualizas la fila objetivo por operaciones, respeta la convención elegida.
---PAGE---
# 10. Artificiales y certificados de terminación
## Inicializar no es resolver
Con restricciones ≤ y b≥0, las holguras proporcionan B=I y xB=b. Una restricción ≥ se convierte en ax−s=b y no aporta por sí sola una columna +1 útil. Puedes introducir t≥0: ax−s+t=b. En una igualdad también puede hacer falta una artificial si no existe una base factible evidente.

Las artificiales no describen recursos reales: permiten resolver un **problema auxiliar**. En máximo se penalizan con −M; en mínimo, con +M. M debe ser positiva y suficientemente grande, o tratarse simbólicamente. Como alternativa conceptual, fase I minimiza la suma de artificiales y fase II recupera el objetivo original.

## Diagnóstico correcto en maximización
**Óptimo del original.** Base factible para el original, artificiales a cero y rⱼ≥0 para todas las no básicas. Si todas esas rⱼ son estrictamente positivas, la solución es única. Una rⱼ cero puede permitir otro óptimo, pero en degeneración debes comprobar un desplazamiento factible no nulo; cambiar base no siempre cambia punto.

**No acotado.** Desde una base factible del original, existe una entrante con rⱼ<0 y yⱼ≤0 componente a componente. Hay mejora y ninguna básica limita el crecimiento. No basta encontrar una columna de signos no positivos sin comprobar que mejore.

**Infactible.** La fase I termina correctamente y su mínimo es positivo: las artificiales no pueden ser todas cero. Con gran M simbólica correctamente aplicada, la misma idea se expresa al terminar con alguna artificial positiva.

**No son pruebas de infactibilidad:** una artificial positiva a mitad del algoritmo; una artificial básica con valor cero; una mala base que da valores negativos; o no haber encontrado todavía una base factible.

**Autocomprobación.** Forma estándar no exige artificiales en su definición. B no tiene que ser I para iniciar: basta invertibilidad y B⁻¹b≥0. La holgura no lleva penalización M.
---PAGE---
# 11. Dualidad: construir y usar el dual
## Pareja simétrica que debes dominar
> Primal: max cᵀx, Ax≤b, x≥0
> Dual: min bᵀy, Aᵀy≥c, y≥0

Cada fila del primal genera una variable dual; cada columna, una restricción dual. Si el primal tiene n variables y m restricciones, el dual tiene m variables y n restricciones. Los objetivos intercambian recursos b y beneficios c. La matriz se transpone, no se invierte. El dual del dual recupera el primal.

**Ejemplo.** Max 3x₁+2x₂; x₁+x₂≤4; 2x₁+x₂≤6; x≥0. Dual: min 4y₁+6y₂; y₁+2y₂≥3; y₁+y₂≥2; y≥0.

**Dualidad débil.** Para cualquier par factible, cᵀx≤bᵀy. Un dual factible limita por arriba un máximo primal. Si ambos valores coinciden, ambos son óptimos. **Dualidad fuerte:** si existe un óptimo finito en uno, existe en el otro y sus valores coinciden.

**Estados.** Primal no acotado implica dual infactible, y a la inversa intercambiando papeles. Primal infactible no obliga a dual no acotado: ambos pueden ser infactibles. «Óptimo infinito» es una forma confusa de hablar: distingue objetivo no acotado de infinitas soluciones con valor óptimo finito.

## Filas y signos en un primal máximo general
|Elemento primal|Correspondencia dual|
|Restricción ≤|Variable dual ≥0|
|Restricción ≥|Variable dual ≤0|
|Restricción =|Variable dual libre|
|Variable xⱼ≥0|Restricción dual ≥ cⱼ|
|Variable xⱼ≤0|Restricción dual ≤ cⱼ|
|Variable xⱼ libre|Restricción dual = cⱼ|

Puedes evitar memorizar todos los casos transformando primero a la forma simétrica. No apliques la regla «primal siempre maximiza» a una formulación de minimización sin normalizarla.
---PAGE---
# 12. Interpretación económica y sensibilidad
## Tres cantidades diferentes
**Solución x*.** Qué hacer: producir, transportar o asignar. **Holguras/excesos.** Cuánto sobra de un máximo o cuánto se supera un mínimo. **Precios sombra y*.** Cuánto cambia marginalmente el valor óptimo por unidad adicional de un recurso, bajo las condiciones de sensibilidad pertinentes.

> (y*)ᵀ = cBᵀB⁻¹, para una base primal óptima adecuada
> Si la base sigue siendo factible y óptima: Δz* = (y*)ᵀΔb

**Ejemplo.** Max 3x+y; x≤2; y≤3; x,y≥0. Óptimo (2,3), z=9 y precios (3,1). Aumentar el primer límite de 2 a 3 aumenta el óptimo a 12. Aquí la estructura se mantiene; en otros problemas un cambio grande puede activar otras restricciones y modificar el precio.

**Con una base fija.** Si solo cambia b, comprueba B⁻¹(b+Δb)≥0. Los costes reducidos no cambian porque A y c no cambian. Mientras la base siga factible, el mismo certificado de optimalidad se conserva. Si el cálculo da alguna básica negativa, esa base ya no describe una solución admisible y no debes extrapolar su precio sin reoptimizar.

## Complementariedad
Para la pareja max con ≤ y min con ≥, en soluciones óptimas:

> yᵢ(bᵢ−aᵢx) = 0
> xⱼ((Aᵀy)ⱼ−cⱼ) = 0

Holgura primal positiva ⇒ precio sombra cero. Precio sombra positivo ⇒ restricción activa. **La implicación inversa no vale:** precio cero no obliga a holgura positiva, y una restricción activa puede tener precio cero.

**Contraejemplo.** Max x, x≤1, y≤1, x,y≥0. El punto (1,1) es óptimo y el límite y≤1 está activo, pero su precio sombra puede ser cero: aumentar ese recurso no mejora un objetivo que no depende de y.

**Autocomprobación.** Un precio de 4 €/hora y una variación válida de 3 horas predicen 12 €, no tres horas sobrantes ni un beneficio total de 4 €.
---PAGE---
# 13. Transporte, asignación y camino mínimo
## Transporte
Orígenes i con capacidad aᵢ, destinos j con demanda bⱼ y costes cᵢⱼ. Variable xᵢⱼ: cantidad enviada de i a j.

> min ΣᵢΣⱼ cᵢⱼxᵢⱼ; Σⱼxᵢⱼ≤aᵢ; Σᵢxᵢⱼ≥bⱼ; xᵢⱼ≥0

Si se exige satisfacer exactamente demanda, usa igualdad. Si hay oferta y demanda equilibradas y todo debe enviarse, ambas familias pueden ser igualdades. No cambies automáticamente «al menos» por «exactamente» sin justificarlo. En la red completa de m orígenes y n destinos hay mn decisiones.

## Asignación
xᵢⱼ=1 si asignas individuo i a tarea j; 0 si no. Min Σcᵢⱼxᵢⱼ. Cada individuo exactamente una tarea: Σⱼxᵢⱼ=1. Cada tarea exactamente un individuo: Σᵢxᵢⱼ=1. Con cantidades distintas de personas y tareas, esas dos familias no son simultáneamente posibles sin adaptar el modelo, permitir tareas libres o añadir elementos ficticios.

El mínimo individual de cada fila puede competir por la misma tarea. La solución debe satisfacer ambas familias, no simplemente escoger cada mínimo por separado. Los modelos clásicos tienen propiedades de integridad con datos apropiados, pero eso no convierte cualquier PL de redes modificada en entera automáticamente.

## Camino mínimo
En un grafo dirigido, xᵢⱼ indica seleccionar el arco i→j en una formulación binaria. Min Σdᵢⱼxᵢⱼ. Usando salidas menos entradas: +1 en el origen, −1 en el destino y 0 en nodos intermedios. Solo existen variables para arcos del grafo.

Un flujo unitario conservado representa la conexión. Con costes no negativos existe una solución óptima sin ciclos de coste positivo; ciclos de coste cero pueden empatar. Los balances por sí solos no prohíben ciclos adicionales. No confundas «arco seleccionado» con «arco de coste uno».

**Autocomprobación.** Transporte decide cuánto; asignación decide a quién. Las capacidades limitan sumas de envíos, no cada envío aisladamente sin controlar el total.
---PAGE---
# 14. Condiciones lógicas con variables binarias
## Activación y coste fijo
Sea y∈{0,1} una apertura y 0≤x≤U una producción. La restricción x≤Uy obliga a x=0 si y=0. Si y=1 permite producir hasta U, pero **no obliga a producir**. Si la apertura cuesta F, el objetivo incluye −Fy en un máximo de beneficio o +Fy en un mínimo de coste.

**Lote mínimo.** Si al abrir se exige producir al menos L, añade x≥Ly. Así, cerrado da x=0; abierto da L≤x≤U. No confundir esta condición con la mera disponibilidad de fabricar.

**Modo bajo consumo.** Si y=1 limita x a 100 y la capacidad normal es 500: x≤100+400(1−y), x≥0. Cuando y=0 se permite hasta 500; cuando y=1 hasta 100. No obliga a activar el modo cuando se produce poco.

## Umbrales enteros y equivalencias
Con x entero, 0≤x≤U, y=1 si y solo si x≥K, y K≥1:

> x ≥ Ky
> x ≤ (K−1) + (U−K+1)y

Con y=0 queda 0≤x≤K−1; con y=1 queda K≤x≤U. Es una equivalencia completa. Una sola desigualdad puede representar solo una dirección de la condición.

**Umbral continuo.** No sustituyas automáticamente x>300 por x≥301 si x es continuo. Tampoco x>300 equivale a x≥300. Una separación ε>0 necesita hipótesis explícitas sobre tolerancia o valores admitidos; puede excluir valores reales válidos entre ambos límites. Las desigualdades estrictas no son las restricciones cerradas habituales de una PL.

## Binarias: reglas útiles
|Intención|Restricción|
|Como máximo una de a,b|a+b≤1|
|Exactamente una|a+b=1|
|Al menos una|a+b≥1|
|a implica b|a≤b|
|a y b se activan juntas|a=b|

**M grande en lógica.** Usa cotas válidas para desactivar una condición. No es el mismo papel que penalizar artificiales en Simplex, aunque compartan la letra M.
---PAGE---
# 15. Programación entera y ramificación y acotación
**Entera pura:** todas las decisiones enteras. **Mixta:** combina enteras y continuas. **Binaria:** decisiones 0–1. El objetivo y las restricciones siguen siendo lineales.

## Relajar, ramificar y podar
La relajación lineal retira integridad, conservando restricciones y cotas. En máximo, su óptimo es cota superior del entero; en mínimo, cota inferior. Un óptimo continuo fraccionario no se convierte en óptimo entero redondeando: puede violar restricciones o perder calidad.

**Incumbente:** mejor solución entera factible encontrada. Su valor es cota inferior del máximo o superior del mínimo. Para un máximo sin candidato se inicia en −∞; para un mínimo, +∞.

1. Resuelve la relajación del nodo.
2. Si es infactible, poda ese nodo.
3. Si su cota no puede mejorar al incumbente, poda por cota.
4. Si la solución relajada es entera en las variables exigidas, considérala para actualizar el incumbente y cierra el nodo.
5. Si sigue siendo fraccionaria y prometedora, elige una variable entera xᵢ con valor v no entero. Crea dos ramas: xᵢ≤⌊v⌋ y xᵢ≥⌈v⌉.

**Ejemplo de ramas.** Con x*=3,4, usa x≤3 y x≥4. No eliminas ningún valor entero y excluyes la fracción actual. Con x≤2 y x≥4 perderías el valor entero 3.

**Poda de máximo.** Incumbente 37 y cota relajada 35: poda. Cota 40,5: puede mejorar; no podes solo porque la solución sea fraccionaria. Si únicamente buscas un óptimo, una cota igual a 37 también puede podarse. Enumerar todos los óptimos requeriría tratar esa igualdad de otro modo.

**Profundidad.** Es el orden de explorar nodos: continuar por descendientes antes de otras ramas. No modifica la función objetivo ni obliga a que la primera solución entera sea la mejor.

**Autocomprobación.** En mínimo se invierten las cotas: un nodo con cota inferior 12 no mejora un incumbente 10. La infactibilidad de una rama no implica que todo el problema sea infactible.
---PAGE---
# 16. Conceptos que se confunden en los tests
|No confundir|Regla para decidir|
|Factible / óptima|Cumplir restricciones / además no poder mejorar|
|Región no acotada / objetivo no acotado|Forma de F / posibilidad de mejorar sin límite|
|Básica / básica factible|Resolver BxB=b / además xB≥0|
|Básica / positiva|Una básica puede valer cero|
|Degenerada / singular|Básica cero / matriz sin inversa|
|Holgura / artificial|Sobrante o exceso / ayuda algorítmica|
|Coste reducido / mejora|r=z−c / mejora por unidad = −r|
|Entrada / salida|Coste reducido / cociente factible|
|Precio sombra / holgura|Valor marginal / cantidad sobrante|
|Activa / precio positivo|Igualdad en un punto / multiplicador positivo|
|Relajación / redondeo|Cambiar dominios / modificar un candidato|
|Incumbente / cota relajada en max|Valor alcanzable inferior / límite superior|
|Como máximo una / exactamente una|a+b≤1 permite (0,0) / a+b=1 no|

## Cuatro contraejemplos para recordar
**«Toda variable básica es positiva».** xB=(0,2) es básica factible degenerada. **«Sin mejora siempre hay óptimo original».** Si al terminar el auxiliar queda artificial positiva, el original es infactible. **«Precio cero implica inactividad».** Max x, x≤1, y≤1 tiene óptimo (1,1) con precio de y igual a cero. **«Región ilimitada implica no acotación».** Min x, x≥2, y≥0 tiene mínimo 2.

**Prueba por sustitución.** En lógica binaria enumera (0,0), (0,1), (1,0), (1,1). En una condición con M evalúa por separado y=0 e y=1. En Simplex calcula signos antes de dividir. Estas comprobaciones cortas son más fiables que reconocer una frase de memoria.

**Autocomprobación.** ¿Una variable artificial cero puede estar en la base al final? Sí. ¿Una r cero garantiza mejora estricta? No. ¿Un punto con y=0 es necesariamente degenerado? No: debe ser una variable básica cero en la representación considerada.
---PAGE---
# 17. Auditoría de las recopilaciones aportadas
Las marcas de respuesta no se toman como autoridad. Dos archivos comparten el núcleo de 20 preguntas; la recopilación de 60 incluye las 30 de otra más breve. No se interpretan como cuatro convocatorias independientes ni se deducen años que no figuran.

**Referencias:** A = wuolah-free-TEST-1 (1).pdf; B = wuolah-free-Test-1.pdf; C = wuolah-free-TEST1.pdf; D = wuolah-free-tipotest1.pdf. En D la numeración se reinicia; se indica su orden global.

|Pregunta o grupo|Corrección o matiz necesario|
|C 10 y 16; D 10 y 16|Con r=z−c, el aumento por unidad es −r, no r. La mejora total también multiplica por θ.|
|C 20; D 20|Las artificiales ayudan a construir una base inicial auxiliar; convertir desigualdades a igualdades corresponde a holguras/excesos.|
|C 22; D 22|Cumplir igualdades no basta para una base factible: se exige B invertible y B⁻¹b≥0.|
|C 55|Precio sombra cero no implica restricción inactiva. Puede estar activa y tener multiplicador cero.|
|C 3 y 25; D 3 y 25|No basta paralelismo con cualquier restricción. Debe existir una cara factible óptima con puntos distintos.|
|A/B 19|En estándar las variables son no negativas; en una PL general pueden ser libres. El enunciado sin contexto admite interpretaciones distintas.|
|A/B 6|Para certificar no acotación hace falta una dirección que mejore el objetivo, no solo yⱼ≤0 para una columna cualquiera.|
|C 9,24,36; D 9,24|El criterio sin mejora requiere factibilidad original y artificiales a cero.|
|C 18; D 18|Sin fijar el sentido primal, no siempre es cierto que el primal maximiza: también hay primal mínimo con dual máximo.|
|C 56|«Solución óptima infinita» mezcla no acotación e infinitos óptimos; hay que precisar cuál se quiere decir.|

El parcial práctico de 2023 calcula 200·5+110·30=4300, pero su conclusión escribe 4330: el valor correcto es **4300 €**. La guía mantiene los modelos y verifica sus resultados.

Los nuevos simulacros evitan preguntas sin respuesta inequívoca y añaden las hipótesis necesarias. En tu examen, identifica primero la convención de clase y el contexto del enunciado.
---PAGE---
# R01. Parcial de refrescos (2021, modelo 81)
## Enunciado y modelo
Dos botellas: A de 4 litros y B de 2 litros. Deben entregarse al menos 10 litros. Hay 270 g de saborizante; A consume 27 g y B 18 g. No puede haber más B que A. Ingresos por botella: 5 € y 6 €. Sin costes adicionales, el objetivo del enunciado usa esos ingresos como beneficio.

Variables x,y: botellas A y B. Modelo continuo:

> max z = 5x + 6y
> 4x + 2y ≥ 10; 27x + 18y ≤ 270; y ≤ x; x,y ≥ 0

**Intersecciones factibles.** Con y=0: el mínimo de litros da x=5/2 y el máximo de saborizante da x=10. Con y=x: 6x=10 da (5/3,5/3); 45x=270 da (6,6). Comprueba cada punto en todas las restricciones.

|Vértice|Objetivo|
|(5/2,0)|25/2 = 12,5|
|(5/3,5/3)|55/3 ≈ 18,33|
|(6,6)|66|
|(10,0)|50|

**Resultado.** (6,6), z*=66 €. Litros: 4·6+2·6=36, superiores al mínimo. Saborizante: 27·6+18·6=270, recurso agotado. La relación y≤x está activa.

**Estándar.** 4x+2y−s₁=10; 27x+18y+s₂=270; x−y−s₃=0; todas no negativas. Valores: s₁=26 litros de exceso, s₂=0 g, s₃=0 botellas de diferencia. Objetivo de auxiliares cero.

**Qué te pueden preguntar.** La restricción de litros es ≥, no ≤. El exceso s₁ no es un precio sombra. La solución óptima satisface un mínimo con margen, y eso es válido. Aunque las botellas sean contables, aquí se ha resuelto el modelo continuo pedido; el óptimo además es entero.
---PAGE---
# R02. Parcial de relojes (2021, modelo 82)
## Datos y formulación
x: relojes de pie; y: relojes de pared por semana. Montaje: 5x+4y≤40; madera: 8x+4y≤40; envíos: 2x+2y≤22. Beneficios: 300 y 200 €. Dominios de la PL: x,y≥0.

> max z = 300x + 200y

**Reducir el dibujo con cuidado.** Como x≥0, 5x+4y≤8x+4y; por tanto, cumplir madera implica cumplir montaje. Además, 8x+4y≤40 implica x+y≤10, que es más fuerte que x+y≤11 de los envíos. Ambas restricciones son redundantes respecto a madera y no negatividad.

Los vértices son (0,0), (5,0) y (0,10). Sus beneficios son 0, 1500 y 2000 €. El óptimo único es **x=0, y=10, z*=2000 €**.

**Comprobar recursos.** Montaje: 40 de 40 horas; madera: 40 de 40; envíos: 20 de 22. Holguras: 0, 0 y 2 horas.

**Estándar.**

> 5x + 4y + s₁ = 40
> 8x + 4y + s₂ = 40
> 2x + 2y + s₃ = 22; x,y,s ≥ 0

**Matiz interesante.** Una restricción redundante puede estar activa en el óptimo: la de montaje lo está en (0,10). Redundante no significa necesariamente «nunca se cumple con igualdad». Tampoco que tenga su propio precio sombra positivo.

**Explicación del beneficio.** Producir un reloj de pie ocupa las horas de madera de dos de pared, pero deja 300 €, frente a 400 € de esos dos. La restricción limitante favorece a los de pared. Comparar solo 300 frente a 200 sin tener en cuenta consumos llevaría a una decisión incorrecta.
---PAGE---
# R03. Parcial de bicicletas (2021, modelo 84)
## Formulación
x: bicicletas de competición; y: de calle. Disponibles: 100 ruedas, 120 sillines y 80 horas de montaje acumuladas entre dos operarios. Cada bicicleta usa dos ruedas y un sillín; montaje de 2 y 1 horas.

> max z = 300x + 100y
> 2x+2y≤100; x+y≤120; 2x+y≤80; x,y≥0

La primera restricción equivale a x+y≤50; implica la de sillines, que es redundante. No son 40 horas de montaje total: hay dos operarios intercambiables de 40 horas cada uno.

**Vértices.** (0,0), (0,50), (40,0) y la intersección de x+y=50 con 2x+y=80. Restando, x=30; después y=20.

|Punto|z|
|(0,0)|0|
|(0,50)|5000|
|(30,20)|11000|
|(40,0)|12000|

**Óptimo.** 40 de competición, ninguna de calle; 12000 €. Uso: 80 ruedas, 40 sillines y 80 horas. Quedan 20 ruedas y 80 sillines. La existencia de recursos sobrantes no impide que el óptimo esté limitado por otro recurso.

**Forma estándar y auxiliares.**

> 2x+2y+s₁=100; x+y+s₂=120; 2x+y+s₃=80

En el óptimo s=(20,80,0). Las auxiliares no aportan beneficio. El cruce (30,20) es factible pero no óptimo, aunque agote simultáneamente ruedas y horas.

**Pregunta conceptual.** ¿Toda solución óptima agota todos los recursos? No. Basta que cualquier cambio que mejore el beneficio requiera violar alguna condición; no es necesario consumir todo.
---PAGE---
# R04. Parcial GreenTech (2023)
## Beneficio, proporciones y redundancia
x: EcoBike; y: EcoScooter. Beneficios unitarios: 500−300=200 y 250−140=110 €. Se exige x≥5 y al menos dos patinetes por bicicleta: y≥2x.

> max z = 200x + 110y
> 4x+2y≤80; 6x+3y≤120; x≥5; y≥2x; x,y≥0

Las restricciones de materiales y energía son proporcionales: ambas equivalen a 2x+y≤40. No generan dos fronteras distintas.

**Vértices.** Con x=5 e y=2x: (5,10). Con x=5 y 2x+y=40: (5,30). Con y=2x y 2x+y=40: (10,20).

|Vértice|Beneficio|
|(5,10)|1000+1100=2100|
|(5,30)|1000+3300=4300|
|(10,20)|2000+2200=4200|

**Resultado correcto.** x*=5, y*=30; z*=4300 €. El número 4330 escrito en la conclusión del solucionario aportado es una errata aritmética. La solución usa 80 kg y 120 kWh. Cumple y≥2x con exceso 20.

**Estándar.** 4x+2y+s₁=80; 6x+3y+s₂=120; x−s₃=5; −2x+y−s₄=0; variables no negativas. En el óptimo s=(0,0,0,20).

**Precaución de rango.** Las dos primeras filas son proporcionales en las variables originales. Tras añadir holguras distintas, la matriz ampliada cambia. Al elegir una base, comprueba independencia de las columnas efectivas; no inviertas una matriz con filas o columnas dependientes sin verificarla.

**Trampa de test.** Usar 500x+250y maximiza ingresos, no el beneficio neto solicitado cuando se proporcionan costes.
---PAGE---
# R05. Enumerar bases y distinguir factibilidad
Max 2x+y, sujeto a x+y+s₁=4; x+s₂=3; todas no negativas. Orden de columnas: x,y,s₁,s₂.

> A = [[1,1,1,0],[1,0,0,1]]; b=(4,3)

Hay C(4,2)=6 parejas candidatas. Para cada una fija las otras dos variables a cero y resuelve:

|Básicas|Valores de las básicas|Clasificación|
|x,y|(3,1)|Factible; z=7|
|x,s₁|(3,1)|Factible; z=6|
|x,s₂|(4,−1)|Básica no factible|
|y,s₁|No hay inversa|No forman base|
|y,s₂|(4,3)|Factible; z=4|
|s₁,s₂|(4,3)|Factible; z=0|

**Por qué falla (y,s₁).** Ambas columnas valen (1,0)ᵀ. La matriz es singular: su segunda fila queda cero y no puede producir el término independiente 3. No debes etiquetarla como «base infactible»: no es una base válida.

**Por qué (x,s₂) no es factible.** El sistema tiene solución y B es invertible, pero s₂=−1 viola el dominio. La base existe; su solución básica es inadmisible.

**Relación geométrica.** Las cuatro soluciones básicas factibles corresponden a (3,1), (3,0), (0,4) y (0,0). El máximo es 7 en (3,1). El límite combinatorio cuenta candidatos, no cuatro vértices garantizados ni seis bases válidas.

**Verificación de B=(x,s₁).** B=[[1,1],[1,0]], B⁻¹=[[0,1],[1,−1]]. Multiplicar por b=(4,3) da (3,1). cB=(2,0), de modo que z=2·3+0·1=6. No confundas el valor de s₁ con el de y: y es no básica y vale cero.
---PAGE---
# R06. Simplex completo con dos pivotes
Resolvemos max 2x+y; x+y≤4; x≤3; x,y≥0. Añadimos s₁,s₂.

**Iteración 0.** B₀=(s₁,s₂)=I; xB=(4,3); cB=(0,0); z=0. Para x: yx=(1,1), rₓ=−2. Para y: yy=(1,0), rᵧ=−1. Entra x, por ser −2 el más negativo.

Cocientes para x: 4/1=4 y 3/1=3. Sale s₂; θ=3. Las viejas básicas pasan a (1,0) y x=3. La mejora es 2·3=6.

**Iteración 1.** Orden B₁=(s₁,x). B=[[1,1],[0,1]]; B⁻¹=[[1,−1],[0,1]]. xB=(1,3); cB=(0,2); z=6.

Para y: aᵧ=(1,0); yᵧ=B⁻¹aᵧ=(1,0); rᵧ=0·1+2·0−1=−1. Para s₂: y=(−1,1); r=0·(−1)+2·1−0=2. Entra y.

Solo la primera componente de yᵧ es positiva. Cociente 1/1=1: sale s₁ y θ=1. Mejora 1·1=1.

**Iteración 2.** B₂=(y,x)=[[1,1],[0,1]]; xB=(1,3), ahora cB=(1,2). Aunque B numéricamente coincide con la anterior, las variables y costes asociados no son los mismos. z=1+6=7.

Para s₁: y=(1,0), r=1. Para s₂: y=(−1,1), r=−1+2=1. Todas las no básicas tienen r>0 y la solución es factible sin artificiales: óptimo único.

**Interpretación.** x=3,y=1; ambas restricciones activas; s₁=s₂=0. Precios sombra: cBᵀB⁻¹=(1,1). Un pequeño aumento válido de cualquiera de los dos recursos mejora el objetivo una unidad por unidad de recurso.

**Control.** Objetivos 0→6→7; los pivotes mantienen factibilidad. El menor valor básico inicial era 3 y salió s₂, pero la razón correcta es el cociente, no simplemente ser menor.
---PAGE---
# R07. Artificial y gran M sin confundir auxiliares
## Problema
Max z=x, sujeto a x≥2, x≤3, x≥0. Estándar: x−s₁=2; x+s₂=3. No aparece directamente una identidad positiva de auxiliares: −s₁ no proporciona una básica no negativa con x=0.

Introduce t≥0 en la primera: x−s₁+t=2. Objetivo auxiliar penalizado: max x−Mt. Base inicial (t,s₂)=I; xB=(2,3); cB=(−M,0); z=−2M.

**Primera entrada.** Para x, y=(1,1), rₓ=−M−1. Para s₁, y=(−1,0), r=M. Entra x. Cocientes 2/1 y 3/1: θ=2, sale t.

**Nueva base (x,s₂).** B=[[1,0],[1,1]], B⁻¹=[[1,0],[−1,1]]. xB=(2,1), cB=(1,0). Ya t=0. Para s₁: y=(−1,1), r=−1. Aumentar el exceso permite aumentar x, así que entra s₁. Cociente solo en segunda fila: 1/1=1, sale s₂.

**Base final (x,s₁).** x=3, s₁=1 y z=3. La segunda restricción está saturada. La primera tiene exceso uno: producimos una unidad más que el mínimo dos. Con B=[[1,−1],[1,0]], B⁻¹=[[0,1],[−1,1]], cB=(1,0), se obtiene r de s₂ igual a 1 y de t igual a M, no negativos.

**Qué ocurrió.** La artificial salió sin representar ningún recurso económico. El exceso s₁ permaneció como cantidad legítima del modelo. No penalices s₁ con −M; su coeficiente real es cero.

**Variante infactible.** Si el límite x≤3 se cambia por x≤1, el mínimo auxiliar de t es 1: con x=1 y s₁=0, t=1. Ningún x satisface x≥2 y x≤1. La positividad al terminar, no al principio, certifica infactibilidad.
---PAGE---
# R08. Dual y certificado de optimalidad
## Formulación primal
Max 3x₁+2x₂; x₁+x₂≤4; 2x₁+x₂≤6; x≥0. Sus vértices son (0,0), (3,0), (2,2), (0,4). Los valores son 0,9,10,8. Óptimo primal: (2,2), z*=10.

**Dual.** Min 4y₁+6y₂; y₁+2y₂≥3; y₁+y₂≥2; y≥0. Como ambas decisiones primales son positivas, buscamos igualdades duales: y₁+2y₂=3 y y₁+y₂=2. Restando, y₂=1 y luego y₁=1.

**Certificado.** (1,1) es dual factible y vale 4+6=10. El primal factible (2,2) también vale 10. Por dualidad débil ningún primal puede superar 10: ambos son óptimos, sin necesidad de buscar más puntos.

**Cálculo desde la base.** B=(a₁,a₂)=[[1,1],[2,1]], B⁻¹=[[-1,1],[2,−1]]. cB=(3,2), así que cBᵀB⁻¹=(1,1). Es el mismo precio obtenido por las igualdades duales.

**Holguras.** Primal: 4−(2+2)=0 y 6−(4+2)=0. Dual: (1+2)−3=0 y (1+1)−2=0. Los productos de complementariedad son cero.

**Interpretación.** Ambos recursos tienen valor marginal 1 €/unidad en los rangos adecuados. El hecho de que tengan el mismo precio no significa que sean el mismo recurso ni que todos los problemas con dos recursos compartan ese precio.

**Trampas.** El dual tiene dos variables porque el primal tiene dos restricciones; aquí coincide con el número primal de variables solo por casualidad. Igualdad de objetivos no dice que x*=y*: aquí x*=(2,2), y*=(1,1).
---PAGE---
# R09. Hasta dónde se puede usar un precio sombra
Usa el primal de R08. Cambia el primer recurso de 4 a 4+δ y mantén el segundo en 6. La base B=(a₁,a₂) y su inversa son las mismas.

> xB(δ) = [[−1,1],[2,−1]] · (4+δ,6)
> x₁ = 2−δ; x₂ = 2+2δ

**Factibilidad de la base.** 2−δ≥0 implica δ≤2. 2+2δ≥0 implica δ≥−1. Por tanto, para −1≤δ≤2 la base sigue factible. Como solo cambió b, los costes reducidos conservan su signo y la base sigue siendo óptima, incluso en los extremos donde puede ser degenerada.

**Valor.** z(δ)=3(2−δ)+2(2+2δ)=10+δ. El precio del primer recurso es 1 y la predicción es exacta en ese intervalo.

**Ejemplo válido.** δ=1: recursos (5,6), solución (1,4), z=11. La mejora es una unidad.

**Fuera del intervalo.** δ=3 daría la supuesta solución (−1,8), inadmisible. No aceptes z=13 por extrapolar. Con recursos (7,6), el punto (0,6) es óptimo con z=12: el segundo recurso impide seguir mejorando a razón de uno por unidad del primero. Certifica con y=(0,2): y₁+2y₂=4≥3, y₁+y₂=2, objetivo dual 0·7+2·6=12.

**Lección.** Un precio sombra no es una promesa ilimitada. Para variaciones simultáneas usa B⁻¹(b+Δb)≥0; los intervalos individuales no se pueden combinar arbitrariamente sin comprobar esa condición conjunta.

**Unidades.** Si b₁ mide kg y el objetivo euros, y₁ se mide en €/kg. La holgura del primer recurso, en cambio, mide kg.
---PAGE---
# R10. Transporte de dos orígenes a dos destinos
Capacidades: A=4 y B=6. Demandas exactas: destino 1=5, destino 2=5. Costes por unidad: A→1:1; A→2:4; B→1:3; B→2:2.

**Variables.** a=xA1, b=xA2, c=xB1, d=xB2, todas no negativas. Min z=a+4b+3c+2d. Salidas a+b≤4, c+d≤6. Entradas a+c=5, b+d=5. Como oferta total y demanda total son 10, ambas capacidades se agotan.

**Reducir a una variable.** Llama t=a. De a+b=4 sale b=4−t. De a+c=5 sale c=5−t. De b+d=5 sale d=1+t. No negatividad exige 0≤t≤4.

> z(t)=t+4(4−t)+3(5−t)+2(1+t)=33−4t

El coste disminuye con t: el mínimo está en t=4. Resultado: a=4, b=0, c=1, d=5. Coste: 4+0+3+10=17.

**Comprobar.** A envía 4; B envía 6. Destino 1 recibe 5 y destino 2 recibe 5. Asignar todo A a destino 2 porque hay capacidad sería más caro; hay que comparar costes y restricciones conjuntamente.

**Qué significa t.** No se impuso que el envío fuese binario. Es una cantidad. Con datos enteros, el transporte clásico equilibrado admite una solución óptima entera por su estructura; aquí además la deducción encuentra directamente valores enteros. Si añades restricciones generales, revisa esa propiedad antes de extrapolar.

**Variante de infactibilidad.** Si la segunda capacidad baja de 6 a 5 sin otra fuente, oferta máxima 9<demanda10: imposible. Cambiar los costes no repara la falta de suministro.
---PAGE---
# R11. Asignación: el mínimo local no basta
Tres personas A,B,C y tres tareas 1,2,3. Costes:

|Persona|Tarea 1|Tarea 2|Tarea 3|
|A|4|1|3|
|B|2|0|5|
|C|3|2|2|

Variable xᵢⱼ∈{0,1}. Cada fila suma uno y cada columna suma uno. Objetivo min Σcᵢⱼxᵢⱼ.

**Enumeración de las seis asignaciones posibles.** La terna indica la tarea de A, B y C, respectivamente:

|Asignación|Coste|
|(1,2,3)|4+0+2=6|
|(1,3,2)|4+5+2=11|
|(2,1,3)|1+2+2=5|
|(2,3,1)|1+5+3=9|
|(3,1,2)|3+2+2=7|
|(3,2,1)|3+0+3=6|

**Óptimo.** A→2, B→1, C→3; coste mínimo 5. La matriz de decisión es [[0,1,0],[1,0,0],[0,0,1]]. Sus filas y columnas suman uno.

**Por qué falla la elección individual.** A y B prefieren la tarea 2, pero no pueden hacerla ambos. El aparente coste 1+0+2=3 no es factible porque asigna dos personas a la misma tarea y deja otra libre.

**Si hubiera cuatro tareas.** Con tres personas no se pueden exigir exactamente una tarea por persona y exactamente una persona para cada una de cuatro tareas: las sumas totales serían tres y cuatro. Debes adaptar las condiciones o añadir una persona ficticia con significado apropiado, no ignorar una igualdad.
---PAGE---
# R12. Camino mínimo y balances
Grafo dirigido con nodos S,A,B,T y arcos: S→A coste 2; S→B coste 5; A→B coste 1; A→T coste 6; B→T coste 2. Todos los costes son no negativos.

**Variables.** xSA, xSB, xAB, xAT, xBT binarias. Objetivo:

> min 2xSA + 5xSB + xAB + 6xAT + 2xBT

**Balances, salidas menos entradas:**

> S: xSA + xSB = 1
> A: xAB + xAT − xSA = 0
> B: xBT − xSB − xAB = 0
> T: −xAT − xBT = −1

No hay variable xBA porque ese arco no existe. Una de las ecuaciones de balance es redundante al sumar todas, pero escribirlas ayuda a interpretar el flujo.

**Caminos posibles.** S→A→T cuesta 8. S→B→T cuesta 7. S→A→B→T cuesta 5. Óptimo: xSA=xAB=xBT=1; las otras dos cero.

**Verificación.** S genera una unidad; A recibe y envía una; B recibe y envía una; T recibe una. Coste 2+1+2=5. No selecciones el arco con coste mínimo aisladamente: A→B cuesta 1 pero no conecta por sí solo S con T.

**Matiz de redes.** Este grafo no tiene ciclos. En una red general los balances pueden permitir ciclos adicionales. Con costes no negativos los de coste positivo no interesan al mínimo, pero un ciclo de coste cero puede empatar. Si necesitas garantizar un camino simple para cualquier solución factible, el modelo requiere condiciones adicionales.
---PAGE---
# R13. Umbral entero y coste de activación
## Placas y adaptador
x: número entero de placas, 0≤x≤50. Se compra un adaptador de coste F=200 € si y solo si se compran al menos 20 placas. y∈{0,1} indica comprarlo. Coste de placas: 30 € por unidad.

> min z = 30x + 200y
> x ≥ 20y
> x ≤ 19 + 31y

Estas restricciones expresan la condición; el resto del modelo debe decir cuánta energía o cuántas placas hacen falta. Sin una demanda, el mínimo global sería x=y=0. La lógica por sí sola no obliga a comprar.

**Caso y=0.** x≥0 y x≤19. Está prohibido comprar 20 o más sin adaptador. **Caso y=1.** x≥20 y x≤50. Se permite cualquier cantidad del tramo alto.

**Comprobaciones del borde.** x=19 obliga a y=0: con y=1 violaría x≥20. x=20 obliga a y=1: con y=0 violaría x≤19. x=50 también exige y=1 y es admisible.

**Añadir demanda x≥22.** Como x≥22, necesariamente y=1. El coste creciente da x=22 y coste 30·22+200=860 €. No se usa un adaptador por placa: el coste fijo aparece una sola vez con y.

**Por qué no x≤20+30y.** Con y=0 permitiría x=20, incumpliendo la equivalencia deseada. El 19 procede de que x es entero: «menos de 20» equivale a «como máximo 19». Si x fuera continuo, 19 excluiría valores como 19,5; no podría reutilizarse esa transformación sin más.

**Relación con M.** Aquí la constante ajustada 31 proviene de U−K+1=50−20+1. Es una cota justificada, más informativa que escoger un millón por costumbre.
---PAGE---
# R14. Árbol entero completo de ramificación y acotación
Max z=3x+2y, sujeto a 2x+y≤4; x+2y≤4; x,y≥0 enteros.

**Raíz relajada.** Intersección: x=y=4/3 y z=20/3≈6,667. Los vértices de ejes dan 6 y 4; por tanto el cruce es el óptimo relajado y cota superior. No es solución entera.

**Ramificar en x:** rama I x≤1; rama II x≥2. Conserva las restricciones originales en ambas.

**Rama I.** El óptimo continuo es x=1,y=1,5, z=6. Para comprobarlo, sobre el límite x≤1 interesa usar x al máximo y el segundo recurso limita y a (4−x)/2. El resultado es fraccionario: ramifica en y≤1 o y≥2.

**Rama I-a, y≤1.** Máximo (1,1), z=5: solución entera, primer incumbente 5. Cierra el nodo.

**Rama I-b, y≥2.** La restricción x+2y≤4 junto a x≥0 implica y=2 y x=0. Valor 4; no mejora 5. Cierra por solución entera o por cota.

**Rama II, x≥2.** 2x+y≤4 y y≥0 obligan x=2,y=0. Valor 6; actualiza incumbente a 6. No quedan nodos pendientes: óptimo entero (2,0), z*=6.

[[GRAPH:tree]]

**Brecha.** El máximo relajado 20/3 es superior al entero 6. Redondear (4/3,4/3) a (1,1) da una factible de valor 5, pero no óptima. Redondear a (2,2) viola ambas capacidades.

**Profundidad.** Si exploras primero I, I-a, I-b y luego II, la primera entera encontrada no es la mejor. La estrategia cambia el orden y el trabajo pendiente, no la definición del óptimo.
---PAGE---
# R15. Leer una tabla y elegir el pivote
Maximización desde una base factible del original. cB=(2,0); xB=(6,4). Para dos no básicas u y v, se conocen columnas transformadas yu=(2,1), yv=(−1,2), y coeficientes cu=7, cv=1.

**Costes reducidos.** zu=2·2+0·1=4, así ru=4−7=−3. zv=2·(−1)+0·2=−2, así rv=−2−1=−3. Hay empate en entrada; adopta la de menor índice, u, como regla explícita de desempate.

**Salida para u.** Cocientes 6/2=3 y 4/1=4. θ=3; sale la primera básica. Las antiguas básicas pasan a (6−2·3,4−1·3)=(0,1). La nueva entrante u vale 3.

**Objetivo.** Antes z=2·6+0·4=12. Mejora −ru·θ=3·3=9, así z nuevo=21. En la nueva base, orden (u, antigua segunda), cB=(7,0) y xB=(3,1); z=7·3=21, comprobación independiente.

**Si se hubiera elegido v.** Solo la segunda componente de yv es positiva: θ=4/2=2. La primera básica aumentaría a 6−(−1)·2=8 y la segunda llegaría a cero. Mejora 3·2=6 y objetivo 18.

**Lección.** Empate en mejora marginal no implica misma mejora total. También puede ocurrir que la regla más negativa no produzca el mayor salto total entre todas las candidatas; la regla de clase se basa en la marginal.

**Qué no hacer.** No escoger la primera básica por tener mayor coste. No incluir 6/(−1)=−6 como cociente limitante de v. No usar Δz=ru·θ, que daría un descenso contrario al sentido de mejora.
---PAGE---
# R16. Degeneración y coste reducido cero sin otro óptimo
## Un caso que exige matizar el test
Max z=−x−y, sujeto a x≤0, y≤0, x,y≥0. La única decisión factible es x=y=0. Su objetivo vale 0 y es un óptimo único.

Forma estándar: x+s₁=0; y+s₂=0; todas no negativas. Elige B=(x,s₂)=I. Entonces xB=(0,0), cB=(−1,0). La base es factible y degenerada, no singular.

**Costes reducidos de no básicas.** Para y, yy=(0,1), zy=0 y ry=0−(−1)=1. Para s₁, ys₁=(1,0), zs₁=−1 y rs₁=−1−0=−1. Esta base no tiene todavía costes reducidos de óptimo, aunque representa el único punto factible óptimo; puede requerir un pivote degenerado para certificarlo.

Entra s₁, θ=0/1=0 y sale x. Base (s₁,s₂), cB=(0,0). Ahora rₓ=rᵧ=1 y se certifica el óptimo único sin mover el punto.

## Un coste cero sin punto alternativo
Cambia el objetivo a max z=−y en el mismo conjunto factible, que sigue siendo solo (0,0). Con B=(s₁,s₂), rₓ=0 y rᵧ=1. La no básica x tiene coste cero, pero su columna es (1,0) y el paso permitido es θ=0. No existe ningún punto factible distinto.

**Conclusión.** Una r no básica cero en el óptimo señala una posible dirección neutra, pero no garantiza siempre un segundo punto óptimo distinto si hay degeneración. En los ejemplos no degenerados usuales, si el paso es positivo aparece un segmento de óptimos.

**Tres objetos distintos.** Puede cambiar la base, mantenerse el mismo punto y mantenerse el mismo objetivo. No trates un cambio de nombre de variables básicas como si fuese necesariamente un desplazamiento a otro vértice.
---PAGE---
# P01–P04. Ejercicios propuestos: modelos y gráfica
Intenta cada problema antes de consultar las soluciones. Escribe variables, objetivo, restricciones y una interpretación del resultado.

## P01. Producción y recurso limitante
Dos productos dejan 4 € y 3 € por unidad. Cada uno ocupa una unidad de almacén, con capacidad 5. Solo el primero consume un componente limitado a dos unidades. Formula la PL y calcula el óptimo gráfico. Pasa a estándar e interpreta las holguras.

## P02. Un mínimo sobre una región ilimitada
Minimiza z=2x+y, sujeto a x+y≥3; x,y≥0. Encuentra los vértices, el óptimo y las restricciones activas. ¿Ser no acotada la región impide el mínimo?

## P03. Conversión y variable libre
Min z=3x−2y, sujeto a −x+y≥−4; x libre y y≤0. Construye una forma estándar con variables no negativas y objetivo de maximización equivalente. Indica cómo recuperar el valor original.

## P04. Porcentaje y beneficio
Un fabricante vende A a 12 € y B a 9 €, con costes unitarios 5 € y 4 €. Dispone de 10 horas; A requiere 2 y B 1. Al menos el 40 % del número total de unidades debe ser A. Formula el modelo continuo y determina el óptimo y beneficio. No confundas porcentaje del total con porcentaje de B.

**Control de aprendizaje.** Si no puedes formular un modelo, inventa una decisión concreta y comprueba si debería estar permitida. Para P04, A=0 y B=10 incumple el porcentaje; tu restricción debe detectarlo.
---PAGE---
# P05–P08. Ejercicios propuestos: bases y Simplex
## P05. Una base diagonal
Para B=[[2,0],[0,3]], b=(8,9) y cB=(5,2), calcula B⁻¹, xB y z. ¿Es una solución básica factible si las no básicas se fijan a cero? ¿Es degenerada?

## P06. Entrada, salida y mejora
En una maximización desde una base factible: xB=(8,6), cB=(0,0). La no básica u tiene cu=4, yu=(2,1); v tiene cv=3, yv=(1,3). Calcula sus costes reducidos, elige entrada por la regla de clase y halla salida, paso y mejora. No uses simultáneamente las dos columnas.

## P07. Certificados distintos
Clasifica cada situación de una maximización: a) base factible del original, r=(1,2); b) base factible del original, una no básica con r=−2 y y=(0,−1); c) fase I terminada con suma mínima de artificiales 0,5; d) artificial básica cero al terminar una fase I de valor cero. Explica qué se sabe y qué no.

## P08. Otro Simplex completo
Max z=3x+2y; x+y≤4; 2x+y≤6; x,y≥0. Empieza con base de holguras. Muestra cada entrada, los cocientes y los objetivos. Comprueba el resultado por intersecciones y construye un certificado dual.

**Control de aprendizaje.** Un coste reducido y una columna transformada son datos diferentes. Si la columna tiene componentes no positivas, pregunta además si el coste tiene signo de mejora. Para concluir óptimo original, comprueba las artificiales.
---PAGE---
# P09–P12. Ejercicios propuestos: dual y redes
## P09. Construcción del dual
Escribe el dual de max 5x+2y, sujeto a 2x+y≤8; x+3y≤9; x,y≥0. Indica número de variables, número de restricciones y dominios. No es necesario resolverlo.

## P10. Sensibilidad con límites
Max z=2x+y; x+y≤4; x≤3; x,y≥0. En el óptimo (3,1), calcula los precios sombra y el rango de variación δ del primer recurso que mantiene la base óptima de x,y, con el segundo recurso fijo. Predice el nuevo valor para δ=1.

## P11. Transporte pequeño
Dos orígenes de capacidad 3 y 2; destinos con demandas exactas 2 y 3. Costes [[1,4],[3,2]]. Formula las cuatro variables y encuentra el mínimo reduciendo a un parámetro. Verifica todos los balances.

## P12. Asignación y camino
a) Dos personas y dos tareas tienen costes [[4,1],[2,5]]. Encuentra la asignación mínima y su matriz binaria.
b) Arcos S→A:2, S→T:6, A→T:1. Escribe balances y encuentra el camino mínimo. ¿Qué diferencia hay entre su coste y el número de arcos seleccionados?

**Control de aprendizaje.** El dual no es «la segunda mejor solución». En transporte hay una variable por pareja; en camino solo por arco existente. Capacidad máxima y demanda exacta no son el mismo tipo de restricción.
---PAGE---
# P13–P16. Ejercicios propuestos: enteras y casos límite
## P13. Ramificar y podar
Max 5x+4y; x+y≤3,5; x≤2; x,y≥0 enteros. Resuelve la raíz relajada. Ramifica en y y completa el árbol necesario para certificar el óptimo entero, indicando cotas e incumbente. No sustituyas el árbol por un redondeo sin justificación.

## P14. Activación y tramo
Producción entera x entre 0 y 80. Una alarma y vale 1 si y solo si x≥30. Formula la equivalencia. Otra binaria a representa abrir la fábrica: si está cerrada no produce, y si abre produce al menos 10 y como máximo 80. Formula también la apertura y un coste total con 2 €/unidad y 100 € de apertura.

## P15. Activa con precio cero
Max z=x; x≤1; y≤1; x,y≥0. Demuestra que (1,1) es óptimo y encuentra una solución dual óptima. ¿Qué ocurre con el precio del segundo recurso, aunque su restricción esté activa en ese punto? ¿Es único el óptimo primal?

## P16. Comparar dos bases degeneradas
Sistema x+s₁=0; y+s₂=2, variables no negativas. Objetivo max y. Estudia B=(s₁,s₂): valores, degeneración y costes reducidos de x e y. Haz el pivote de mejora posible y explica si una básica cero obliga a que el óptimo no sea único.

**Control de aprendizaje.** Una cota superior en un máximo no es una cantidad que ya hayas conseguido. Un incumbente sí debe venir de una solución entera factible. En un modelo mixto, solo las variables declaradas enteras deben cumplir integridad al aceptar el candidato.
---PAGE---
# Soluciones P01–P04
## P01
x,y: unidades. Max 4x+3y; x+y≤5; x≤2; x,y≥0. Vértices (0,0),(2,0),(2,3),(0,5); objetivos 0,8,17,15. Óptimo único (2,3), valor 17. Estándar: x+y+s₁=5; x+s₂=2. Ambas holguras cero. La primera condición limita almacén y la segunda componentes; no deben sumarse como si fueran la misma unidad.

## P02
F es el semiplano por encima de x+y=3 en el primer cuadrante. Vértices (3,0) y (0,3); objetivos 6 y 3. El objetivo aumenta al alejarse en direcciones no negativas, así que el mínimo es (0,3), z=3. Están activas x=0 y x+y=3; y≥0 no está activa. La región ilimitada admite mínimo finito.

## P03
Multiplica −x+y≥−4 por −1: x−y≤4. Sustituye x=u−v y y=−w, con u,v,w≥0. Restricción u−v+w+s=4; todas no negativas. Objetivo original f=3u−3v+2w. Maximización equivalente: g=−3u+3v−2w. Al terminar, x=u−v, y=−w y f*=−g*. No se pierde libertad de signo de x.

## P04
Margen A=7 y B=5. Max 7x+5y; 2x+y≤10; x≥0,4(x+y); x,y≥0. El porcentaje equivale a 3x≥2y o y≤1,5x. Vértices: (0,0), (5,0) y la intersección y=1,5x con 2x+y=10: x=20/7, y=30/7. Objetivos 0,35 y 290/7≈41,429. Óptimo en ese cruce. Cumple x/(x+y)=0,4 y usa todas las horas. Si se exigen unidades enteras, hay que resolver otro problema; no declarar enteras estas fracciones.
---PAGE---
# Soluciones P05–P08
## P05
B⁻¹=[[1/2,0],[0,1/3]]. xB=(4,3). z=5·4+2·3=26. Es factible porque ambos valores son no negativos y las igualdades se satisfacen; no degenerada porque ninguna básica vale cero. Nada de esto certifica optimalidad sin analizar las otras columnas y costes.

## P06
zu=zv=0 porque cB=(0,0). ru=−4 y rv=−3: entra u. Sus cocientes son 8/2=4 y 6/1=6; sale la primera básica, θ=4. Las antiguas básicas quedan (0,2) y u=4. El objetivo inicial era cero y aumenta 4·4=16. Si hubieras elegido v, el paso sería min(8,2)=2 y la mejora 6, pero no es la elegida por la regla dada.

## P07
a) Óptimo único, pues ambas r son estrictamente positivas y la solución ya es factible para el original. b) Objetivo no acotado: hay mejora y ninguna componente positiva limita el paso. c) Original infactible: no se eliminan todas las artificiales. d) La fase I alcanzó factibilidad original; una artificial cero puede permanecer por degeneración. Hay que preparar una base adecuada y optimizar el objetivo original; no se puede concluir infactibilidad ni optimalidad de ese objetivo solo por el valor cero auxiliar.

## P08
Inicial s=(4,6), rₓ=−3, rᵧ=−2. Entra x; cocientes 4 y 3: sale segunda holgura. Queda x=3, s₁=1, z=9. En la tabla de base (s₁,x), la columna de y es (1/2,1/2), cB=(0,3): rᵧ=3/2−2=−1/2. Cocientes 1/(1/2)=2 y 3/(1/2)=6: entra y, sale s₁. Punto (2,2), z=10. Los costes de las holguras son 1 y 1; óptimo. Dual y=(1,1) factible con objetivo 10, que certifica el resultado.
---PAGE---
# Soluciones P09–P12
## P09
Min 8u+9v; 2u+v≥5; u+3v≥2; u,v≥0. Dos variables duales por las dos restricciones originales, y dos restricciones por x e y. Los límites 8 y 9 pasan al objetivo; los coeficientes 5 y 2 pasan a los términos independientes duales.

## P10
B de x,y es [[1,1],[1,0]], B⁻¹=[[0,1],[1,−1]]. cB=(2,1), ydualᵀ=(1,1). Con b=(4+δ,3), solución x=3, y=1+δ. La base es factible si δ≥−1; no hay límite superior porque el segundo recurso fija x y el primero permite aumentar y. Los costes reducidos no cambian. Para δ=1: (3,2), z=8, frente al valor inicial 7.

## P11
Sean a,b envíos del primer origen y c,d del segundo. a+b=3 y c+d=2 al agotarse oferta total cinco; a+c=2 y b+d=3. Con t=a: b=3−t, c=2−t, d=t; 0≤t≤2. Coste t+4(3−t)+3(2−t)+2t=18−4t. Mínimo en t=2: (a,b,c,d)=(2,1,0,2), coste 10. Las cantidades satisfacen capacidades 3 y 2 y demandas 2 y 3.

## P12
a) Diagonal: 4+5=9. Cruzada: 1+2=3. Óptimo matriz [[0,1],[1,0]], coste 3. b) Variables xSA,xST,xAT. S: xSA+xST=1; A: xAT−xSA=0; T: −xST−xAT=−1. El camino S→A→T cuesta 2+1=3 y utiliza dos arcos, frente al directo de coste 6 y un arco. Menos arcos no implica menor coste.
---PAGE---
# Soluciones P13–P16
## P13
Raíz: conviene x por su coeficiente mayor, hasta x=2; después y=1,5. Usamos punto y coma para separar coordenadas cuando hay decimales. Cota superior 16; fraccionaria. Rama y≤1: óptimo relajado (2,1), valor 14 entero, incumbente 14. Rama y≥2: el óptimo relajado es (1,5; 2), valor 15,5. Ramifica en x: x≤1 da (1; 2,5), cota 15; x≥2 es infactible porque x+y≥4>3,5. En el nodo x≤1, ramifica y: y≤2 da (1,2), valor 13, que no mejora 14; y≥3 da (0,5; 3), cota 14,5. Ramifica x: x≤0 tiene óptimo relajado (0; 3,5), cota 14, igual al incumbente: poda por cota. Su mejor punto entero es (0,3), valor 12. La rama x≥1 es infactible. No quedan nodos: óptimo (2,1), z=14. Cada par indica (x; y); la coma dentro de una coordenada es decimal.

## P14
Alarma: x≥30y y x≤29+51y. Apertura: 10a≤x≤80a. Coste min 2x+100a. Si falta demanda u otro requisito, cerrar y producir cero es válido y óptimo. No sumar el coste 100 por unidad: aparece ligado a a una sola vez. Para y=0 el umbral permite hasta 29; para y=1 exige al menos 30.

## P15
Para cualquier factible x≤1, z≤1. (1,1) alcanza 1. Dual: min u+v; u≥1; v≥0; u,v≥0. u=1,v=0 da valor 1. La segunda restricción primal está activa en (1,1) pero su precio es cero. Hay infinitos óptimos (1,y), 0≤y≤1: la ausencia de y en el objetivo deja ese tramo indiferente.

## P16
B=(s₁,s₂)=I, xB=(0,2), cB=(0,0): degenerada. rₓ=0, rᵧ=−1. Entra y, columna (0,1), solo segundo cociente válido: θ=2 y sale s₂. Punto original (0,2), z=2. Es óptimo único: x siempre es cero por la primera igualdad y y no supera dos. En la nueva base queda una básica s₁=0, demostrando que degeneración no implica múltiples puntos óptimos. La r de x sigue cero, pero su paso factible es cero.
---PAGE---
# Simulacros y modo de corrección
Los tres simulacros siguientes tienen 20 preguntas y tres opciones, con una única correcta. Incluyen dos preguntas de cada bloque del banco. No repiten preguntas entre sí. Las letras correctas se equilibran sin seguir una secuencia cíclica.

**Antes de empezar.** Tapa o separa el solucionario. No se fija un tiempo oficial que no está confirmado: anota tu duración para comparar sesiones. Si luego conoces la duración real, úsala como límite.

**Durante.** Marca una sola opción o deja en blanco. Anota un signo de duda si has acertado por descarte sin dominar la regla. No mires la corrección hasta terminar las 20.

**Después.** Cuenta aciertos, fallos y blancos. Las explicaciones identifican por qué cada alternativa es correcta o incorrecta. Revisa primero los errores de concepto y después los de cálculo. Vuelve al apartado citado.

**Interpretar la nota.** Con reglas A por acierto y −P por fallo, puntuación = A·aciertos − P·fallos. Sin penalización, el porcentaje de aciertos es una medida de repaso, no una conversión confirmada a la nota oficial.

**Objetivo de dominio.** Poder responder y justificar, sin reconocer la posición, las mismas ideas con otros números y con el sentido máximo/mínimo cambiado. La web posterior amplía esta práctica con 360 preguntas y opciones barajadas.
---PAGE---
[[EXAMS]]
---PAGE---
# 18. Formulario y comprobación final
## Modelo, base y pivote
> Estándar docente: max/min cᵀx; Ax=b; x≥0; b≥0
> Base: B cuadrada m×m, invertible; xB=B⁻¹b; xN=0
> Factibilidad: xB≥0; degeneración: alguna básica =0
> Objetivo: z=cBᵀxB
> Dirección: yⱼ=B⁻¹aⱼ; zⱼ=cBᵀyⱼ; rⱼ=zⱼ−cⱼ
> Máximo: entra una no básica con rⱼ<0, en clase la más negativa
> Salida: θ=min{xBᵢ/yᵢⱼ : yᵢⱼ>0}
> Viejas básicas: xB nuevo=xB−yⱼθ; mejora Δz=−rⱼθ

**Máximo, base factible original.** Sin mejora y sin artificiales positivas: óptimo. Todas las r no básicas estrictamente positivas: único. r negativa y columna transformada no positiva: no acotado. Auxiliar correctamente terminado con artificiales necesariamente positivas: infactible original.

## Dual y enteras
> Max cᵀx, Ax≤b, x≥0 ↔ min bᵀy, Aᵀy≥c, y≥0
> Factibles: cᵀx≤bᵀy; óptimos finitos: z*=w*
> Precio: yᵀ=cBᵀB⁻¹; Δz*=yᵀΔb si la base sigue válida
> Complementariedad: yᵢsᵢ=0; xⱼ((Aᵀy)ⱼ−cⱼ)=0
> Rama entera: xᵢ≤⌊v⌋ / xᵢ≥⌈v⌉

Máximo entero: relajación=cota superior; incumbente=cota inferior. Poda si cota superior≤incumbente. Mínimo: relajación=cota inferior; incumbente=cota superior. Poda si cota inferior≥incumbente.

**Chequeo final.** ¿Sé modelar porcentajes? ¿Sé dibujar semiplanos? ¿Sé distinguir base singular y degenerada? ¿Puedo explicar el signo de Δz? ¿He separado precio sombra y sobrante? ¿He comprobado y=0 e y=1 en cada condición? ¿Puedo justificar una poda? Si una respuesta es no, vuelve al ejemplo correspondiente antes de repetir tests.
---PAGE---
# 19. Fuentes y trazabilidad
## Material docente local
Programación-lineal_6a3278935dff09c7fce4d3c168a817fc.pdf, presentación de 117 páginas del curso 2026–2027: resolución gráfica, Simplex, modelización, dualidad y programación entera. Las repeticiones por animaciones no se consideran temas distintos.

programacion-lineal-es_8aada05f45f8ab5d3f8e8a5751c8a628.pdf, 68 páginas: definiciones, formas, Simplex, dualidad, redes, condiciones e integridad. Se conserva su convención de forma estándar y de costes reducidos.

representacion_4fd2842c9246fff8e9b2fd9d3e9a4fab.pdf, 12 páginas: formulación y representación de problemas. simplex_ad210ba8a33c72d2ce4b367a6019f17c.pdf, 21 páginas: problemas y cálculos de Simplex. introduccion-es_0fb9c487d0b1e44d1a1ce9892d4945c0.pdf, 24 páginas: contexto de algoritmos y optimización. Su contenido general de computación no amplía el alcance del bloque de programación lineal aquí estudiado.

## Parciales prácticos
R01: parciales/2021_Octubre_GINF_SOL_81.pdf. R02: modelo 82. R03: modelo 84. R04: parciales/2023_Octubre_GINF_SOL.pdf. Se verifican restricciones, vértices y valores, y se corrige expresamente la errata de beneficio de 2023.

## Recopilaciones de tests
Las cuatro fuentes Wuolah identificadas en el apartado 17 se usan para detectar conceptos, distractores y ambigüedades. La repetición entre archivos no equivale a confirmación independiente, y las respuestas señaladas no se presuponen oficiales. El título de algunas menciona programación dinámica, pero el contenido revisado no justifica añadirla a esta guía.

## Material original de práctica
R05–R16, P01–P16 y los tres simulacros se desarrollan para esta guía. El banco consta de 200 preguntas conceptuales y 160 de cálculo o aplicación; el archivo questions.json almacena opciones con identificadores estables, solución, explicación, tema, dificultad y referencia.

La fuente editable es study/guia.md; el generador y las comprobaciones están en scripts. El PDF se compone y revisa como documento paginado, no como una colección de capturas.
