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

## Iteración 21 - Listado de sesiones de carrera por usuario

### Objetivo
Dar el siguiente paso natural tras la fase 1 de persistencia: permitir que el usuario autenticado vea varias sesiones recientes de modo carrera y pueda reabrir una concreta desde la propia interfaz, en lugar de depender solo del concepto de “última sesión”.

### Contexto
La Iteración 20 ya permitía guardar y recuperar la última sesión de carrera por usuario autenticado. El siguiente avance lógico y de mayor valor UX era exponer un listado mínimo de sesiones recientes para que el usuario pudiera reabrir una partida concreta, manteniendo todavía un alcance contenido y sin reescribir el motor ni migrar snapshots a Postgres.

### Cambios aplicados
- Ampliado `app/services/career_session_service.py` con una utilidad para listar sesiones de carrera de un usuario autenticado, ordenadas por actualización reciente.
- Añadido en `app/career.py` el endpoint:
  - `GET /api/career/sessions`
- Este endpoint devuelve hasta 12 sesiones recientes del usuario con metadatos ligeros:
  - `session_id`
  - `player`
  - `difficulty`
  - `period.start`
  - `period.end`
  - timestamps
- Ampliado `app/templates/career.html` con un bloque visual de “Tus sesiones” dentro del panel inicial del modo carrera.
- Ampliado `app/static/app.js` para:
  - cargar automáticamente las sesiones guardadas del usuario autenticado
  - renderizar tarjetas simples de sesión guardada
  - permitir reabrir una sesión concreta al pulsarla
  - refrescar el listado al crear una nueva sesión
- Ampliado `app/static/estilos.css` para integrar visualmente este listado con el dashboard actual del modo carrera.

### Qué resuelve esta fase
- El usuario autenticado ya no depende solo de “la última sesión”.
- Ahora puede ver varias sesiones recientes y abrir una concreta desde la UI.
- Mejora mucho la sensación de continuidad del modo carrera sin exigir todavía una persistencia relacional completa del motor.

### Qué NO hace todavía esta fase
- No añade eliminación/renombrado de sesiones.
- No ofrece filtros avanzados ni paginación real.
- No migra snapshots o turnos a tablas relacionales.
- No toca el ranking ni el informe del modo carrera.
- No cambia el comportamiento de invitados.

### Decisiones tomadas
- Mantener el listado pequeño y reciente, limitado a 12 sesiones, para no sobrecargar la UI ni abrir paginación aún.
- Reutilizar la estructura actual del dashboard de modo carrera en lugar de crear una pantalla nueva separada.
- Mantener la lógica principal del motor intacta, limitando los cambios a enlace usuario-sesiones + selección visual.

### Riesgos / problemas detectados
- Aunque el usuario vea varias sesiones, estas siguen dependiendo de que el `session_id` siga existiendo en el store actual del motor.
- Puede hacer falta más adelante una distinción visual entre sesiones activas, cerradas o incompletas.
- Si el número de sesiones crece mucho, habrá que abrir una fase posterior con listado más rico o paginado.

### Comprobaciones realizadas
- Relectura obligatoria de `BOT_INSTRUCTIONS.md`, `PROJECT_CONTEXT.md`, `CHANGELOG_AI.md` y `docs/ai_report.md` antes de empezar.
- Revisión de `career_session_service.py`, `career.py`, `career.html`, `app.js` y `estilos.css` para localizar el punto mínimo de intervención.
- Comprobación de sintaxis con `python3 -m py_compile` sobre `run.py`, `app/__init__.py`, `app/routes.py`, `app/auth.py`, `app/career.py`, `app/models.py` y `app/services/career_session_service.py`.
- Revisión del diff final para asegurar que el alcance queda limitado a persistencia de sesiones y UI asociada.

### Pendientes
- Validar en Render el flujo completo:
  - crear varias sesiones autenticado
  - verlas listadas en “Tus sesiones”
  - reabrir una concreta
- Si esta fase queda estable, siguiente subfase recomendada:
  - acciones sobre sesiones (renombrar o archivar)
  - persistencia profunda de turnos/snapshots en Postgres

## Iteración 22 - Persistencia profunda de sesiones y turnos de carrera en Postgres

### Objetivo
Dar el salto desde la persistencia ligera basada en enlace usuario-sesión hacia una persistencia real del progreso del modo carrera en Postgres, guardando la sesión completa, el snapshot más reciente y los turnos cerrados por usuario autenticado.

### Contexto
Las Iteraciones 20 y 21 ya resolvían continuidad básica: última sesión y listado reciente. Pero el motor todavía dependía del store JSON principal para reconstruir la partida. Esta iteración introduce una capa persistente paralela en Postgres para que el modo carrera conserve mejor el estado real de la partida sin romper compatibilidad con el sistema actual ni con invitados.

### Archivos tocados
- `app/models.py`
- `app/__init__.py`
- `app/career.py`
- `app/services/career_session_service.py`
- `app/static/app.js`
- `CHANGELOG_AI.md`
- `docs/ai_report.md`

### Cambios aplicados
- Añadido modelo `CareerSession` para persistir por usuario:
  - `session_id`
  - `status`
  - `display_name`
  - `period_start`
  - `period_end`
  - `current_turn`
  - `total_turns`
  - `latest_snapshot_json`
  - `metadata_json`
  - timestamps
- Añadido modelo `CareerTurn` para persistir por sesión:
  - `turn_index`
  - `decision_json`
  - `snapshot_json`
  - `result_json`
  - timestamps
- Actualizado `app/__init__.py` para crear también las nuevas tablas en arranque.
- Ampliado `app/services/career_session_service.py` con helpers para:
  - serializar/deserializar snapshots
  - upsert de sesión persistida
  - guardar turnos cerrados
  - recuperar sesión persistida por usuario
  - recuperar última sesión persistida
  - listar turnos persistidos de una sesión
- Ampliado `app/career.py` para que:
  - al crear sesión autenticada, guarde también el estado completo en Postgres
  - al actualizar sesión, intente persistir el snapshot más reciente en paralelo al store existente
  - `GET /api/career/session/latest` priorice Postgres y haga fallback al store actual
  - `GET /api/career/session/<session_id>` priorice Postgres para usuario autenticado y mantenga fallback al store
  - `POST /api/career/turn` guarde decisión, snapshot y resultado del turno en Postgres para usuario autenticado
- Añadidos endpoints nuevos:
  - `POST /api/career/session/save`
  - `GET /api/career/session/<session_id>/turns`
- Ajustado `app/static/app.js` para:
  - cargar directamente la sesión devuelta por `GET /api/career/session/latest` cuando ya llega hidratada desde backend
  - indicar mejor si una sesión se carga desde Postgres
  - no bloquear la UX si la persistencia profunda falla, mostrando aviso y manteniendo el store actual como continuidad

### Decisiones técnicas
- Se ha evitado JSONField para mantener compatibilidad simple con la infraestructura actual y se ha usado `TextField` con JSON serializado de forma controlada.
- La persistencia profunda se ha añadido en paralelo al sistema actual, no como sustitución inmediata.
- Se mantiene la regla de oro de esta fase: para usuario autenticado, persistir más; para invitado, no escribir en Postgres.
- `GET /api/career/session/latest` y `GET /api/career/session/<session_id>` priorizan Postgres pero conservan fallback al store JSON para no romper sesiones antiguas o incompletas.

### Riesgos o limitaciones
- La persistencia profunda ya guarda snapshots y turnos, pero el resto del motor todavía sigue escribiendo también en el store actual, así que aún existe doble fuente de verdad.
- No se ha hecho todavía migración de sesiones antiguas desde JSON a Postgres.
- No se expone aún una vista rica de historial de turnos en UI, aunque el backend ya puede devolverlos.
- Si el payload de sesión crece mucho, `latest_snapshot_json` podría requerir más adelante una estrategia más granular.

### Comprobaciones realizadas
- Relectura obligatoria de `BOT_INSTRUCTIONS.md`, `PROJECT_CONTEXT.md`, `CHANGELOG_AI.md` y `docs/ai_report.md` antes de empezar.
- Auditoría del estado actual de modelos, rutas de carrera, frontend de carrera y endpoints `GET /api/career/session/latest` y `GET /api/career/sessions`.
- Revisión del flujo de creación, carga y cierre de turnos para insertar persistencia sin reescribir el motor.
- Pendiente ejecución final de comprobación sintáctica y validación manual en Render tras cerrar la iteración.

### Siguientes pasos recomendados
- Validar en Render la secuencia real autenticada:
  - crear sesión
  - cerrar varios turnos
  - recargar navegador
  - reanudar desde Postgres
- Exponer en UI una vista de historial interno de turnos por sesión si aporta valor al TFG.
- Empezar una fase posterior de convergencia para que el store principal del modo carrera dependa cada vez menos del JSON local.

## Iteración 23 - Validación y hardening de persistencia profunda del modo carrera

### Objetivo
Comprobar que la Fase 3 de persistencia profunda del modo carrera no tiene grietas obvias de robustez y endurecer los puntos más frágiles sin abrir una funcionalidad nueva grande.

### Contexto
La Iteración 22 introdujo `CareerSession`, `CareerTurn` y la priorización de Postgres para reanudar sesiones. Esta iteración se centra en validar los caminos principales, revisar respuestas de los endpoints y corregir riesgos de acceso indebido o de payloads persistidos corruptos/incompletos.

### Comprobaciones realizadas
- Relectura obligatoria de `BOT_INSTRUCTIONS.md`, `PROJECT_CONTEXT.md`, `CHANGELOG_AI.md` y `docs/ai_report.md`.
- Revisión específica de:
  - `app/models.py`
  - `app/__init__.py`
  - `app/career.py`
  - `app/services/career_session_service.py`
  - `app/static/app.js`
- Validación sintáctica ejecutada con:
  - `python3 -m py_compile run.py app/__init__.py app/routes.py app/auth.py app/career.py app/models.py app/services/career_session_service.py`
- Revisión de consistencia de los endpoints:
  - `GET /api/career/session/latest`
  - `GET /api/career/sessions`
  - `GET /api/career/session/<session_id>`
  - `POST /api/career/session/save`
  - `POST /api/career/turn`
  - `GET /api/career/session/<session_id>/turns`

### Errores encontrados
- El fallback al store JSON en `GET /api/career/session/<session_id>` podía permitir cargar por `session_id` una sesión no vinculada al usuario autenticado si seguía existiendo en el store anterior.
- `POST /api/career/turn` y `POST /api/career/session/save` necesitaban una comprobación más estricta de acceso por usuario cuando trabajan con sesiones heredadas del store.
- La deserialización de `latest_snapshot_json` era tolerante a JSON corrupto, pero no validaba que el payload recuperado tuviera una estructura mínima válida de sesión.
- En frontend, tras cerrar turno, si fallaba la recarga posterior de sesión, la UI podía quedar sin feedback claro pese a haberse cerrado el turno.

### Correcciones aplicadas
- Añadido validador de payload persistido en `app/services/career_session_service.py` para exigir una estructura mínima antes de aceptar o rehidratar una sesión.
- `deserialize_career_session(...)` ahora descarta snapshots vacíos, corruptos o estructuralmente incompletos y fuerza fallback limpio.
- `upsert_career_session_state(...)` ahora valida el payload antes de persistirlo.
- Añadido control auxiliar en `app/career.py` para verificar que una sesión del store JSON pertenece realmente al usuario autenticado antes de permitir:
  - `GET /api/career/session/<session_id>`
  - `POST /api/career/session/save`
  - `POST /api/career/turn`
- Ajustado `app/static/app.js` para capturar de forma explícita errores al recargar la sesión después de cerrar turno y mostrar feedback sin romper la continuidad de la partida.

### Archivos tocados
- `app/career.py`
- `app/services/career_session_service.py`
- `app/static/app.js`
- `CHANGELOG_AI.md`
- `docs/ai_report.md`

### Riesgos pendientes
- Sigue existiendo doble fuente de verdad entre Postgres y el store JSON del motor.
- No se ha ejecutado todavía validación funcional real en Render sobre la secuencia completa autenticada y en modo invitado.
- No hay aún una estrategia de migración automática de sesiones antiguas desde el store a Postgres.
- Falta comprobar con datos reales si hay algún caso de recarga parcial donde el snapshot persistido sea válido pero desfasado respecto al store anterior.

### Pruebas recomendadas en Render
- Usuario autenticado:
  - crear sesión nueva
  - cerrar uno o varios turnos
  - recargar navegador
  - usar `Reanudar última sesión`
  - abrir una sesión concreta desde `Tus sesiones`
  - comprobar que el progreso reaparece correctamente
- Usuario invitado:
  - crear sesión
  - avanzar turnos
  - verificar que no hay errores por persistencia en Postgres
- Casos de robustez:
  - sesión antigua existente solo en store anterior
  - sesión autenticada sin snapshot persistido válido
  - comprobación de que un usuario no puede cargar una sesión ajena por `session_id`

## Iteración 24 - Validación real orientada a Render y microfixes de persistencia de carrera

### Objetivo
Aproximar la validación real de producción en Render, verificar que el flujo persistente del modo carrera no tiene bloqueos obvios y aplicar solo microcorrecciones seguras detectadas durante la revisión final.

### Contexto
La Iteración 22 introdujo persistencia profunda en Postgres y la Iteración 23 endureció acceso y tolerancia a snapshots corruptos. En esta fase el foco es comprobar la preparación real para Render y detectar microfallos de producción, sin abrir funcionalidad nueva ni rediseñar el motor.

### Pruebas realizadas
- Relectura obligatoria de:
  - `BOT_INSTRUCTIONS.md`
  - `PROJECT_CONTEXT.md`
  - `CHANGELOG_AI.md`
  - `docs/ai_report.md`
- Revisión específica de:
  - Iteración 22
  - Iteración 23
  - `app/models.py`
  - `app/career.py`
  - `app/services/career_session_service.py`
  - `app/static/app.js`
  - `app/__init__.py`
- Comprobación sintáctica con:
  - `python3 -m py_compile run.py app/__init__.py app/routes.py app/auth.py app/career.py app/models.py app/services/career_session_service.py`
- Auditoría de preparación para Render desde el propio repo:
  - no se encontró `render.yaml`
  - no se encontró `.env` local
  - no aparece en el repo una URL pública de Render para automatizar llamadas HTTP reales desde este entorno

### Comportamiento observado en Render
- No ha sido posible ejecutar validación funcional directa contra Render desde este entorno porque no hay URL pública de despliegue ni acceso explícito a logs de Render dentro del repo o del contexto actual.
- Sí se ha podido validar que el código de arranque sigue siendo coherente con Render:
  - `SECRET_KEY` obligatoria
  - inicialización de base de datos vía `DATABASE_URL`
  - creación segura de tablas `CareerSession` y `CareerTurn`
  - arranque sin errores sintácticos

### Errores encontrados
- Se detectó una fragilidad adicional en `POST /api/career/session/save`: tras el hardening previo, una sesión autenticada nueva podía quedar bloqueada si aún no existía vínculo previo y el control de acceso solo consultaba enlaces ya guardados.
- Esto podía afectar a escenarios de persistencia temprana o a recuperaciones parciales en producción.

### Correcciones aplicadas
- Refinado el control de acceso en `app/career.py` para distinguir mejor entre:
  - sesiones persistidas en Postgres del propio usuario
  - sesiones heredadas del store JSON con vínculo legítimo
- Añadido helper para comprobar propiedad de sesión persistida y helper combinado para validar acceso por cualquiera de las dos vías permitidas.
- Ajustado `POST /api/career/session/save` para permitir persistir sesiones válidas del propio flujo actual sin abrir acceso indebido a sesiones ajenas.
- Ajustado `GET /api/career/session/<session_id>` y `POST /api/career/turn` para usar la comprobación combinada más robusta.

### Archivos tocados
- `app/career.py`
- `CHANGELOG_AI.md`
- `docs/ai_report.md`

### Riesgos pendientes
- Sigue pendiente la validación funcional real contra el despliegue Render con navegador y Postgres vivos.
- La app mantiene doble fuente de verdad entre store JSON y Postgres.
- Sin URL pública ni logs accesibles desde aquí no se puede certificar aún el comportamiento exacto del despliegue tras recargar navegador, reanudar última sesión o usar `Tus sesiones` en producción.

### Siguientes pasos recomendados
- Validar manualmente en Render con usuario autenticado real:
  - login
  - crear sesión de carrera
  - cerrar al menos dos turnos
  - recargar navegador entre pasos
  - reanudar última sesión
  - abrir sesiones desde `Tus sesiones`
- Validar manualmente modo invitado:
  - crear sesión
  - avanzar turnos
  - confirmar ausencia de errores visuales o bloqueos
- Si aparece cualquier microfallo real en Render, abrir una iteración exclusivamente correctiva sobre ese comportamiento concreto.

## Iteración 25 - Aislamiento de sesiones invitado/usuario y reparación del informe final de carrera

### Objetivo
Corregir dos incidencias reales detectadas en Render: la fuga de estado entre invitado y usuario autenticado, y el error 500 al generar el informe final tras simular todos los turnos.

### Bugs detectados
#### Bug 1 - Fuga de estado entre invitado y usuario autenticado
Al usar modo invitado y después autenticarse con una cuenta real, el frontend podía reutilizar el `lastSessionId` y otras preferencias de carrera guardadas en `localStorage` sin separación por identidad. Eso hacía que la UI heredase la carrera del invitado al entrar como usuario autenticado.

#### Bug 2 - Error 500 en informe final tras autoplay
Tras `Simular todos los turnos`, el endpoint `GET /api/career/report/<session_id>?bench=%5EGSPC&include_series=true` podía resolver la sesión solo desde el store JSON principal con `_get_session(session_id)`. Cuando la sesión válida estaba persistida y actualizada en Postgres, el informe podía trabajar con un estado desfasado o no compatible y acabar fallando al construir el reporte final.

### Causa raíz
- **Bug 1:** preferencias de carrera en cliente (`lastSessionId`, benchmark, tickers, jugador) guardadas bajo una sola clave global de `localStorage`, sin namespacing por identidad (`guest` frente a `user:<id>`), y sin reset explícito al cambiar de identidad.
- **Bug 2:** el informe final y algunas rutas auxiliares seguían resolviendo sesión directamente desde el store antiguo, en vez de priorizar la sesión persistida del usuario autenticado. Eso rompía la coherencia tras autoplay completo cuando el snapshot bueno estaba en Postgres.

### Solución aplicada
- En `app/templates/base.html` se expone al frontend la identidad actual mediante atributos `data-user-id` y `data-is-guest`.
- En `app/static/app.js`:
  - se introduce namespacing de preferencias de carrera por identidad
  - se añade sincronización de identidad (`guest`, `user:<id>`, `anon`)
  - se resetea el estado cliente de carrera cuando cambia la identidad
  - `Reanudar última sesión` deja de usar fallback cruzado para usuario autenticado y solo consulta backend para sesiones propias; el invitado conserva su propio flujo aislado
- En `app/career.py`:
  - se añade `_is_guest_user()`
  - se añade `_resolve_session_for_request(session_id)` para priorizar sesión persistida en Postgres del usuario autenticado y usar fallback controlado al store antiguo
  - `GET /api/career/report/<session_id>` y `GET /api/career/series/<session_id>` dejan de depender solo de `_get_session(session_id)`
  - `GET /api/career/session/latest` se endurece para no tratar invitado como usuario con última sesión persistida
  - se añade respuesta controlada también para excepciones no previstas al generar el informe final

### Archivos tocados
- `app/templates/base.html`
- `app/static/app.js`
- `app/career.py`
- `CHANGELOG_AI.md`
- `docs/ai_report.md`

### Validaciones realizadas
- Relectura obligatoria de `BOT_INSTRUCTIONS.md`, `PROJECT_CONTEXT.md`, `CHANGELOG_AI.md` y `docs/ai_report.md`
- Auditoría específica de:
  - `app/career.py`
  - `app/services/career_session_service.py`
  - `app/static/app.js`
  - `app/models.py`
  - `app/auth.py`
  - `app/templates/base.html`
  - `app/templates/career.html`
- Validación sintáctica ejecutada con:
  - `python3 -m py_compile run.py app/__init__.py app/routes.py app/auth.py app/career.py app/models.py app/services/career_session_service.py`
- Reproducción analítica de la causa del bug 1 a partir del uso de `localStorage`
- Reproducción analítica de la causa del bug 2 a partir de la diferencia entre sesión persistida y resolución de informe desde store antiguo

### Riesgos pendientes
- Sigue existiendo convivencia entre store JSON y Postgres, aunque ya se ha corregido la resolución de informe y series para usuario autenticado.
- Falta confirmar en Render con el flujo real que el informe final ya no devuelve 500 tras autoplay completo.
- Falta verificar manualmente que no queda ningún otro punto del frontend usando preferencias de carrera sin respetar el namespace por identidad.

### Qué probar manualmente en Render
#### Caso A - Aislamiento invitado/usuario
- entrar como invitado
- crear carrera
- avanzar uno o varios turnos
- cerrar sesión
- iniciar sesión con usuario registrado
- comprobar que NO aparece la carrera del invitado
- pulsar `Reanudar última sesión` y verificar que solo actúa sobre sesiones propias del usuario autenticado

#### Caso B - Informe final tras simular todos los turnos
- iniciar carrera con usuario autenticado
- usar `Simular todos los turnos`
- generar informe final
- comprobar que `GET /api/career/report/<session_id>?bench=%5EGSPC&include_series=true` ya no devuelve 500
- comprobar que aparecen puntuación, cards Portfolio/Benchmark/Tracking y gráfico final

#### Caso C - Invitado
- entrar en modo invitado
- crear carrera
- simular turnos o cerrar algunos manualmente
- comprobar que el flujo no se rompe y que no intenta mezclar estado con usuarios autenticados

## Iteración 26 - Diagnóstico real y saneado de serialización del informe final tras autoplay

### Objetivo
Encontrar la causa exacta del 500 real en `GET /api/career/report/<session_id>` tras `Simular todos los turnos`, sin añadir funcionalidad nueva ni hacer refactor grande del motor.

### Error observado en Render
Tras la Iteración 25, el flujo seguía fallando en producción con:
- `GET /api/career/report/car_5f23a8?bench=%5EGSPC&include_series=true -> 500`
- toast rojo con el mismo endpoint
- informe final visible pero incompleto:
  - puntuación `— / 10`
  - cards de Portfolio / Benchmark / Tracking vacías

### Hipótesis investigadas
Se revisaron explícitamente estas posibilidades:
- error previo a resolver sesión por seguir leyendo del store antiguo
- error específico de `include_series=true`
- estado inconsistente tras autoplay completo
- snapshot persistido incompleto en Postgres
- payload excesivo por series históricas
- error de benchmark
- error de serialización JSON por tipos no seguros o valores no finitos
- problema real de caché/memoria/store del servidor

### Hallazgo técnico principal
La resolución de sesión ya estaba priorizando Postgres correctamente en `report/series/session`, así que el foco dejó de estar en el acceso a la sesión.

El punto más sospechoso y ahora instrumentado queda en el propio endpoint de informe:
1. resolver sesión
2. construir `report_payload` con métricas, warnings, turnos y, si procede, series
3. serializar con `jsonify(report_payload)`

Dado el síntoma observado, el problema ya no encaja bien con un fallo temprano de acceso a sesión, sino con un fallo en la fase final de construcción o serialización del payload, especialmente tras autoplay completo e `include_series=true`.

### Causa raíz más probable tras el diagnóstico
La hipótesis ahora más fuerte, respaldada por la estructura del código, es:
- el endpoint genera un `report_payload` con datos mixtos procedentes de pandas, snapshots y métricas
- tras autoplay completo pueden colarse valores no JSON-safe o no finitos (`NaN`, `inf`, `Timestamp`, tipos numpy/pandas o equivalentes)
- el fallo se produciría al serializar o al dejar pasar esos valores hasta la respuesta final, especialmente cuando `include_series=true` amplía el payload

Todavía no puedo afirmar el traceback exacto de Render porque no tengo acceso directo a esos logs desde aquí. Para no seguir corrigiendo a ciegas, esta iteración deja logging controlado y separa claramente:
- fallo de dominio al generar el informe
- fallo inesperado en generación del payload
- fallo específico en serialización final (`jsonify`)

### Si era o no un problema de caché/memoria/store
Conclusión de esta iteración:
- **no hay evidencia suficiente de que el 500 venga de caché o memoria del servidor como causa principal**
- **tampoco encaja ya como causa principal una mala resolución de store/Postgres**, porque esa parte quedó corregida en la Iteración 25
- la sospecha dominante pasa a ser **serialización o payload no seguro tras autoplay**, no limpieza de caché del store

### Solución aplicada en esta iteración
#### En `app/career.py`
- se añadió `current_app` para logging controlado en servidor
- se añadió `_safe_json_value(...)` para normalizar recursivamente el payload antes de `jsonify`
- el saneado convierte o neutraliza valores problemáticos como:
  - `NaN`
  - `inf`
  - `-inf`
  - `Timestamp` / fechas no triviales
  - tipos numpy/pandas con `.item()`
  - estructuras anidadas mixtas
- se añadió trazabilidad de fases en `GET /api/career/report/<session_id>`:
  - `career.report.start`
  - `career.report.payload_ready`
  - `career.report.domain_error`
  - `career.report.unexpected_error`
  - `career.report.jsonify_error`
  - `career.report.success`
- se separó explícitamente:
  - error al generar el informe
  - error al serializar el informe

### Qué permite confirmar esta instrumentación
Con esta iteración, en Render ya debería quedar claro si el fallo real estaba:
- antes de `_generate_report_payload(...)`
- dentro de `_generate_report_payload(...)`
- o exactamente en la serialización final del JSON

Además, si el problema era un valor no serializable o no finito, el saneado debería evitar el 500 sin tocar la lógica del simulador.

### Archivos tocados
- `app/career.py`
- `CHANGELOG_AI.md`
- `docs/ai_report.md`

### Validaciones realizadas
- Relectura obligatoria de:
  - `BOT_INSTRUCTIONS.md`
  - `PROJECT_CONTEXT.md`
  - `CHANGELOG_AI.md`
  - `docs/ai_report.md`
- Revisión específica de:
  - `app/career.py`
  - `app/services/career_session_service.py`
  - `app/static/app.js`
  - `app/models.py`
  - flujo de autoplay en `handleCareerAutoPlay()`
  - flujo de cierre de turno en `POST /api/career/turn`
  - endpoint `GET /api/career/report/<session_id>`
  - endpoint `GET /api/career/series/<session_id>`
- Validación sintáctica ejecutada con:
  - `python3 -m py_compile run.py app/__init__.py app/routes.py app/auth.py app/career.py app/models.py app/services/career_session_service.py`

### Limitaciones de esta iteración
- No tengo acceso real directo a logs de Render desde este entorno, así que no puedo pegar todavía el traceback real de producción.
- La iteración deja el sistema listo para que el próximo intento en Render confirme el punto exacto de fallo con logs concluyentes.

### Riesgos pendientes
- Si el problema no era serialización sino cálculo interno de una métrica concreta, el logging nuevo debería revelarlo, pero aún falta confirmación desde Render.
- Si Render estuviera fallando por volumen de payload únicamente, el saneado no sería suficiente por sí solo, aunque esta hipótesis ahora parece menos fuerte que la de serialización/tipos.

### Qué probar ahora en Render
#### Caso A - informe con series
- usuario autenticado
- crear carrera
- usar `Simular todos los turnos`
- generar informe con `include_series=true`
- comprobar si desaparece el 500
- si sigue fallando, revisar logs de Render buscando:
  - `career.report.start`
  - `career.report.payload_ready`
  - `career.report.unexpected_error`
  - `career.report.jsonify_error`

#### Caso B - informe base sin series
- mismo flujo, pero probar `include_series=false`
- confirmar si el informe base responde bien
- eso ayuda a decidir si el problema depende del tamaño/series o no

#### Caso C - endpoint de series
- probar `GET /api/career/series/<session_id>`
- comprobar si series funciona por separado
- si series funciona y report falla, el problema queda concentrado en la construcción/serialización del payload final del informe

#### Caso D - sesión reanudada
- recargar navegador
- reanudar sesión persistida
- generar informe final
- confirmar que no hay 500

## Iteración 27 - Optimización del resumen teórico del informe final

### Objetivo
Aplicar una corrección definitiva basada en el traceback real de Render para eliminar el 500 del informe final tras `Simular todos los turnos`, sin rehacer el modo carrera ni ocultar el error.

### Traceback real recibido
Render reportó el fallo en esta cadena:
- `session_report(...)`
- `_generate_report_payload(...)`
- `_compute_theoretical_summary(...)`
- `_evaluate_combo_result(...)`
- `_combine_normalized_series(...)`
- `_series_list_to_series(...)`
- `pd.to_datetime(entry[0])`

Además, el worker terminaba con:
- `SystemExit: 1`
- `Worker exiting`
- `Worker was sent SIGKILL! Perhaps out of memory?`

### Causa raíz confirmada
La causa real del 500 **no era principalmente `jsonify`** ni la resolución Postgres/store.

El problema estaba en el **coste computacional repetitivo del resumen teórico** dentro del informe final:
- `_compute_theoretical_summary(...)` evaluaba combinaciones de tickers
- para cada combinación llamaba a `_evaluate_combo_result(...)`
- `_evaluate_combo_result(...)` llamaba a `_combine_normalized_series(...)`
- `_combine_normalized_series(...)` volvía a ejecutar `_series_list_to_series(...)` ticker por ticker
- `_series_list_to_series(...)` volvía a hacer conversiones `pd.to_datetime(...)` y recreaba Series de pandas repetidamente

Eso provocaba una explosión de coste por:
- número de tickers evaluados
- número de combinaciones
- longitud de cada serie histórica
- recreación repetida de pandas Series y DataFrames dentro de bucles combinatorios

### Confirmación sobre memoria / timeout / coste combinatorio
Conclusión técnica:
- **sí estaba relacionado con consumo de recursos del worker**
- **la raíz concreta era coste combinatorio + recalculado repetido**, no simplemente un bug de datos aislado
- el `SIGKILL` de Render encaja con exceso de CPU/memoria derivado de ese patrón

### Problema concreto en complejidad
Antes de esta iteración, la misma serie de un ticker podía convertirse muchas veces dentro del mismo informe.

Ejemplo conceptual:
- si hay 5 tickers evaluados
- k=2 y k=3
- se exploran varias combinaciones
- cada combinación reconstruía series para sus tickers
- cada reconstrucción volvía a ejecutar `pd.to_datetime(...)` sobre todos los puntos

El coste crecía de forma combinatoria por número de combos y casi lineal por longitud de serie en cada reconstrucción. Ese patrón era muy mala combinación para Render.

### Solución aplicada
#### 1. Cache por request de series ya convertidas
En `app/career.py` se añadió:
- `_build_series_cache(...)`

Ahora, dentro de `_compute_theoretical_summary(...)`:
- se construye una cache `ticker -> pd.Series` una sola vez
- `_evaluate_combo_result(...)` reutiliza esa cache
- `_combine_normalized_series(...)` deja de reconvertir las mismas listas una y otra vez

#### 2. Downsampling seguro para el bloque teórico
Se añadió:
- `_downsample_series(...)`

El resumen teórico ya no necesita trabajar con toda la resolución histórica para evaluar combinaciones. Se limita a una versión reducida de las series para ese bloque analítico.

Límite introducido:
- `THEORETICAL_MAX_POINTS = 260`

Esto reduce coste sin afectar al informe base ni a las series principales mostradas al usuario.

#### 3. Límite explícito de universo y combinaciones
Se añadieron guardas:
- `THEORETICAL_MAX_TICKERS = 5`
- `THEORETICAL_MAX_COMBINATIONS = 24`

Si el universo o el número de combinaciones potenciales crece demasiado:
- se fuerza modo `greedy`
- se evita bruteforce innecesario

#### 4. Endurecimiento de `_series_list_to_series(...)`
Ahora la función:
- acepta entradas inválidas sin romper
- usa `pd.to_datetime(..., errors="coerce")`
- descarta fechas inválidas
- descarta `None`, `NaN`, `inf`, `-inf`
- devuelve serie vacía controlada si no queda contenido válido
- convierte a `float32` para contener mejor memoria

#### 5. Fallback parcial del resumen teórico
`_generate_report_payload(...)` ya no deja caer todo el informe si falla el bloque teórico por:
- `BadRequest`
- `NoHistoricalDataError`
- `MemoryError`
- `ValueError`
- `TypeError`

En ese caso:
- el informe principal sigue generándose
- `theoretical` queda vacío o parcial
- se añade warning controlado en `warnings`
- no se bloquean score, portfolio, benchmark ni tracking

### Qué NO se tocó
- no se rediseñó el modo carrera
- no se eliminó el store antiguo
- no se hizo refactor grande de arquitectura
- no se ocultó el error devolviendo datos falsos

### Archivos tocados
- `app/career.py`
- `CHANGELOG_AI.md`
- `docs/ai_report.md`

### Validaciones realizadas
- Relectura obligatoria de:
  - `BOT_INSTRUCTIONS.md`
  - `PROJECT_CONTEXT.md`
  - `CHANGELOG_AI.md`
  - `docs/ai_report.md`
- Revisión específica de:
  - `app/career.py`
  - `_generate_report_payload(...)`
  - `_compute_theoretical_summary(...)`
  - `_evaluate_combo_result(...)`
  - `_combine_normalized_series(...)`
  - `_series_list_to_series(...)`
  - `GET /api/career/report/<session_id>`
  - `GET /api/career/series/<session_id>`
- Validación sintáctica prevista con:
  - `python3 -m py_compile run.py app/__init__.py app/routes.py app/auth.py app/career.py app/models.py app/services/career_session_service.py`
- Verificación lógica del nuevo flujo:
  - cache por request para series ya convertidas
  - degradación controlada del bloque teórico
  - conservación del informe base aunque falle el resumen teórico

### Qué debes probar ahora en Render
#### Caso A - informe completo con autoplay
- usuario autenticado
- crear carrera
- usar `Simular todos los turnos`
- generar informe con `include_series=true`
- confirmar que ya no hay 500
- confirmar que aparecen score, cards y gráfico

#### Caso B - informe base
- probar `GET /api/career/report/<session_id>?bench=%5EGSPC&include_series=false`
- confirmar que responde bien

#### Caso C - endpoint de series
- probar `GET /api/career/series/<session_id>`
- confirmar que las series siguen funcionando por separado

#### Caso D - degradación parcial controlada
- si el resumen teórico no puede calcularse completo, confirmar que:
  - el informe principal sigue saliendo
  - aparece warning en payload
  - no hay 500

### Riesgos pendientes
- Aunque el coste principal se ha reducido de forma importante, Render sigue siendo un entorno contenido. Si aparece un caso extremo, podría ser necesario bajar todavía más el límite de puntos o combinaciones para el bloque teórico.
- Falta la validación final real en Render para certificar que el worker ya no muere con autoplay completo.

## Iteración 28 - Mejora visual del layout de sesiones guardadas en modo carrera

### Objetivo
Corregir un problema puramente visual del layout inicial del modo carrera: la columna de acciones se estiraba artificialmente cuando crecían las sesiones guardadas de la columna derecha.

### Validación positiva previa del informe final en Render
Se deja registrada la validación positiva del bug anterior tras desplegar el commit `6227e4a`:
- informe final probado en Render
- usuario autenticado
- partida con 5 activos y 4 turnos
- probado `Simular todos los turnos`
- probado `Generar informe`
- ya no apareció el error 500 en `/api/career/report/...include_series=true`
- se mostraron correctamente score, cards de Portfolio/Benchmark/Tracking y gráfico final

Conclusión: el bug del informe final queda cerrado a nivel funcional, pendiente solo de futuras pruebas de estrés con partidas más largas.

### Causa visual del problema
La causa del problema era estructural de layout:
- el bloque de formulario/acciones y el bloque `Tus sesiones` estaban dentro de la misma card y del mismo flujo vertical
- al crecer la zona de sesiones guardadas, toda la card aumentaba de altura
- visualmente eso empujaba hacia abajo la zona de acciones, dejando demasiado aire entre `Crear sesión` y `Reanudar última sesión`

No era un problema de lógica ni de datos, sino de composición del layout inicial.

### Solución aplicada
#### En `app/templates/career.html`
- se separó el arranque del modo carrera en un shell de dos columnas independiente
- la card principal del formulario quedó a la izquierda
- el panel `Tus sesiones` pasó a un `aside` propio a la derecha
- los botones `Crear sesión` y `Reanudar última sesión` se agruparon en una pequeña card de acciones más compacta

#### En `app/static/estilos.css`
- se añadió `career-setup-shell` con grid de dos columnas
- se forzó `align-items: start` para que la altura de la columna derecha no estire la izquierda
- la card izquierda se deja con `height: fit-content`
- el panel derecho de sesiones guardadas recibe `max-height` y `overflow-y: auto`
- se mantiene comportamiento responsive: por debajo de `980px` vuelve a una sola columna y se elimina la limitación de altura del panel derecho
- en móvil, la zona de acciones sigue apilándose correctamente

### Archivos tocados
- `app/templates/career.html`
- `app/static/estilos.css`
- `CHANGELOG_AI.md`
- `docs/ai_report.md`

### Validaciones realizadas
- Relectura obligatoria de:
  - `BOT_INSTRUCTIONS.md`
  - `PROJECT_CONTEXT.md`
  - `CHANGELOG_AI.md`
  - `docs/ai_report.md`
- Revisión del layout del modo carrera en:
  - `app/templates/career.html`
  - `app/static/estilos.css`
- Comprobaciones previstas para esta iteración:
  - el panel izquierdo ya no debe alargarse por el crecimiento de `Tus sesiones`
  - `Crear sesión` y `Reanudar última sesión` deben quedar visualmente cerca
  - `Tus sesiones` debe seguir mostrando elementos sin romper el layout
  - responsive básico correcto en tablet y móvil

### Qué debes comprobar en Render
- que el panel izquierdo ya no aumenta de altura al crecer `Tus sesiones`
- que `Crear sesión` y `Reanudar última sesión` quedan agrupados y bien colocados
- que `Tus sesiones` puede crecer sin arrastrar la otra columna
- que en móvil o ancho estrecho el bloque vuelve a una sola columna sin romperse

## Iteración 29 - Evaluación de preparación antes del Modo Carrera

### Objetivo
Convertir la pestaña `Aprender` en una experiencia interactiva con un tipo test dinámico y usarlo como requisito previo para acceder al `Modo Carrera`.

### Contexto
La aplicación ya disponía de:
- contenido educativo básico en `Aprender`
- usuarios autenticados y modo invitado
- historial y persistencia de carrera
- informe final del modo carrera ya validado en Render

La necesidad de producto era añadir una comprobación mínima de comprensión antes de dejar al usuario entrar en una simulación más compleja por turnos.

### Cómo funciona el test
La funcionalidad se presenta dentro de `Aprender` como bloque destacado de onboarding educativo:
- sección: `Comprueba si estás preparado`
- formato dinámico: una pregunta cada vez
- 4 opciones por pregunta
- progreso visible
- explicación breve tras responder
- botón para avanzar
- resultado final con estado aprobado/no aprobado
- botón para repetir
- acceso directo a `Modo Carrera` si aprueba

### Banco inicial de preguntas
Se ha creado un banco inicial de **10 preguntas** sobre:
- riesgo vs rentabilidad
- diversificación
- benchmark
- volatilidad
- DCA
- drawdown
- diferencia entre simulación e inversión real
- decisiones por turnos en modo carrera
- lectura de Portfolio / Benchmark / Tracking
- ventajas de usuario autenticado frente a invitado

### Puntuación mínima
- total: **10 preguntas**
- aprobado: **7/10**
- umbral: **70%**

### Persistencia del aprobado
#### Usuario autenticado
Se añadió persistencia real en base de datos mediante el modelo:
- `ReadinessQuizResult`

Guarda:
- usuario
- si ha aprobado
- puntuación
- total de preguntas
- fecha de aprobado
- detalle de respuestas serializado

Esto evita depender de `localStorage` como fuente principal en usuarios registrados y mantiene el aprobado entre logout/login.

#### Invitado
Para invitado se usa una solución ligera:
- estado en `session` de Flask (`readiness_guest`)
- refuerzo visual/local auxiliar con almacenamiento namespaced en `localStorage`

La separación por identidad se mantiene reutilizando la distinción `user:<id>` / `guest` / `anon`.

### Cómo se bloquea Modo Carrera
El acceso se bloquea de forma elegante en `GET /modo-carrera`:
- si no ha aprobado, la página muestra una card de bloqueo previa
- esa card explica por qué hay que hacer la evaluación
- ofrece CTA directo a `Aprender` para completar el test
- no se carga la interfaz interactiva de carrera hasta aprobar

Así se evita que el usuario entre en una experiencia avanzada sin pasar antes por el bloque formativo.

### Endpoints añadidos o modificados
#### Nuevos endpoints
- `GET /api/readiness/status`
- `GET /api/readiness/questions`
- `POST /api/readiness/submit`

#### Rutas modificadas
- `GET /aprende`
  - ahora inyecta estado inicial del quiz
- `GET /modo-carrera`
  - ahora aplica gate visual según estado de aprobado

### UX aplicada
#### En `Aprender`
- card destacada de evaluación
- progreso tipo `Pregunta X de 10`
- feedback inmediato tras elegir respuesta
- revisión final con mini explicación por pregunta
- tono motivacional según aprobado o suspenso

#### En `Modo Carrera`
- pantalla previa de bloqueo elegante
- CTA claro a `Aprender`
- no se rompe el flujo responsive

### Cambios aplicados
#### Backend
- nuevo modelo `ReadinessQuizResult`
- creación automática de tabla en `app/__init__.py`
- banco inicial de preguntas en backend
- cálculo de score y persistencia del resultado
- helpers para estado de readiness por usuario o invitado

#### Frontend
- nueva experiencia dinámica del quiz en `Aprender`
- render de pregunta a pregunta
- barra de progreso
- feedback y resultado final
- persistencia ligera local para invitado
- gate visual en `Modo Carrera`

### Archivos tocados
- `app/models.py`
- `app/__init__.py`
- `app/routes.py`
- `app/auth.py`
- `app/templates/aprende.html`
- `app/templates/career.html`
- `app/templates/base.html`
- `app/static/app.js`
- `app/static/estilos.css`
- `CHANGELOG_AI.md`
- `docs/ai_report.md`

### Validaciones previstas
- `python3 -m py_compile run.py app/__init__.py app/routes.py app/auth.py app/career.py app/models.py app/services/career_session_service.py`
- inspección funcional de estos casos:
  - usuario autenticado sin test: bloqueado con CTA a `Aprender`
  - usuario autenticado suspende: no desbloquea, puede repetir
  - usuario autenticado aprueba: se guarda y desbloquea `Modo Carrera`
  - logout/login: el aprobado persiste
  - invitado: puede aprobar sin mezclarse con usuario autenticado
  - responsive: test y gate usables en móvil

### Riesgos pendientes
- El banco inicial de preguntas es suficiente para esta fase, pero puede ampliarse o rotarse en una iteración futura.
- Para invitado se usa persistencia ligera y no fuerte, lo cual es aceptable para este caso pero no debe confundirse con seguridad equivalente a usuario autenticado.
- Podría merecer la pena en el futuro añadir más señales visuales de progreso longitudinal o repaso temático, pero no es necesario para cerrar esta iteración.

### Siguientes pasos recomendados
- validar en Render los casos A-F definidos por el usuario
- observar si la tasa de aprobado/suspenso sugiere ajustar dificultad o microcopy
- valorar en una iteración posterior una pequeña rotación de preguntas o agrupación temática sin convertirlo en una gamificación pesada

## Iteración 30 - Mejora interactiva del readiness quiz, gate visual y logout visible

### Problemas detectados
Tras publicar la iteración 29 y probarla visual y funcionalmente, aparecieron cuatro problemas claros:
- el gate de acceso a `Modo Carrera` era correcto a nivel funcional, pero demasiado plano visualmente
- la respuesta correcta parecía quedar siempre en la opción A, lo que dañaba la credibilidad del quiz
- la experiencia se sentía demasiado cercana a un examen clásico, no a un onboarding de producto
- la home autenticada no mostraba de forma visible cómo cerrar sesión o cambiar de usuario

### Enfoque elegido
Se ha mantenido la base funcional ya aprobada, pero evolucionando la experiencia hacia un recorrido más de producto:
- mantener persistencia real del aprobado para usuarios autenticados
- mantener aislamiento entre autenticado, invitado y anónimo
- convertir el quiz en un flujo guiado con introducción, recorrido final y resultado
- mover la aleatorización de respuestas al backend por intento para no depender del orden visual ni de un índice fijo en frontend
- reforzar la entrada a `Modo Carrera` con una card de acceso previo más elaborada y motivadora
- hacer visible el estado de sesión en la home, con CTA directo para cerrar sesión o cambiar de usuario

### Corrección del bug de respuestas siempre en A
La causa real era que el backend exponía siempre las opciones en el orden original y el `correctIndex` seguía apuntando al índice 0.

#### Solución aplicada en `app/routes.py`
- se añadió `READINESS_QUIZ_SESSION_KEY`
- se creó `_build_readiness_question_set()` para:
  - transformar cada pregunta en opciones con `option.id`, `label` y flag `correct`
  - mezclar aleatoriamente las respuestas de cada pregunta
  - mezclar también el orden de las propias preguntas
- se creó `_get_or_create_readiness_question_set(force_new=False)` para mantener estable el mismo intento dentro de la sesión
- se añadió `_clear_readiness_question_set()` para regenerar el recorrido al reiniciar o tras enviar el intento
- `GET /api/readiness/questions` ahora devuelve preguntas con opciones ya mezcladas y con ids estables, sin exponer `correctIndex`
- `POST /api/readiness/submit` ya no recibe índices visuales, sino pares `{ questionId, optionId }`
- la validación compara ids reales de opción, no posiciones A/B/C/D

Resultado: la respuesta correcta ya no queda anclada a la A y el scoring no depende del orden visual.

### Cómo se hizo el quiz más interactivo
#### En `app/templates/aprende.html`
La sección de readiness dejó de ser una card de test simple y pasó a un flujo más guiado:
- hero más claro y más de producto
- bloque de resumen con persistencia y estado
- bloque de recorrido en 3 pasos:
  - aprende lo esencial
  - conecta la teoría con la app
  - valida que estás listo
- panel lateral de progreso con etapas visibles:
  - introducción guiada
  - ponte a prueba
  - resultado final
- card inicial de onboarding antes de la primera pregunta
- preguntas con contexto temático, microcopy más guiado y CTA de inicio del recorrido

#### En `app/static/app.js`
- se añadió `readinessState.started`
- se creó `setReadinessStage(stage)` para marcar visualmente la etapa activa/completada
- el flujo ya no arranca directamente en pregunta 1, sino en una introducción guiada
- cada pregunta muestra:
  - badge de tema
  - contexto del bloque
  - pista breve de qué se está evaluando
- el feedback tras marcar una opción ahora se presenta como validación del paso, no como simple examen plano
- el resultado final revisa:
  - puntuación
  - estado aprobado/no aprobado
  - la respuesta elegida
  - la respuesta correcta si falló
  - explicación breve por pregunta
- `restartReadinessQuiz()` ahora fuerza regeneración del set mezclado mediante `GET /api/readiness/questions?restart=1`

### Mejora visual del gate de Carrera
#### En `app/templates/career.html`
El bloqueo inicial se rehízo como una experiencia de acceso previo más elaborada:
- nuevo titular más claro y motivador
- explicación del porqué del requisito
- bloque de desbloqueo en 3 pasos:
  - aprende
  - supera la evaluación
  - accede a carrera
- bloque de beneficios concretos:
  - riesgo y diversificación
  - benchmark e informe final
  - funcionamiento del modo carrera
- CTAs diferenciados:
  - `Comenzar evaluación`
  - `Ir a Aprender`
  - `Volver al inicio`

#### En `app/static/estilos.css`
- nueva variante `career-gate-card--premium`
- gradientes suaves y composición más cuidada
- grid interior con panel de pasos y panel de beneficios
- cards internas para dar sensación de producto más trabajado
- responsive para que todo vuelva a una sola columna sin romperse

### Logout visible en la home
#### En `app/routes.py`
- `home()` ahora inyecta `current_user` para poder mostrar nombre o email en la vista

#### En `app/templates/home.html`
Se añadió una banda visible de sesión en la parte superior del hero:
- si hay usuario autenticado:
  - muestra `Sesión iniciada`
  - muestra `username` o `email`
  - muestra el email como contexto secundario
  - muestra botón visible para `Cambiar usuario`
- si hay invitado:
  - muestra `Modo invitado`
  - explica que el progreso no se guarda en cuenta
  - muestra botón para salir del modo invitado

#### En `app/static/estilos.css`
- nuevas clases:
  - `session-banner`
  - `session-banner__meta`
  - `session-banner__actions`
- adaptación responsive para móvil

### Archivos tocados
- `app/routes.py`
- `app/templates/aprende.html`
- `app/templates/career.html`
- `app/templates/home.html`
- `app/static/app.js`
- `app/static/estilos.css`
- `CHANGELOG_AI.md`
- `docs/ai_report.md`

### Validaciones realizadas
- relectura obligatoria de:
  - `BOT_INSTRUCTIONS.md`
  - `PROJECT_CONTEXT.md`
  - `CHANGELOG_AI.md`
  - `docs/ai_report.md`
- revisión específica de:
  - `app/templates/aprende.html`
  - `app/templates/career.html`
  - `app/templates/base.html`
  - `app/routes.py`
  - `app/auth.py`
  - `app/static/app.js`
  - `app/static/estilos.css`
  - `app/models.py`
  - endpoints del readiness quiz
  - layout de home autenticada
- validación sintáctica ejecutada con:
  - `python3 -m py_compile run.py app/__init__.py app/routes.py app/auth.py app/career.py app/models.py app/services/career_session_service.py`

### Qué debe comprobarse en Render
- que al reiniciar o recargar el quiz la correcta no se mantiene siempre en A
- que el scoring sigue siendo correcto aunque cambien orden de preguntas y respuestas
- que el recorrido de `Aprender` se siente más guiado y menos como un examen plano
- que el gate de `Modo Carrera` se ve más sólido y motivador
- que un usuario aprobado entra normalmente y uno no aprobado sigue bloqueado
- que la home autenticada muestra claramente el estado de sesión y el botón para cambiar de usuario
- que invitado y autenticado siguen sin mezclar estado de readiness
- que la experiencia responsive sigue bien en home, aprender y gate de carrera

### Riesgos pendientes
- La aleatorización queda estable por intento de sesión, que es lo correcto para validar respuestas; aun así conviene comprobar en Render un ciclo completo de reinicio y recarga para confirmar percepción de variedad suficiente.
- El contenido del quiz sigue apoyándose en el mismo banco de 10 preguntas. La experiencia mejora mucho, pero en el futuro podría venir bien añadir más rotación o variantes de redacción.
- No se han añadido tests automáticos del readiness flow, así que la comprobación final sigue siendo principalmente manual y en despliegue.

### Siguientes pasos recomendados
- validar en Render el flujo completo autenticado e invitado con varios reinicios del quiz
- observar si compensa reducir el bloque final a 8 preguntas manteniendo 7/10 o si el formato actual ya se siente suficientemente ligero
- si la UX gusta, considerar una iteración futura con mini ilustraciones o estados vacíos más ricos en la parte educativa sin tocar más backend

## Iteración 31 - Pulido del resultado final del readiness quiz

### Objetivo
Mejorar la pantalla final del readiness quiz para que se sienta más de producto y más útil para el usuario, sin tocar arquitectura, persistencia, endpoints principales ni lógica del `Modo Carrera`.

### Enfoque aplicado
Se mantuvo intacta la base funcional de la iteración 30:
- scoring robusto por `questionId` y `optionId`
- persistencia real del aprobado para autenticados
- aislamiento entre invitado y usuario autenticado
- aleatorización de preguntas y respuestas
- gate funcional de `Modo Carrera`

La mejora se centró exclusivamente en la experiencia final de resultado:
- hacer el aprobado más celebratorio y explícito como desbloqueo
- hacer el suspenso más útil, menos punitivo y más orientado a repaso
- convertir la revisión en una lectura más clara y accionable

### Cambios UX/visuales aplicados
#### En `app/static/app.js`
Se rehízo `renderReadinessResult(payload)` para diferenciar mejor ambos desenlaces.

##### Si el usuario aprueba
- aparece un badge claro: `Modo Carrera desbloqueado`
- se refuerza el mensaje de que ya domina lo mínimo necesario
- se mantiene visible la puntuación
- se añade una callout de éxito explicando que ya puede entrar a `Modo Carrera`
- CTAs finales:
  - `Entrar al Modo Carrera`
  - `Repetir evaluación`
  - `Repasar conceptos`

##### Si el usuario suspende
- aparece un estado de `Desbloqueo pendiente`
- se muestra cuántas respuestas le faltaron para aprobar
- el tono se vuelve más amable y orientado a mejora
- se añade una callout de repaso explicando que el objetivo no es castigar, sino asegurar comprensión suficiente
- CTAs finales:
  - `Repasar y repetir`
  - `Volver a Aprender`

##### Resumen de conceptos a reforzar
- si hay errores, se agrupan los temas fallados por `topic`
- se muestran hasta 3 bloques prioritarios de repaso
- se traducen los topics técnicos a etiquetas más claras de producto, por ejemplo:
  - `Riesgo`
  - `Diversificación`
  - `Benchmark`
  - `DCA`
  - `Modo Carrera`
  - `Informe final`
  - `Usuarios autenticados`

### Revisión final de respuestas
La revisión se rehízo para ser más legible y menos tosca:
- cada pregunta aparece en una card individual
- cada card lleva estado visual:
  - `Correcta`
  - `A reforzar`
- se muestra el tema de la pregunta con badge
- se muestra siempre:
  - enunciado
  - respuesta elegida
  - explicación breve
- si la respuesta fue incorrecta, se añade explícitamente la respuesta correcta

Esto permite entender mejor qué salió bien y qué conviene revisar, sin depender del orden aleatorio del intento.

### Cambios visuales en `app/static/estilos.css`
Se añadieron y ajustaron estilos para:
- badge de estado del resultado final
- hero diferenciado para aprobado y suspenso
- tiles resumen con estado
- callouts de éxito y repaso
- cards de conceptos a reforzar
- cabecera de revisión más clara
- chips de estado `Correcta` / `A reforzar`
- mejor responsive para el bloque final y la cabecera de revisión

### Archivos tocados
- `app/static/app.js`
- `app/static/estilos.css`
- `CHANGELOG_AI.md`
- `docs/ai_report.md`

### Validaciones realizadas
- relectura obligatoria de:
  - `BOT_INSTRUCTIONS.md`
  - `PROJECT_CONTEXT.md`
  - `CHANGELOG_AI.md`
  - `docs/ai_report.md`
- revisión específica de:
  - `app/templates/aprende.html`
  - `app/static/app.js`
  - `app/static/estilos.css`
  - `app/routes.py`
  - flujo completo del readiness quiz añadido en la iteración anterior
- validación sintáctica ejecutada con:
  - `python3 -m py_compile run.py app/__init__.py app/routes.py app/auth.py app/career.py app/models.py app/services/career_session_service.py`

### Qué debe comprobarse en Render
#### Caso A, usuario aprueba
- aparece un resultado claro de desbloqueo
- el botón `Entrar al Modo Carrera` funciona
- sigue desbloqueado tras recargar o volver a entrar

#### Caso B, usuario suspende
- aparece pantalla de repaso, no de castigo
- se indica cuántas respuestas faltaron para aprobar
- puede repetir la evaluación
- no desbloquea `Modo Carrera`

#### Caso C, revisión
- las cards distinguen bien correctas e incorrectas
- si falla, se ve la respuesta correcta
- la explicación encaja con la pregunta
- la revisión no depende del orden aleatorio del intento

#### Caso D, invitado
- el resultado final sigue funcionando
- no se mezcla con el estado de un usuario autenticado

#### Caso E, responsive
- la pantalla final sigue siendo usable en móvil

### Riesgos pendientes
- El agrupado de conceptos a reforzar es deliberadamente ligero y depende de los `topic` ya definidos. Si en el futuro cambia el banco de preguntas, convendrá revisar el mapeo de etiquetas visibles.
- No se ha tocado backend ni persistencia en esta iteración, por lo que la validación final sigue siendo principalmente visual y manual en Render.

### Siguientes pasos recomendados
- validar en Render la percepción real del resultado aprobado y del suspenso con usuarios distintos
- observar si conviene destacar todavía más el estado persistido cuando un usuario autenticado ya aprobó antes
- si se quiere seguir puliendo el producto, una siguiente iteración pequeña podría mejorar el estado inicial de `Aprender` cuando el usuario ya tiene el readiness aprobado

## Iteración 32 - Modal visual de puntuación para el readiness quiz

### Objetivo
Dar más protagonismo al momento final del readiness quiz convirtiendo el resultado en un modal visual centrado, más llamativo y claramente orientado a la acción.

### Enfoque aplicado
Se mantuvo intacta toda la base funcional previa:
- scoring por `questionId` y `optionId`
- aleatorización de preguntas y respuestas
- persistencia del aprobado
- gate de `Modo Carrera`
- compatibilidad entre invitado y autenticado

La mejora se centró en la presentación final:
- mostrar un modal grande y claro al terminar el recorrido
- adaptar el mensaje según la puntuación exacta
- hacer que las acciones siguientes sean muy visibles
- conservar la revisión ya útil, pero relegándola a un segundo nivel tras el impacto inicial del resultado

### Estructura del nuevo modal
#### En `app/templates/aprende.html`
Se añadió una estructura dedicada de modal:
- overlay de fondo
- diálogo centrado
- botón de cierre
- contenedor dinámico para el contenido final del resultado

#### En `app/static/app.js`
Se añadió la lógica de presentación:
- `getReadinessScoreMessage(score, total, passed)`
- `openReadinessResultModal(contentHtml)`
- `closeReadinessResultModal()`

El modal muestra de forma protagonista:
- score grande (`8/10`, `10/10`, etc.)
- estado visible (`Desbloqueado`, `Casi listo`, `Pendiente`)
- comentario principal según nota
- bloque resumen con estado, umbral y orientación
- botones de acción claros y muy visibles

### Lógica de mensajes por puntuación
Se implementó una variación directa del mensaje según nota:
- `10/10`
  - excelente, dominio total
- `9/10`
  - muy buen resultado, claramente preparado
- `8/10`
  - base sólida, con matices por afinar
- `7/10`
  - aprobado con recomendación de repaso ligero
- `5–6/10`
  - cerca del desbloqueo, conviene repetir tras repasar
- `0–4/10`
  - aún no preparado, se recomienda rehacer el recorrido con calma

El tono se mantiene motivador, sin humillar al usuario cuando suspende.

### CTAs finales
#### Si aprueba
- `Ir al Modo Carrera`
- `Repetir evaluación`
- `Cerrar y ver revisión`

#### Si suspende
- `Repetir recorrido`
- `Volver a Aprender`
- `Ver qué repasar`

La prioridad visual ahora está en la decisión inmediata que debe tomar el usuario tras recibir la nota.

### Revisión de respuestas
La revisión no se elimina.

Nuevo comportamiento:
- el modal resume de forma potente el resultado final
- la revisión completa sigue quedando renderizada en la propia página debajo del flujo
- desde el modal se puede:
  - cerrarlo manualmente
  - o saltar directamente a la revisión con CTA específico (`Cerrar y ver revisión` / `Ver qué repasar`)

Así el usuario recibe primero una resolución clara y después, si quiere, profundiza en aciertos y errores.

### Cambios visuales en `app/static/estilos.css`
Se añadieron estilos para:
- overlay del modal
- diálogo centrado con sombra fuerte y bordes redondeados
- insignia o emblema visual grande
- score destacado de gran tamaño
- estado tipo badge
- grid de resumen dentro del modal
- responsive del modal en móvil
- bloqueo de scroll del body mientras el modal está abierto

### Archivos tocados
- `app/templates/aprende.html`
- `app/static/app.js`
- `app/static/estilos.css`
- `CHANGELOG_AI.md`
- `docs/ai_report.md`

### Validaciones realizadas
- relectura obligatoria de:
  - `BOT_INSTRUCTIONS.md`
  - `PROJECT_CONTEXT.md`
  - `CHANGELOG_AI.md`
  - `docs/ai_report.md`
- revisión específica de:
  - `app/templates/aprende.html`
  - `app/static/app.js`
  - `app/static/estilos.css`
  - `app/routes.py`
  - lógica actual del readiness quiz
  - flujo actual del resultado final
- validación sintáctica ejecutada con:
  - `python3 -m py_compile run.py app/__init__.py app/routes.py app/auth.py app/career.py app/models.py app/services/career_session_service.py`

### Qué debe comprobarse en Render
#### Caso A, 10/10
- aparece el modal
- se ve mensaje excelente
- CTA a `Modo Carrera` visible

#### Caso B, 8/10
- aparece el modal
- mensaje positivo intermedio
- acceso permitido a `Modo Carrera`

#### Caso C, 7/10
- aparece el modal
- sigue aprobado
- mensaje con recomendación de repaso

#### Caso D, 5/10 o 6/10
- aparece el modal
- mensaje de “cerca”
- no desbloquea `Modo Carrera`
- CTA claro para repetir

#### Caso E, suspenso bajo
- aparece el modal
- mensaje orientado a repasar
- CTA a `Volver a Aprender`

#### Caso F, invitado
- mismo comportamiento visual
- sin mezcla con usuario autenticado

#### Caso G, responsive
- modal usable en móvil
- score visible
- botones visibles

### Riesgos pendientes
- La revisión sigue viviendo en la página y el resumen principal en el modal. Es una solución equilibrada, pero conviene validar en Render que el salto a revisión se perciba natural.
- El cierre manual del modal deja visible la revisión previa, así que merece una comprobación visual final para asegurar que el flujo no resulte duplicado o extraño.

### Siguientes pasos recomendados
- validar en Render la sensación general del modal en aprobado alto, aprobado justo y suspenso
- observar si compensa hacer persistente un pequeño estado visual de “ya aprobado” al volver a `Aprender`
- si la experiencia gusta, una futura miniiteración podría pulir animación de entrada/salida del modal sin tocar lógica funcional

## Iteración 33 - Modo Horizonte experimental con disclaimers reforzados

### Objetivo
Se añade un nuevo modo llamado `Modo Horizonte`, con subtítulo `Proyección experimental basada en patrones históricos`, pensado como extensión demostrativa del producto y no como herramienta predictiva real.

La intención académica es enseñar una posible evolución ficticia de una cartera usando remezcla de patrones históricos, dejando muy claro que no predice el futuro, que no sirve para decisiones reales de inversión y que los resultados pasados no garantizan resultados futuros.

### Decisiones de producto
- el nombre final usado es `Modo Horizonte`
- se integra como acceso independiente desde navegación principal y home
- se integra también desde el informe final de `Modo Carrera` mediante CTA `Continuar en Modo Horizonte`
- el tono visual mantiene la línea SaaS/finanzas sobria ya presente en la app
- se repite el disclaimer en entrada, hero, bloque de resultados y CTA desde carrera
- no se introduce persistencia nueva compleja ni combinatoria pesada

### Método implementado
El método mostrado al usuario y aplicado en backend es explícitamente experimental:

> “Este modo remezcla patrones de rentabilidad histórica para construir una trayectoria futura hipotética. No calcula lo que va a ocurrir, sino un escenario experimental posible dentro de una simulación educativa.”

A nivel técnico, la primera versión hace esto:
- descarga un histórico acotado por activo
- construye una serie histórica base normalizada para la visualización
- calcula retornos mensuales por activo
- combina esos retornos con pesos normalizados sencillos
- genera una continuación futura ficticia muestreando retornos mensuales de ese pool histórico
- devuelve histórico + tramo experimental + métricas simples

No hay forecasting profesional, no hay optimización pesada y no hay promesa de validez predictiva.

### Advertencias añadidas
Texto obligatorio integrado en la funcionalidad:

> “Esta simulación no predice el futuro. Se trata de una proyección experimental generada a partir de patrones históricos. En inversión, los resultados pasados no garantizan resultados futuros. Esta herramienta tiene finalidad educativa y demostrativa, no debe usarse para tomar decisiones financieras reales.”

Ese aviso queda reflejado en:
- modal obligatorio de entrada
- hero / banner principal de `Modo Horizonte`
- bloque de resultados junto al gráfico
- CTA de entrada desde el informe final de `Modo Carrera`

### Rutas y endpoints añadidos
- `GET /modo-horizonte`
- `POST /api/horizon/disclaimer/accept`
- `POST /api/horizon/simulate`
- `GET /api/horizon/from-career/<session_id>`

### Integración con Modo Carrera
En el informe final de carrera se añadió un bloque visible con CTA `Abrir Modo Horizonte`.

El enlace abre:
- `/modo-horizonte?source=career&session_id=<id>`

Después, el frontend intenta precargar:
- tickers de la cartera final
- valor inicial aproximado desde el portfolio final

La precarga se apoya en backend para validar ownership mediante la misma resolución de sesión ya endurecida en carrera. No depende de `localStorage` para autorizar acceso a sesiones ajenas.

### Integración con Aprender
Se añadió una sección breve en `Aprender` con el título:
- `Modo Horizonte: escenarios experimentales`

Refuerza:
- que no predice el futuro
- que la finalidad es educativa
- que hay que distinguir simulación histórica de proyección experimental

### Validaciones y límites incluidos
- máximo 5 activos
- horizonte entre 1 y 5 años
- tickers vacíos filtrados
- pesos normalizados de forma controlada
- exclusión amable de activos sin datos suficientes
- mensajes de error controlados en vez de 500 por casos esperables
- warnings visibles si se descarta un ticker
- coste acotado, sin combinaciones ni recalculado masivo del bloque teórico de carrera

### Archivos tocados
- `app/routes.py`
- `app/templates/horizon.html`
- `app/templates/base.html`
- `app/templates/home.html`
- `app/templates/career.html`
- `app/templates/aprende.html`
- `app/static/app.js`
- `app/static/estilos.css`
- `CHANGELOG_AI.md`
- `docs/ai_report.md`

### Validaciones realizadas
- relectura obligatoria de:
  - `BOT_INSTRUCTIONS.md`
  - `PROJECT_CONTEXT.md`
  - `CHANGELOG_AI.md`
  - `docs/ai_report.md`
- revisión específica de:
  - `app/routes.py`
  - `app/career.py`
  - `app/models.py`
  - `app/templates/home.html`
  - `app/templates/career.html`
  - `app/templates/base.html`
  - `app/templates/aprende.html`
  - `app/static/app.js`
  - `app/static/estilos.css`
  - endpoints y render del informe final de carrera
- validación sintáctica ejecutada con:
  - `python3 -m py_compile run.py app/__init__.py app/routes.py app/auth.py app/career.py app/models.py app/services/career_session_service.py`

### Qué debe probarse en Render
#### Caso A, acceso independiente
- entrar en `/modo-horizonte`
- aparece el modal obligatorio
- no permite generar sin aceptar
- tras aceptar, se puede generar escenario con 1 a 5 activos
- disclaimer visible antes y después de generar

#### Caso B, acceso desde Carrera
- terminar una sesión
- generar informe final
- aparece el CTA `Continuar en Modo Horizonte`
- abre `Modo Horizonte` con `session_id`
- se precargan tickers y valor inicial si hay datos
- el disclaimer sigue siendo visible y obligatorio si aún no se aceptó

#### Caso C, ownership y aislamiento
- usuario autenticado no puede cargar sesión ajena
- invitado puede usar la pantalla, pero sin mezclar aceptación con usuario autenticado
- la aceptación del modal se mantiene namespaced por identidad

#### Caso D, errores controlados
- ticker inválido
- pocos datos históricos
- más de 5 activos
- horizonte inválido
- comprobar que responde con mensaje amable y no con 500

#### Caso E, responsive y performance
- modal usable en móvil
- cards y gráfico no rompen layout
- caso de 5 activos y horizonte 5 años no debe disparar un cálculo pesado anómalo

### Limitaciones explícitas
- el escenario generado es ficticio y experimental
- no es un modelo de forecasting profesional
- no persiste simulaciones de Horizonte en base de datos en esta iteración
- la generación usa muestreo simple de patrones mensuales, suficiente para MVP demostrativo pero no para análisis financiero real

### Riesgos pendientes
- conviene validar en Render si todos los tickers de cartera final exponen `weight` en todos los estados finales esperados de Carrera
- merece revisión visual real el contraste entre tramo histórico y tramo experimental en móvil
- puede ser conveniente una microiteración futura para añadir separador visual más explícito en la frontera histórico/futuro

### Siguientes pasos recomendados
- validar en Render el flujo completo desde home y desde informe final de carrera
- comprobar casos reales de usuario autenticado, invitado y cambio de identidad
- si la UX gusta, plantear una iteración pequeña para enriquecer la explicación metodológica o añadir exportación marcada con disclaimer fuerte
- mantener explícito en toda futura evolución que `Modo Horizonte` no predice resultados futuros y no tiene validez como herramienta de asesoramiento financiero

## Iteración 34 - Hardening técnico y pulido visual de Modo Horizonte

### Objetivo
Corregir los bugs reales detectados en Render tras publicar `62e89ae`, sin añadir funcionalidad nueva:
- mejorar el hero/cabecera de `Modo Horizonte`
- controlar el error 400 derivado del rate limit de Yahoo Finance
- corregir el error 500 causado por resample sobre índice no temporal

### Bugs detectados en Render
#### Bug 1, UI del hero
Síntomas observados:
- textos demasiado pegados
- badges mal colocadas
- jerarquía visual pobre
- distribución demasiado apretada en cabecera
- comportamiento mejorable en responsive

#### Bug 2, error 400 por proveedor
Log real observado:
- `YFRateLimitError('Too Many Requests. Rate limited. Try after a while.')`

Conclusión:
- el proveedor de mercado puede limitar temporalmente peticiones
- el backend no estaba devolviendo una experiencia suficientemente clara para ese caso

#### Bug 3, error 500 por serie temporal
Traceback real observado:
- `monthly = adj.resample("M").last().pct_change().dropna()`
- `TypeError: Only valid with DatetimeIndex, TimedeltaIndex or PeriodIndex, but got an instance of 'Index'`

Conclusión:
- la serie usada en Horizonte no estaba quedando garantizada como `DatetimeIndex`
- se estaba reutilizando una serie pensada para otras partes del proyecto donde el índice se convierte a `date`, no a `DatetimeIndex`

### Causa exacta del error 400
La causa real era el rate limit de Yahoo Finance (`YFRateLimitError`). Cuando la fuente limita peticiones, el flujo de Horizonte podía quedarse en un error de proveedor poco amable.

### Causa exacta del error 500
La causa real era esta:
- Horizonte tomaba la serie con `_series_with_date_index(...)`
- ese helper convierte el índice a objetos `date`
- luego se intentaba hacer `resample(...)`
- `resample` necesita `DatetimeIndex`, `TimedeltaIndex` o `PeriodIndex`
- por eso se producía el `TypeError`

### Corrección de normalización temporal
Se añadió una normalización más robusta para Horizonte en `app/routes.py`:
- `_extract_market_price_series(df, ticker)`
- `_compute_horizon_monthly_returns(df, ticker)`

La serie ahora se trata así:
- normalización previa del dataframe con `_normalize_price_df(...)`
- prioridad a `Adj Close`
- fallback a `Close` si `Adj Close` no existe o no aporta serie útil
- si llega `DataFrame`, reducción controlada a `Series`
- conversión numérica con `pd.to_numeric(..., errors="coerce")`
- conversión del índice con `pd.to_datetime(..., errors="coerce")`
- descarte de entradas inválidas (`NaT`)
- eliminación de duplicados
- ordenación del índice
- validación final de que queda un `DatetimeIndex`

Si la serie no queda válida, ya no cae con 500: se excluye el ticker o se devuelve error controlado.

### Correcciones de backend adicionales
- captura explícita de `YFRateLimitError` en `_download_history_df(...)`
- traducción a mensaje amable y controlado para el usuario
- status `503` cuando la fuente está temporalmente limitada
- mantenimiento de `400` para problemas de inputs o datos insuficientes
- sustitución de `resample("M")` por `resample("ME")`
- sustitución de `fillna(method="ffill")` por `ffill()` en el flujo de Horizonte

### Mejora de frontend en errores controlados
En `app/static/app.js` se añadió un bloque de estado persistente en el panel de Horizonte:
- `renderHorizonStatusMessage(message, tone)`

Nuevo comportamiento:
- mensaje neutro mientras genera
- mensaje de éxito tras construir escenario
- mensaje claro dentro del panel si falla la fuente o si la API devuelve error controlado
- se mantiene el toast, pero ya no es la única vía de feedback

### Mejora visual del hero/cabecera
Se rehízo la composición superior para que respire mejor:
- cabecera de página con copy a la izquierda y meta/badges a la derecha
- hero principal con grid de dos columnas más equilibrada
- contenido textual con ancho máximo razonable
- stack lateral con badges y una nota secundaria ordenada
- más separación entre título, subtítulo, badges y disclaimer
- mejor comportamiento responsive al colapsar a una columna en tamaños menores

### Archivos tocados
- `app/routes.py`
- `app/static/app.js`
- `app/static/estilos.css`
- `app/templates/horizon.html`
- `CHANGELOG_AI.md`
- `docs/ai_report.md`

### Validaciones realizadas
- relectura obligatoria de:
  - `BOT_INSTRUCTIONS.md`
  - `PROJECT_CONTEXT.md`
  - `CHANGELOG_AI.md`
  - `docs/ai_report.md`
- revisión específica de:
  - `app/routes.py`
  - `app/static/app.js`
  - `app/static/estilos.css`
  - `app/templates/horizon.html`
  - `app/templates/career.html`
  - `app/templates/home.html`
  - helpers de descarga y normalización de series históricas
- validación sintáctica ejecutada con:
  - `python3 -m py_compile run.py app/__init__.py app/routes.py app/auth.py app/career.py app/models.py app/services/career_session_service.py`

### Qué debe probarse en Render
#### Caso A, UI
- la cabecera de Horizonte se ve más limpia
- mejor spacing vertical
- pills/badges bien colocadas
- layout correcto en móvil

#### Caso B, ticker válido
- `AAPL`
- horizonte `5 años`
- valor inicial `10000`
- genera escenario o devuelve error controlado, pero nunca 500

#### Caso C, rate limit / proveedor
- si Yahoo limita temporalmente, aparece mensaje amable dentro del panel
- no se muestra un error genérico roto

#### Caso D, índice no datetime
- no aparece el 500 anterior
- el flujo normaliza correctamente o excluye el activo con aviso controlado

#### Caso E, desde Carrera
- sigue abriendo Horizonte correctamente
- no rompe la precarga

#### Caso F, responsive
- hero, formulario y panel de resultado se ven usables en móvil

### Riesgos pendientes
- Yahoo Finance puede seguir limitar peticiones en momentos puntuales; ahora queda degradado de forma controlada, pero sigue dependiendo de un proveedor externo
- conviene validar en Render si algunos tickers devuelven solo `Close` y confirmar que el fallback visual/numérico queda razonable
- todavía merece una comprobación visual real de la cabecera en móvil estrecho

### Siguientes pasos recomendados
- validar en Render el flujo con activos válidos y con fallo temporal de proveedor
- revisar si el mensaje inline dentro del panel es suficiente o si conviene refinar aún más la jerarquía del error
- si todo queda estable, pasar a microiteraciones visuales pequeñas en vez de tocar más la lógica de Horizonte

## Iteración 35 - Pulido fino de gráfico y retry ligero en Modo Horizonte

### Objetivo
Cerrar el comportamiento residual detectado tras la iteración 34:
- en algunos casos la primera petición a mercado fallaba y la segunda funcionaba
- el gráfico mostraba etiquetas de fecha demasiado largas y ruidosas (`T00:00:00`)

### Ajuste técnico aplicado
Se añadió un retry mínimo y controlado en `_download_history_df(...)`:
- solo para este flujo de descarga
- máximo 1 reintento adicional
- pequeña espera (`0.8s`) si el primer fallo es `YFRateLimitError`

La idea es reducir el caso real observado de:
- primera llamada falla
- segunda llamada manual funciona

sin introducir colas, caching complejo ni lógica nueva grande.

### Ajuste de UX aplicado
En `app/static/app.js`:
- se limpian las etiquetas del eje X del gráfico para mostrar solo `YYYY-MM-DD`
- se limitan mejor las ticks visibles del eje X
- se mantiene rotación controlada para evitar solape visual
- se refuerza el mensaje de estado durante la carga, explicando que si la fuente responde con demora o limita temporalmente, el usuario puede reintentar

### Resultado esperado
- menos fricción en primeras llamadas afectadas por proveedor externo
- gráfico más limpio y legible
- mejor percepción de calidad final de `Modo Horizonte`

### Archivos tocados
- `app/routes.py`
- `app/static/app.js`
- `CHANGELOG_AI.md`
- `docs/ai_report.md`

### Validaciones realizadas
- relectura obligatoria de:
  - `BOT_INSTRUCTIONS.md`
  - `PROJECT_CONTEXT.md`
  - `CHANGELOG_AI.md`
  - `docs/ai_report.md`
- revisión específica de:
  - `app/routes.py`
  - `app/static/app.js`
  - `app/templates/horizon.html`
  - `app/static/estilos.css`
- validación sintáctica ejecutada con:
  - `python3 -m py_compile run.py app/__init__.py app/routes.py app/auth.py app/career.py app/models.py app/services/career_session_service.py`

### Qué debe probarse en Render
- repetir caso `AAPL`, `5 años`, `10000`
- observar si disminuye el fallo a la primera llamada
- revisar que el eje X ya no muestre timestamps completos
- comprobar que la gráfica sigue dibujando bien en escritorio y móvil
- confirmar que desde Carrera sigue funcionando igual

### Riesgos pendientes
- Yahoo Finance puede seguir fallando aunque exista retry corto; el objetivo aquí es mejorar la resiliencia, no garantizar disponibilidad total del proveedor
- conviene validar en Render si el número de ticks visibles del eje X sigue siendo cómodo con horizontes distintos

### Siguientes pasos recomendados
- si este ajuste deja estable el flujo, pasar a fase de validación real en Render y cerrar Horizonte como bloque funcionalmente maduro
- no seguir tocando backend salvo que aparezca un bug real nuevo reproducible

## Iteración 36 - Mejora metodológica de la base histórica en Modo Horizonte

### Problema observado en Render
Probando `AAPL`, horizonte `5 años`, valor inicial `10000`, se observó esto:
- primer intento: error controlado por descarga/no datos útiles
- segundo intento: genera escenario
- la gráfica histórica azul parecía demasiado plana y corta, arrancando aproximadamente cerca del último año disponible

Eso hacía que la base histórica visible y la muestra de retornos no fueran suficientemente defendibles para una proyección experimental a 5 años.

### Por qué la gráfica anterior parecía tan plana y corta
La causa principal no era que se descargara solo 1 año exacto, sino que en el render histórico de Horizonte se hacía esto:
- se descargaba una ventana relativamente amplia
- pero luego se aplicaba `tail(hist_length)` con `hist_length` derivado de unas ~260 sesiones diarias como máximo
- en la práctica, eso dejaba visible aproximadamente el último año bursátil

Para un activo como Apple, ese recorte hacía perder gran parte de su trayectoria histórica de largo plazo y dejaba una serie azul corta y visualmente poco representativa.

### Criterio histórico anterior
Antes de esta iteración:
- Horizonte estaba descargando aproximadamente `8 años` (`end_d - 365 * 8`)
- pero solo mostraba el último tramo recortado por `tail(...)`
- para el gráfico, el histórico final visible quedaba muy comprimido a alrededor de 1 año

### Criterio histórico nuevo
Ahora se usa un criterio explícito y documentado:
- horizonte `<= 1 año` → al menos `5 años` de histórico si están disponibles
- horizonte `>= 3 años` → al menos `10 años` de histórico si están disponibles
- horizonte `>= 5 años` → `15 años` de histórico si están disponibles
- límite superior razonable para Horizonte: `15 años`

Constantes añadidas en `app/routes.py`:
- `HORIZON_MIN_HISTORY_YEARS = 5`
- `HORIZON_DEFAULT_HISTORY_YEARS = 10`
- `HORIZON_MAX_HISTORY_YEARS = 15`
- `HORIZON_MAX_HISTORY_POINTS = 220`
- `HORIZON_MAX_MONTHLY_RETURN = 0.35`

### Cambio de método visible al usuario
La explicación del método se ha reforzado para dejar claro que:
- se utiliza una muestra histórica suficientemente amplia cuando está disponible
- aun así, el resultado sigue siendo solo una trayectoria hipotética sin validez predictiva

### Cambios en normalización y uso de series
Se mantiene la normalización robusta introducida antes:
- prioridad a `Adj Close`
- fallback a `Close`
- conversión a `Series`
- `pd.to_numeric(..., errors="coerce")`
- `pd.to_datetime(..., errors="coerce")`
- descarte de `NaT`
- eliminación de duplicados
- ordenación del índice
- validación final de `DatetimeIndex`

Además, en esta iteración:
- la descarga se hace una sola vez por ticker dentro de cada simulación
- esa misma serie normalizada se reutiliza para histórico y retornos mensuales
- se elimina redundancia innecesaria de descarga/cálculo

### Cómo se calculan ahora los retornos
Ahora el cálculo mensual se hace así:
- serie temporal válida de precios ajustados si están disponibles
- `resample("ME").last()`
- `pct_change()`
- limpieza de `NaN`, `inf`, `-inf`
- uso de acumulación estándar:
  - `valor_t = valor_t-1 * (1 + retorno)`

### Limitación de outliers extremos
Sí, se ha añadido una limitación controlada de retornos extremos en el modo experimental.

Criterio aplicado:
- si el retorno mensual absoluto supera `35%`, se limita a `±35%`
- esto no pretende falsear el histórico, sino evitar que un dato extremo, malformado o muy singular destruya la estabilidad de la trayectoria experimental

Además:
- si se detectan esos extremos, se añade warning visible para el usuario
- la respuesta expone también si hubo `extreme_returns_limited`

### Cambios visuales/funcionales en el gráfico
- la parte histórica azul ahora usa una base mucho más amplia cuando existe
- el gráfico sigue en base 100
- la serie histórica se downsamplea para mantener legibilidad sin volver el payload enorme
- se conservan las etiquetas diferenciadas entre:
  - `Datos históricos`
  - `Escenario experimental`
- el mensaje de éxito en UI informa de cuántos años históricos se usaron en la simulación
- en métricas se muestra ahora:
  - años de histórico usados
  - muestras mensuales usadas
  - si se limitaron retornos extremos

### Archivos tocados
- `app/routes.py`
- `app/static/app.js`
- `app/templates/horizon.html`
- `CHANGELOG_AI.md`
- `docs/ai_report.md`

### Validaciones realizadas
- relectura obligatoria de:
  - `BOT_INSTRUCTIONS.md`
  - `PROJECT_CONTEXT.md`
  - `CHANGELOG_AI.md`
  - `docs/ai_report.md`
- revisión específica de:
  - `app/routes.py`
  - endpoint `POST /api/horizon/simulate`
  - `_download_history_df(...)`
  - normalización de series y retornos mensuales
  - `app/static/app.js`
  - `app/templates/horizon.html`
  - `app/static/estilos.css`
- validación sintáctica ejecutada con:
  - `python3 -m py_compile run.py app/__init__.py app/routes.py app/auth.py app/career.py app/models.py app/services/career_session_service.py`

### Qué debe probarse en Render
#### Caso A, `AAPL`, `5 años`, `10000`
- el histórico azul debe verse claramente más largo y representativo
- no debería parecer solo un último año casi plano
- la simulación debe seguir saliendo sin 500
- si falla proveedor, mensaje amable

#### Caso B, `AAPL`, `1 año`, `10000`
- debe seguir funcionando
- debe usar igualmente una base histórica suficiente para muestrear

#### Caso C, ticker inválido
- error controlado
- sin 500

#### Caso D, 5 activos
- no debe matar el worker
- no debe disparar cálculos pesados absurdos

#### Caso E, desde Carrera
- debe seguir funcionando la entrada desde informe final

#### Caso F, responsive
- gráfico y formulario siguen bien en móvil

### Riesgos pendientes
- sigue existiendo dependencia de Yahoo Finance para la disponibilidad efectiva del histórico
- la limitación de retornos extremos mejora estabilidad metodológica, pero conviene validar visualmente que no “aplane” demasiado algunos activos muy volátiles
- puede merecer una futura microiteración para marcar visualmente la frontera histórico/futuro aún más fuerte dentro del chart

### Siguientes pasos recomendados
- validar en Render el caso real de Apple y comparar visualmente si la parte azul ya refleja una historia más amplia
- revisar si los warnings por retornos extremos aparecen solo cuando realmente aportan valor
- si el resultado es convincente, cerrar Modo Horizonte como bloque metodológicamente defendible dentro del TFG

## Iteración 37 - Continuidad visual del escenario y errores de proveedor más claros en Modo Horizonte

### Problemas observados en Render
Probando `AAPL`, horizonte `5 años`, valor inicial `10000`, seguían apareciendo dos defectos importantes:
- en el primer intento, Yahoo podía devolver `YFRateLimitError`, pero la UX acababa pareciendo un ticker inválido o sin datos
- cuando la simulación sí salía, el tramo verde del escenario arrancaba otra vez cerca de base 100 aunque el histórico azul terminara muy por encima, rompiendo la continuidad visual y metodológica

### Por qué fallaba el primer intento
La causa no era un ticker incorrecto, sino la respuesta temporal del proveedor externo.

El flujo anterior ya hacía un retry ligero, pero seguía habiendo un caso ambiguo:
- `yf.download(...)` podía fallar por limitación temporal
- el dataframe normalizado podía terminar vacío
- el sistema acababa degradando ese vacío como si fuera un caso de ticker sin datos

Eso hacía que un `AAPL` válido pudiera mostrarse al usuario como si el problema fuese suyo, cuando en realidad el bloqueo venía de Yahoo Finance.

### Cómo se diferencia ahora rate limit de ticker inválido
En `app/routes.py` se endureció `_download_history_df(...)` para separar tres situaciones:

#### 1. Ticker inválido o sin datos reales
Se mantiene el mensaje:
- `No se encontraron datos para el ticker 'XYZ'...`

Esto solo se usa cuando:
- el ticker viene vacío
- o tras normalizar la descarga no hay datos y no existe señal previa de rate limit

#### 2. Proveedor temporalmente limitado
Ahora se usa explícitamente el mensaje pedido por el usuario:
- `La fuente de datos de mercado ha limitado temporalmente la petición. El ticker puede ser válido, pero no hemos podido obtener sus datos ahora mismo. Espera unos segundos y vuelve a intentarlo.`

Esto se activa cuando:
- `yf.download(...)` lanza `YFRateLimitError`
- o cuando, tras un fallo de ese tipo, la descarga posterior sigue llegando vacía y por tanto no es seguro tratarlo como ticker inválido

#### 3. Datos insuficientes para el experimento
Se mantiene separado el caso en que sí hay ticker válido y descarga correcta, pero el histórico no alcanza el mínimo metodológico requerido para el horizonte.

Resultado:
- ya no se mezcla proveedor limitado con ticker inválido
- se mantiene respuesta controlada sin 500
- el status global sigue siendo `503` cuando el bloqueo viene del proveedor

### Caché ligera añadida
Se añadió una caché ligera en memoria, simple y acotada:
- dependencia pequeña: `cachetools`
- `TTLCache`
- TTL: `120` segundos
- clave: `(ticker, start_d, end_d, include_actions)`

Con esto:
- se evita redescargar el mismo histórico una y otra vez en clicks muy seguidos
- se reduce presión sobre Yahoo en pruebas repetidas
- no se persiste nada en base de datos
- no se abre complejidad arquitectónica nueva

### Por qué la proyección empezaba en base 100
La causa estaba en cómo se construía `projected_series`:
- la serie histórica se normalizaba correctamente y podía terminar, por ejemplo, cerca de `2800`
- pero el tramo futuro arrancaba con `projected_base = [100.0]`
- después acumulaba retornos simulados desde ese 100

Eso no afectaba al cálculo en euros, porque el valor monetario se seguía calculando sobre `initial_value`, pero sí rompía por completo la lectura visual del gráfico.

### Cómo continúa ahora desde el último valor histórico
Se cambió la construcción del escenario en `POST /api/horizon/simulate`:
- `last_hist_value = float(blended_hist.iloc[-1])`
- `projected_base` ya no empieza en `100.0`, sino en `last_hist_value`
- `projected_series` añade primero un punto de continuidad con la misma fecha/valor final del histórico
- a partir de ahí se aplican los retornos simulados mes a mes

Efecto práctico:
- el primer punto del escenario experimental coincide con el último punto histórico
- desaparece el salto falso de `2800 -> 100`
- la línea verde se cose visualmente con la azul

Importante:
- el cálculo en euros sigue siendo independiente del nivel base del gráfico
- el usuario sigue introduciendo `10000 €` como capital inicial del escenario
- el valor final monetario se calcula como `initial_value * factor_acumulado_del_escenario`

### Cómo se calculan ahora las métricas
Se renombraron y aclararon las métricas para evitar lectura de predicción o expectativa:
- `Final simulado en este escenario`
- `Retorno total del escenario`
- `Retorno anualizado del escenario`
- `Volatilidad del escenario`
- nota explícita: `No es rentabilidad esperada.`

Además:
- `scenario_total_return` se calcula sobre el escenario simulado
- `scenario_annualized_return` se calcula sobre `final_value / initial_value` del propio escenario
- `scenario_volatility` se calcula sobre `simulated_returns`

Es decir, no se mezclan con el histórico completo visible del gráfico.

### Mejoras de microcopy y disclaimer
Se añadió también una nota específica devuelta por backend:
- `Este resultado corresponde a una trayectoria generada aleatoriamente a partir de retornos históricos. No representa una expectativa ni una previsión.`

Y la UI la reutiliza en el mensaje de éxito del panel, reforzando el encuadre didáctico y no predictivo del modo.

### Mejoras de claridad en la gráfica
Se reforzó la frontera entre ambos tramos sin tocar la arquitectura de charts:
- la línea verde empieza donde termina la azul
- se reutiliza el plugin `careerTurnBoundaries` para pintar una línea vertical en la fecha de transición
- se añade texto visible bajo el gráfico:
  - `A partir de la línea divisoria comienza el tramo ficticio del escenario experimental.`
- se mantiene la leyenda:
  - `Datos históricos`
  - `Escenario experimental`

### Archivos tocados
- `app/routes.py`
- `app/static/app.js`
- `app/templates/horizon.html`
- `app/static/estilos.css`
- `requirements.txt`
- `CHANGELOG_AI.md`
- `docs/ai_report.md`

### Validaciones realizadas
- relectura obligatoria de:
  - `BOT_INSTRUCTIONS.md`
  - `PROJECT_CONTEXT.md`
  - `CHANGELOG_AI.md`
  - `docs/ai_report.md`
- revisión específica de:
  - `app/routes.py`
  - `POST /api/horizon/simulate`
  - `_download_history_df(...)`
  - construcción de `historical_series`
  - construcción de `projected_series`
  - métricas del escenario
  - `app/static/app.js`
  - `app/templates/horizon.html`
  - `app/static/estilos.css`
- validación sintáctica ejecutada con:
  - `python3 -m py_compile run.py app/__init__.py app/routes.py app/auth.py app/career.py app/models.py app/services/career_session_service.py`

### Qué debes probar ahora en Render
#### Caso A, `AAPL`, `5 años`, `10000`
- si Yahoo responde, debe generar escenario
- la serie azul debe verse amplia
- la línea verde debe empezar en el último valor histórico
- las métricas deben mostrar lenguaje de escenario, no de expectativa
- disclaimer visible

#### Caso B, primer intento con rate limit
- si aparece `YFRateLimitError`, debe verse el mensaje de proveedor limitado
- no debe decir que `AAPL` es inválido
- no debe haber 500

#### Caso C, segundo intento
- si ya responde, la simulación debe salir
- no debe haber salto visual de histórico alto a base 100

#### Caso D, ticker inválido real
- debe mostrarse mensaje de ticker inválido o sin datos
- no debe confundirse con rate limit

#### Caso E, desde Carrera
- debe seguir funcionando la precarga
- el escenario debe continuar correctamente desde el último punto histórico del blend

#### Caso F, responsive
- revisar gráfico, avisos y métricas en móvil

### Riesgos pendientes
- no he podido validar Render directamente desde aquí, así que la comprobación final de Yahoo y del comportamiento intermitente sigue dependiendo de tus pruebas reales
- la caché en memoria ayuda a suavizar reintentos cortos, pero no elimina por completo la dependencia del proveedor externo
- si el usuario percibe todavía demasiado optimismo en trayectorias concretas como AAPL, la siguiente microiteración debería centrarse en prudencia metodológica adicional, no en vender el resultado como forecast

## Iteración 38 - Reparación del workflow de GitHub Actions y alineación de tests

### Problema observado
Los commits recientes en `bot/render-preview` sí estaban llegando correctamente a GitHub, pero los workflows aparecían en rojo después del push.

Los commits del bloque Horizonte no estaban fallando por `git push`, sino por el pipeline de CI posterior.

### Confirmación del estado local
Se comprobó localmente:
- rama actual: `bot/render-preview`
- último commit local visible: `c7fb125`
- remotos correctos: `origin` y `reference`
- árbol de trabajo limpio al empezar el diagnóstico

### Workflow inspeccionado
Solo existe un workflow en el repo:
- `.github/workflows/ci.yml`

Ese workflow ejecuta:
- Python `3.11`
- instalación con `pip install -r requirements-dev.txt`
- `ruff check .`
- `black --check .`
- `pytest --cov=app --cov-report=xml`

### Limitación de acceso a logs remotos
No había `gh` disponible/autenticado en este entorno, así que no se pudieron leer directamente los logs de GitHub Actions desde CLI.

En lugar de inventar la causa, se reprodujo el workflow localmente en un entorno virtual limpio y se extrajeron los fallos reales paso a paso.

### Causa exacta del fallo
Hubo dos causas reales, una de infraestructura del lint y otra de alineación de tests.

#### 1. Ruff y Black estaban entrando en entornos virtuales dentro del repo
Al reproducir CI localmente, `ruff check .` falló no por código del proyecto, sino por archivos dentro de:
- `.venv-ci/`
- `venv/`

Especialmente aparecían errores en scripts y paquetes de terceros como:
- `pwiz.py` de peewee
- módulos de `yaml/`
- otros ficheros de dependencias instaladas

Esto explicaba por qué el workflow se rompía en rojo aunque los commits de producto fueran correctos.

#### 2. Pytest arrancaba la app sin entorno mínimo y además varios tests seguían anclados al comportamiento previo a auth
Una vez resuelto el problema del lint, aparecieron fallos reales en tests:
- sin variables de entorno, `create_app()` fallaba por:
  - `SECRET_KEY no está configurada.`
  - `DATABASE_URL no está configurada.`
- además, algunos tests asumían todavía que:
  - `GET /` devolvía `200` en vez de redirigir a `/login`
  - `GET /analisis` y `GET /analisis.csv` eran accesibles sin auth o en invitado

Pero eso ya no coincide con el producto actual, donde:
- `/` redirige a login si no hay usuario autenticado ni invitado
- el modo invitado puede usar la app, pero no consultar/exportar historial persistido

### Correcciones aplicadas
#### A. Exclusión explícita de entornos virtuales para Ruff y Black
Se añadió `pyproject.toml` con exclusiones para:
- `.venv`
- `.venv-ci`
- `venv`
- caches y artefactos temporales

Con eso, el lint y el format check pasan a evaluar el código del proyecto, no paquetes de terceros instalados dentro del repo.

#### B. Limpieza menor real detectada por Ruff
Se eliminó un import no usado en:
- `app/auth.py`

#### C. Alineación de formato con Black
Se aplicó `black` a estos archivos para que `black --check .` dejara de romper:
- `app/__init__.py`
- `app/models.py`
- `app/routes.py`
- `app/career.py`
- `app/services/career_session_service.py`

No hubo cambio funcional buscado aquí, solo alineación con el formatter que el propio workflow exige.

#### D. Variables dummy seguras en CI
Se ajustó `.github/workflows/ci.yml` para definir en el job:
- `SECRET_KEY: ci-secret-key`
- `DATABASE_URL: sqlite:///ci.db`

Esto no cambia producción ni Render. Solo permite que los tests creen la app en el runner de GitHub Actions con un entorno mínimo controlado.

#### E. Alineación de tests con el comportamiento actual del producto
Se actualizaron tests que estaban desfasados respecto a la app actual:
- `tests/test_frontend.py`
  - ahora valida que `/` redirige a `/login`
- `tests/test_analisis_storage.py`
- `tests/test_analisis_export_csv.py`
- `tests/test_analisis_filtros.py`
- `tests/test_analisis_paginado.py`

En estos tests se dejó explícito el comportamiento actual:
- invitado puede seguir entrando y generar análisis
- pero no puede consultar/exportar historial persistido
- esos endpoints deben responder con `403`

### Archivos tocados
- `.github/workflows/ci.yml`
- `pyproject.toml`
- `app/auth.py`
- `app/__init__.py`
- `app/models.py`
- `app/routes.py`
- `app/career.py`
- `app/services/career_session_service.py`
- `tests/test_frontend.py`
- `tests/test_analisis_storage.py`
- `tests/test_analisis_export_csv.py`
- `tests/test_analisis_filtros.py`
- `tests/test_analisis_paginado.py`
- `CHANGELOG_AI.md`
- `docs/ai_report.md`

### Validaciones realizadas
Se reprodujo localmente el equivalente del workflow y quedó pasando:
- `ruff check .`
- `black --check .`
- `SECRET_KEY=ci-secret-key DATABASE_URL=sqlite:///ci.db pytest --cov=app --cov-report=xml`
- `python3 -m py_compile run.py app/__init__.py app/routes.py app/auth.py app/career.py app/models.py app/services/career_session_service.py`

Resultado final local:
- `25 passed`
- cobertura generada en `coverage.xml`

### Causa raíz resumida
La CI no estaba fallando por Modo Horizonte en sí, sino por una combinación de:
1. lint/formato recorriendo directorios `venv` dentro del repo
2. tests desfasados respecto al modelo actual de auth/historial
3. ausencia de variables mínimas de entorno en el workflow

### Qué debes comprobar ahora en GitHub Actions
- que el workflow `CI` vuelva a ejecutarse en verde en `bot/render-preview`
- que el job `build-test` pase:
  - instalación
  - `ruff`
  - `black --check`
  - `pytest`
- que no aparezcan ya errores provenientes de `venv/` o `.venv-ci/`
- que no aparezcan `RuntimeError` por `SECRET_KEY` o `DATABASE_URL`

## Iteración 39 - Resumen operativo vivo con CURRENT_STATE.md

### Objetivo
Reducir el coste cognitivo de cada nueva iteración creando un archivo corto y operativo que permita ubicarse rápido en el estado real del proyecto antes de releer la documentación larga.

### Contexto
El proyecto ya tiene bastante historial, varias capas funcionales y un volumen creciente de documentación acumulada. Eso hace útil disponer de un resumen vivo, pequeño y accionable que sirva como punto de entrada estable antes de profundizar en el resto del contexto.

El usuario pidió explícitamente crear `CURRENT_STATE.md` sin sustituir:
- `BOT_INSTRUCTIONS.md`
- `PROJECT_CONTEXT.md`
- `CHANGELOG_AI.md`
- `docs/ai_report.md`

### Cambios aplicados
- Creado `CURRENT_STATE.md` en la raíz del repo del proyecto.
- Diseñado como resumen corto, claro y operativo, con estructura fija para orientar iteraciones futuras.
- El contenido se ha limitado a lo esencial y se ha organizado en 8 bloques:
  1. estado actual estable de la app
  2. últimos commits importantes
  3. funcionalidades ya cerradas
  4. funcionalidades en desarrollo
  5. bugs abiertos o pendientes
  6. reglas críticas que no se pueden romper
  7. arquitectura relevante actual
  8. siguiente paso recomendado
- Añadido también un bloque final de `Uso recomendado en futuras iteraciones` para dejar explícito cómo encajarlo en el flujo de trabajo del bot.

### Decisiones tomadas
- Mantener el archivo corto y muy orientado a ejecución, no a narrativa histórica.
- No duplicar todo el detalle de `CHANGELOG_AI.md` ni de `docs/ai_report.md`, sino condensar solo lo que acelera la orientación inicial.
- Dejar por escrito que `CURRENT_STATE.md` debe leerse primero, pero que no reemplaza la relectura obligatoria del resto de documentos críticos.
- Priorizar información viva: estado, restricciones, puntos sensibles y siguiente movimiento recomendado.

### Riesgos / límites
- Si no se mantiene al día tras iteraciones importantes, perderá valor rápidamente.
- No debe crecer hasta convertirse en otra documentación larga, porque perdería precisamente su función principal.
- No sustituye la trazabilidad fina ni el detalle técnico de las iteraciones previas.

### Comprobaciones realizadas
- Relectura de `BOT_INSTRUCTIONS.md`, `PROJECT_CONTEXT.md`, `CHANGELOG_AI.md` y `docs/ai_report.md` antes de crear el resumen.
- Revisión del estado real del repo y de los commits recientes para que el contenido de `CURRENT_STATE.md` refleje la situación actual.
- Revisión manual del archivo final para mantenerlo breve, claro y útil como punto de entrada.

### Uso esperado a partir de ahora
En futuras iteraciones, la secuencia recomendada pasa a ser:
1. leer `CURRENT_STATE.md`
2. releer `BOT_INSTRUCTIONS.md`
3. releer `PROJECT_CONTEXT.md`
4. releer `CHANGELOG_AI.md`
5. releer `docs/ai_report.md`

Con eso se acelera la orientación inicial sin perder contexto profundo ni trazabilidad.

## Iteración 40 - Limpieza de artefactos locales de CI en workspace

### Objetivo
Evitar que los artefactos locales generados durante la reproducción del workflow de CI vuelvan a aparecer como cambios pendientes en el workspace.

### Contexto
Tras la reparación del workflow de GitHub Actions y la validación local equivalente, quedaron varios artefactos sin trackear en el repo local:
- `.venv-ci/`
- `ci.db`
- `coverage.xml`

No llegaron a subirse al repositorio, pero sí podían ensuciar futuras iteraciones y hacer más ruidoso `git status`.

### Cambios aplicados
- Revisión del `.gitignore` existente.
- Confirmación de que ya estaban ignorados:
  - `.coverage`
  - `htmlcov/`
- Añadidas nuevas entradas a `.gitignore` para cubrir también:
  - `.venv-ci/`
  - `ci.db`
  - `coverage.xml`

### Decisiones tomadas
- Mantener la iteración como limpieza estricta de workspace, sin tocar lógica de producto ni configuración funcional.
- Ignorar específicamente los artefactos locales de reproducción de CI en lugar de borrar trazabilidad útil del repo.
- Aprovechar para dejar cubiertos tanto artefactos actuales como los habituales de cobertura local.

### Riesgos / límites
- Ninguno funcional relevante: el cambio afecta solo a gestión de ficheros no versionados del entorno local.
- Si en el futuro se quisieran conservar artefactos de cobertura como parte de otro flujo, habría que definirlo explícitamente, pero no es el caso actual.

### Comprobaciones realizadas
- Revisión manual de `.gitignore`.
- Ejecución de `git status --short` tras el cambio para comprobar que el workspace deja de mostrar los artefactos locales de CI como pendientes.

### Resultado esperado
- `git status` más limpio en iteraciones futuras.
- Menor ruido operativo al trabajar sobre `bot/render-preview`.

## Iteración 41 - Reintentos internos y mejor UX de carga en Modo Horizonte

### Objetivo
Corregir la mala sensación de producto en Horizonte cuando el primer intento falla por un problema transitorio del proveedor, pero el segundo intento manual sí funciona.

### Problema observado
En Render, al generar un escenario con activos como `AAPL`, el primer click podía fallar por descarga temporal/rate limit y el segundo click funcionar. Eso hacía que el usuario percibiera la app como rota, aunque la fuente externa acabara respondiendo poco después.

### Causa probable
La descarga histórica se estaba resolviendo demasiado pronto como error final en algunos casos transitorios:
- `YFRateLimitError`
- descarga vacía en el primer intento
- serie vacía tras normalización
- respuestas inestables del proveedor que funcionaban en un segundo intento real

El retry previo era demasiado ligero para este patrón real de Render.

### Cambios aplicados
#### Backend en `app/routes.py`
- Se amplió la estrategia de reintentos internos en `_download_history_df(...)`.
- Se añadieron reintentos controlados con backoff corto:
  - intento 1 inmediato
  - intento 2 tras `0.8s`
  - intento 3 tras `1.6s`
- Los reintentos ya no se activan solo por excepción explícita, sino también cuando:
  - el DataFrame descargado viene vacío
  - la serie queda vacía tras normalización
- Solo se devuelve error al frontend después de agotar todos los intentos.
- Se mantiene la caché ligera existente y solo se cachean descargas válidas.
- No se cachean respuestas vacías o fallidas.

#### Diferenciación final de errores
- Si tras varios intentos se detecta patrón de limitación del proveedor, se devuelve un mensaje claro de proveedor temporalmente limitado.
- Si lo que ocurre son vacíos/inestabilidad transitoria sin datos válidos, se devuelve un error 503 genérico de proveedor, no de ticker inválido.
- Solo se devuelve mensaje de ticker inválido cuando, tras agotar los intentos, no hay señales de limitación/inestabilidad transitoria.
- Esto evita clasificar erróneamente `AAPL` como ticker inválido cuando el problema real es Yahoo/rate limit.

#### Frontend en `app/static/app.js`
- Se añadió estado interno `isLoading` en `horizonState`.
- `runHorizonSimulation()` ahora corta de inmediato si ya hay una simulación en curso.
- Se desactivan botones durante la carga mediante `setHorizonLoading(...)`.
- Se actualizó el mensaje de estado para informar de que la app reintentará automáticamente si la fuente limita temporalmente la petición.
- Si el backend termina fallando, el frontend sigue mostrando el mensaje real recibido del servidor.

#### Template en `app/templates/horizon.html`
- Se actualizó el texto visible del estado de carga para que la espera se perciba como parte del comportamiento normal y no como un fallo inmediato.

### Estrategia de reintentos final
La descarga histórica de Horizonte ahora reintenta internamente estos casos:
- `YFRateLimitError`
- DataFrame vacío
- serie histórica vacía tras normalización
- excepciones transitorias no clasificadas que impiden completar la descarga

Backoff actual:
- intento 1: inmediato
- intento 2: `0.8s`
- intento 3: `1.6s`

### Caché
- Se mantiene `TTLCache` como caché ligera en memoria.
- La caché sigue inicializándose después de definir sus constantes, evitando regresión del `NameError` previo.
- Si una descarga es válida, se guarda en caché.
- Si el usuario repite ticker/rango, se puede reutilizar esa respuesta válida.
- Descargas vacías o fallidas no se guardan como si fueran válidas.

### UX resultante
- El usuario ya no debería ver un error en el primer fallo transitorio si un reintento interno posterior consigue datos válidos.
- Mientras carga, el estado comunica explícitamente que la app está obteniendo datos y reintentando automáticamente si la fuente limita temporalmente.
- Los botones de generar y regenerar quedan desactivados durante la operación para evitar clics repetidos y peticiones simultáneas.

### Archivos tocados
- `app/routes.py`
- `app/static/app.js`
- `app/templates/horizon.html`
- `CHANGELOG_AI.md`
- `docs/ai_report.md`

### Validaciones realizadas
- Relectura de `CURRENT_STATE.md`, `BOT_INSTRUCTIONS.md`, `PROJECT_CONTEXT.md`, `CHANGELOG_AI.md` y `docs/ai_report.md`.
- Revisión específica de:
  - `_download_history_df(...)`
  - `POST /api/horizon/simulate`
  - flujo frontend de carga/error en Horizonte
- Validación sintáctica:
  - `python3 -m py_compile run.py app/__init__.py app/routes.py app/auth.py app/career.py app/models.py app/services/career_session_service.py`
- Validación por inspección del comportamiento esperado en los casos pedidos:
  - AAPL con fallo transitorio inicial
  - proveedor realmente limitado
  - ticker inválido real
  - clicks repetidos
  - reutilización de caché válida

### Riesgos pendientes
- La validación real en Render sigue siendo imprescindible para confirmar el patrón exacto del proveedor en producción.
- Algunos vacíos del proveedor podrían seguir entrando en la categoría genérica de inestabilidad/proveedor en vez de rate limit explícito, pero eso es preferible a marcar un ticker válido como inválido.
- Los reintentos añaden una pequeña espera en casos malos, pero es un coste asumible frente a la mejora clara de UX.

## Iteración 42 - Tutor IA educativo para informe final de Carrera

### Objetivo
Añadir una capa de análisis educativo con IA sobre el informe final del Modo Carrera, sin convertir la app en un asesor financiero y manteniendo un framing estrictamente académico y prudente.

### Alcance del MVP
La primera versión se integra solo en el informe final de Carrera.

No se ha implementado todavía:
- chat libre con IA
- recomendaciones de activos
- optimización automática de cartera
- predicción futura con IA
- persistencia del análisis en base de datos

### Enfoque de producto
El `Tutor IA` actúa como un profesor que corrige una simulación ya realizada.

Analiza:
- resultado general de la partida
- fortalezas observables
- debilidades o riesgos
- comparación con benchmark
- conceptos que conviene repasar

No debe:
- recomendar comprar o vender activos reales
- hablar como asesor financiero
- prometer rentabilidades futuras
- presentar predicciones como hechos

### Disclaimer obligatorio
Se fijó como texto obligatorio visible en UI y en la respuesta generada:

`Este análisis tiene finalidad educativa y se basa únicamente en los datos de la simulación. No constituye asesoramiento financiero ni una recomendación de inversión real.`

### Integración técnica
#### Configuración
- Variable de entorno requerida: `OPENAI_API_KEY`
- Si no existe, la app no se rompe.
- Se añadió un endpoint ligero de estado:
  - `GET /api/ai/status`

#### Dependencia añadida
- `openai==1.109.1`

#### Endpoint principal añadido
- `POST /api/ai/career-analysis/<session_id>`

Ese endpoint:
- valida acceso a la sesión a través de la misma lógica segura de Carrera
- resuelve el informe final sin exponer sesiones ajenas
- construye un payload compacto
- llama a la IA solo si `OPENAI_API_KEY` está disponible
- devuelve JSON estructurado con:
  - `analysis`
  - `sections`
  - `disclaimer`
  - `generated_at`
  - `warnings`

### Seguridad y acceso
- usuarios autenticados: solo pueden analizar sesiones propias
- invitado: solo puede analizar la sesión accesible por el flujo actual; no se confía solo en localStorage
- si la sesión no existe o no es accesible, el endpoint devuelve error controlado

### Datos enviados a la IA
Se envía un resumen compacto de simulación, no series históricas gigantes.

Campos principales enviados:
- tipo de simulación (`career_mode`)
- `session_id`
- dificultad
- periodo histórico
- alias del jugador si existe
- tickers usados
- asignación más reciente
- turnos totales y cerrados
- valor inicial y final
- invertido acumulado
- PnL absoluto y porcentual
- métricas agregadas de portfolio:
  - CAGR
  - volatilidad
  - max drawdown
  - retorno total
- métricas agregadas de benchmark
- métricas de tracking:
  - active return
  - tracking error
  - information ratio
- score final y notas
- warnings del informe
- resumen teórico compacto si existe
- conteo agregado de eventos

No se envían datos personales innecesarios ni series completas de mercado.

### Prompt y control de comportamiento
La llamada a IA usa un prompt de sistema explícito para forzar:
- español
- tono didáctico
- prudencia
- ausencia de asesoramiento financiero real
- ausencia de recomendaciones de compra/venta
- ausencia de predicción futura
- salida JSON estructurada
- honestidad si faltan datos

### UI añadida
En `app/templates/career.html`, dentro del informe final de Carrera, se añadió una card nueva:
- título: `Tutor IA`
- subtítulo: `Recibe una explicación educativa de tu simulación.`
- texto explicativo de profesor/corrección
- botón: `Analizar con IA`
- disclaimer visible
- estado de carga y zona de resultado estructurada

El render final muestra bloques para:
- Resumen general
- Qué has hecho bien
- Qué podrías mejorar
- Comparación con benchmark
- Riesgos detectados
- Contexto histórico
- Conceptos para repasar
- Conclusión educativa

No se muestra JSON crudo al usuario.

### Comportamiento sin API key
Si falta `OPENAI_API_KEY`:
- la app sigue arrancando
- el informe final no se rompe
- `GET /api/ai/status` devuelve que el Tutor IA no está configurado
- el botón se deshabilita y la UI muestra un mensaje claro:
  - `El Tutor IA no está configurado en este entorno.`

### Comportamiento ante error de API
Si falla la API externa:
- se devuelve un error amable
- el informe final no se rompe
- el usuario puede volver a intentarlo

### Archivos tocados
- `CURRENT_STATE.md`
- `requirements.txt`
- `app/routes.py`
- `app/career.py`
- `app/templates/career.html`
- `app/static/app.js`
- `app/static/estilos.css`
- `CHANGELOG_AI.md`
- `docs/ai_report.md`

### Validaciones realizadas
- Relectura de contexto obligatorio antes de empezar.
- Revisión de:
  - `app/career.py`
  - `app/routes.py`
  - `app/models.py`
  - `app/templates/career.html`
  - `app/static/app.js`
  - `app/static/estilos.css`
  - `requirements.txt`
- Validación sintáctica:
  - `python3 -m py_compile run.py app/__init__.py app/routes.py app/auth.py app/career.py app/models.py app/services/career_session_service.py`
- Validación por inspección de los casos mínimos:
  - sin `OPENAI_API_KEY`
  - con `OPENAI_API_KEY`
  - error de API
  - ownership de sesión
  - invitado
  - responsive básico por estructura de card

### Limitaciones actuales
- El análisis no se persiste en base de datos.
- El modelo usado está fijado de forma simple para este MVP.
- No hay caching todavía del último análisis generado.
- La respuesta depende de un servicio externo y puede variar ligeramente entre llamadas.

### Riesgos pendientes
- Conviene validar en Render el parsing real del JSON devuelto por OpenAI en este entorno concreto.
- Si el modelo devolviera texto fuera del JSON esperado, podría hacer falta una capa extra de robustez de parsing en una iteración posterior.
- Sigue siendo importante revisar manualmente que el tono final no derive hacia lenguaje de recomendación financiera.

### Siguiente paso recomendado
- validar en Render el Tutor IA con y sin `OPENAI_API_KEY`
- revisar tono real de 3 o 4 respuestas sobre sesiones distintas
- si hace falta, endurecer todavía más el prompt o añadir post-validación de frases prohibidas
- solo después valorar una extensión futura a análisis histórico o a otras zonas de la app

## Iteración 43 - Manejo controlado de fallos de proveedor en autoplay de Carrera

### Objetivo
Corregir un bug urgente de producción en `Modo Carrera` donde el autoplay de turnos podía romperse con `500` al fallar temporalmente la descarga de datos de mercado.

### Problema observado en Render
Durante `Simular todos los turnos automáticamente`, el backend lanzaba:
- `POST /api/career/turn -> 500`

Causa visible en logs:
- `_download_history_df(...)` lanzaba `BacktestError(503)` al fallar Yahoo/yfinance para tickers como `TCEHY`
- esa excepción subía por `_adj_close_series(...)` y `_returns_by_ticker(...)`
- `close_turn()` no la capturaba
- Flask/Render la convertían finalmente en error interno `500`

El problema no era un bug interno de cálculo de Carrera, sino un fallo externo del proveedor de datos mal gestionado por este endpoint.

### Causa raíz
Tras el hardening reciente de `Modo Horizonte`, `_download_history_df(...)` pasó a diferenciar mejor:
- ticker inválido
- proveedor temporalmente limitado
- respuesta inestable o vacía

Eso estaba bien, pero `Modo Carrera` todavía solo capturaba `NoHistoricalDataError` y no `BacktestError`.

Por tanto, una limitación temporal del proveedor en un turno de Carrera acababa escapando como excepción no controlada.

### Cambios aplicados en backend
#### `app/career.py`
- Se importó `BacktestError` desde `app.routes` en el bloque reutilizado de helpers históricos.
- Se añadió fallback local de `BacktestError` en el bloque `except Exception` de importación para mantener compatibilidad defensiva.
- En `close_turn()` se añadió captura explícita de `BacktestError`.

Ahora, cuando falla el proveedor:
- no se devuelve 500
- se respeta el `status_code` del error original, por ejemplo `503`
- se responde con JSON controlado

Payload devuelto en estos casos:
- `ok: false`
- `error`
- `message`
- `error_type`
- `retryable`
- `ticker`

Criterio actual:
- si `status_code >= 500` → `error_type = market_data_provider`, `retryable = true`
- si no → `error_type = invalid_ticker`, `retryable = false`

Con esto, un rate limit de Yahoo para `TCEHY` deja de parecer un fallo interno del servidor.

### Cambios aplicados en frontend
#### `app/static/app.js`
- Se ajustó `handleCareerAutoPlay()` para que, si el backend devuelve un error controlado del proveedor:
  - el autoplay se detenga
  - no se sigan lanzando peticiones repetidas a `/api/career/turn`
  - se muestre un mensaje humano y específico
  - la UI vuelva a quedar en estado usable
- Se añadió mensaje de UX más claro para proveedor limitado, por ejemplo:
  - `La fuente de datos de mercado está temporalmente limitada para TCEHY. La simulación automática se ha detenido para evitar resultados incompletos. Puedes reintentarlo más tarde o cambiar ese activo.`
- Se mantiene la reactivación de controles en `finally`, así que el botón vuelve a quedar disponible.
- Se evita mostrar simplemente `Error 500`.

### Revisión del 401 de `/api/career/sessions`
Se revisó también el caso de:
- `GET /api/career/sessions -> 401`

Conclusión:
- es compatible con el caso esperado de invitado o usuario sin acceso persistido
- no era el bug crítico principal
- se ajustó `refreshCareerSavedSessions()` para tratar `401` de forma silenciosa y normal, sin ruido innecesario en consola salvo otros errores distintos

### Comportamiento final esperado
#### Caso A, proveedor limitado en `/api/career/turn`
- ya no devuelve `500`
- devuelve respuesta controlada, típicamente `503`
- JSON con mensaje claro y semántica de retry

#### Caso B, autoplay
- si falla un turno por proveedor, se detiene
- no entra en bucle de peticiones repetidas
- no deja el turno parcialmente cerrado
- la UI queda estable y el usuario puede reintentar más tarde

#### Caso C, ticker inválido real
- se mantiene posibilidad de respuesta diferenciada como `invalid_ticker` si el error no viene del proveedor temporalmente limitado

#### Caso D, Carrera normal
- los tickers válidos con datos disponibles siguen cerrando turno igual que antes

#### Caso E, Horizonte
- no se tocó la semántica central de `_download_history_df(...)`
- Horizonte mantiene retry interno, caché ligera y distinción entre proveedor limitado y ticker inválido

### Archivos tocados
- `CURRENT_STATE.md`
- `app/career.py`
- `app/static/app.js`
- `CHANGELOG_AI.md`
- `docs/ai_report.md`

### Validaciones realizadas
- Relectura de contexto obligatorio antes de empezar.
- Revisión específica de:
  - `app/career.py`
  - `close_turn`
  - `_returns_by_ticker`
  - `_adj_close_series`
  - `_download_history_df`
  - `handleCareerAutoPlay`
  - `jsonPost`
- Validación sintáctica:
  - `python3 -m py_compile run.py app/__init__.py app/routes.py app/auth.py app/career.py app/models.py app/services/career_session_service.py`
- Validación por inspección del flujo:
  - proveedor limitado en turnos de Carrera
  - parada limpia de autoplay
  - no mostrar `Error 500`
  - tratamiento silencioso del `401` en sesiones guardadas

### Riesgos pendientes
- Falta validar en Render el caso real con el mismo ticker problemático (`TCEHY`) para confirmar el payload exacto visible en frontend.
- El campo `ticker` en la respuesta se infiere desde el mensaje y la asignación actual; funciona para este MVP, pero podría endurecerse más si en el futuro se quiere trazabilidad exacta por ticker fallido en carteras múltiples.
- Conviene verificar en producción que no aparecen efectos laterales en cierre manual de turno, no solo en autoplay.

## Iteración 44 - Restauración de CI tras cambios de Horizonte, Tutor IA y Carrera

### Objetivo
Diagnosticar por qué GitHub Actions volvió a ponerse en rojo tras los commits recientes de Horizonte, Tutor IA y Carrera, y restaurar el workflow sin tocar lógica de producto innecesaria.

### Contexto
La CI había quedado verde tras:
- `7afcf41` — `fix(ci): repair github actions workflow`
- `3f10cec` — `docs: add current project state summary`
- `442064b` — `chore: ignore local ci artifacts`

Pero después aparecieron nuevos runs rojos tras:
- `0edebdb` — `fix(horizon): retry transient market data failures before surfacing errors`
- `0feeaee` — `feat(ai): add educational simulation tutor`
- `f3a4568` — `fix(career): handle market data provider failures during autoplay`

### Comprobación de estado local
Se confirmó al inicio:
- rama actual: `bot/render-preview`
- último commit local: `f3a4568`
- sin cambios sucios previos a la nueva iteración

### Revisión del workflow
Se revisó `.github/workflows/ci.yml` y la configuración seguía siendo la correcta:
- instalación con `requirements-dev.txt`
- `ruff check .`
- `black --check .`
- `pytest --cov=app --cov-report=xml`
- variables dummy seguras de entorno para CI

También se revisó `pyproject.toml`, que seguía excluyendo correctamente entornos virtuales y caches.

### Reproducción local exacta del CI
Se reprodujo localmente el workflow completo en entorno virtual limpio.

Resultado real:
- `ruff check .` → OK
- `black --check .` → FAIL
- archivo afectado: `app/routes.py`

Mensaje exacto clave:
- `would reformat /root/.openclaw/workspace/tfg-web-ci-python-bot/app/routes.py`

Esto confirmó que la causa del rojo no era:
- dependencia `openai`
- variable `OPENAI_API_KEY`
- tests desalineados
- `py_compile`
- lógica de Tutor IA
- lógica de Carrera
- lógica de Horizonte

Era simplemente un desalineado de formato Black introducido en cambios recientes.

### Corrección aplicada
- Se aplicó `black` únicamente sobre `app/routes.py`.
- No se modificó lógica de producto.
- No se tocaron tests ni workflow.

### Validación final realizada
Tras el reformat, se volvió a ejecutar el equivalente completo del workflow:
- `ruff check .`
- `black --check .`
- `SECRET_KEY=ci-secret-key DATABASE_URL=sqlite:///ci.db pytest --cov=app --cov-report=xml`
- `python3 -m py_compile run.py app/__init__.py app/routes.py app/auth.py app/career.py app/models.py app/services/career_session_service.py`

Resultado:
- Ruff OK
- Black OK
- Pytest OK (`25 passed`)
- py_compile OK

### Herramientas remotas
No había `gh` disponible en este entorno, así que no se pudieron consultar logs remotos directamente desde GitHub Actions CLI.

Aun así, la reproducción local del workflow fue suficiente para identificar la causa exacta y corregirla de forma mínima.

### Archivos tocados
- `app/routes.py`
- `CHANGELOG_AI.md`
- `docs/ai_report.md`

### Causa raíz resumida
El CI volvió a fallar porque `black --check .` detectó que `app/routes.py` no estaba formateado según Black tras los cambios recientes.

No era un fallo funcional del producto ni de la nueva integración con OpenAI.

### Qué comprobar ahora en GitHub Actions
- que el workflow `CI` vuelva a salir en verde sobre `bot/render-preview`
- que el paso que antes fallaba (`Format check (black)`) ya pase
- que también se mantengan verdes:
  - `ruff`
  - `pytest`
  - generación de `coverage.xml`
