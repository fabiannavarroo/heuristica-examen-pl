# Criterio · Programación lineal

Web de repaso personal de Heurística y Optimización: **360 preguntas**, tres opciones por pregunta y una única correcta, con explicación y referencias a una **guía PDF de 65 páginas**.

**[Abrir la web](https://fabiannavarroo.github.io/heuristica-examen-pl/)** · **[Descargar la guía](https://fabiannavarroo.github.io/heuristica-examen-pl/guia-programacion-lineal.pdf)**

## Estudiar

- Práctica libre por temas y dificultad, con corrección inmediata.
- Simulacros de 20 o 30 preguntas con corrección final. En modo general cubren los diez temas y mezclan un 70 % conceptual con un 30 % de aplicación.
- Repaso de fallos: acertar en un nuevo intento retira la pregunta de pendientes.
- Prioridad a preguntas menos practicadas, sin duplicados dentro de una sesión.
- Preguntas y opciones barajadas. Las letras correctas difieren como máximo en una por sesión, sin secuencias prefijadas.
- Historial y sesión guardados en el navegador. No hay cuentas, servidor ni envío de respuestas. El historial no se sincroniza entre dispositivos; borrar los datos del sitio lo elimina.

El banco contiene **200 preguntas conceptuales y 160 preguntas de cálculo/aplicación**, agrupadas en diez temas de 36 preguntas. Las numéricas tienen distintas instancias de familias de problemas; cambiar los números no cuenta como un concepto adicional. La guía incluye 16 resueltos, 16 propuestos con soluciones separadas y tres tests de 20 preguntas. Se explican las erratas y ambigüedades detectadas en las recopilaciones usadas para estudiar. No se presenta este material como examen o solucionario oficial. No se presupone penalización ni duración del examen.

## Archivos

- `web/`: aplicación estática sin dependencias de ejecución ni compilación, banco y PDF descargable.
- `study/guia.md`: teoría, ejercicios y soluciones editables.
- `study/simulacros.md`: simulacros y soluciones generados de forma reproducible.
- `study/questions.json`: banco con IDs de preguntas/opciones, explicación, dificultad y referencia.
- `scripts/build_bank.py`: redacción y generación del banco.
- `scripts/build_pdf.py`: maquetación PDF, índices, diagramas y comprobación de cobertura de glifos.
- `scripts/verify_content.py`: comprobaciones numéricas y de estructura.
- `scripts/test_engine.mjs`: pruebas del motor independiente de la interfaz.

Los documentos originales aportados como material de clase se mantienen fuera de este repositorio. La guía referencia sus nombres para trazabilidad.

## Ejecutar localmente

```sh
python3 -m http.server 8765 --directory web
```

Abrir `http://localhost:8765`. Los módulos y el banco requieren servir la carpeta por HTTP; no abrir el HTML directamente con `file://`.

```sh
node scripts/test_engine.mjs
node --check web/app.mjs
```

## Regenerar contenido y PDF

Python 3 con `reportlab`, `pypdf`, `numpy` y, para la revisión visual, `Pillow` y Poppler.

```sh
python3 scripts/build_bank.py
python3 scripts/verify_content.py
mkdir -p tmp/pdfs
python3 scripts/build_pdf.py
cp study/questions.json web/questions.json
cp output/pdf/guia-programacion-lineal.pdf web/guia-programacion-lineal.pdf
```

En macOS se usan Arial Unicode y Arial Bold del sistema. En Linux se buscan DejaVu Sans y DejaVu Sans Bold; se pueden elegir fuentes con `GUIDE_FONT` y `GUIDE_BOLD_FONT`. La generación comprueba que todos los caracteres usados existen en la fuente de cada fragmento. Los subíndices/superíndices se componen como tales, sin depender de glifos Unicode ausentes.

## Publicar

GitHub Pages se configura con GitHub Actions. El workflow ejecuta las comprobaciones del motor y publica únicamente `web/` al actualizar `main`.

## Validación

- 360 IDs y enunciados únicos, tres opciones distintas y una respuesta válida por pregunta.
- 60 preguntas de PDF distintas, en tres grupos equilibrados de 20.
- 450 sesiones de prueba del equilibrio de letras, sin repetición interna.
- Persistencia, corrección diferida, blancos, filtros, prioridad de preguntas nuevas e idempotencia del registro.
- Óptimos de los parciales y otros modelos comprobados mediante enumeración independiente de vértices; problemas enteros y asignación por enumeración; umbrales verificados en todo su dominio.
- Comprobación de los resultados de las 160 preguntas de cálculo, junto a revisión editorial de los conceptos.
- PDF de 65 páginas renderizado y revisado; tipografía matemática sin glifos ausentes.
- Flujos de práctica, reanudación, fallos y simulacro comprobados en navegador; revisión en escritorio y móvil.
