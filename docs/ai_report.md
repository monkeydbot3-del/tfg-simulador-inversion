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

Pero el nivel visual todavía se percibía como “funcional” más que como producto pulido:
- landing simple y algo plana en jerarquía visual
- densidad visual alta en pantallas complejas
- falta de sistema visual más robusto para estados, feedback y bloques informativos
- componentes heterogéneos entre páginas

### Consistencia de interfaz
Puntos buenos:
- existe un layout base común
- botones y cards reaparecen de forma consistente en varias vistas
- la navegación principal está unificada

Problemas detectados antes de esta iteración:
- había todavía estilos inline en partes del frontend
- convivían modales, toasts y componentes heredados
- textos, tono y microcopy no siempre compartían la misma voz
- el modo carrera seguía teniendo una complejidad visual superior al resto

### UX y navegación
Fortalezas:
- la estructura principal se entiende
- el usuario tiene modos diferenciados: práctica, carrera, manual
- existe contenido educativo y manual amplio

Fricciones previas:
- el modo análisis seguía teniendo bastante carga para usuarios novatos
- la navegación entre aprendizaje, análisis, historial y carrera podía sentirse fragmentada
- el manual sigue siendo muy largo dentro de la interfaz
- aún quedaban incoherencias visibles de microcopy y estilo

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

## Iteración 04. Dirección visual más ambiciosa y profesional

### Objetivo de la iteración
Aplicar una primera iteración visual importante basada en principios actuales de diseño de producto web, manteniendo el proyecto defendible académicamente, sobrio y funcional.

### Referencias y principios investigados
Aunque varias URLs concretas devolvieron 404 o contenido mínimo, la investigación permitió apoyarse en líneas de diseño ampliamente aceptadas en producto digital actual y en el enfoque de Material Design 3:
- **Jerarquía visual fuerte**: títulos claros, subtítulos útiles, agrupación visual por niveles y acciones primarias destacadas.
- **Espaciado consistente**: más aire entre secciones, separación nítida entre bloques funcionales y reducción de densidad innecesaria.
- **Sistema de superficies**: uso de cards, paneles y capas suaves para estructurar la información sin ruido.
- **Controles más escaneables**: formularios con mejor agrupación, etiquetas claras, ayudas breves y foco visual más fuerte.
- **Tablas más legibles**: encabezados más claros, ritmo de filas más limpio y hover sutil para exploración.
- **Navegación con identidad**: cabecera más sólida, marca visual simple y enlaces con mejor feedback.
- **Estética de producto sobria**: nada extravagante, pero sí más cercana a una app moderna y cuidada.

### Dirección visual elegida
Se elige una dirección visual tipo **producto moderno y académico**, con estas características:
- paleta original conservada pero mejor refinada
- fondos más ricos y menos planos
- superficies blancas o translúcidas suaves
- sombras contenidas pero más sofisticadas
- bloques de hero más editoriales
- badges, callouts y tarjetas informativas para reforzar comprensión
- diseño más consistente entre landing, práctica, exploración y análisis

### Cambios aplicados
#### 1. Navegación y marco global
- Rediseño de `app/templates/base.html` para incorporar una identidad de marca más sólida en cabecera.
- Añadido un bloque de marca con icono textual y subtítulo de producto.
- Mejora del aspecto general de la top nav para acercarla a una interfaz más profesional.

#### 2. Home / landing
- Rediseño más ambicioso de `app/templates/home.html`.
- Hero principal más rico, con badge de contexto, mensajes más claros y dos llamadas a la acción principales.
- Nuevo panel lateral de valor con resumen del propósito de la app.
- Añadido un bloque de métricas o capacidades resumidas para hacer la propuesta más visual y escaneable.
- Se mantienen los tres accesos principales, pero con mejor envoltorio visual.

#### 3. Pantalla de inicio del modo práctica
- Mejora de `app/templates/inicio.html` con hero más orientado a producto.
- Inclusión de un bloque lateral explicando qué puede hacer el usuario en esta sección.
- Añadido un `info-strip` con beneficios concretos del rediseño, reforzando jerarquía y lectura rápida.

#### 4. Pantalla de ejemplos de empresas
- Mejora de `app/templates/empresas.html` con cabecera más editorial y badge contextual.
- Refinamiento del contenedor principal y del panel de acciones.
- Tabla presentada dentro de una superficie más cuidada y coherente con el resto del sistema visual.

#### 5. Pantalla de nuevo análisis
- Rediseño de `app/templates/analisis.html` para hacerlo más guiado y menos plano.
- Nuevo bloque introductorio con callout lateral para preparar al usuario antes de rellenar el formulario.
- Selector de modo de inversión rehecho como control segmentado más expresivo y profesional.
- Tarjetas más elevadas para bloques funcionales.
- Nueva barra de envío con mejor contexto y cierre visual del flujo.

#### 6. Sistema visual CSS
- Ampliación importante de `app/static/estilos.css`.
- Se añaden tokens visuales y mejoras de:
  - fondos de página
  - navegación
  - marca
  - héroes y paneles
  - cards elevadas
  - badges y callouts
  - tablas
  - layouts responsive
  - submit bars y bloques informativos
- Resultado: una experiencia visual más cohesionada y claramente más “producto”.

### Impacto del rediseño
El resultado de esta iteración no cambia la lógica del simulador, pero sí mejora de forma notable:
- la percepción de calidad del producto
- la legibilidad del contenido
- la claridad de acciones principales
- la consistencia entre pantallas
- la sensación de proyecto final más cuidado y presentable ante evaluación académica

### Estado tras la iteración
La aplicación sigue preparada para Render con la misma configuración ya validada:
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn run:app`
- **Variables de entorno obligatorias:** ninguna
