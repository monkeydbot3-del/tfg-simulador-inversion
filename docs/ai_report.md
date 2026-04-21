# AI Report

## Diagnóstico inicial

### Confirmación de contexto operativo
- Repositorio local: `/root/.openclaw/workspace/tfg-web-ci-python-bot`
- Rama activa inicial del diagnóstico: `bot/diagnostico-inicial`
- Rama activa actual de trabajo y despliegue: `bot/render-preview`
- Remotos configurados:
  - `origin`: `git@github.com:monkeydbot3-del/tfg-web-ci-python-bot.git`
  - `reference`: `git@github.com:sanlaja/tfg-web-ci-python.git`

### Estado de los archivos de contexto persistente
Ya existen en el repo y deben releerse antes de cada iteración:
- `BOT_INSTRUCTIONS.md`
- `PROJECT_CONTEXT.md`
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
- La app expone un objeto WSGI válido desde `run.py` mediante `app = create_app()`.
- `gunicorn` ya está incluido en dependencias.

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
6. **Riesgo de despliegue** detectado y corregido en esta iteración: `requirements.txt` estaba en UTF-16, lo que podía romper la instalación de dependencias en Render.

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
- hay todavía estilos inline en partes del frontend
- conviven modales, toasts y componentes heredados
- textos, tono y microcopy no siempre comparten la misma voz
- el modo carrera sigue teniendo una complejidad visual superior al resto

### UX y navegación
Fortalezas:
- la estructura principal se entiende
- el usuario tiene modos diferenciados: práctica, carrera, manual
- existe contenido educativo y manual amplio

Fricciones:
- el modo análisis sigue teniendo bastante carga para usuarios novatos
- la navegación entre aprendizaje, análisis, historial y carrera puede sentirse fragmentada
- el manual sigue siendo muy largo dentro de la interfaz
- aún quedan incoherencias visibles de microcopy y estilo

## Iteración 01. Textos clave y home

### Objetivo de la iteración
Atacar mejoras visibles y seguras, sin tocar lógica de negocio:
- pulir la home
- mejorar la claridad del modo práctica
- corregir algunos textos rotos o poco consistentes
- eliminar un pequeño uso de estilo inline

### Cambios aplicados
- Rediseño ligero de `app/templates/home.html` para convertir la landing en una entrada más clara y orientada a decisiones.
- Mejora del copy y jerarquía visual en `app/templates/inicio.html`.
- Ajuste de textos globales en `app/templates/base.html`.
- Corrección de dos textos visibles en `app/templates/career.html`.
- Sustitución de `style="display:none"` por clases/atributos más consistentes en `app/templates/analisis.html`.
- Mejora del texto del precheck de Yahoo Finance en `app/templates/analisis.html`.
- Limpieza y consolidación de estilos duplicados de la landing en `app/static/estilos.css`.
- Creación de estilos reutilizables para `hero__actions`, `hero--split`, nueva landing y mejor comportamiento responsive.

## Iteración 02. Mojibake visible y feedback UI básico

### Objetivo de la iteración
Corregir errores visibles de textos rotos y reducir incoherencias claras de feedback, sin tocar la lógica del simulador.

### Cambios aplicados
- Sustitución de `alert()` por toasts reutilizables en interacciones de:
  - copiar URL
  - listado de empresas
  - historial
  - ordenación y recarga de tablas
- Mejora del sistema de toasts en `app/static/app.js` para que cree el contenedor si no existe en la página actual.
- Corrección de textos visibles con mojibake en `app/career.py` para errores y mensajes que pueden llegar al usuario.
- Corrección de bloques visibles de observaciones y resumen en `app/data/analisis.json`.
- Corrección parcial de textos visibles/documentales en `app/routes.py` relacionados con análisis e historial.

## Iteración 03. Preparación mínima para Render

### Objetivo de la iteración
Comprobar si la aplicación puede desplegarse en Render con configuración simple y aplicar solo el ajuste mínimo imprescindible para evitar fallos de arranque.

### Hallazgos
- `run.py` ya expone un objeto WSGI válido: `app = create_app()`.
- `gunicorn` ya está incluido en `requirements.txt`.
- No se detecta dependencia obligatoria de variables de entorno para arrancar.
- Sí se detecta un problema real de despliegue: `requirements.txt` estaba codificado en UTF-16.

### Cambio mínimo aplicado
- Conversión de `requirements.txt` a UTF-8 para que Render pueda instalar dependencias correctamente con `pip install -r requirements.txt`.

### Configuración recomendada para Render
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn run:app`
- **Variables de entorno obligatorias:** ninguna
- **Variables opcionales recomendables:** ninguna imprescindible para arrancar

### Estado tras la iteración
Con el ajuste aplicado, el proyecto queda razonablemente preparado para un despliegue básico en Render, sin tocar la lógica del simulador.
