# Frontend Redesign Brief - Guía ampliada y accionable

## 1. Propósito de este documento

Este documento transforma la investigación visual inicial en una guía práctica para rediseñar la interfaz completa de la aplicación.

No es un resumen conceptual, sino un documento de trabajo para tomar decisiones consistentes al rediseñar pantallas, componentes y layouts sin romper la base funcional ya estabilizada.

### Objetivo principal
Construir una interfaz más:
- moderna
- profesional
- defendible académicamente
- usable
- coherente
- reconocible como producto cuidado

### Objetivo secundario
Evitar que la app parezca:
- una plantilla SaaS genérica
- una landing de IA ensamblada con patrones previsibles
- una interfaz demasiado blanda, demasiado brillante o demasiado homogénea

---

## 2. Diagnóstico claro del diseño actual

## 2.1 Qué se percibe como genérico

### Home
- estructura de bloques visualmente correcta, pero todavía cercana a patrones de landing repetibles
- demasiada dependencia de secciones limpias pero poco distintivas
- posible sensación de “producto bonito pero no del todo memorable”

### Formularios y auth
- login y registro son funcionales y más pulidos que antes, pero aún pueden sentirse como formularios estándar con personalización limitada
- falta una personalidad más clara en la presentación de la experiencia de acceso

### Dashboards y áreas de trabajo
- la app resuelve bastante información mediante cards similares entre sí
- hay módulos correctos, pero no siempre queda clara la prioridad entre bloque principal, bloque de soporte y bloque secundario

## 2.2 Qué parece hecho por IA

### Patrones frecuentes que conviene reducir
- cards clonadas con radios y sombras muy parecidas
- pills y badges usados como recurso visual por defecto
- secciones excesivamente simétricas
- bloques con “buen gusto genérico” pero poca intención diferenciada
- ritmo visual demasiado uniforme
- repetición del mismo patrón de título + texto + caja en muchas superficies

### Señales concretas de estética IA a vigilar
- gradientes suaves añadidos sin motivo fuerte
- exceso de superficies elevadas visualmente
- hero o secciones centrales con texto demasiado neutro o demasiado centrado
- distribución donde todo parece igual de importante
- uso de adornos visuales previsibles en vez de jerarquía real

## 2.3 Pantallas con demasiado texto o con texto mejorable

### Home
- puede beneficiarse de textos más cortos, más tensos y con mejor ritmo
- conviene reducir copy tipo explicación general si no empuja a una acción clara

### Aprender
- riesgo de densidad excesiva si todos los bloques compiten por atención
- necesita estructura más editorial y menos acumulativa

### Readiness quiz
- las instrucciones y resultados deben ser más claros y compactos
- no conviene que el usuario sienta exceso de lectura antes de actuar

### Informe final y Tutor IA
- el contenido puede crecer mucho y requerir una estructura visual que corte mejor la lectura
- hay que evitar muros de texto o secciones demasiado parecidas entre sí

## 2.4 Partes con demasiadas cards

### Modo Práctica
- resultados, métricas y detalle pueden sentirse como una suma de bloques equivalentes

### Modo Carrera
- es una zona especialmente sensible: sesiones, decisiones, eventos, informe, ranking y continuidad generan una interfaz compleja
- necesita menos sensación de “apilar widgets” y más sensación de recorrido guiado

### Horizonte
- el modo experimental puede terminar pareciendo otra colección de tarjetas si no se jerarquiza mejor

### Historial
- riesgo de repetir cards sin una estructura más fuerte de lista, tabla o resumen jerárquico

## 2.5 Problemas de jerarquía visual

### Problemas principales
- demasiados bloques con peso parecido
- CTAs importantes que no siempre dominan visualmente el contexto
- encabezados que a veces introducen, pero no ordenan de verdad
- exceso de módulos hermanos donde debería haber niveles
- gráficos, texto y métricas sin una narrativa visual lo bastante marcada en algunas zonas

### Resultado percibido
La app funciona, pero en varias pantallas aún parece más una suma de secciones correctas que una experiencia con dirección visual firme.

---

## 3. Dirección visual final

La dirección final recomendada es una **fintech educativa moderna**.

### Debe sentirse
- académica, pero no aburrida
- profesional, pero no bancaria
- humana, pero no infantil
- sobria, pero visualmente atractiva
- contemporánea, pero no de moda vacía

### Personalidad deseada
- segura
- clara
- útil
- creíble
- limpia
- con criterio editorial

### Lo que NO debe ser
- una web excesivamente corporativa o fría
- una demo startup llena de gradientes y brillos
- una interfaz recargada de microdecoración
- una estética “AI product” obvia

### Principio central
El diseño debe transmitir que la herramienta sirve para aprender, analizar y simular con seriedad, sin parecer un panel financiero agresivo ni una landing genérica de software.

---

## 4. Paleta concreta

## 4.1 Colores principales

### Verde profundo, color de marca
- `#176B52`
- uso: botones primarios, highlights positivos, elementos clave de marca

### Grafito
- `#1F2937`
- uso: títulos, texto principal, contraste estructural

## 4.2 Colores secundarios

### Azul petróleo
- `#1F4E5F`
- uso: bloques informativos, navegación secundaria, estados técnicos, algunos acentos

### Gris azulado
- `#5B6B7A`
- uso: texto secundario, etiquetas, soporte visual sobrio

## 4.3 Fondos

### Fondo general cálido
- `#F6F4EF`

### Fondo alternativo muy claro
- `#FBFAF7`

### Fondo de secciones técnicas o destacadas
- `#EEF3F2`

## 4.4 Superficies

### Superficie principal
- `#FFFFFF`

### Superficie secundaria
- `#F8FAFB`

### Superficie elevada discreta
- `#FCFCFB`

## 4.5 Textos

### Texto principal
- `#17212B`

### Texto secundario
- `#556270`

### Texto suave / ayuda
- `#73808C`

### Texto inverso
- `#FFFFFF`

## 4.6 Estados

### Success
- fondo: `#E8F6EF`
- texto/borde: `#176B52`

### Warning
- fondo: `#FFF5E6`
- texto/borde: `#A15C00`

### Error
- fondo: `#FDECEC`
- texto/borde: `#B42318`

### Info
- fondo: `#EAF3F8`
- texto/borde: `#1F4E5F`

## 4.7 Reglas de uso
- usar el verde como color de decisión, no como pintura masiva
- usar neutros para sostener la interfaz
- reservar los acentos para puntos de intención real
- evitar varios colores compitiendo en una misma vista sin motivo claro

---

## 5. Tipografía

## 5.1 Stack recomendado

```css
font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
```

Si no se introduce `Inter`, el sistema puede funcionar bien con una jerarquía afinada basada en tipografía del sistema.

## 5.2 Escala tipográfica recomendada

### H1
- tamaño: `clamp(2rem, 3vw, 3.25rem)`
- peso: `700`
- line-height: `1.08`

### H2
- tamaño: `clamp(1.5rem, 2.2vw, 2.25rem)`
- peso: `700`
- line-height: `1.12`

### H3
- tamaño: `1.25rem` a `1.5rem`
- peso: `650` o `700`
- line-height: `1.2`

### Body
- tamaño base: `1rem`
- peso: `400` o `450`
- line-height: `1.6`

### Small
- tamaño: `0.875rem`
- peso: `400` o `500`
- line-height: `1.5`

### Labels / UI compacta
- tamaño: `0.875rem`
- peso: `600`
- line-height: `1.3`

## 5.3 Reglas tipográficas
- evitar grandes masas de texto centrado
- usar centrado solo en hero, vacíos muy concretos o mensajes controlados
- alinear a izquierda la mayoría del contenido funcional
- no usar subtítulos largos si no añaden claridad
- reducir adjetivación vacía y mantener copy útil
- dar más fuerza a números, métricas y estados clave

---

## 6. Sistema de layout

## 6.1 Ancho máximo
- contenedor principal recomendado: `1200px` a `1280px`
- contenidos especialmente densos: hasta `1320px` si hace falta
- formularios o bloques de lectura: anchos más contenidos

## 6.2 Grid
- grid principal de 12 columnas en escritorio
- layouts de 2 y 3 columnas cuando exista jerarquía real
- evitar tres columnas por simple simetría si la lectura sufre

## 6.3 Spacing
- sistema base recomendado en múltiplos de `4px`
- escala práctica:
  - `4`
  - `8`
  - `12`
  - `16`
  - `24`
  - `32`
  - `40`
  - `48`
  - `64`

## 6.4 Estructura de páginas
- header claro
- introducción breve cuando haga falta
- bloque principal dominante
- información secundaria agrupada
- acciones bien localizadas
- estados y feedback integrados cerca del punto de acción

## 6.5 Densidad visual
- landing y acceso: más aire
- dashboards y pantallas de trabajo: más densidad controlada
- informes: lectura guiada y menos repetición estructural

## 6.6 Responsive
- móvil no debe ser solo apilar todo
- revisar orden de lectura, jerarquía y CTAs
- evitar tarjetas kilométricas en pantallas pequeñas
- simplificar grids complejos a grupos más legibles

---

## 7. Componentes base

## 7.1 Botones

### Tipos recomendados
- primario
- secundario
- ghost
- destructivo
- terciario de enlace visual

### Reglas
- el primario no debe convivir con demasiados primarios iguales en una misma vista
- radios moderados, no excesivamente blandos
- hover y focus claros
- disabled realmente legible

## 7.2 Cards
- menos cards por defecto
- diferenciar cards de resumen, cards operativas y cards de soporte
- usar borde, fondo y espaciado antes que sombra excesiva
- evitar que todas tengan misma presencia

## 7.3 Inputs
- foco muy visible
- labels siempre claros
- helper text legible
- error junto al campo, no perdido en la página

## 7.4 Selects
- alineados con inputs
- estados hover/focus claros
- no parecer controles del navegador incrustados sin estilo

## 7.5 Badges
- solo para clasificación o estado real
- tamaño contenido
- evitar el badge como decoración permanente

## 7.6 Modales
- título muy claro
- contenido con buena respiración
- CTA principal inequívoco
- cierre secundario bien visible

## 7.7 Toasts
- compactos
- informativos
- no teatrales
- color y texto suficientes para comprender la acción

## 7.8 Tablas
- más protagonismo cuando la información sea comparativa
- filas limpias
- cabeceras claras
- mejor que una colección de cards si la estructura es realmente tabular

## 7.9 Gráficos
- integrados con el sistema cromático
- leyendas limpias
- fondos discretos
- texto auxiliar sobrio
- evitar saturar la gráfica con adornos UI externos

## 7.10 Estados vacíos
- mensaje breve
- acción sugerida cuando proceda
- menos plantilla, más contexto real

## 7.11 Estados de error
- mensajes concretos
- tono claro
- siguiente paso accionable
- visualmente visibles sin dramatismo

## 7.12 Estados loading
- discretos pero evidentes
- evitar loaders gigantes o ambiguos
- explicar qué se está haciendo cuando el proceso no sea instantáneo

---

## 8. Rediseño por pantalla

## 8.1 Home

### Qué debe cambiar
- hero con más intención y menos estructura genérica de landing
- jerarquía más fuerte entre propuesta principal y bloques secundarios
- menos simetría automática
- menos bloques equivalentes
- CTA principal más claro

### Qué debe transmitir
- producto serio
- herramienta académica y práctica
- acceso rápido a modos principales

## 8.2 Login / Registro

### Qué debe cambiar
- composición más cuidada
- mejor equilibrio entre branding, confianza y simplicidad
- menos sensación de formulario estándar aislado
- mejor jerarquía en títulos, ayuda y acciones

### Qué debe transmitir
- acceso sencillo
- producto estable
- experiencia limpia y madura

## 8.3 Aprender

### Qué debe cambiar
- estructura más editorial
- mejor agrupación temática
- menos sensación de lista uniforme de bloques
- mejor respiración entre contenidos

### Qué debe transmitir
- aprendizaje guiado
- claridad conceptual
- apoyo real al usuario

## 8.4 Readiness quiz

### Qué debe cambiar
- introducción más breve
- preguntas mejor presentadas
- foco en responder, no en leer demasiado
- feedback más claro y más ordenado

### Qué debe transmitir
- paso serio, pero accesible
- filtro pedagógico, no castigo

## 8.5 Modo Práctica

### Qué debe cambiar
- mejor separación entre configuración, resultados y detalle
- métricas más jerarquizadas
- menos cards equivalentes
- gráficas integradas con más limpieza

### Qué debe transmitir
- análisis útil y controlado
- claridad al comparar resultados

## 8.6 Modo Carrera

### Qué debe cambiar
- narrativa visual por flujo
- mejor distinción entre estado de sesión, decisiones, resultados y continuidad
- paneles menos clonados
- acciones principales más claras

### Qué debe transmitir
- progresión
- estrategia
- contexto histórico jugable

## 8.7 Informe final

### Qué debe cambiar
- transformar el informe en una lectura guiada, no en una acumulación de módulos
- destacar KPIs clave
- organizar mejor comparaciones, score, warnings y continuidad

### Qué debe transmitir
- cierre sólido
- análisis serio
- lectura clara y presentable

## 8.8 Tutor IA

### Qué debe cambiar
- mejor integración con el informe final
- salida más editorial y menos bloque técnico suelto
- estados de generación más claros
- disclaimer visible pero bien integrado

### Qué debe transmitir
- apoyo educativo prudente
- claridad y confianza

## 8.9 Modo Horizonte

### Qué debe cambiar
- separar mejor lo experimental de lo histórico
- integrar disclaimers con madurez visual
- mejorar el flujo entre entrada, contexto, resultados y advertencias

### Qué debe transmitir
- experimento controlado
- continuidad con Carrera
- prudencia metodológica

## 8.10 Historial

### Qué debe cambiar
- menos repetición de módulos equivalentes
- uso más claro de listas, agrupaciones o tablas según convenga
- filtros y acciones mejor organizados

### Qué debe transmitir
- memoria útil
- acceso rápido
- lectura eficiente

---

## 9. Reglas para evitar estética IA

### Menos
- gradientes por defecto
- pills innecesarias
- cards clonadas
- simetría artificial
- copy genérico
- blandura visual universal

### Más
- jerarquía
- intención
- contraste
- ritmo visual
- densidad útil
- asimetría controlada
- decisiones claras sobre qué domina y qué acompaña

### Test rápido de validación visual
Si una pantalla pudiera pertenecer indistintamente a:
- un SaaS cualquiera
- una startup IA cualquiera
- una plantilla genérica bonita

entonces todavía le falta identidad.

---

## 10. Plan de implementación por fases

## Fase 1 — Sistema visual base
- variables CSS
- tokens de color
- tipografía
- espaciado
- botones
- cards
- formularios
- layout base

## Fase 2 — Home / Login / Navegación
- home
- navbar
- hero
- auth
- accesos principales

## Fase 3 — Aprender / Quiz
- página aprender
- readiness quiz
- modal de resultado
- gate visual hacia Carrera

## Fase 4 — Modo Práctica
- formulario
- resultados
- detalle
- estados vacíos y de error

## Fase 5 — Modo Carrera
- dashboard
- controles
- sesiones guardadas
- ranking
- informe parcial si aplica

## Fase 6 — Horizonte
- entrada
- disclaimers
- resultados
- continuidad con Carrera

## Fase 7 — Tutor IA e informes
- informe final
- tutor IA
- secciones narrativas
- warnings y continuidad

## Fase 8 — Responsive y pulido final
- móvil
- tablet
- contraste
- foco
- spacing fino
- consistencia transversal

---

## 11. Reglas técnicas

- no tocar backend salvo necesidad real
- no tocar endpoints
- no cambiar IDs usados por JS
- no romper auth
- no romper invitado
- no romper Carrera
- no romper Horizonte
- no romper Tutor IA
- no borrar disclaimers obligatorios
- validar visualmente y funcionalmente al final de cada fase
- mantener commits pequeños y reversibles

### Restricción importante
El rediseño debe construirse sobre la app existente. No debe convertirse en una reescritura desordenada de templates, scripts o flujos.

---

## 12. Siguiente uso recomendado

Antes de empezar a rediseñar:
1. leer este brief completo
2. usar `docs/frontend_redesign_research.md` como apoyo conceptual
3. ejecutar primero la Fase 1
4. tocar solo la capa visual necesaria en cada iteración
5. validar que cada pantalla sigue funcionando antes de continuar
