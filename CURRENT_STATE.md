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
- Validación real en Render del `Tutor IA` con y sin `OPENAI_API_KEY`.
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
- Trabajar solo en este repo: `/root/.openclaw/workspace/tfg-web-ci-python-bot`.
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
1. validar en Render el estado actual de `Modo Horizonte`
2. validar el `readiness quiz` completo en entorno real
3. confirmar que GitHub Actions queda verde tras `7afcf41`
4. si Render confirma todo estable, volver a microiteraciones pequeñas de pulido visual y metodológico

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
