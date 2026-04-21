# CHANGELOG_AI

## 2026-04-21
- Se clona el repositorio de trabajo `monkeydbot3-del/tfg-web-ci-python-bot` en el workspace.
- Se configura el remoto de referencia `sanlaja/tfg-web-ci-python` como `reference`.
- Se crea la rama de trabajo `bot/diagnostico-inicial`.
- Se realiza análisis inicial del proyecto sin aplicar cambios funcionales ni visuales.
- Hallazgo clave: el estado actual del repo del bot coincide con `reference/main` en el árbol versionado consultado.
- Hallazgo clave: faltan los archivos de contexto persistente indicados por el usuario (`BOT_INSTRUCTIONS.md`, `PROJECT_CONTEXT.md`) y también faltaban en el repo `CHANGELOG_AI.md` y `docs/ai_report.md`, que se crean en esta iteración.
- Se releen los archivos de contexto persistente ya presentes en el repo antes de continuar.
- Se crea la rama `bot/iteracion-01-textos-y-home` para una mejora incremental segura.
- Se mejora la landing principal con una estructura más clara, más orientada a decisiones y visualmente más consistente.
- Se mejora el bloque de inicio del modo práctica con mejor jerarquía visual, copy más claro y acciones agrupadas.
- Se ajustan textos globales de navegación y título base para reforzar consistencia de producto.
- Se corrigen textos visibles en modo carrera y en el precheck del análisis.
- Se sustituye un estilo inline por clases/atributos más consistentes en `analisis.html`.
- Se consolidan y limpian estilos CSS duplicados de la landing y se mejora el responsive básico de esa zona.
- No se han aplicado cambios en la lógica de negocio del simulador en esta iteración.
