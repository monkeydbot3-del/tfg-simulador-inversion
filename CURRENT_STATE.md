# CURRENT_STATE.md

## Propósito
Resumen operativo corto del estado actual del proyecto.

Úsalo como primer archivo de orientación al empezar cada nueva iteración.
No sustituye a:
- `BOT_INSTRUCTIONS.md`
- `PROJECT_CONTEXT.md`
- `CHANGELOG_AI.md`
- `docs/ai_report.md`

Después de leer este archivo, relee siempre esos cuatro documentos antes de tocar código.

---

## 1. Estado actual estable de la app
- App web Flask de simulación de inversiones, ya bastante evolucionada a nivel visual, UX y estructura funcional.
- Hay soporte de autenticación mínima por email con persistencia en Postgres para usuarios autenticados.
- Existe acceso invitado funcional, con restricciones claras sobre historial persistido.
- El flujo de análisis principal está operativo, con resultados, detalle enriquecido e historial por usuario.
- El `Modo Carrera` está operativo, con persistencia progresiva y generación de informe final estabilizada.
- El `readiness quiz` actúa como gate real previo al `Modo Carrera`.
- El `Modo Horizonte` existe como función experimental y educativa, accesible de forma independiente y también desde Carrera.
- El `Tutor IA` MVP existe sobre el informe final de Carrera como capa educativa opcional, dependiente de `OPENAI_API_KEY`.
- La CI de GitHub Actions ha sido reparada y validada localmente.

---

## 2. Últimos commits importantes
- `7afcf41` — `fix(ci): repair github actions workflow`
- `c7fb125` — `docs: record iteration 37 commit hash`
- `d0fbc5d` — `fix(horizon): align projections with historical series and clarify provider errors`
- `d219096` — `fix(horizon): improve historical basis for future scenarios`
- `0c9f581` — `fix(horizon): surface API error messages in frontend`
- `bbd606d` — `fix(horizon): polish chart labels and add light retry`
- `a825abf` — `fix(horizon): harden simulation flow and improve horizon layout`
- `62e89ae` — `feat(horizon): add experimental future scenario mode`

---

## 3. Funcionalidades ya cerradas
- Rediseño visual base de home, navegación, dashboards y pantallas principales.
- Limpieza de textos visibles y corrección de mojibake en UI.
- Login y registro rediseñados visualmente.
- Auth mínima con email, hash de contraseña y sesión Flask.
- Persistencia Postgres con Peewee para usuarios.
- Acceso invitado funcional.
- Historial de análisis por usuario autenticado.
- Gráficas en resultados de análisis y detalle de historial.
- Modo Carrera persistente por fases, con sesiones, turnos y snapshots en Postgres.
- Informe final de Carrera corregido y estabilizado en producción.
- Readiness quiz integrado como requisito real para Carrera.
- Modal visual de resultados del quiz.
- Modo Horizonte MVP implementado.
- Hardening importante de Horizonte frente a rate limit, series temporales y continuidad visual.
- CI reparada para que valide el proyecto real y no entornos virtuales dentro del repo.

---

## 4. Funcionalidades en desarrollo
- Validación real en Render de `Modo Horizonte` tras las últimas iteraciones.
- Corrección de la integración real entre `Modo Carrera` y `Modo Horizonte` para que la continuación experimental precargue la cartera y el contexto final de la partida.
- Validación real en Render del `Tutor IA` con y sin `OPENAI_API_KEY`.
- Corrección del renderizado frontend del Tutor IA para que la respuesta 200 del backend se muestre de forma estable y segura en la UI.
- Cache busting simple para `app.js` y `estilos.css`, evitando que navegadores sirvan assets obsoletos tras nuevos deploys.
- Hardening del backend del Tutor IA para que sesiones incompletas o respuestas no estructuradas del proveedor no escalen a error 500/HTML sin JSON controlado.
- Acotación temporal del Tutor IA con timeout explícito, modelo configurable y respuesta compacta para evitar esperas de ~30s rematadas en 500 por timeout externo.
- Apertura de rama específica de rediseño frontend `feature/frontend-redesign-v2` y creación de una guía de investigación visual previa al rediseño real, sin tocar todavía código de producto.
- Ampliación del trabajo documental del rediseño con `docs/frontend_redesign_brief.md`, ya orientado a ejecución práctica por fases, sistema visual y rediseño por pantalla.
- Inicio de la Fase 1 del rediseño frontend con una nueva base visual global en `app/static/estilos.css`: tokens de color, tipografía, spacing, botones, cards, formularios, badges, modales, toasts y layout base, sin tocar lógica de producto.
- Fase 2 del rediseño ya aplicada sobre navegación global, home, login y registro con una composición más editorial y profesional, manteniendo intacta la lógica funcional.
- Microiteración correctiva de Fase 2 tras revisión real en Render: nueva paleta más actual, navbar más compacta, login/registro mucho más limpios y jerarquía de botones igualada en home.
- Fase 2.2 aplicada tras nueva revisión en Render: home realineada sobre un eje común y nueva identidad cálida-profesional con base crema, grafito y acento navy/terracota.
- Microiteración posterior sobre Fase 2.2 para corregir la aplicación de la paleta: se eliminan CTAs multicolor/gradientes decorativos y se consolida una distribución semántica de color por fondo, superficie, texto, borde, primario, acento y estados.
- Ajuste adicional de la base cálida para eliminar restos verdosos en fondos, inputs y superficies suaves, manteniendo el navy como primario y el terracota solo como acento.
- Microiteración final de Fase 2 para compactar la navbar en desktop, evitar el salto de línea de “Horizonte” y neutralizar superficies suaves auxiliares como el bloque “Antes de empezar”.
- Nueva microiteración de coherencia visual para eliminar el gradiente verdoso residual real del fondo global y extender el lenguaje de panel cálido superior a cards inferiores de home y secciones principales de práctica.
- Apertura de Fase 3 del rediseño frontend: rediseño visual de `Aprender` y del `readiness quiz`, manteniendo intacta la lógica de desbloqueo de Carrera, persistencia y flujo funcional.
- Microiteración posterior de Fase 3 para reducir el exceso de cards en `Aprender`, convertir el progreso lateral del readiness en una timeline no clicable y dar un tratamiento más editorial a hero y bloques de apoyo.
- Microcorrección final sobre Fase 3.1 para dar aire superior a las imágenes de `Aprender` y eliminar microcopy redundante del hero y del bloque “Del concepto a la simulación”, sin tocar la lógica del readiness.
- Microiteración final de Fase 3 para equilibrar verticalmente las imágenes de `Aprender`, eliminar el fondo resaltado del estado activo de la timeline y aprovechar mejor la altura de la columna `Tu progreso`.
- Microcorrección final adicional para distribuir verticalmente los tres pasos de la timeline `Tu progreso` a lo largo de toda la columna, manteniendo el readiness intacto a nivel funcional.
- Apertura de Fase 4 del rediseño frontend para rediseñar visualmente `Modo Práctica / Nuevo análisis`, manteniendo intacta la lógica del formulario, DCA/Sin DCA y generación de análisis.
- Validación real en Render del `readiness quiz` completo en flujo autenticado e invitado.
- Posible microiteración metodológica de prudencia en Horizonte si las trayectorias siguen pareciendo demasiado optimistas.
- Mejora de velocidad de arranque cognitivo del bot mediante documentación operativa como este archivo.

---

## 5. Bugs abiertos o pendientes
- Pendiente validación manual en Render de Horizonte con casos reales:
  - `AAPL`, `5 años`, `10000`
  - ticker inválido real
  - flujo desde `Modo Carrera`
  - responsive móvil
- Pendiente comprobar en producción que, cuando Yahoo limita peticiones, el mensaje mostrado es el de proveedor limitado y no el de ticker inválido.
- Pendiente confirmar visualmente en Render que la transición azul/verde del gráfico de Horizonte se entiende bien en móvil.
- Pendiente comprobar en GitHub Actions que el workflow remoto aparece en verde tras el commit `7afcf41`.
- Bug urgente detectado en Render: `POST /api/career/turn` podía acabar en 500 durante autoplay cuando Yahoo/yfinance devolvía limitación temporal del proveedor para un ticker de la cartera.
- La corrección de ese flujo está en curso y debe validar que Carrera trate los errores de proveedor como respuesta controlada, no como error interno 500.

---

## 6. Reglas críticas que no se pueden romper
- Trabajar solo en este repo de presentación: `/root/.openclaw/workspace/tfg-web-ci-python-bot` (remote esperado: `simulador-inversion-tfg`).
- Usar el repo original solo como referencia.
- No tocar nunca `main` ni ramas principales.
- Rama fija actual de trabajo: `bot/render-preview`.
- Hacer commit y push al final de cada iteración útil.
- Antes de cada iteración, leer:
  - `CURRENT_STATE.md`
  - `BOT_INSTRUCTIONS.md`
  - `PROJECT_CONTEXT.md`
  - `CHANGELOG_AI.md`
  - `docs/ai_report.md`
- No rehacer la app desde cero.
- No hacer refactor estructural grande sin motivo fuerte.
- No tocar lógica del simulador salvo bug real o ajuste mínimo necesario.
- No romper auth, invitado, historial, readiness, Carrera ni Horizonte al tocar otra cosa.
- No introducir complejidad innecesaria ni features extravagantes.
- Mantener cambios defendibles académicamente.
- Documentar siempre la iteración en `CHANGELOG_AI.md` y `docs/ai_report.md`.

---

## 7. Arquitectura relevante actual
- Backend: Flask.
- Templates: Jinja2.
- Frontend: JavaScript + CSS propio.
- Datos de mercado: `yfinance`.
- Procesado: `pandas`.
- Persistencia: Render Postgres con `DATABASE_URL`.
- ORM ligero: Peewee.
- Auth: sesión Flask + hash de contraseña Werkzeug.
- Driver: `psycopg2-binary`.
- Modelos clave actuales:
  - `User`
  - `AnalysisHistory`
  - `CareerSessionLink`
  - `CareerSession`
  - `CareerTurn`
  - `ReadinessQuizResult`
- Rutas/áreas especialmente sensibles:
  - `app/routes.py`
  - `app/career.py`
  - `app/services/career_session_service.py`
  - `app/auth.py`
- Horizonte:
  - usa disclaimers obligatorios
  - usa histórico amplio con downsampling
  - distingue ticker inválido, proveedor limitado y datos insuficientes
  - usa caché ligera `TTLCache` en memoria
- Tutor IA:
  - analiza solo simulaciones de Carrera
  - envía payload compacto, no series completas gigantes
  - requiere `OPENAI_API_KEY`
  - debe mantener siempre disclaimer educativo y no asesorar sobre inversión real
- CI:
  - workflow principal en `.github/workflows/ci.yml`
  - valida `ruff`, `black`, `pytest` y compilación equivalente local
  - usa variables dummy seguras en CI para arrancar la app

---

## 8. Siguiente paso recomendado
Prioridad recomendada inmediata:
1. revalidar en Render la home, navbar, login y registro tras corregir la aplicación de la paleta y limpiar definitivamente el sistema de botones
2. mantener el rediseño separado por fases, sin tocar backend salvo necesidad real
3. validar cada fase visual antes de seguir con la siguiente
4. conservar como punto de retorno el tag `v1.0-functional` y la rama `stable/pre-redesign`

Recomendación práctica:
- no abrir ahora una feature grande nueva
- cerrar primero validaciones externas pendientes
- si aparece un fallo real en Render, hacer fix mínimo, documentarlo y volver a validar

---

## Uso recomendado en futuras iteraciones
1. Leer `CURRENT_STATE.md` para ubicarse en 1 minuto.
2. Releer los 4 documentos obligatorios para contexto profundo.
3. Confirmar rama, estado git y últimos commits.
4. Elegir una iteración pequeña con impacto real.
5. Validar localmente lo necesario.
6. Documentar, commit y push.
