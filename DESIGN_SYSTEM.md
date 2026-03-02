# Sistema de Diseño - JIC Frontend

## Tabla de contenidos
- [Paleta de colores](#paleta-de-colores)
- [Componentes visuales](#componentes-visuales)
- [Patrones de interacción](#patrones-de-interacción)

---

## Paleta de colores

### Color principal
**Nombre:** Primary (Violeta/Cobalt)  
**Hex:** `#3a2f9d`  
**Uso:** Botones primarios, bordes activos, iconos destacados, estados hover en componentes interactivos.  
**Variantes:**
- `bg-primary/5` → opacity 5% (fondos muy suaves)
- `bg-primary/30` → opacity 30% (bordes y overlays)
- `bg-primary/90` → opacity 90% (estados hover)

### Color secundario
**Nombre:** Secondary (Teal muted)  
**Hex:** `#b2d9d5` (aproximado)  
**Uso:** Fondos de thumbnails de video, estados hover en áreas neutras.

### Color acento (Amber/Amarillo)
**Nombre:** Amber  
**Hex:** `#fbbf24` (amber-400)  
**Uso:** Badges, iconos de alerta/información, elementos destacados en páginas específicas (la-jic, resultados).  
**Variantes:**
- `bg-amber-300/20` → Fondos de iconos informativos
- `text-amber-700` → Texto en badges

### Escala neutral (Stone)
**Colores:**
- `stone-50` → Fondos muy claros, secciones alternadas
- `stone-100` → Botones neutros, estados por defecto
- `stone-200` → Hover en botones neutros
- `stone-300` → Bordes neutros
- `stone-400` → Hover en bordes

**Uso:** Secciones de contenido, botones secundarios, divisores.

### Colores semánticos
| Nombre | Hex aproximado | Uso |
|--------|----------------|-----|
| **Foreground** | #0f1419 | Texto principal |
| **Background** | #f7f8f9 | Fondo de página |
| **Card** | #ffffff | Fondos de tarjetas |
| **Border** | #d0d1d6 | Bordes generales |
| **Muted foreground** | #717177 | Texto secundario |

---

## Componentes visuales

### 1. Tab bar (Barra de pestañas)
**Ubicación:** `src/lib/components/recursos/tabs.svelte`  
**Descripción:** Barra horizontal con pestañas para cambiar entre secciones (Documentos, Boletines, Memorias, Galería, Videos).

**Estilos:**
- **Estado inactivo:** 
  - Texto: `text-muted-foreground`
  - Borde inferior: `border-transparent`
- **Estado activo:**
  - Texto: `text-primary` (#3a2f9d)
  - Borde inferior: `border-primary` (#3a2f9d)
- **Hover:**
  - Texto: `hover:text-foreground`

**Código de ejemplo:**
```svelte
<button
  class="border-b-2 px-4 py-3 font-medium {activeTab === 'docs'
    ? 'border-primary text-primary'
    : 'border-transparent text-muted-foreground hover:text-foreground'}"
>
  Documentos
</button>
```

---

### 2. Card (Tarjeta genérica)
**Ubicación:** Múltiples componentes (boletines, memorias, videos, resultados)  
**Descripción:** Contenedor rectangular con borde, fondo blanco y sombra al pasar.

**Estilos:**
- Fondo: `bg-card` (blanco)
- Borde: `border-border` (#d0d1d6)
- Esquinas redondeadas: `rounded-xl`
- Transición: `transition-all`
- **Hover:**
  - Borde: `hover:border-primary/30` (violeta al 30%)
  - Sombra: `hover:shadow-md`

**Variantes:**
- **Card con acento teal:** Memorias
  - Hover: `hover:border-teal/30`
  - Icono: `text-teal`

**Código de ejemplo:**
```svelte
<div class="group rounded-xl border border-border bg-card p-5 transition-all hover:border-primary/30 hover:shadow-md">
  <!-- contenido -->
</div>
```

---

### 3. Botón primario
**Ubicación:** Encabezado, llamadas a acción, formularios  
**Descripción:** Botón sólido con color principal, usado para acciones principales.

**Estilos:**
- Fondo: `bg-primary` (#3a2f9d)
- Texto: `text-primary-foreground` (blanco)
- Esquinas: `rounded-lg`
- **Hover:**
  - Fondo: `hover:bg-primary/90` (violeta más oscuro)

**Código de ejemplo:**
```svelte
<button class="bg-primary px-3 py-1.5 text-primary-foreground rounded-lg hover:bg-primary/90 transition-colors">
  Reproducir
</button>
```

---

### 4. Botón secundario / neutro
**Ubicación:** Controles de categorías, filtros, opciones alternativas  
**Descripción:** Botón con fondo neutro y borde, menos prominente que el primario.

**Estilos:**
- Fondo: `bg-neutral-primary` o `bg-stone-100`
- Borde: `border-border` o `border-stone-300`
- Texto: `text-heading` o `text-foreground`
- **Hover:**
  - Borde: `hover:border-stone-400`
  - Fondo: `hover:bg-stone-100` o `hover:bg-primary/5`

**Código de ejemplo:**
```svelte
<button class="border border-stone-300 bg-neutral-primary px-3 py-2 rounded-lg hover:border-stone-400 hover:bg-stone-100 transition-colors">
  Categoría
</button>
```

---

### 5. Badge / Píldora
**Ubicación:** Etiquetas de año (historial), duración de videos, información  
**Descripción:** Etiqueta pequeña y redondeada para marcar información.

**Variantes:**

**Badge informativo (teal):**
- Fondo: `bg-teal/10` (teal al 10%)
- Texto: `text-teal`
- Forma: `rounded-full`

**Badge de duración (video):**
- Fondo: `bg-black/70` (negro al 70%)
- Texto: `text-white`
- Posición: `absolute` (esquina inferior derecha)

**Badge de categoría (amber):**
- Fondo: `bg-amber-300/20` (amber al 20%)
- Texto: `text-amber-700`

**Código de ejemplo:**
```svelte
<!-- Informativo -->
<span class="rounded-full bg-teal/10 px-3 py-1 text-teal font-semibold text-xs">
  JIC 2024
</span>

<!-- Duración -->
<span class="rounded bg-black/70 px-1.5 py-0.5 text-white text-xs font-medium">
  5:32
</span>

<!-- Categoría -->
<span class="rounded-full bg-amber-300/20 px-2.5 py-0.5 text-amber-700 text-xs font-semibold">
  Destacado
</span>
```

---

### 6. Modal / Lightbox
**Ubicación:** Ampliación de imágenes, reproductor de vídeos  
**Descripción:** Ventana emergente con overlay oscuro, contenido central y botón de cierre.

**Estilos:**
- **Overlay:**
  - Fondo: `bg-black/60` (imagen) o `bg-black/70` (video)
  - Blur: `backdrop-blur-sm`
  - Posición: `fixed inset-0 z-50`
- **Contenedor:**
  - Fondo: `bg-card` o `bg-white`
  - Esquinas: `rounded-xl` o `rounded-2xl`
  - Sombra: `shadow-2xl`
- **Botón cerrar:**
  - Fondo: `bg-white` / `bg-transparent`
  - Esquinas: `rounded-full` / `rounded-lg`
  - **Hover:** `hover:bg-stone-100` o `hover:bg-secondary`

**Código de ejemplo:**
```svelte
{#if selectedImage}
  <div class="fixed inset-0 z-50 bg-black/60 backdrop-blur-sm flex items-center justify-center">
    <div class="relative bg-white rounded-2xl shadow-2xl max-w-3xl">
      <img src={selectedImage} alt="Ampliado" class="w-full h-auto rounded-xl" />
      <button class="absolute -top-3 -right-3 bg-white text-black rounded-full w-8 h-8 hover:bg-stone-100">
        ×
      </button>
    </div>
  </div>
{/if}
```

---

### 7. Video card
**Ubicación:** `src/lib/components/recursos/tabs.svelte` (pestaña Videos)  
**Descripción:** Tarjeta con miniatura de vídeo, botón "play" superpuesto y controles de acción.

**Estilos:**
- **Contenedor:**
  - Fondo: `bg-card`
  - Borde: `border-border`
  - Esquinas: `rounded-xl`
  - Overflow: `overflow-hidden`
- **Thumbnail:**
  - Relación aspecto: `aspect-video`
  - Fondo: `bg-secondary`
- **Overlay play (hover):**
  - Fondo: `bg-foreground/30` (fondo oscuro 30%)
  - Opacidad: `opacity-0` → `group-hover:opacity-100`
  - Botón: `rounded-full bg-white/90`
  - Icono: `text-primary`

**Código de ejemplo:**
```svelte
<div class="group overflow-hidden rounded-xl border border-border bg-card">
  <button class="relative w-full aspect-video bg-secondary">
    <img src={v.thumbnail} alt={v.title} class="w-full h-full object-cover" />
    <div class="absolute inset-0 bg-foreground/30 opacity-0 group-hover:opacity-100 flex items-center justify-center">
      <div class="h-14 w-14 rounded-full bg-white/90 flex items-center justify-center">
        <svg class="text-primary"><!-- icono play --></svg>
      </div>
    </div>
  </button>
  <div class="p-4">
    <h3 class="font-semibold text-foreground group-hover:text-primary">{v.title}</h3>
    <p class="text-muted-foreground text-sm">{v.description}</p>
  </div>
</div>
```

---

### 8. Navbar / Header
**Ubicación:** `src/lib/components/header.svelte`  
**Descripción:** Barra de navegación fija en la parte superior con fondo translúcido.

**Estilos:**
- Fondo: `bg-neutral-card/95` (translúcido)
- Backdrop: `backdrop-blur-sm`
- Borde inferior: `border-b border-default`
- Posición: `fixed w-full z-20 top-0`
- **Botón principal:**
  - Fondo: `bg-primary`
  - Texto: `text-primary-foreground`
  - **Hover:** `hover:bg-primary/90`
- **Links de navegación:**
  - Activo: `bg-primary/10 text-primary`
  - Inactivo: `text-muted-foreground`
  - **Hover:** `hover:bg-secondary/70 hover:text-foreground`

---

### 9. Footer
**Ubicación:** `src/lib/components/footer.svelte`  
**Descripción:** Pie de página con enlaces, redes sociales e información.

**Estilos:**
- Fondo: `bg-foreground` (#0f1419)
- Texto: `text-background` (texto claro sobre oscuro)
- **Iconos:**
  - Fondo: `bg-primary` (#3a2f9d)
  - Texto: `text-primary-foreground`
- **Enlaces:**
  - Opacidad: `opacity-70` → `hover:opacity-100`

---

### 10. Pagination (Paginación)
**Ubicación:** Componente reutilizable `src/lib/components/pagination.svelte`  
**Descripción:** Controles numerados para navegar entre páginas.

**Estilos:**
- Fondo: Configurable via prop `color` (ejemplo: `bg-stone-50`)
- Botones activos: `bg-primary`, `text-primary-foreground`
- Botones inactivos: `bg-card`, `border-border`
- **Hover:**
  - Borde: `hover:border-primary/30`
  - Fondo: `hover:bg-primary/5`

**Código de página:**
```svelte
<Pagination color="bg-stone-50" />
```

---

### 11. Galería de imágenes
**Ubicación:** `src/lib/components/recursos/tabs.svelte`  
**Descripción:** Grid de miniaturas con efecto zoom al pasar.

**Estilos:**
- Grid: `grid-cols-2 md:grid-cols-3 gap-4`
- Imagen: `hover:scale-110 transition-transform duration-500`
- Botón contenedor: `bg-transparent rounded-base border-0`

---

### 12. Formulario de contacto
**Ubicación:** `src/lib/components/contacto/contact.svelte`  
**Descripción:** Tarjetas con información de contacto.

**Estilos:**
- **Contenedor:** `bg-stone-50`, `bg-card`, `rounded-xl`, `p-8`
- **Icono:**
  - Fondo: `bg-primary/10` (violeta) o `bg-teal/10` (teal)
  - Esquinas: `rounded-lg`
  - Tamaño: `h-12 w-12`
- **Botón enviar:**
  - Fondo: `bg-primary`
  - Texto: `text-primary-foreground`
  - **Hover:** `hover:bg-primary/90`

---

### 13. Grid de resultados / filtros
**Ubicación:** `src/lib/components/resultados/results.svelte`  
**Descripción:** Botones de filtro o filas de resultado en tabla.

**Estilos:**
- Botones:
  - Fondo: `bg-stone-100`
  - Borde: `border-border`
  - **Hover:**
    - Fondo: `hover:bg-stone-200`
    - Borde: `hover:border-primary/30`
    - Transición hover secundaria: `hover:bg-primary/5`

---

## Patrones de interacción

### Estados comunes

#### Hover (Pasar el mouse)
- **Primario:** Borde cambia a `border-primary/30`, fondo a `bg-primary/5`, sombra aumenta
- **Secundario:** Borde a `border-stone-400`, fondo a `bg-stone-100` o `bg-stone-200`
- **Texto:** Color a `text-foreground` o `text-primary`

#### Active (Seleccionado)
- Borde: `border-primary` (color completo)
- Texto: `text-primary` (color completo)
- Fondo: `bg-primary/10` (fondo muy suave)

#### Disabled (Deshabilitado)
- Opacidad reducida
- Sin transiciones

#### Focus (Foco para accesibilidad)
- Ring: `focus:ring-4 focus:ring-primary`
- Outline: `focus:outline-none`

---

## Variantes de opacidad

Las opacidades se usan para crear jerarquía visual y estados:

| Opacidad | Uso |
|----------|-----|
| `/5` | Fondos muy suaves en hover |
| `/10` | Fondos de iconos, badges informativos |
| `/20` | Fondos de elementos secundarios |
| `/30` | Bordes en estados hover, overlays |
| `/60` | Overlays oscuros (lightbox de imagen) |
| `/70` | Overlays muy oscuros (vídeo), badges |
| `/90` | Estados hover primarios |

---

## Notas de implementación

1. **Reutilización:** La mayoría de componentes visuales usan la misma paleta. Solo cambia `--primary` para alterar toda la interfaz.

2. **Componentes configurables:**
   - `Hero`: Acepta props `color` y `text_color`
   - `Pagination`: Acepta prop `color`
   - `Resource-card`: Acepta prop `accent`

3. **Transiciones:** Todas las transiciones usan `transition-colors` (color) o `transition-all` (múltiples propiedades) con duración por defecto.

4. **Accesibilidad:**
   - Todos los botones tienen `cursor-pointer` y estados de hover claros
   - Los modales usan `role="dialog"` y `aria-modal="true"`
   - Los elementos interactivos tienen `group` para efectos colectivos

5. **Responsive:** Las propiedades cambian entre `sm:`, `md:`, `lg:` breakpoints (Tailwind por defecto).

---

## Ejemplo de uso en componente nuevo

```svelte
<script>
  let isHovered = false;
</script>

<!-- Card estándar -->
<div 
  class="rounded-xl border border-border bg-card p-5 transition-all hover:border-primary/30 hover:shadow-md"
  on:mouseenter={() => isHovered = true}
  on:mouseleave={() => isHovered = false}
>
  <!-- Contenido -->
  <h3 class="font-semibold text-foreground">{title}</h3>
  <p class="mt-2 text-muted-foreground">{description}</p>
  
  <!-- Botón -->
  <button class="mt-4 bg-primary text-primary-foreground px-4 py-2 rounded-lg hover:bg-primary/90 transition-colors">
    Acción
  </button>
</div>
```

---

**Versión:** 1.0  
**Actualizado:** 27 de febrero de 2026
