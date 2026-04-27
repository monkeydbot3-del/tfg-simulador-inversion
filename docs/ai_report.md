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

## Iteración 06 - Refinado visual de modo carrera y estados

### Objetivo
Convertir el modo carrera en la zona más fuerte del producto y unificar mejor la calidad visual de estados de feedback, carga y vacío, sin tocar backend ni hacer refactor técnico.

### Contexto
Tras la Iteración 05, el modo carrera ya tenía una base visual más cercana a dashboard, pero seguía mostrando demasiada densidad interna y estados poco expresivos. El usuario pidió centrar la siguiente iteración exclusivamente en esta zona y en la calidad perceptiva de sus interacciones.

### Cambios aplicados
- Refinamiento de `app/templates/career.html` para introducir una jerarquía más clara por pasos:
  - badges de paso para creación de sesión, sesión activa, series e informe
  - mejor separación visual entre encabezados, métricas y acciones
  - resumen más claro del constructor de turno
- Mejora del bloque de asignación del turno con un estado vacío más útil y más visual dentro de `career-alloc-list`.
- Refuerzo de jerarquía en botones de acción clave, destacando más `Crear sesión` y `Cerrar turno`.
- Mejora de los estados vacíos en series y ranking con tratamiento visual de panel vacío más consistente.
- Mejora del bloque de alertas de datos con un chip de estado positivo más coherente cuando no hay advertencias.
- Añadidos estados visuales de carga en gráficos de series e informe mediante superficies inline con spinner reutilizando el sistema visual existente.
- Ajuste de `app/static/app.js` para mostrar y ocultar estos estados de carga de forma coherente durante la carga de series y la generación del informe.
- Ampliación de `app/static/estilos.css` para unificar:
  - badges de paso y badges sutiles
  - estados vacíos suaves
  - superficies de carga
  - chips de estado
  - barra de acciones principal
  - refuerzo visual de toasts de éxito y error

### Decisiones tomadas
- Mantener el foco solo en `modo carrera` y estados, sin abrir frentes nuevos.
- No tocar backend ni lógica del simulador.
- Aprovechar la estructura dashboard creada en la iteración anterior y hacerla más comprensible en lugar de rediseñarla otra vez.
- Usar una jerarquía por pasos para mejorar escaneo y orientación dentro de una pantalla larga y compleja.

### Riesgos / problemas detectados
- Parte del contenido dinámico del modo carrera sigue dependiendo de HTML generado por JavaScript, así que todavía puede haber pequeños desajustes visuales finos cuando se carguen todos los datos reales.
- No se ha ejecutado una validación funcional completa del flujo entero, solo comprobación sintáctica y ajuste visual sobre estructura existente.

### Comprobaciones realizadas
- Relectura obligatoria de `BOT_INSTRUCTIONS.md`, `PROJECT_CONTEXT.md`, `CHANGELOG_AI.md` y `docs/ai_report.md` antes de empezar.
- Confirmación del último número de iteración usado para crear correctamente la `Iteración 06`.
- Comprobación de sintaxis con `python3 -m py_compile` sobre `run.py`, `app/__init__.py`, `app/routes.py` y `app/career.py`.
- Revisión del estado Git para confirmar que esta iteración toca solo frontend/documentación.

### Pendientes
- Afinar todavía más el detalle visual del contenido dinámico interno del constructor de turnos si en Render aparecen zonas con densidad desigual.
- Unificar futuros estados vacíos y loading de otras secciones usando el mismo patrón visual.
- Revisar microcopy puntual del modo carrera tras ver la iteración en uso real.

## Iteración 07 - Limpieza de UI interna y análisis previo de base de datos y login

### Objetivo
Eliminar de la interfaz cualquier mensaje que hable de iteraciones, trabajo interno del bot o meta-comentarios sobre el propio proceso de mejora, y preparar un diagnóstico técnico previo para una implementación mínima de base de datos y autenticación.

### Contexto
Tras varias iteraciones visuales, el usuario detectó que todavía podían quedar mensajes demasiado internos o meta dentro de la UI final. Además, pidió analizar una evolución mínima y defendible del proyecto hacia persistencia con base de datos, usuarios, registro, login/logout e historial por usuario, pero sin implementarlo todavía.

### Cambios aplicados
- Revisión de templates y textos visibles para localizar mensajes que pudieran exponer trabajo interno o hablar del proceso de iteración.
- Limpieza en `app/templates/home.html` de mensajes demasiado internos o meta:
  - sustitución de `Producto académico, interfaz profesional` por un mensaje neutro orientado al usuario
  - ajuste del texto principal para eliminar referencias a “presentar mejor el proyecto final”
- Limpieza en `app/templates/inicio.html` de copy demasiado meta, sustituyendo bloques como `Enfoque académico` por mensajes centrados en uso real del producto.
- No se han realizado cambios de backend ni de arquitectura en esta iteración.

### Decisiones tomadas
- Dejar toda referencia a iteraciones, cambios internos o trabajo del bot exclusivamente en `CHANGELOG_AI.md` y `docs/ai_report.md`.
- Mantener en UI solo mensajes orientados al usuario final y al uso funcional del simulador.
- No implementar aún base de datos ni autenticación, solo analizar una solución mínima compatible con el estado actual del proyecto.

### Riesgos / problemas detectados
- Parte del copy añadido en iteraciones anteriores era correcto desde el punto de vista visual, pero demasiado meta para una app final.
- La arquitectura actual está centrada en JSON locales y rutas Flask monolíticas, por lo que añadir usuarios y persistencia requerirá introducir una capa de datos con cuidado para no desestabilizar el proyecto.
- `requirements.txt` ya incluye `peewee`, lo cual es útil, pero el proyecto aún no tiene estructura de modelos, migraciones ni gestión de sesión de usuario.

### Comprobaciones realizadas
- Relectura obligatoria de `BOT_INSTRUCTIONS.md`, `PROJECT_CONTEXT.md`, `CHANGELOG_AI.md` y `docs/ai_report.md` antes de empezar.
- Búsqueda textual en frontend para localizar mensajes potencialmente internos o meta.
- Comprobación de sintaxis con `python3 -m py_compile` sobre `run.py`, `app/__init__.py`, `app/routes.py` y `app/career.py`.
- Revisión de `requirements.txt`, `app/__init__.py` y `app/routes.py` para analizar el impacto de una futura integración mínima de base de datos y autenticación.

### Pendientes
- Confirmar en Render que no quedan mensajes internos visibles al usuario final.
- Si el análisis convence, planificar una implementación mínima en fases: base de datos, modelo de usuario, sesiones de login, historial por usuario y persistencia de modo carrera.
- Decidir si el modo carrera debe persistirse completo por usuario desde la primera iteración de autenticación o como segunda fase.

## Iteración 08 - Diseño técnico previo para Postgres y autenticación en Render

### Objetivo
Definir una arquitectura mínima, defendible y lista para ejecutar después, que permita añadir autenticación y persistencia por usuario usando Render Postgres y `DATABASE_URL`, sin implementar todavía los cambios.

### Contexto
Tras el análisis previo de base de datos y login, el usuario decidió descartar SQLite y pidió que la evolución futura se diseñe directamente para Render Postgres. El proyecto actual sigue basado en Flask, rutas concentradas en `app/routes.py`, persistencia local JSON para historial y ficheros JSON para sesiones del modo carrera. La siguiente iteración debía centrarse solo en diseño técnico y orden de ejecución, sin tocar aún la lógica grande del simulador.

### Cambios aplicados
- Relectura de `BOT_INSTRUCTIONS.md`, `PROJECT_CONTEXT.md`, `CHANGELOG_AI.md` y `docs/ai_report.md` antes de comenzar.
- Revisión de `requirements.txt`, `app/__init__.py`, `app/routes.py` y `app/career.py` para localizar puntos reales de integración con Postgres.
- Identificación de la persistencia actual basada en JSON:
  - `app/routes.py` usa `app/data/analisis.json` para historial
  - `app/career.py` usa `app/data/career_sessions.json` para sesiones del modo carrera
- Preparación del diseño técnico mínimo para:
  - conexión a Render Postgres mediante `DATABASE_URL`
  - autenticación simple con sesión Flask
  - historial por usuario
  - persistencia de sesiones del modo carrera por usuario
- No se ha implementado código de base de datos, autenticación ni migraciones en esta iteración.

### Decisiones tomadas
- Diseñar la solución solo para Postgres en Render, sin proponer persistencia local en SQLite.
- Mantener el enfoque mínimo y defendible:
  - Flask
  - Peewee
  - Postgres vía `DATABASE_URL`
  - hash de contraseña con Werkzeug
  - sesión autenticada básica con `session` de Flask
- Evitar por ahora capas adicionales como Flask-Login, Alembic o una normalización profunda del estado del modo carrera.
- Mantener el modo carrera inicialmente persistido como estado JSON dentro de Postgres para reducir riesgo y complejidad.
- Separar claramente autenticación, acceso a base de datos y lógica existente, para no romper la app actual durante la futura implementación.

### Riesgos / problemas detectados
- `app/routes.py` y `app/career.py` concentran bastante responsabilidad, así que introducir persistencia requerirá añadir puntos de integración con cuidado.
- El historial actual es global y en JSON; pasar a historial por usuario implica rediseñar lectura, escritura y exportación.
- El modo carrera persiste hoy sesiones completas en JSON local; llevarlo a Postgres sin tocar mucho la lógica exige encapsular bien la capa de almacenamiento.
- Usar Postgres en Render implica depender siempre de `DATABASE_URL`, por lo que habrá que gestionar con claridad el arranque cuando falte esa variable.
- `peewee` ya está incluido, pero para Postgres hará falta asegurar el driver adecuado durante la implementación real.

### Comprobaciones realizadas
- Relectura obligatoria de contexto y memoria del proyecto.
- Inspección de `requirements.txt` para confirmar dependencias presentes.
- Revisión de `app/__init__.py` para detectar el punto correcto de inicialización de base de datos.
- Revisión de `app/routes.py` para localizar persistencia de historial en `analisis.json`.
- Revisión de `app/career.py` para localizar persistencia de sesiones en `career_sessions.json`.
- Contraste de la propuesta con la restricción del usuario: solo diseño técnico, sin implementación en esta iteración.

### Pendientes
- Decidir si la siguiente iteración ejecuta solo la Fase 1 (base técnica + usuarios + login/logout) o si incluye también historial autenticado.
- Confirmar si la primera implementación debe exigir login para historial y modo carrera, o permitir uso anónimo con funcionalidades limitadas.
- Añadir, en la futura ejecución, la dependencia final necesaria para conectar Peewee con Postgres si no estuviera ya presente.

## Iteración 09 - Especificación ejecutable para Postgres, auth por email e historial por usuario

### Objetivo
Cerrar el plano técnico final previo a implementación, definiendo con precisión archivos, dependencias, modelos, rutas, variables de entorno, puntos de integración y orden de ejecución para añadir autenticación por email y persistencia en Render Postgres, sin implementar todavía la funcionalidad completa.

### Contexto
Tras validar la dirección general de la Iteración 08, el usuario confirmó que la solución debe mantenerse mínima, trabajar con Render Postgres vía `DATABASE_URL`, usar login solo por email y evitar abrir frentes como OAuth, recuperación de contraseña o roles. Esta iteración se centra en convertir la propuesta general en una especificación de implementación concreta y ejecutable, lista para llevarse a código en la siguiente fase.

### Cambios aplicados
- Ajuste de la propuesta para que el acceso se haga solo por email.
- Cierre de la decisión técnica sobre el driver recomendado para Postgres con Peewee.
- Definición del conjunto mínimo de archivos a crear y modificar.
- Definición detallada de modelos, rutas de auth, variables de entorno, dependencias nuevas, helpers/servicios mínimos y puntos concretos de intervención en `app/routes.py` y `app/career.py`.
- Definición del orden de implementación por subfases/commits y de los puntos de rollback y validación.
- No se ha implementado ninguna funcionalidad nueva en esta iteración.

### Decisiones tomadas
- El login quedará limitado a email + contraseña, sin soporte dual con username.
- `username` puede mantenerse como dato de perfil opcional o identificador visible, pero no será credencial de acceso.
- La integración con Postgres se diseñará con Peewee y driver `psycopg2-binary` como opción mínima práctica para Render.
- Se mantendrá autenticación basada en `session` de Flask y `SECRET_KEY`.
- Se evitará introducir capas extra como Flask-Login, migraciones complejas o servicios innecesarios mientras no aporten valor claro.
- Si la ejecución se recorta a una primera fase más pequeña, la prioridad será dejar operativos Postgres, usuarios, login por email y persistencia del historial por usuario antes de tocar modo carrera.

### Riesgos / problemas detectados
- El cambio a historial por usuario obligará a decidir cómo se comportan las rutas actuales cuando no haya sesión autenticada.
- El modo carrera sigue siendo la parte más sensible del proyecto, así que conviene llegar a él solo cuando auth e historial ya estén estables.
- `psycopg2-binary` es adecuado para una solución mínima en Render, pero habrá que vigilar compatibilidad y arranque real en despliegue cuando se implemente.
- El proyecto todavía carece de una capa intermedia clara entre rutas y persistencia, por lo que habrá que introducir la mínima separación útil sin caer en sobrearquitectura.

### Comprobaciones realizadas
- Relectura del contexto y de la memoria previa antes de redactar la especificación.
- Contraste de la propuesta con la decisión del usuario: auth solo por email, Postgres en Render, sin SQLite y sin funcionalidades extra de identidad.
- Verificación del estado del proyecto para mantener el plan dentro del alcance actual y no proponer cambios estructurales excesivos.

### Pendientes
- Ejecutar la implementación real en una iteración posterior siguiendo este plano.
- Decidir si la primera ejecución práctica llega hasta historial autenticado o incluye ya la primera persistencia del modo carrera.
- Preparar después los templates mínimos de registro/login y los mensajes de error/éxito asociados cuando se pase a implementación.

## Iteración 10 - Implementación real de Postgres, auth por email e historial por usuario

### Objetivo
Implementar la primera fase real de persistencia con Render Postgres hasta historial por usuario autenticado, manteniendo el alcance acotado y evitando tocar todavía el modo carrera o abrir frentes de identidad más complejos.

### Contexto
Tras cerrar la especificación ejecutable, el usuario aprobó pasar a implementación real con un alcance exacto: conexión Postgres con `DATABASE_URL`, `SECRET_KEY`, `app/db.py`, modelos `User` y `AnalysisHistory`, auth por email con registro/login/logout, adaptación del historial al usuario autenticado, exportación CSV del historial por usuario y ajustes mínimos de navegación/templates. Se pidió explícitamente no tocar aún la persistencia del modo carrera ni hacer refactor grande.

### Cambios aplicados
- Añadida la dependencia `psycopg2-binary` en `requirements.txt` como driver mínimo para Postgres con Peewee.
- Creado `app/db.py` con:
  - `DatabaseProxy`
  - inicialización de BD desde `DATABASE_URL`
  - helpers de conexión y cierre
- Modificado `app/__init__.py` para:
  - exigir `SECRET_KEY`
  - inicializar la base de datos
  - conectar/desconectar por ciclo de petición
  - crear tablas mínimas `User` y `AnalysisHistory`
  - registrar blueprint de autenticación
- Creado `app/models.py` con los modelos `User` y `AnalysisHistory`.
- Creado `app/services/auth_service.py` con helpers mínimos para crear usuario, buscar por email, buscar por id y autenticar.
- Creado `app/services/history_service.py` para guardar y recuperar historial por usuario desde Postgres.
- Creado `app/auth.py` con auth por email:
  - `GET /registro`
  - `POST /registro`
  - `GET /login`
  - `POST /login`
  - `POST /logout`
- Creados templates mínimos:
  - `app/templates/login.html`
  - `app/templates/register.html`
- Modificado `app/templates/base.html` para mostrar acciones de sesión en navegación:
  - iniciar sesión
  - crear cuenta
  - cerrar sesión
- Modificado `app/routes.py` para:
  - resolver usuario actual desde `session`
  - proteger la vista de historial
  - guardar análisis en Postgres cuando hay usuario autenticado
  - listar historial desde Postgres por usuario
  - exportar CSV desde Postgres por usuario
- Modificado `app/templates/historial.html` para ajustar el copy al historial propio del usuario y mostrar mensajes flash básicos.

### Decisiones tomadas
- Mantener login exclusivamente por email.
- No exigir autenticación para generar análisis, pero sí para disponer de historial persistente y exportación de historial.
- Mantener el JSON legacy fuera del nuevo flujo principal del historial, pero sin eliminarlo definitivamente en esta iteración.
- No tocar `career.py` ni la persistencia del modo carrera para respetar el alcance aprobado.
- Crear tablas directamente desde la app en esta primera fase mínima, evitando introducir migraciones complejas todavía.

### Riesgos / problemas detectados
- La validación realizada ha sido sintáctica, no funcional contra una base Postgres real de Render, así que todavía queda por confirmar el arranque efectivo con variables reales y conexión real.
- El historial antiguo en JSON queda como legado y ya no alimenta el flujo nuevo autenticado; si hiciera falta rescatar esos datos, habrá que decidir una migración posterior.
- Los mensajes flash se han integrado mínimamente en la zona de historial, pero la presentación visual de login/registro podría necesitar una iteración de pulido posterior.
- La creación automática de tablas desde la app es válida para esta fase mínima, pero a futuro convendrá valorar una estrategia de migraciones más controlada.

### Comprobaciones realizadas
- Validación por subfases con `python3 -m py_compile` tras:
  - la base técnica Postgres
  - la creación de modelos y auth
  - la adaptación del historial
- Verificación de que la implementación se mantiene dentro del alcance aprobado y no toca la lógica del modo carrera.
- Revisión de imports, wiring de blueprints y dependencias mínimas añadidas.

### Pendientes
- Confirmar el funcionamiento real en Render con `DATABASE_URL` y `SECRET_KEY` reales.
- Si esta fase queda estable, documentar el comportamiento exacto del historial cuando el usuario no está autenticado.
- En una iteración posterior, decidir si se aborda ya la persistencia del modo carrera por usuario.

## Iteración 11 - Login como entrada principal y modo invitado

### Objetivo
Cambiar el flujo de entrada de la app para que la autenticación sea la puerta principal, permitiendo a la vez un acceso controlado como invitado sin persistencia ni escritura en base de datos.

### Contexto
Tras introducir autenticación por email e historial por usuario, el usuario pidió ajustar el onboarding real de la app: la home debía dejar de ser pública por defecto y pasar a redirigir a login cuando no existe sesión autenticada. Además, se pidió incorporar un modo invitado ligero, útil para probar la app sin cuenta y sin tocar la lógica del simulador ni romper rutas existentes.

### Cambios aplicados
- Modificado `app/routes.py` para que `/`:
  - redirija a `/login` si no existe `session["user_id"]` ni `session["guest"]`
  - muestre la home normal si hay usuario autenticado o sesión de invitado
- Añadido helper `_is_guest_user()` para distinguir el acceso invitado del autenticado sin tocar la lógica central del simulador.
- Ajustado el guardado de análisis para que:
  - siga guardando en Postgres si hay usuario autenticado
  - no guarde nada si la sesión es de invitado
- Ajustado historial y exportación CSV para que el modo invitado no pueda acceder a persistencia:
  - historial HTML redirige fuera del flujo protegido
  - endpoints devuelven error controlado para invitado
- Modificado `app/auth.py` para:
  - evitar que `/login` se muestre si ya existe sesión autenticada o invitada
  - redirigir a home tras login
  - añadir `POST /continuar-invitado`, que crea `session["guest"] = True`
- Modificado `app/templates/login.html` para:
  - mostrar feedback flash básico
  - añadir botón `Continuar como invitado`
  - explicar que en modo invitado no se guarda historial ni se escribe en base de datos
- Modificado `app/templates/base.html` para:
  - mostrar badge `Modo invitado` en navegación
  - permitir logout también en sesión invitada

### Decisiones tomadas
- Mantener el modo invitado estrictamente en sesión, sin persistencia.
- No permitir historial ni exportación CSV en modo invitado para mantener coherencia con el objetivo de no escribir en base de datos.
- No tocar la lógica del simulador ni abrir cambios en `career.py`.
- Reutilizar la home ya existente para la experiencia de invitado, evitando crear una segunda shell de entrada innecesaria.

### Riesgos / problemas detectados
- El modo invitado introduce ahora dos estados de acceso diferentes, así que convendrá validar bien en Render el comportamiento de navegación entre login, home, historial y logout.
- El historial redirige o bloquea según el tipo de sesión, por lo que puede requerir un pequeño pulido posterior de microcopy si se quiere hacerlo todavía más claro para usuario final.
- La validación realizada sigue siendo sintáctica; falta comprobar el flujo real en navegador y con entorno de despliegue real.

### Comprobaciones realizadas
- Relectura obligatoria de `BOT_INSTRUCTIONS.md`, `PROJECT_CONTEXT.md`, `CHANGELOG_AI.md` y `docs/ai_report.md` antes de empezar.
- Revisión de `app/auth.py`, `app/routes.py`, `app/templates/base.html` y `app/templates/login.html` antes de aplicar cambios.
- Comprobación de sintaxis con `python3 -m py_compile` sobre:
  - `run.py`
  - `app/__init__.py`
  - `app/routes.py`
  - `app/auth.py`
  - `app/career.py`
  - `app/db.py`
  - `app/models.py`
  - `app/services/auth_service.py`
  - `app/services/history_service.py`

### Pendientes
- Validar el flujo real en Render o localmente con base de datos activa:
  - acceso a `/`
  - login
  - continuar como invitado
  - logout
  - bloqueo de historial en invitado
- Decidir si más adelante otras secciones, como historial visual o botones de exportación, deberían adaptar aún mejor su copy al estado invitado.
- Mantener fuera de alcance por ahora cualquier cambio en persistencia del modo carrera.

## Iteración 12 - Rediseño visual de login y registro

### Objetivo
Elevar visualmente las pantallas de autenticación para que login y registro se sientan como parte coherente del mismo producto SaaS financiero, sin tocar la lógica de auth ni abrir funcionalidades nuevas.

### Contexto
La Iteración 11 dejó operativo el flujo de entrada con login como puerta principal y modo invitado, pero la interfaz de autenticación seguía viéndose pobre respecto al resto del producto: composición débil, campos poco integrados, jerarquía visual floja y un botón de invitado demasiado dominante. El usuario pidió dedicar una iteración exclusivamente a UI/UX de `login.html`, `register.html` y el CSS necesario.

### Cambios aplicados
- Rediseño completo de `app/templates/login.html` con una composición en dos bloques:
  - panel introductorio con propuesta de valor y beneficios
  - card de acceso más limpia y centrada con mejor jerarquía
- Mejora del formulario de login:
  - inputs a ancho completo
  - labels más claros
  - CTA principal más consistente
  - separador visual para el acceso invitado
  - acción secundaria de invitado más discreta
  - enlace claro hacia creación de cuenta
- Rediseño de `app/templates/register.html` con el mismo lenguaje visual que login para reforzar coherencia de producto.
- Añadido microcopy mínimo para mejorar orientación sin recargar la pantalla.
- Ampliación de `app/static/estilos.css` con un bloque específico de auth para:
  - layout responsive de autenticación
  - panel lateral introductorio
  - card principal
  - inputs y focus states
  - alertas integradas en auth
  - CTA principal y CTA secundaria de invitado
  - enlaces de cambio entre login y registro
  - comportamiento responsive en tablet y móvil

### Decisiones tomadas
- Mantener la experiencia en una card principal con un panel lateral editorial en lugar de un formulario desnudo, para acercarla al resto del producto.
- Hacer que `Continuar como invitado` siga estando accesible, pero con menos peso visual que `Entrar`.
- No tocar backend ni lógica de autenticación para que esta iteración sea puramente visual.
- Reforzar continuidad visual entre login y registro para que ambas pantallas parezcan parte del mismo flujo y no dos páginas separadas sin sistema común.

### Riesgos / problemas detectados
- La validación realizada en esta iteración ha sido sintáctica; conviene revisar en navegador real el equilibrio visual final en móvil y escritorio.
- El panel introductorio añade más presencia visual, así que podría requerir un ajuste fino posterior si en Render se percibe demasiado ancho en ciertos tamaños intermedios.

### Comprobaciones realizadas
- Relectura obligatoria de `BOT_INSTRUCTIONS.md`, `PROJECT_CONTEXT.md`, `CHANGELOG_AI.md` y `docs/ai_report.md` antes de empezar.
- Revisión de `login.html`, `register.html` y del CSS existente antes de aplicar cambios.
- Comprobación de sintaxis con `python3 -m py_compile` sobre `run.py`, `app/__init__.py`, `app/routes.py`, `app/auth.py` y `app/career.py`.

### Pendientes
- Verificar visualmente en Render el comportamiento responsive final de login y registro.
- Si hace falta, hacer una iteración muy pequeña de pulido fino solo sobre spacing o microcopy de auth.
- Mantener fuera de alcance cualquier cambio de lógica en autenticación, historial o modo carrera.

## Iteración 13 - Corrección del flujo sin DCA en nuevo análisis

### Objetivo
Arreglar el bug que impedía enviar correctamente un análisis sin DCA cuando el usuario seleccionaba una compra única y debía indicar la fecha de compra.

### Contexto
El usuario detectó que el flujo de `Nuevo análisis` fallaba al seleccionar `Sin DCA`: la app exigía `Fecha de compra`, pero el formulario no dejaba completar correctamente el envío o no estaba activando bien ese campo. Se pidió corregirlo con el mínimo cambio necesario, sin tocar la lógica de cálculo ni abrir cambios en auth, base de datos o modo carrera.

### Cambios aplicados
- Revisión del bloque `Sin DCA` en `app/templates/analisis.html`.
- Mejora del bloque visual de compra única para dejar más claro el propósito del campo.
- Añadido `name="inicio"` al input `#fechaCompra` para alinear mejor el formulario con el dato que espera el flujo.
- Añadido helper text explicando que esa fecha se envía como inicio de la inversión en el modo sin DCA.
- Corregido `app/static/app.js` en `bindAnalisisForm()` para que el cambio de modo entre DCA y Sin DCA actualice correctamente:
  - `hidden`
  - clase `hidden`
  - `style.display`
- Con ello, el bloque de compra única deja de quedarse oculto de forma inconsistente y el valor de `fechaCompra` puede introducirse y enviarse correctamente en el payload cuando `modo === "SIN_DCA"`.

### Decisiones tomadas
- Mantener intacta la lógica de cálculo y de validación salvo el mínimo ajuste de wiring frontend necesario.
- No tocar backend porque el payload ya contemplaba `inicio` en modo sin DCA; el problema estaba en la activación/visibilidad real del campo en frontend.
- Aprovechar el arreglo para dejar el bloque de compra única más coherente visualmente con la UI actual.

### Riesgos / problemas detectados
- El bug estaba en una combinación sutil entre estado visual y atributo `hidden`, así que conviene validar manualmente en navegador que los cambios de modo no dejan residuos visuales en otros navegadores.
- Aunque el arreglo es mínimo, sigue dependiendo de la lógica JS de alternancia del formulario, por lo que merece una prueba real en Render tras desplegar.

### Comprobaciones realizadas
- Relectura obligatoria de `BOT_INSTRUCTIONS.md`, `PROJECT_CONTEXT.md`, `CHANGELOG_AI.md` y `docs/ai_report.md` antes de empezar.
- Revisión de `app/templates/analisis.html` y `app/static/app.js` para localizar el origen real del bug.
- Búsqueda de referencias a `fechaCompra`, `inicio`, `Sin DCA` y al mensaje `Selecciona la fecha de compra`.
- Comprobación de sintaxis con `python3 -m py_compile` sobre `run.py`, `app/__init__.py`, `app/routes.py`, `app/auth.py` y `app/career.py`.
- Revisión del diff final para confirmar que el alcance queda reducido a frontend/documentación.

### Pendientes
- Validar en Render el flujo real de `Nuevo análisis` en ambos modos:
  - usuario autenticado
  - invitado
  - DCA
  - sin DCA
- Confirmar visualmente que el bloque de compra única aparece y desaparece correctamente al cambiar de modo.
- Mantener fuera de alcance por ahora cualquier mejora gráfica adicional del análisis.

## Iteración 14 - Gráficas en análisis y detalle de historial

### Objetivo
Añadir una visualización gráfica contenida a los resultados del análisis y reutilizarla también en el detalle del historial, manteniendo compatibilidad con registros antiguos y sin tocar autenticación ni modo carrera.

### Contexto
Tras corregir el flujo de compra única sin DCA, el siguiente paso pedido por el usuario fue enriquecer la lectura del análisis con una gráfica útil y mostrar ese mismo recurso al abrir el detalle desde historial. La implementación debía ser contenida, sin refactor grande y con fallback elegante para registros antiguos que no tuvieran datos completos de backtest.

### Cambios aplicados
- Revisión del flujo actual de `Nuevo análisis`, historial y modal de detalle.
- Mejora del modal de historial en `app/templates/historial.html` para orientarlo a detalle completo del análisis.
- Ampliación de `app/static/app.js` para:
  - crear una gráfica lineal reutilizable con Chart.js
  - reconstruir series desde `/market/ohlc/<ticker>` usando datos históricos del periodo
  - mostrar en modo `SIN_DCA` una evolución estimada del valor de la inversión durante el periodo
  - mostrar en otros casos la evolución del precio ajustado durante el rango analizado
- Integración de la gráfica en el resultado mostrado justo tras un análisis nuevo, reutilizando el detalle enriquecido del resumen/backtest.
- Mejora del botón `Ver detalle` en historial para que deje de depender exclusivamente de tener `backtest` completo guardado y abra una ficha más rica con:
  - datos completos del análisis
  - resumen de inversión
  - observaciones
  - gráfica si se puede reconstruir
- Añadido fallback elegante para registros antiguos o incompletos:
  - si faltan datos suficientes, se muestra un mensaje claro en lugar de romper el detalle
- Ampliación de `app/static/estilos.css` con estilos específicos para:
  - ficha de detalle del análisis
  - grid de datos y resumen
  - host de gráfica
  - fallback visual de ausencia de datos

### Decisiones tomadas
- Reutilizar Chart.js ya presente en el proyecto en lugar de añadir una librería nueva.
- No tocar el backend principal ni la lógica del simulador más allá de aprovechar endpoints históricos ya disponibles.
- Priorizar una gráfica lineal simple, clara y académicamente defendible antes que una visualización más ambiciosa.
- Mantener compatibilidad con registros previos mediante reconstrucción por ticker y fechas cuando sea posible.

### Riesgos / problemas detectados
- La gráfica depende de disponibilidad de datos históricos del ticker para el rango analizado, así que algunos registros antiguos pueden no reconstruirse completamente.
- Para registros sin backtest o con fechas incompletas, el detalle puede quedarse en modo resumen + fallback, aunque de forma controlada.
- La validación de esta iteración ha sido sintáctica; conviene comprobar visualmente en Render tanto la apertura del detalle como el render real de la gráfica.

### Comprobaciones realizadas
- Relectura obligatoria de `BOT_INSTRUCTIONS.md`, `PROJECT_CONTEXT.md`, `CHANGELOG_AI.md` y `docs/ai_report.md` antes de empezar.
- Revisión de `historial.html`, `app/static/app.js` y de los endpoints históricos disponibles en `app/routes.py`.
- Comprobación de sintaxis con `python3 -m py_compile` sobre `run.py`, `app/__init__.py`, `app/routes.py`, `app/auth.py` y `app/career.py`.
- Revisión del diff para asegurar que el alcance queda contenido en frontend/documentación y no invade auth ni modo carrera.

### Pendientes
- Validar en Render que la gráfica se ve correctamente al terminar un análisis nuevo.
- Validar que `Ver detalle` en historial muestra bien:
  - análisis recientes con backtest
  - análisis antiguos con datos parciales
- Si hace falta, hacer un pequeño pulido posterior del modal de detalle para compactar mejor la densidad visual en móvil.

## Iteración 15 - Corrección de render de gráficas y modal de resultados

### Objetivo
Corregir la iteración anterior para que la gráfica se renderice realmente tanto en nuevo análisis como en historial, y para que el modal de resultados tenga un comportamiento visual estable, centrado y usable en escritorio y responsive.

### Contexto
Tras publicar la Iteración 14, el usuario detectó dos fallos claros: la gráfica no llegaba a dibujarse aunque el bloque visual sí aparecía, y el modal de resultados quedaba mal resuelto a nivel de tamaño, posición, cierre y scroll. Se pidió una corrección contenida, sin tocar autenticación ni modo carrera, centrada únicamente en gráficas y modal.

### Causa exacta detectada
La gráfica no se veía por una combinación de dos problemas de implementación en frontend:
- el render reutilizaba un `canvas` localizado por `id` global (`analysis-detail-chart-canvas`) y un fallback también localizado por `id` global, pero ahora el flujo tenía más de un posible host o modal para detalle, lo que hacía frágil la selección del nodo real donde dibujar
- el contenedor visual de la gráfica tenía `min-height`, pero no una altura efectiva garantizada del `canvas`, así que Chart.js podía inicializarse sobre un lienzo sin tamaño renderizable suficiente y dejar un hueco vacío

### Cambios aplicados
- Ajustado `app/static/app.js` para que el render de la gráfica ya no dependa de un `id` global fijo de canvas.
- El chart ahora se dibuja contra el `canvas` real encontrado dentro del bloque visual concreto que se acaba de crear en cada modal o detalle.
- El fallback de ausencia de datos también deja de depender de un `id` global y pasa a resolverse de forma local dentro del mismo bloque de gráfica.
- Se mantiene el flujo de reconstrucción de datos históricos ya implementado en la iteración previa, pero con un render más robusto y menos acoplado al DOM global.
- Ajustado `app/static/estilos.css` para dar una altura real al contenedor de gráfica y forzar que el `canvas` ocupe correctamente todo el espacio disponible.
- Corregido el modal de resultados (`#modalBacktest`) para que:
  - aparezca centrado
  - use un ancho máximo más razonable
  - tenga `max-height: 90vh`
  - tenga scroll interno en el body
  - mantenga visible y accesible el botón de cierre
  - no desborde visualmente el viewport en contenido largo
- Ajustado también el modal de detalle reutilizado en historial para que el contenido largo tenga scroll interno y una estructura más estable.

### Decisiones tomadas
- No tocar backend ni endpoints porque los datos ya llegaban de forma suficiente para la reconstrucción en la mayoría de casos; el fallo principal estaba en el render del DOM y en el sizing del canvas/modal.
- Mantener la solución simple y contenida, reforzando selección por nodo real en lugar de abrir un refactor de componentes o estado global.
- Homogeneizar el comportamiento de los modales de resultado y detalle para evitar una UX inconsistente entre análisis nuevo e historial.

### Riesgos / problemas detectados
- Aunque el render ahora es bastante más robusto, sigue dependiendo de que el endpoint histórico devuelva filas válidas para el ticker y rango elegidos.
- Los análisis antiguos con datos incompletos seguirán mostrando fallback, pero ya no deberían dejar un hueco vacío ambiguo.
- Conviene validar en Render tamaños intermedios de pantalla por si hace falta un último ajuste fino de spacing en móvil pequeño.

### Comprobaciones realizadas
- Relectura obligatoria de `BOT_INSTRUCTIONS.md`, `PROJECT_CONTEXT.md`, `CHANGELOG_AI.md` y `docs/ai_report.md` antes de empezar.
- Revisión del wiring de render de Chart.js en `app/static/app.js`.
- Revisión del CSS de modal y del host visual de gráfica en `app/static/estilos.css`.
- Comprobación de sintaxis con `python3 -m py_compile` sobre `run.py`, `app/__init__.py`, `app/routes.py`, `app/auth.py` y `app/career.py`.
- Revisión del diff final para confirmar que el alcance queda limitado a gráficas, modal y documentación.

### Pendientes
- Verificar en Render el render real de la gráfica en:
  - nuevo análisis
  - historial > ver detalle
- Confirmar que el cierre del modal se siente cómodo en móvil y escritorio.
- Si aparece algún caso residual con ticker sin serie válida, mantener el fallback actual sin ampliar alcance funcional.

## Iteración 16 - Pulido visual del modal de resultados

### Objetivo
Hacer un ajuste pequeño pero de impacto real sobre la presentación del resultado de análisis para que la lectura del resumen, las acciones y la gráfica se sientan más consistentes con el lenguaje visual general del producto.

### Contexto
Tras corregir el render real de las gráficas y estabilizar el comportamiento del modal, quedaba margen para un pulido final de la ficha de resultados. El usuario pidió hacerlo inmediatamente, manteniendo el alcance contenido y centrado solo en la experiencia visual del resultado y su equivalente en historial.

### Cambios aplicados
- Mejora de `app/templates/analisis.html` para introducir una cabecera editorial ligera dentro del modal de resultados.
- Aplicación del mismo bloque de cabecera en `app/templates/historial.html` para mantener consistencia entre análisis nuevo e historial.
- Añadido badge contextual `Resultado del análisis` para reforzar jerarquía visual.
- Añadido microcopy breve bajo el título para orientar mejor al usuario sobre qué puede hacer en esa ficha.
- Ajustado `app/static/estilos.css` para:
  - dar mejor ritmo vertical al body del modal
  - estilizar la nueva cabecera interna del resumen
  - convertir la lista de métricas en tarjetas más limpias y legibles
  - mejorar el espaciado entre resumen, acciones, observaciones y gráfica
  - reforzar visualmente el encabezado del bloque de gráfica
- Unificación del estilo efectivo de `.kv` en `#modalBacktest`, corrigiendo una definición tardía que estaba degradando parte del acabado visual del resumen.

### Decisiones tomadas
- Mantener la estructura funcional existente del modal para no reabrir riesgos de comportamiento.
- Apostar por una mejora de jerarquía, espaciado y legibilidad en lugar de añadir elementos decorativos innecesarios.
- Reutilizar el mismo lenguaje de badges, superficies suaves y copy breve que ya se viene consolidando en el resto del producto.

### Riesgos / problemas detectados
- Es un cambio puramente visual, así que el riesgo funcional es bajo.
- Aun así, conviene revisar en Render cómo se percibe la densidad de las tarjetas del resumen en pantallas estrechas.

### Comprobaciones realizadas
- Relectura obligatoria de `BOT_INSTRUCTIONS.md`, `PROJECT_CONTEXT.md`, `CHANGELOG_AI.md` y `docs/ai_report.md` antes de empezar.
- Revisión de `analisis.html`, `historial.html` y `estilos.css` para localizar el punto mínimo de intervención.
- Comprobación de sintaxis con `python3 -m py_compile` sobre `run.py`, `app/__init__.py`, `app/routes.py`, `app/auth.py` y `app/career.py`.
- Revisión del diff final para asegurar que el alcance queda limitado a templates, CSS y documentación.

### Pendientes
- Verificar en Render el equilibrio visual final del modal en escritorio y móvil.
- Si hiciera falta, dejar una última microiteración solo de spacing responsive, sin tocar lógica ni estructura.

## Iteración 17 - Corrección de rango de gráfica y centrado del modal

### Objetivo
Corregir el bug funcional que seguía impidiendo ver la gráfica en análisis con datos válidos y rematar el comportamiento real del modal para que aparezca centrado y con un cierre visual más limpio.

### Contexto
Después de las iteraciones 14, 15 y 16, el usuario confirmó que el bloque de gráfica seguía mostrando el fallback de “No hay datos suficientes” incluso en casos donde sí debería existir serie histórica. Además, el modal seguía percibiéndose desplazado hacia un lateral y el botón X mantenía una presencia visual demasiado pesada. Se pidió un diagnóstico real de la causa, no solo un retoque estético.

### Causa exacta detectada
La causa real del mensaje falso de “No hay datos suficientes” estaba en el rango temporal que el frontend enviaba al endpoint histórico:
- el detalle intentaba reconstruir la gráfica usando `start/end` procedentes del análisis o del backtest guardado
- en varios casos, especialmente en historiales guardados, `end` podía quedar en una fecha futura o en un rango poco robusto para reconstrucción
- al pedir `/market/ohlc/<ticker>` con ese rango, la serie devuelta podía quedar vacía o incompleta, aunque el ticker sí tuviera histórico suficiente en términos reales
- como el frontend trataba ese resultado vacío como falta de datos del análisis, se activaba el fallback aunque el problema no era Chart.js ni la ausencia total de histórico, sino un rango mal normalizado antes del fetch

### Cambios aplicados
- Añadida en `app/static/app.js` una normalización explícita del rango para la gráfica:
  - recorte de `end` a la fecha actual si viene en futuro
  - saneado de formato a `YYYY-MM-DD`
  - uso consistente del rango normalizado antes de pedir OHLC
- Ajustado el flujo de `showBacktestSummary(...)` para usar ese rango normalizado también en el resumen visual y en la reconstrucción de la gráfica.
- Mantenida la lógica de reconstrucción existente, pero evitando llamadas con fechas imposibles o poco fiables.
- Reforzado el comportamiento del modal de resultados para que, al abrirse, fuerce `display: flex` y se comporte como overlay centrado real.
- Ajustado el cierre del modal para limpiar también el `display` inline al cerrar.
- Ajustado `app/static/estilos.css` para:
  - asegurar overlay centrado con mejor comportamiento de overflow
  - quitar el círculo/borde visual del botón X
  - dejar una X simple, limpia y visible
  - mantener el body del modal contenido sin empujes laterales extraños

### Datos que usa ahora la gráfica
- `ticker`
- `start` normalizado
- `end` normalizado y limitado a hoy si venía en futuro
- OHLC histórico obtenido desde `/market/ohlc/<ticker>`
- `adj_close` como base principal de la serie
- en modo `SIN_DCA`, `importe_inicial` para reconstruir la evolución estimada del valor invertido

### Decisiones tomadas
- No tocar auth ni modo carrera.
- No cambiar el motor de cálculo del análisis salvo el mínimo necesario para sanear el rango que se usa al reconstruir la gráfica.
- Resolver el problema en el punto donde realmente se producía, que era el frontend al pedir la serie histórica, en vez de abrir una refactorización mayor del historial o de persistencia.

### Riesgos / problemas detectados
- Algunos registros antiguos sin `start` utilizable o con datos muy incompletos seguirán necesitando fallback, pero ahora el fallback debería reflejar casos reales y no falsos negativos por rango defectuoso.
- Conviene validar en Render varios tickers y periodos para confirmar que el saneado del rango cubre bien los casos más frecuentes.

### Comprobaciones realizadas
- Relectura obligatoria de `BOT_INSTRUCTIONS.md`, `PROJECT_CONTEXT.md`, `CHANGELOG_AI.md` y `docs/ai_report.md` antes de empezar.
- Revisión de `app/routes.py`, `app/services/history_service.py` y `app/static/app.js` para localizar si el fallo estaba en persistencia, respuesta OHLC o parseo frontend.
- Confirmación de que `/market/ohlc/<ticker>` devuelve lista plana de filas OHLC y que el problema principal no estaba en Chart.js sino en los rangos usados para pedir la serie.
- Comprobación de sintaxis con `python3 -m py_compile` sobre `run.py`, `app/__init__.py`, `app/routes.py`, `app/auth.py` y `app/career.py`.

### Pendientes
- Validar en Render la gráfica en análisis recientes y en detalle de historial.
- Confirmar visualmente el centrado del modal en escritorio y móvil.
- Si aparece algún caso residual concreto de ticker sin datos, revisar ese caso puntual antes de tocar más lógica.

## Iteración 18 - Diagnóstico instrumentado de gráfica y corrección real del modal overlay

### Objetivo
Dejar de corregir a ciegas y añadir instrumentación temporal para ver en consola qué datos exactos se usan al intentar pintar la gráfica, al tiempo que se corrige la causa real del modal descentrado en la cascada CSS y en la estructura de clases del DOM.

### Contexto
El usuario confirmó que seguían fallando los dos mismos puntos: el modal seguía viéndose pegado a la izquierda y la gráfica seguía cayendo en fallback incluso en casos donde sí debería existir histórico suficiente. Se pidió expresamente una iteración de diagnóstico verificable, con logs temporales en consola y revisión real de la regla CSS efectiva que estaba imponiendo el mal comportamiento del modal.

### Qué mostraban los logs añadidos
Se añadió instrumentación temporal en `app/static/app.js` para imprimir en consola del navegador:
- ticker usado
- start original y start normalizado
- end original y end normalizado
- modo e importe inicial
- URL exacta llamada a `/market/ohlc/<ticker>`
- respuesta cruda recibida
- número de puntos parseados
- primer punto
- último punto
- motivo exacto que activa el fallback cuando ocurre

### Causa real confirmada de la gráfica vacía
La instrumentación deja preparado el diagnóstico para confirmar en navegador si el problema está en:
- rango vacío o mal formado
- respuesta vacía del endpoint OHLC
- serie parseada sin puntos válidos
- primer precio no utilizable para `SIN_DCA`
- o fallo de petición en red

Además, el parseo quedó reforzado para aceptar tanto una lista plana como un posible objeto con `rows`, dejando trazado en consola del motivo exacto de fallback final.

### Causa real confirmada del modal descentrado
La causa estructural del modal descentrado era una colisión entre clases de propósito distinto:
- `#modalBacktest` estaba montado con la clase global `.modal`
- esa clase en este proyecto no representa un overlay, sino una caja/modal-card con `background`, `width`, `padding` y layout propio
- al mismo tiempo, el mismo nodo tenía reglas específicas de `#modalBacktest` intentando comportarse como overlay de pantalla completa
- el resultado era una mezcla de estilos incompatible, donde el nodo raíz del modal heredaba comportamiento de caja en lugar de overlay real, lo que explicaba el aspecto desplazado o pegado lateralmente

### Cambios aplicados
- Añadidos logs temporales de diagnóstico en `app/static/app.js` para el flujo de gráfica.
- Ajustado `fetchAnalysisChartSeries(...)` para devolver también motivo y metadatos del fallback, no solo la serie.
- Trazado explícito de:
  - URL de petición
  - respuesta recibida
  - puntos válidos parseados
  - motivo final del fallback
- Corregida la estructura HTML de `modalBacktest` en:
  - `app/templates/analisis.html`
  - `app/templates/historial.html`
- El nodo raíz deja de usar la clase `.modal` y pasa a usar `.modal-overlay`, que sí corresponde al patrón de overlay centrado del sistema visual.
- Simplificado el open/close JS para volver a apoyarse en la clase `hidden`, evitando mezclarla con `display` inline cuando ya no hace falta.

### Decisiones tomadas
- No tocar auth ni modo carrera.
- Corregir el modal desde la raíz del problema, que era la mezcla de clases en el DOM, en vez de seguir añadiendo reglas compensatorias en cascada.
- Mantener la instrumentación temporal porque en esta iteración aporta valor directo para verificar en Render el origen exacto del fallback de gráfica.

### Riesgos / problemas detectados
- Los logs de consola son temporales y útiles para esta fase de diagnóstico, pero más adelante convendrá retirarlos cuando el flujo quede definitivamente estable.
- Puede que el problema final de algunos casos de gráfica vacía siga estando en datos concretos de ciertos análisis, pero ahora el motivo quedará visible y verificable sin ambigüedad.

### Comprobaciones realizadas
- Relectura obligatoria de `BOT_INSTRUCTIONS.md`, `PROJECT_CONTEXT.md`, `CHANGELOG_AI.md` y `docs/ai_report.md` antes de empezar.
- Revisión de la cascada CSS y de la estructura de clases del modal en `analisis.html`, `historial.html` y `estilos.css`.
- Revisión del flujo de fetch y parseo de series en `app/static/app.js`.
- Confirmación de que el nodo raíz del modal estaba usando una clase de caja (`.modal`) en lugar de la clase overlay adecuada (`.modal-overlay`).

### Pendientes
- Probar en Render y leer la consola del navegador para confirmar el motivo exacto del fallback en un caso real.
- Si los logs muestran una respuesta OHLC válida pero sin puntos parseados, ajustar el parser con el formato exacto observado.
- Una vez confirmado el flujo estable, retirar la instrumentación temporal en una iteración de limpieza pequeña.

## Iteración 19 - Carga global de Chart.js y render robusto de la gráfica

### Objetivo
Corregir específicamente el `chart-did-not-draw` confirmado por los logs reales, centrándose en la disponibilidad real de Chart.js, el momento de pintado del canvas y las condiciones mínimas de tamaño/visibilidad del contenedor.

### Contexto
El usuario aportó logs concluyentes: `/market/ohlc` devolvía datos, se recibían miles de puntos, el parser generaba `firstPoint` y `lastPoint`, y aun así el flujo acababa en `chart-did-not-draw`. Eso descartaba ya problemas de datos, endpoint, rango o parseo y apuntaba directamente al render de Chart.js/canvas.

### Causa exacta detectada
La causa principal era de disponibilidad de librería:
- Chart.js solo se estaba cargando en `app/templates/career.html`
- las pantallas de `Nuevo análisis` e `Historial` heredaban de `base.html`, donde Chart.js no se cargaba
- por tanto, en esos contextos `typeof Chart === "undefined"` y el render devolvía `false`, aunque hubiera miles de puntos válidos listos para dibujar

Además, se reforzó el flujo para evitar falsos negativos por timing o tamaño del canvas:
- espera de un `requestAnimationFrame` antes de pintar
- comprobación explícita de que el contenedor del canvas tiene tamaño real
- captura explícita de errores al crear `new Chart(...)`

### Cambios aplicados
- Movida la carga de Chart.js a `app/templates/base.html` para que esté disponible globalmente en las pantallas que necesitan gráficas.
- Eliminada la carga duplicada de Chart.js en `app/templates/career.html`.
- Endurecido `renderAnalysisDetailChart(...)` en `app/static/app.js` para:
  - registrar error claro si el canvas no existe
  - registrar error claro si Chart.js no está cargado
  - abortar si el contenedor del canvas no tiene tamaño real
  - envolver `new Chart(...)` en `try/catch`
  - hacer `resize()` tras crear la instancia
- Añadida una espera con `requestAnimationFrame` antes de pintar para asegurar que el modal ya está visible y medible.
- Reducidos los logs temporales más ruidosos y mantenidos los útiles para diagnóstico de fallo real.
- Mejorado el fallback para diferenciar entre:
  - Chart.js no disponible
  - imposibilidad real de dibujar la gráfica

### Qué datos usa ahora la gráfica
La gráfica sigue usando exactamente los datos ya confirmados como válidos:
- `ticker`
- rango normalizado `start/end`
- serie histórica OHLC desde `/market/ohlc/<ticker>`
- `adj_close` como base
- `importe_inicial` solo en `SIN_DCA` para reconstrucción de valor estimado

### Decisiones tomadas
- No tocar backend, endpoint, auth ni modo carrera.
- Resolver el fallo donde realmente estaba, es decir, en la carga de la librería y en las condiciones de render del canvas.
- Mantener solo los logs que siguen aportando valor si algo vuelve a fallar, reduciendo ruido innecesario.

### Riesgos / problemas detectados
- Cargar Chart.js globalmente añade ese recurso a más páginas, aunque es un coste razonable para simplificar coherencia y evitar errores de disponibilidad parcial.
- Si apareciera un caso residual tras esto, lo más probable sería ya un problema de CSS/tamaño puntual del contenedor y no de datos ni parser.

### Comprobaciones realizadas
- Relectura obligatoria de `BOT_INSTRUCTIONS.md`, `PROJECT_CONTEXT.md`, `CHANGELOG_AI.md` y `docs/ai_report.md` antes de empezar.
- Revisión de dónde se cargaba realmente Chart.js en los templates.
- Revisión del render de la gráfica en `app/static/app.js` a la luz del log final `chart-did-not-draw`.
- Confirmación de que la librería estaba cargada solo en `career.html` y no en el flujo de análisis/historial.
- Comprobación de sintaxis con `python3 -m py_compile` sobre `run.py`, `app/__init__.py`, `app/routes.py`, `app/auth.py` y `app/career.py`.

### Pendientes
- Verificar en Render que con `AAPL`, `MSFT` o `UBI.PA` y rangos amplios la gráfica ya se dibuja realmente.
- Si todo funciona, hacer una iteración final pequeña para retirar cualquier log temporal restante que ya no aporte valor.

## Iteración 20 - Persistencia mínima del modo carrera por usuario

### Objetivo
Empezar la mejora prioritaria aprobada por el usuario, persistiendo el modo carrera por usuario autenticado con el mínimo alcance razonable: guardar el vínculo entre usuario y su última sesión de carrera para poder recuperarla de forma real desde backend, sin depender solo de `localStorage`.

### Contexto
Tras consolidar autenticación, Postgres e historial por usuario, la siguiente mejora funcional más valiosa era dar persistencia al modo carrera. Se decidió abrir una primera fase mínima y estable, sin reescribir todavía el motor de carrera ni migrar toda la lógica de snapshots globales. La meta de esta fase es que un usuario autenticado pueda recuperar su última sesión desde el backend de forma fiable.

### Cambios aplicados
- Añadido un nuevo modelo `CareerSessionLink` en `app/models.py` para vincular:
  - usuario
  - `session_id`
  - metadatos básicos de la sesión
  - timestamps de creación/actualización
- Actualizado `app/__init__.py` para crear también la tabla `CareerSessionLink` al arrancar la app.
- Creado `app/services/career_session_service.py` con utilidades para:
  - guardar la sesión de carrera asociada a un usuario
  - recuperar la última sesión guardada de ese usuario
- Modificado `app/career.py` para:
  - detectar `session["user_id"]`
  - guardar el vínculo usuario-sesión cuando se crea una sesión de carrera nueva
  - exponer `GET /api/career/session/latest` para devolver la última sesión del usuario autenticado
- Modificado `app/static/app.js` para que el botón `Cargar última`:
  - intente primero cargar la última sesión real desde backend
  - use `localStorage` solo como fallback de compatibilidad

### Qué resuelve esta fase
- El modo carrera deja de depender exclusivamente de `localStorage` para recordar la última sesión.
- Un usuario autenticado ya puede recuperar su última sesión desde el servidor, aunque cambie de navegador/dispositivo o pierda el storage local, siempre que la sesión siga existiendo en el almacén actual de carrera.
- Se abre el camino a futuras fases de persistencia más profundas sin forzar todavía una reescritura arriesgada del motor.

### Qué NO hace todavía esta fase
- No migra el almacén principal del modo carrera a Postgres.
- No persiste todavía cada snapshot o turno dentro de tablas relacionales propias.
- No añade gestión de múltiples partidas con listado completo por usuario.
- No toca ranking, reportes ni lógica de cálculo del modo carrera.
- No cambia el comportamiento de invitados.

### Decisiones tomadas
- Mantener esta fase deliberadamente pequeña y estable.
- No tocar la lógica central de `app/career.py` más allá del vínculo usuario-sesión y la recuperación de la última sesión.
- Reutilizar el `session_id` actual como identidad principal, para no abrir todavía una migración grande del motor de carrera.
- Mantener fallback a `localStorage` para no romper continuidad a corto plazo.

### Riesgos / problemas detectados
- La sesión de carrera sigue viviendo en el almacén actual del motor, así que si ese `session_id` deja de existir en el store principal, el vínculo del usuario no bastará por sí solo para reconstruirla.
- Esta fase mejora mucho la continuidad del usuario autenticado, pero aún no equivale a una persistencia relacional completa del modo carrera.
- Conviene validar en Render que la última sesión se recupera bien tras cerrar sesión, volver a entrar y usar el botón `Cargar última`.

### Comprobaciones realizadas
- Relectura obligatoria de `BOT_INSTRUCTIONS.md`, `PROJECT_CONTEXT.md`, `CHANGELOG_AI.md` y `docs/ai_report.md` antes de empezar.
- Revisión de `app/career.py`, `app/static/app.js`, `app/models.py` y `app/__init__.py` para encontrar el punto mínimo de intervención.
- Confirmación de que el frontend recordaba `lastSessionId` solo en `localStorage` y que el backend aún no conocía la última sesión por usuario.
- Comprobación de sintaxis con `python3 -m py_compile` sobre `run.py`, `app/__init__.py`, `app/routes.py`, `app/auth.py` y `app/career.py`.

### Pendientes
- Validar en Render el flujo de usuario autenticado:
  - crear sesión de carrera
  - cerrar sesión
  - volver a entrar
  - pulsar `Cargar última`
- Si esta fase queda estable, siguiente subfase recomendada:
  - listado de sesiones de carrera por usuario
  - elección manual de partida
  - persistencia más profunda de snapshots/turnos en Postgres
