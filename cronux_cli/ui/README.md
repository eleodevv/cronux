# Cronux UI v2 - Nueva Interfaz Moderna

UI/UX completamente rediseñada con diseño moderno tipo Glassmorphism y gradientes.

## 🎨 Características de Diseño

### Estilo Visual
- **Glassmorphism**: Tarjetas con efecto de vidrio
- **Gradientes vibrantes**: Botones y elementos con gradientes coloridos
- **Animaciones fluidas**: Transiciones suaves entre estados
- **Neumorphism**: Efectos de profundidad sutiles

### Paleta de Colores
- **Gradiente Principal**: Púrpura (#667EEA → #764BA2)
- **Gradiente Secundario**: Rosa (#F093FB → #F5576C)
- **Gradiente Éxito**: Azul (#4FACFE → #00F2FE)
- **Gradiente Peligro**: Naranja-Rosa (#FA709A → #FEE140)

## 📁 Estructura

```
ui/
├── cronux_ui_v2.py          # Aplicación principal
├── theme/
│   └── colors.py            # Sistema de colores y temas
├── screens/
│   ├── home_screen.py       # Pantalla de inicio
│   ├── wizard_screen.py     # Wizard de crear proyecto
│   └── project_screen.py    # Vista de proyecto (TODO)
├── components/
│   ├── gradient_button.py   # Botón con gradiente
│   ├── glass_card.py        # Tarjetas glassmorphism
│   └── project_type_card.py # Tarjeta de tipo de proyecto
└── utils/
    └── (utilidades futuras)
```

## 🚀 Ejecutar

```bash
# Activar entorno virtual
source cronux_venv/bin/activate

# Ejecutar UI v2
python cronux_cli/ui/cronux_ui_v2.py
```

## 🎯 Pantallas Implementadas

### 1. Home Screen (✅ Completa)
- Header con logo y gradiente
- Botón de cambio de tema
- Estado vacío con ilustración
- Botón "Nuevo Proyecto" con gradiente

### 2. Wizard Screen (✅ Completa)
- **Paso 1**: Selección de tipo de proyecto
  - 8 tipos: Node.js, Python, Java, PHP, Ruby, .NET, Go, General
  - Tarjetas animadas con gradientes
  - Iconos SVG dinámicos
  
- **Paso 2**: Detalles del proyecto
  - Campo de nombre
  - Selector de carpeta (zenity)
  
- **Paso 3**: Confirmación
  - Resumen de datos
  - Botón "Crear Proyecto"

### 3. Project Screen (⏳ Pendiente)
- Vista de versiones
- Timeline de cambios
- Acciones (guardar, restaurar)

## 🎨 Componentes Reutilizables

### GradientButton
Botón moderno con gradiente y sombra.

```python
GradientButton(
    text="Mi Botón",
    icon=ft.Icons.ADD,
    gradient_colors=["#667EEA", "#764BA2"],
    on_click=handler,
)
```

### GlassCard
Tarjeta con efecto glassmorphism.

```python
GlassCard(
    content=mi_contenido,
    padding=20,
    blur=10,
)
```

### ProjectTypeCard
Tarjeta animada para tipos de proyecto.

```python
ProjectTypeCard(
    nombre="Node.js",
    icono_path="assets/icons/nodeblanco.svg",
    descripcion="React, Vue, Next.js",
    is_selected=True,
    gradient_colors=["#68D391", "#38B2AC"],
)
```

## 🌓 Temas

### Modo Claro
- Fondo: Blanco (#FFFFFF)
- Secundario: Gris claro (#F5F7FA)
- Texto: Negro (#1A202C)

### Modo Oscuro
- Fondo: Azul oscuro (#0F1419)
- Secundario: Gris oscuro (#1A1F2E)
- Texto: Blanco (#F7FAFC)

## 📝 TODO

- [ ] Implementar pantalla de proyecto
- [ ] Conectar con lógica de crear_proyecto.py
- [ ] Implementar lista de proyectos en home
- [ ] Agregar pantalla de versiones
- [ ] Implementar timeline de cambios
- [ ] Agregar animaciones de carga
- [ ] Implementar búsqueda y filtros

## 🎯 Diferencias con v0.1.1

| Característica | v0.1.1 | v2 |
|----------------|--------|-----|
| Diseño | Minimalista | Glassmorphism + Gradientes |
| Colores | Rojo principal | Gradientes múltiples |
| Estructura | 1 archivo | Múltiples pantallas |
| Botones | Sólidos | Con gradientes |
| Tarjetas | Bordes simples | Efecto vidrio |
| Animaciones | Básicas | Fluidas y complejas |

## 💡 Inspiración

- Diseño inspirado en apps modernas como Notion, Linear, y Stripe
- Uso de gradientes vibrantes tipo iOS/macOS
- Glassmorphism popularizado por Windows 11 y macOS Big Sur
