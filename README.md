# CRONUX-CRX

Sistema de Control de Versiones Local Simple y Poderoso

## Descripción

Cronux-CRX (Cronux Control de Revisiones eXtendido) es un sistema de control de versiones local diseñado para ser simple, rápido y efectivo. Funciona completamente offline, sin necesidad de repositorios remotos o configuraciones complejas.

## Características

- **100% Offline**: Funciona completamente sin conexión a internet
- **Interfaz Gráfica y CLI**: Dos formas de trabajar según tu preferencia
- **Simple y Rápido**: Sin configuraciones complejas
- **Multiplataforma**: Disponible para Windows, macOS y Linux
- **Historial Visual**: Visualiza la evolución de tus proyectos
- **Restauración Fácil**: Vuelve a cualquier versión anterior con un clic

## Instalación

### Windows
1. Descarga `CRONUX-CLI-INSTALLER.exe` o `CRONUX-CRX.exe` (GUI)
2. Ejecuta el instalador
3. Sigue las instrucciones en pantalla

### macOS
1. Descarga `Cronux-CRX-Installer.pkg` (CLI) o `CRONUX-CRX.dmg` (GUI)
2. Abre el archivo descargado
3. Sigue las instrucciones de instalación

### Linux
1. Descarga el archivo `.deb` correspondiente
2. Instala con: `sudo dpkg -i cronux-crx-*.deb`
3. Para CLI: El comando `crx` estará disponible globalmente
4. Para GUI: Busca "Cronux-CRX" en tu menú de aplicaciones

## Uso Básico

### CLI (Línea de Comandos)

```bash
# Crear un nuevo proyecto
crx new mi-proyecto

# Guardar una versión
crx save -m "descripción de cambios"

# Ver historial
crx log

# Restaurar una versión
crx restore 1.0

# Ver información del proyecto
crx info

# Eliminar proyecto
crx delete nombre-proyecto
```

### GUI (Interfaz Gráfica)

1. Abre la aplicación Cronux-CRX
2. Crea un nuevo proyecto o abre uno existente
3. Usa los botones para guardar versiones, ver historial y restaurar

## Estructura del Proyecto

```
CRONUX-CRX/
├── cronux_cli/              # Código fuente de la aplicación
│   ├── cli/                 # Módulos CLI
│   │   ├── cronux_cli.py   # Punto de entrada CLI
│   │   ├── crear_proyecto.py
│   │   ├── guardar_version.py
│   │   ├── restaurar_versiones.py
│   │   ├── ver_historial.py
│   │   ├── info_proyecto.py
│   │   └── eliminar_proyecto.py
│   ├── cronux_gui_v3.py    # Interfaz gráfica
│   ├── build_separated.py   # Script de construcción
│   ├── assets/              # Recursos (iconos, imágenes)
│   ├── uninstall.sh         # Desinstalador Linux/macOS
│   └── uninstall.bat        # Desinstalador Windows
├── cronuxEstatico/          # Sitio web estático
└── README.md
```

## Desarrollo

### Requisitos
- Python 3.8+
- tkinter (incluido en Python)
- Flet
- PyInstaller (para crear ejecutables)

### Construir desde el código fuente

```bash
# Clonar el repositorio
git clone https://github.com/eleowebcoding/CRONUX-CRX.git
cd CRONUX-CRX/cronux_cli

# Instalar dependencias
pip install pyinstaller

# Construir ejecutables
python build_separated.py
```

## Desinstalación

### Windows
```cmd
C:\Program Files\Cronux\uninstall.bat
```

### Linux/macOS
```bash
sudo /usr/local/cronux/uninstall.sh
```

## Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## Sitio Web
https://cronux.netlify.app/


