# AI Report

## Diagnóstico inicial

### Confirmación de contexto operativo
- Repositorio local: `/root/.openclaw/workspace/tfg-web-ci-python-bot`
- Rama activa: `bot/diagnostico-inicial`
- Remotos configurados:
  - `origin`: `git@github.com:monkeydbot3-del/tfg-web-ci-python-bot.git`
  - `reference`: `git@github.com:sanlaja/tfg-web-ci-python.git`

### Estado de los archivos de contexto persistente
En esta primera iteración faltan en el repo los siguientes archivos indicados como obligatorios por el usuario:
- `BOT_INSTRUCTIONS.md`
- `PROJECT_CONTEXT.md`

También faltaban estos archivos de seguimiento y se crean en esta iteración:
- `CHANGELOG_AI.md`
- `docs/ai_report.md`

## Diagnóstico técnico

### Estructura del proyecto
El proyecto es una aplicación Flask monolítica con una separación básica entre backend, frontend estático y tests:
- `app/__init__.py`: inicialización de Flask
- `app/routes.py`: rutas HTML, endpoints JSON, lógica de análisis, persistencia y utilidades de mercado
- `app/career.py`: módulo grande y especializado para el modo carrera
- `app/templates/`: vistas Jinja
- `app/static/`: CSS, JS, imágenes y vídeo
- `app/data/`: datos JSON persistidos en el repo
- `tests/`: suite de pruebas relativamente amplia

### Valoración técnica general
Puntos positivos:
- La app tiene una base funcional clara.
- Hay suite de tests y CI declarada.
- La separación `templates/static/data` es razonable para un TFG.
- Hay cobertura funcional relativamente amplia en rutas críticas.

Debilidades técnicas:
- `app/routes.py` concentra demasiadas responsabilidades: vistas, API, validación, normalización, persistencia, exportación y lógica de cálculo.
- `app/career.py` es muy grande y compleja, con alto coste de mantenimiento y riesgo de regresiones.
- La documentación de `README.md` no representa el estado real del proyecto, parece residual de una plantilla inicial mínima.
- Hay un `venv/` dentro del repo, mala práctica de versionado y peso innecesario.
- Existen archivos temporales o dudosos (`sandbox_tmp.py`, `tmp_script.py`) que erosionan limpieza y confianza del repositorio.
- Dependencias de desarrollo y ejecución aparecen mezcladas en `requirements.txt`.
- No se ha podido ejecutar `pytest` en este entorno porque el repo no trae entorno virtual operativo ni pytest instalado localmente.

### Riesgos técnicos detectados
1. **Mojibake / problemas de codificación** en backend, frontend y datos.
2. **Acoplamiento alto** entre frontend y backend.
3. **Escalabilidad baja** por archivos Python muy grandes.
4. **Persistencia local en JSON** dentro del repo, válida para prototipo pero frágil para crecimiento.
5. **Calidad del repositorio irregular** por mezcla de código serio, assets y artefactos temporales.

## Diagnóstico de diseño y UX/UI

### Calidad visual actual
La base visual es correcta y agradable para un TFG:
- paleta coherente en verdes suaves
- tarjetas, sombras y bordes consistentes en buena parte de la app
- navegación superior clara
- formularios razonablemente limpios

Pero el nivel visual todavía se percibe como “funcional” más que como producto pulido:
- landing simple y algo plana en jerarquía visual
- densidad visual alta en pantallas complejas
- falta de sistema visual más robusto para estados, feedback y bloques informativos
- componentes heterogéneos entre páginas

### Consistencia de interfaz
Puntos buenos:
- existe un layout base común
- botones y cards reaparecen de forma consistente en varias vistas
- la navegación principal está unificada

Problemas:
- hay estilos inline en plantillas, señal de consistencia incompleta
- conviven modales, alerts nativos y componentes personalizados
- textos, tono y microcopy no siempre comparten la misma voz
- el modo carrera tiene una complejidad visual superior al resto y parece casi otra app

### UX y navegación
Fortalezas:
- la estructura principal se entiende
- el usuario tiene modos diferenciados: práctica, carrera, manual
- existe contenido educativo y manual amplio

Fricciones:
- la home no prioriza del todo bien la decisión principal del usuario
- el modo análisis tiene muchos campos sin suficiente progresión o agrupación avanzada
- la navegación entre aprendizaje, análisis, historial y carrera puede sentirse fragmentada
- el manual es muy extenso y puede resultar abrumador dentro de la propia interfaz
- el uso de `alert()` reduce sensación de calidad y rompe la experiencia

### Responsive
La base CSS usa `grid`, `clamp` y `auto-fit`, lo cual ayuda.
Sin ejecutar pruebas visuales reales, el responsive parece razonable en estructura, pero hay riesgos claros:
- tablas amplias en empresas e historial
- pantallas muy densas en modo carrera
- navegación superior potencialmente saturada en móvil
- modales y bloques largos del manual pueden requerir refinamiento específico

## Problemas detectados

### 1. Codificación rota en varios puntos
Se observan textos corruptos tipo `Ã`, `â¬`, etc. en:
- `app/routes.py`
- `app/career.py`
- `app/templates/career.html`
- `app/data/analisis.json`

Impacto:
- empeora credibilidad del producto
- afecta UX
- sugiere deuda técnica en tratamiento de encoding

### 2. README desalineado con el producto real
El `README.md` describe un proyecto Flask mínimo, pero el repo contiene una aplicación bastante más compleja.
Impacto:
- mala primera impresión
- documentación poco fiable
- dificulta evaluación académica o técnica

### 3. Arquitectura backend poco modular
`routes.py` y `career.py` concentran demasiada lógica.
Impacto:
- mantenimiento difícil
- alta complejidad cognitiva
- testing y evolución más costosos

### 4. Feedback UI inconsistente
Uso de `alert()` y estilos inline junto a componentes más elaborados.
Impacto:
- experiencia menos profesional
- inconsistencia en estados de error/éxito

### 5. Repositorio poco limpio
Presencia de `venv/` y scripts temporales.
Impacto:
- tamaño innecesario
- ruido técnico
- mala percepción de calidad

### 6. Archivos de contexto del proyecto ausentes
No existen todavía:
- `BOT_INSTRUCTIONS.md`
- `PROJECT_CONTEXT.md`

Impacto:
- falta memoria de proyecto dentro del propio repo
- reduce continuidad operativa

## Oportunidades de mejora de alto impacto

1. **Corregir toda la capa de textos y encoding**.
   Es la mejora con mejor ratio impacto/esfuerzo percibido.

2. **Definir un sistema UI mínimo**.
   Tokens, componentes, estados, tablas, modales, formularios y feedback homogéneo.

3. **Refactorizar por módulos la lógica backend**.
   Separar servicios, validaciones, persistencia y utilidades de mercado.

4. **Replantear la home y los recorridos clave**.
   Dejar más claro qué hacer primero y cómo se relacionan práctica, aprendizaje y carrera.

5. **Pulir el modo carrera como producto principal**.
   Es la parte con más potencial diferencial, pero necesita mejor digestibilidad visual y operativa.

6. **Ordenar el repositorio para defensa de TFG**.
   Limpiar artefactos, actualizar documentación y reforzar impresión de proyecto serio.

## Plan de mejoras por fases

### Fase 0. Higiene y diagnóstico base
- Corregir encoding roto en textos críticos.
- Crear y mantener `BOT_INSTRUCTIONS.md` y `PROJECT_CONTEXT.md`.
- Actualizar `README.md` para reflejar el producto real.
- Identificar y retirar artefactos temporales del repo.
- Preparar una línea base de ejecución local y tests.

### Fase 1. Consistencia visual y microcopy
- Unificar tono y textos de navegación, formularios, ayudas y mensajes.
- Eliminar `alert()` y sustituirlos por toasts/modales consistentes.
- Eliminar estilos inline.
- Revisar jerarquía visual, espaciados y estados interactivos.

### Fase 2. UX de flujos principales
- Mejorar landing y puntos de entrada.
- Simplificar y agrupar mejor el flujo de “Nuevo análisis”.
- Reordenar empresas e historial para reducir fricción.
- Hacer el manual más escaneable y menos intimidante.

### Fase 3. Responsive y accesibilidad
- Revisar navegación en móvil.
- Mejorar tablas, modales y formularios complejos en pantallas pequeñas.
- Revisar focus, contraste, labels, estados y mensajes accesibles.

### Fase 4. Refactor técnico interno
- Extraer lógica de negocio fuera de `routes.py` y `career.py`.
- Separar validación, servicios de mercado, persistencia y reporting.
- Reorganizar dependencias y entorno.
- Fortalecer tests sobre los flujos más sensibles.

### Fase 5. Cierre de calidad para TFG
- Afinar acabado visual final.
- Mejorar documentación técnica y de uso.
- Preparar narrativa de producto y decisiones de diseño para memoria/defensa.
- Priorizar cambios con alto impacto demostrable frente a cambios cosméticos menores.

## Nota de comparación con el repo de referencia
Tras añadir y consultar el remoto `reference`, el árbol versionado visible del repo del bot no muestra diferencias frente a `reference/main` en la comprobación realizada. En esta fase inicial, el repo del bot parece partir del mismo estado base que el original de referencia.
