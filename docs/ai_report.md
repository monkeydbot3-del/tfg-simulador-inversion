# AI Report

## Iteración 01 - Diagnóstico inicial del proyecto

### Objetivo
Realizar un primer análisis real del repositorio de trabajo y dejar trazabilidad mínima para poder iterar con criterio.

### Contexto
El proyecto se acababa de clonar en el workspace del bot y todavía no existía memoria persistente específica de iteraciones dentro del propio repo.

### Cambios aplicados
- Se revisa la estructura general del proyecto.
- Se identifican los módulos principales de backend, frontend, datos y tests.
- Se crean `CHANGELOG_AI.md` y `docs/ai_report.md` para documentar el trabajo posterior.

### Decisiones tomadas
- Usar el repo del bot como único repo de trabajo.
- Tratar el repo original solo como referencia.
- No modificar la lógica de negocio en esta fase.

### Riesgos / problemas detectados
- `app/routes.py` y `app/career.py` concentran demasiada responsabilidad.
- El repo contiene artefactos mejorables como `venv/` y ficheros temporales.
- El proyecto ya mostraba signos de mojibake en textos visibles.

### Comprobaciones realizadas
- Revisión de estructura y archivos base del proyecto.
- Confirmación de remotos y del árbol de trabajo.

### Pendientes
- Mejorar la interfaz principal.
- Corregir textos visibles problemáticos.
- Empezar a elevar la calidad visual del producto.

## Iteración 02 - Mejora inicial de landing y textos clave

### Objetivo
Pulir la home y el modo práctica con mejoras visibles, seguras y defendibles sin tocar la lógica del simulador.

### Contexto
La app tenía una base correcta, pero la primera impresión seguía siendo demasiado plana y funcional para un TFG con ambición de producto final.

### Cambios aplicados
- Rediseño ligero de `app/templates/home.html` para hacer la landing más clara y orientada a decisiones.
- Mejora de jerarquía y copy en `app/templates/inicio.html`.
- Ajustes de textos globales en `app/templates/base.html`.
- Correcciones visibles en `app/templates/career.html`.
- Sustitución de un `style="display:none"` por clases/atributos más consistentes en `app/templates/analisis.html`.
- Consolidación CSS y responsive básico en `app/static/estilos.css`.

### Decisiones tomadas
- Priorizar impacto visual inmediato.
- Evitar cambios estructurales grandes.
- Mejorar primero lo que más ve el usuario al entrar.

### Riesgos / problemas detectados
- Persistían restos de mojibake fuera de las pantallas tocadas.
- La consistencia visual seguía siendo parcial entre secciones.

### Comprobaciones realizadas
- Revisión manual de templates y coherencia visual básica.
- Confirmación de que no se había modificado lógica funcional.

### Pendientes
- Limpiar mojibake visible restante.
- Unificar feedback UI básico.
- Mejorar análisis e historial.

## Iteración 03 - Mojibake visible y feedback UI básico

### Objetivo
Corregir textos rotos visibles y sustituir feedback brusco por interacciones más consistentes.

### Contexto
Tras la primera mejora visual, los errores de codificación y el uso de `alert()` seguían degradando mucho la percepción de calidad.

### Cambios aplicados
- Sustitución de varios `alert()` por toasts en `app/static/app.js`.
- Mejora del sistema de toasts para funcionar aunque falte inicialmente el contenedor.
- Corrección de textos visibles con mojibake en `app/career.py`.
- Corrección de observaciones y resúmenes visibles con mojibake en `app/data/analisis.json`.
- Correcciones parciales de microcopy visible en `app/routes.py`.

### Decisiones tomadas
- Mantener la lógica del simulador intacta.
- Priorizar mensajes visibles al usuario antes que limpieza interna completa.

### Riesgos / problemas detectados
- Quedaban restos de mojibake en backend y documentación interna.
- No se pudo ejecutar la suite de tests en el entorno disponible.

### Comprobaciones realizadas
- Revisión de textos visibles corregidos.
- Verificación manual del sistema de toasts.

### Pendientes
- Seguir limpiando mojibake restante.
- Mejorar el flujo visual del análisis.
- Preparar mejor el despliegue.

## Iteración 04 - Preparación mínima para Render y primera dirección visual de producto

### Objetivo
Dejar el proyecto listo para Render y aplicar una primera elevación visual importante en las pantallas más visibles.

### Contexto
El usuario pidió fijar el trabajo sobre `bot/render-preview`, dejar configuración clara para Render y dar un salto estético más profesional, tipo producto web moderno.

### Cambios aplicados
- Se detecta y corrige un problema de despliegue real: `requirements.txt` estaba en UTF-16 y se convierte a UTF-8.
- Se valida la configuración básica de Render:
  - build `pip install -r requirements.txt`
  - start `gunicorn run:app`
- Se rediseña `app/templates/base.html` con una cabecera más profesional y una identidad visual más clara.
- Se rediseña `app/templates/home.html` con hero ampliado, panel lateral y llamadas a la acción más claras.
- Se mejora `app/templates/inicio.html` con hero más rico y bloques informativos.
- Se refuerza `app/templates/empresas.html` con una presentación más editorial.
- Se mejora `app/templates/analisis.html` con una introducción más guiada, callout lateral y mejor cierre del flujo.
- Se amplía `app/static/estilos.css` con una capa visual más consistente de superficies, navegación, tablas, formularios y responsive.

### Decisiones tomadas
- Mantener una estética sobria y defendible académicamente.
- No introducir efectos extravagantes.
- Consolidar la dirección de producto sin tocar lógica del simulador.

### Riesgos / problemas detectados
- El modo carrera, historial, aprender y manual seguían siendo más débiles visualmente.
- La documentación del proyecto seguía necesitando una estructura más útil a largo plazo.

### Comprobaciones realizadas
- Verificación del punto de entrada WSGI de la app.
- Confirmación de que `gunicorn` ya estaba incluido.
- Comprobación de sintaxis Python básica.
- Confirmación de que el despliegue en Render no requería variables obligatorias.

### Pendientes
- Rediseñar historial y modo carrera.
- Hacer más escaneables aprender y manual.
- Estructurar la memoria del proyecto por iteraciones.

## Iteración 05 - Dashboard visual para historial, carrera y documentación

### Objetivo
Dar un salto visual ambicioso en las zonas con más deuda estética para que la app se sienta más cercana a un producto SaaS financiero o dashboard de inversión, sin tocar la lógica funcional.

### Contexto
Tras la iteración anterior, la home, práctica, análisis y exploración ya tenían una dirección visual más sólida, pero `historial`, `modo carrera`, `aprende` y `manual` seguían mostrando una presentación más antigua y menos unificada. Además, el usuario pidió consolidar `docs/ai_report.md` como memoria persistente estructurada por iteraciones y `CHANGELOG_AI.md` como registro breve acumulativo.

### Cambios aplicados
- Rediseño de `app/templates/historial.html` con cabecera editorial, badge contextual, panel de acciones más limpio y contenedor de tabla más alineado con el sistema visual actual.
- Rediseño de `app/templates/career.html` para presentarlo como dashboard estratégico:
  - nueva cabecera más clara
  - strip superior de valor
  - cards elevadas en sesión, series e informe
  - refuerzo visual de score, métricas, tablas, ranking y bloques de share/exportación
- Mejora de `app/templates/aprende.html` con cabecera independiente, badge contextual y cards más coherentes con la nueva dirección visual.
- Mejora de `app/templates/manual.html` con entrada más clara, estructura más editorial y tratamiento más escaneable del índice y del glosario.
- Ampliación de `app/static/estilos.css` con estilos específicos para:
  - bloques dashboard del modo carrera
  - tablas y wrappers más profesionales
  - manual mejor estructurado
  - glosario y tablas compactas
  - info strips y layouts responsivos adicionales
- Reestructuración completa de `docs/ai_report.md` para dejarlo organizado por iteraciones con numeración estricta y secciones homogéneas.
- Reescritura de `CHANGELOG_AI.md` al formato de memoria breve solicitado: fecha, rama, commit, título y archivos tocados.

### Decisiones tomadas
- Considerar esta como `Iteración 05`, tomando como última iteración documentada la `Iteración 04`.
- No simular búsquedas en internet y apoyarse en principios modernos de UI/UX ya conocidos y consistentes con producto digital actual.
- Priorizar percepción de dashboard financiero mediante jerarquía, densidad visual controlada, cards, tablas y bloques de métricas.
- Mantener todo el trabajo sobre `bot/render-preview`.

### Riesgos / problemas detectados
- El modo carrera sigue siendo la zona más compleja del producto y probablemente necesitará una segunda iteración específica para refinar densidad, estados y microcopy internos.
- Algunas partes del manual continúan siendo extensas por naturaleza, aunque ahora están mejor presentadas.
- No se ha ejecutado test funcional completo, solo comprobación sintáctica básica.

### Comprobaciones realizadas
- Relectura obligatoria de `BOT_INSTRUCTIONS.md`, `PROJECT_CONTEXT.md`, `CHANGELOG_AI.md` y `docs/ai_report.md` antes de empezar.
- Revisión del último número de iteración usado antes de crear la nueva.
- Comprobación de sintaxis con `python3 -m py_compile` sobre `run.py`, `app/__init__.py`, `app/routes.py` y `app/career.py`.
- Revisión del estado Git para confirmar el alcance real de los cambios.

### Pendientes
- Refinar aún más la experiencia visual del modo carrera, especialmente turn builder, estados vacíos, densidad de tablas y métricas.
- Unificar con más detalle estados de feedback, cargas y mensajes vacíos en historial y carrera.
- Seguir corrigiendo restos de microcopy irregular o mojibake residual si aparece en otras zonas.
- Valorar una iteración futura centrada en ranking, reporting y manual avanzado para cierre académico del producto.
