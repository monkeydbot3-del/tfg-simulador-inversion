# Investigación y dirección visual para el rediseño frontend

## 1. Objetivo del rediseño

El rediseño frontend debe perseguir cuatro metas principales:

- modernizar la aplicación
- hacerla más profesional y coherente
- reforzar su calidad percibida y su defensa académica como TFG
- evitar una estética genérica o reconocible como producto "hecho por IA"

La meta no es solo “hacerla más bonita”, sino construir una interfaz con más criterio visual, más intención de producto y una identidad más propia.

---

## 2. Diagnóstico visual actual

### Qué se ve demasiado genérico
- Uso abundante de cards similares entre sí, con jerarquías a veces demasiado planas.
- Secciones que comparten una misma estructura visual aunque su importancia funcional sea distinta.
- Presencia de patrones visuales cómodos pero previsibles, comunes en demos modernas generadas rápidamente.
- Algunos bloques tienen buena limpieza, pero no suficiente carácter propio.

### Qué patrones parecen de IA
- Repetición de pills, badges y bloques redondeados como solución por defecto.
- Demasiadas superficies visuales con comportamiento parecido.
- Tendencia a layouts muy centrados o demasiado simétricos en zonas donde convendría más tensión visual.
- Uso potencialmente excesivo de degradados suaves o brillos si se siguen extendiendo sin control.
- Lenguaje visual correcto, pero a veces demasiado “templateable”.

### Problemas de jerarquía visual
- Algunas pantallas presentan demasiados elementos con peso visual parecido.
- Hay cards importantes que no destacan suficiente frente a información secundaria.
- En flujos complejos, como Carrera u Horizonte, el usuario puede percibir demasiados bloques hermanos sin una narrativa visual clara.
- Navegación, métricas, gráficos y acciones no siempre quedan organizados en un orden de lectura óptimo.

### Partes que necesitan más identidad
- Home y navegación global.
- Dashboard principal y pantallas de análisis.
- Formularios de login/registro y acciones principales.
- Informe final de Carrera.
- Superficies experimentales como Horizonte y Tutor IA, que deben verse integradas pero con personalidad propia.

---

## 3. Dirección visual propuesta

La dirección recomendada es una **fintech educativa** con tono:

- moderno
- limpio
- profesional
- humano
- sobrio, pero no frío

Debe sentirse como una herramienta seria de simulación y aprendizaje, no como:
- una web corporativa rígida
- una demo startup artificial
- una app infantilizada
- un “template IA” genérico

### Rasgos deseables
- interfaz clara y calmada
- mayor sensación de criterio editorial
- uso selectivo del color, no decorativo
- contraste más maduro
- mejores ritmos de espacio, alineación y densidad
- visuales que transmitan confianza, no espectáculo

---

## 4. Paleta de color recomendada

Se puede mantener el verde como base porque ya conecta bien con el dominio de inversión, crecimiento y simulación financiera, pero conviene hacerlo más sobrio y menos brillante.

### Núcleo recomendado
- **Grafito** para texto principal, títulos y estructura
- **Blanco cálido** para fondos y superficies limpias
- **Verde profundo** como color de marca y acciones principales
- **Azul petróleo** o **gris azulado** para capas secundarias, métricas, navegación o estados técnicos

### Uso recomendado
- verde para CTAs principales, resultados positivos y puntos de énfasis
- grafito para dar solidez tipográfica y evitar apariencia blanda
- tonos fríos secundarios para equilibrio y credibilidad
- neutros cálidos para reducir sensación clínica o excesivamente digital

### Evitar
- exceso de degradados genéricos
- verdes demasiado saturados por defecto
- azules demasiado “SaaS template”
- abuso de colores vivos en zonas secundarias

---

## 5. Tipografía

### Sistema tipográfico recomendado
Usar una jerarquía limpia y robusta, preferiblemente basada en:
- tipografía del sistema bien afinada, o
- una sans moderna, sobria y muy legible

La prioridad no es “originalidad tipográfica”, sino:
- claridad
- consistencia
- densidad cómoda
- buen contraste entre títulos, subtítulos y texto base

### Criterios
- títulos más sólidos y menos blandos
- tamaños mejor escalonados
- interlineado más estable
- texto de interfaz muy legible
- labels, métricas y ayudas con sistema claro

### Recomendaciones visuales
- títulos con más peso y menos decoración
- subtítulos más cortos y útiles
- cuerpos de texto ligeramente más compactos donde la interfaz lo permita
- números y KPIs con tratamiento más fuerte y más limpio

---

## 6. Layout

### Mejoras buscadas
- mejor uso del espacio horizontal
- menos repetición de cards apiladas sin intención
- dashboards más compactos y jerárquicos
- formularios más cuidados y menos “bloque por bloque”
- navegación más clara y madura

### Principios
- distinguir mejor entre contenido principal, soporte y acciones
- reducir ruido estructural
- agrupar información relacionada con más intención
- usar columnas, anchos máximos y ritmos de separación más consistentes
- reservar layouts más aireados para landing, y más densos para áreas de trabajo

### Aplicación práctica
- Home con storytelling más claro y menos bloques equivalentes
- Análisis y dashboards con estructura de lectura más profesional
- Carrera y Horizonte con narrativa visual por secciones, no solo por acumulación de módulos
- mejor integración entre textos, métricas y gráficos

---

## 7. Componentes base

### Botones
- más diferenciación entre primario, secundario y ghost
- menos dependencia de estilos genéricos “pill”
- estados hover/focus/disabled más claros

### Cards
- menos inflación de cards
- bordes, radios y sombras más contenidos
- variantes según importancia: datos clave, soporte, alertas, experimental

### Inputs
- más claridad en foco y error
- labels mejor integrados
- ayudas e instrucciones menos grises y más legibles

### Badges
- usar solo cuando aporten clasificación real
- reducir badges puramente decorativos

### Tablas
- más densidad útil
- mejor lectura de filas y columnas
- jerarquía visual para cabeceras y vacíos

### Gráficos
- mejor integración con el resto del sistema visual
- fondos y leyendas más sobrios
- evitar saturación decorativa

### Modales
- jerarquía más clara entre título, contenido y acción
- overlays sobrios
- acciones mejor ordenadas

### Toasts
- menos apariencia genérica
- estados claros y discretos

### Estados vacíos
- menos plantilla universal
- mensajes concretos, útiles y con intención

### Estados de error
- más claridad, menos dramatismo
- instrucciones accionables

### Estados de carga
- menos ambigüedad visual
- cargas breves, honestas y bien integradas

---

## 8. Accesibilidad

El rediseño no debe sacrificar accesibilidad por estética.

### Requisitos mínimos
- contraste suficiente en textos y controles
- foco visible real
- botones claramente distinguibles
- tamaños cómodos en móvil y escritorio
- labels claros
- no depender solo del color para comunicar estado

### Especial atención
- mensajes de error
- métricas positivas/negativas
- botones deshabilitados
- formularios y modales
- gráficas con apoyo textual cuando haga falta

---

## 9. Cómo evitar estética IA

### Evitar
- simetría artificial constante
- exceso de pills innecesarias
- texto centrado como solución por defecto
- degradados suaves en cualquier bloque importante
- iconografía decorativa sin función
- repetición de la misma card para todo
- jerarquías visuales demasiado homogéneas

### Buscar en su lugar
- más ritmo visual
- más contraste de densidad entre zonas
- más decisión en qué destacar y qué dejar en segundo plano
- más personalidad en títulos, estructura y tono
- más intención por pantalla
- composiciones menos previsibles

La app debe parecer diseñada con criterio, no ensamblada a partir de patrones cómodos.

---

## 10. Plan de implementación por fases

### Fase 1 — Sistema visual base
- variables CSS
- paleta
- tipografía
- botones
- cards
- formularios
- layout base

### Fase 2 — Home, login, registro y navegación
- home
- navbar
- hero
- bloques de acceso
- login
- registro

### Fase 3 — Modo Práctica
- formulario principal
- resultados
- detalle
- historial relacionado

### Fase 4 — Modo Carrera
- dashboard de sesión
- controles
- informe final
- ranking y sesiones guardadas

### Fase 5 — Aprender y readiness quiz
- página Aprender
- quiz
- modal de resultados
- gate de acceso a Carrera

### Fase 6 — Modo Horizonte
- entrada independiente
- disclaimers
- formulario
- resultados experimentales
- continuidad visual con Carrera

### Fase 7 — Tutor IA e informes
- tarjeta Tutor IA
- estados de generación
- salida del análisis
- integración con informe final

### Fase 8 — Responsive, accesibilidad y pulido final
- revisión móvil
- revisión tablet
- contraste
- focos
- espacios
- estados edge
- consistencia transversal

---

## 11. Reglas de implementación

- no tocar lógica de backend salvo necesidad real
- no romper endpoints
- no romper auth
- no romper invitado
- no romper Modo Carrera
- no romper Horizonte
- no romper Tutor IA
- validar cada fase antes de pasar a la siguiente
- hacer commits pequeños, claros y reversibles

### Regla de disciplina
El rediseño debe hacerse como una secuencia de capas visuales controladas, no como una reescritura caótica de toda la app de una vez.

---

## 12. Criterio final

Si una pantalla queda “más moderna” pero también más genérica, no es una mejora suficiente.

El objetivo correcto es:
- más calidad visual
- más identidad
- más legibilidad
- más madurez de producto
- más coherencia entre pantallas
- sin romper la funcionalidad ya estabilizada
