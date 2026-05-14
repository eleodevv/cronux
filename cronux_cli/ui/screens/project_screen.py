"""
Pantalla de Proyecto - Vista de versiones con diseño tipo árbol
"""
import flet as ft
import threading
from pathlib import Path
import sys

# Agregar el directorio cli al path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "cli"))
sys.path.insert(0, str(Path(__file__).parent.parent))

from cli_integration import guardar_version_ui, restaurar_version_ui


class ProjectScreen:
    """Pantalla de proyecto con historial de versiones"""
    
    def __init__(self, page: ft.Page, proyecto, on_back, on_refresh=None):
        self.page = page
        self.proyecto = proyecto
        self.on_back = on_back
        self.on_refresh = on_refresh
    
    def build(self):
        """Construye la pantalla de proyecto"""
        return ft.Container(
            content=ft.Column([
                # Header
                self._build_header(),
                
                # Contenido principal
                ft.Container(
                    content=ft.Row([
                        # Panel izquierdo - Información del proyecto
                        self._build_left_panel(),
                        
                        # Panel derecho - Árbol de versiones
                        self._build_right_panel(),
                        
                    ], spacing=0, expand=True),
                    expand=True,
                ),
                
            ], spacing=0),
            expand=True,
            bgcolor="#F7FAFC",
        )
    
    def _build_header(self):
        """Construye el header"""
        # Obtener icono del proyecto
        icono_src = self.proyecto.get("icono")
        
        return ft.Container(
            content=ft.Row([
                # Botón volver
                ft.IconButton(
                    icon=ft.Icons.ARROW_BACK,
                    icon_color="#718096",
                    icon_size=24,
                    on_click=lambda _: self.on_back(),
                    tooltip="Volver",
                ),
                
                ft.Container(width=12),
                
                # Icono y nombre del proyecto
                ft.Container(
                    content=ft.Image(src=icono_src, width=24, height=24) if icono_src else ft.Icon(ft.Icons.FOLDER, size=20, color="#667EEA"),
                    width=40,
                    height=40,
                    border_radius=10,
                    bgcolor="#EDF2F7",
                    alignment=ft.alignment.Alignment(0, 0),
                ),
                
                ft.Container(width=12),
                
                ft.Column([
                    ft.Text(
                        self.proyecto.get("nombre", "Proyecto"),
                        size=18,
                        weight=ft.FontWeight.BOLD,
                        color="#2D3748",
                    ),
                    ft.Text(
                        self.proyecto.get("tipo", "general").upper(),
                        size=12,
                        color="#718096",
                    ),
                ], spacing=2),
                
                ft.Container(expand=True),
                
                # Acciones
                ft.Row([
                    ft.ElevatedButton(
                        content=ft.Row([
                            ft.Icon(ft.Icons.SAVE_OUTLINED, size=18, color="#FFFFFF"),
                            ft.Container(width=6),
                            ft.Text("Guardar Versión", size=14, weight=ft.FontWeight.W_600, color="#FFFFFF"),
                        ], spacing=0),
                        on_click=lambda _: self._save_version(),
                        style=ft.ButtonStyle(
                            bgcolor="#667EEA",
                            padding=ft.Padding.symmetric(horizontal=20, vertical=12),
                            shape=ft.RoundedRectangleBorder(radius=10),
                            elevation=0,
                        ),
                    ),
                    ft.Container(width=8),
                    ft.IconButton(
                        icon=ft.Icons.MORE_VERT,
                        icon_color="#718096",
                        icon_size=22,
                        tooltip="Más opciones",
                    ),
                ], spacing=0),
                
            ]),
            padding=ft.Padding.all(24),
            bgcolor="#FFFFFF",
            border=ft.Border(bottom=ft.BorderSide(1, "#E2E8F0")),
        )
    
    def _build_left_panel(self):
        """Panel izquierdo con información del proyecto mejorado"""
        # Obtener icono del proyecto
        icono_src = self.proyecto.get("icono")
        
        return ft.Container(
            content=ft.Column([
                # Card de información principal con diseño mejorado
                ft.Container(
                    content=ft.Column([
                        # Icono grande centrado
                        ft.Container(
                            content=ft.Image(src=icono_src, width=48, height=48) if icono_src else ft.Icon(ft.Icons.FOLDER, size=40, color="#667EEA"),
                            width=80,
                            height=80,
                            border_radius=16,
                            bgcolor="#EDF2F7",
                            alignment=ft.alignment.Alignment(0, 0),
                        ),
                        
                        ft.Container(height=16),
                        
                        # Nombre del proyecto
                        ft.Text(
                            self.proyecto.get("nombre", "Proyecto"),
                            size=20,
                            weight=ft.FontWeight.BOLD,
                            color="#2D3748",
                            text_align=ft.TextAlign.CENTER,
                        ),
                        
                        ft.Container(height=8),
                        
                        # Badge del tipo
                        ft.Container(
                            content=ft.Text(
                                self.proyecto.get("tipo", "general").upper(),
                                size=11,
                                color="#667EEA",
                                weight=ft.FontWeight.BOLD,
                            ),
                            padding=ft.Padding.symmetric(horizontal=12, vertical=6),
                            border_radius=8,
                            bgcolor="#EDF2F7",
                        ),
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    padding=ft.Padding.all(24),
                    border_radius=12,
                    bgcolor="#FFFFFF",
                    border=ft.Border.all(1, "#E2E8F0"),
                ),
                
                ft.Container(height=20),
                
                # Estadísticas con diseño mejorado
                ft.Container(
                    content=ft.Column([
                        ft.Row([
                            ft.Icon(ft.Icons.BAR_CHART_ROUNDED, size=18, color="#667EEA"),
                            ft.Container(width=8),
                            ft.Text(
                                "Estadísticas",
                                size=15,
                                weight=ft.FontWeight.BOLD,
                                color="#2D3748",
                            ),
                        ]),
                        
                        ft.Container(height=16),
                        
                        # Stats en columna
                        ft.Column([
                            self._build_stat_row(
                                str(len(self.proyecto.get("versiones", []))),
                                "Versiones Guardadas",
                                ft.Icons.ACCOUNT_TREE_OUTLINED,
                                "#667EEA"
                            ),
                            ft.Container(height=12),
                            self._build_stat_row(
                                str(sum(v.get("archivos", 0) for v in self.proyecto.get("versiones", []))),
                                "Archivos Rastreados",
                                ft.Icons.INSERT_DRIVE_FILE_OUTLINED,
                                "#48BB78"
                            ),
                            ft.Container(height=12),
                            self._build_stat_row(
                                self.proyecto.get("tamaño_total", "0 B"),
                                "Tamaño Total",
                                ft.Icons.STORAGE_OUTLINED,
                                "#ED8936"
                            ),
                        ]),
                    ]),
                    padding=ft.Padding.all(20),
                    border_radius=12,
                    bgcolor="#FFFFFF",
                    border=ft.Border.all(1, "#E2E8F0"),
                ),
                
                ft.Container(height=20),
                
                # Ubicación con diseño mejorado
                ft.Container(
                    content=ft.Column([
                        ft.Row([
                            ft.Icon(ft.Icons.FOLDER_OUTLINED, size=16, color="#718096"),
                            ft.Container(width=8),
                            ft.Text("Ubicación", size=13, color="#718096", weight=ft.FontWeight.BOLD),
                        ]),
                        ft.Container(height=10),
                        ft.Text(
                            self.proyecto.get("ruta", "-"),
                            size=12,
                            color="#2D3748",
                            max_lines=2,
                            overflow=ft.TextOverflow.ELLIPSIS,
                        ),
                    ]),
                    padding=ft.Padding.all(16),
                    border_radius=10,
                    bgcolor="#F7FAFC",
                ),
                
                ft.Container(expand=True),
                
                # Acciones con diseño mejorado
                ft.Column([
                    self._build_action_button_v2("Abrir Carpeta", ft.Icons.FOLDER_OPEN_OUTLINED, "#667EEA"),
                    ft.Container(height=8),
                    self._build_action_button_v2("Configuración", ft.Icons.SETTINGS_OUTLINED, "#718096"),
                    ft.Container(height=8),
                    self._build_action_button_v2("Eliminar Proyecto", ft.Icons.DELETE_OUTLINE, "#F56565"),
                ], spacing=0),
                
            ], scroll=ft.ScrollMode.AUTO),
            width=340,
            padding=ft.Padding.all(20),
            bgcolor="#FAFAFA",
        )
    
    def _build_stat_card(self, value, label, icon, color):
        """Crea una card de estadística"""
        return ft.Container(
            content=ft.Column([
                ft.Icon(icon, size=24, color=color),
                ft.Container(height=8),
                ft.Text(value, size=24, weight=ft.FontWeight.BOLD, color="#2D3748"),
                ft.Text(label, size=12, color="#718096"),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=ft.Padding.all(16),
            border_radius=10,
            bgcolor="#F7FAFC",
            expand=True,
        )
    
    def _build_stat_row(self, value, label, icon, color):
        """Crea una fila de estadística"""
        return ft.Container(
            content=ft.Row([
                ft.Container(
                    content=ft.Icon(icon, size=20, color=color),
                    width=40,
                    height=40,
                    border_radius=10,
                    bgcolor=f"{color}15",
                    alignment=ft.alignment.Alignment(0, 0),
                ),
                ft.Container(width=12),
                ft.Column([
                    ft.Text(value, size=18, weight=ft.FontWeight.BOLD, color="#2D3748"),
                    ft.Text(label, size=12, color="#718096"),
                ], spacing=2),
            ]),
            padding=ft.Padding.all(12),
            border_radius=10,
            bgcolor="#F7FAFC",
        )
    
    def _build_action_button_v2(self, text, icon, color):
        """Crea un botón de acción mejorado"""
        is_danger = color == "#F56565"
        
        return ft.Container(
            content=ft.Row([
                ft.Icon(icon, size=18, color=color),
                ft.Container(width=10),
                ft.Text(text, size=14, color=color, weight=ft.FontWeight.W_600),
            ], alignment=ft.MainAxisAlignment.CENTER),
            padding=ft.Padding.symmetric(horizontal=16, vertical=14),
            border_radius=10,
            bgcolor="#FFFFFF" if not is_danger else f"{color}10",
            border=ft.Border.all(1, color if not is_danger else f"{color}40"),
            on_click=lambda _: print(f"Acción: {text}"),
            animate=ft.Animation(150, ft.AnimationCurve.EASE_OUT),
        )
    
    def _build_info_item(self, label, value):
        """Crea un item de información"""
        return ft.Container(
            content=ft.Column([
                ft.Text(label, size=12, color="#A0AEC0", weight=ft.FontWeight.W_600),
                ft.Container(height=4),
                ft.Text(value, size=14, color="#2D3748"),
            ], spacing=0),
            margin=ft.Margin(bottom=16, left=0, right=0, top=0),
        )
    
    def _build_action_button(self, text, icon):
        """Crea un botón de acción"""
        return ft.Container(
            content=ft.Row([
                ft.Icon(icon, size=20, color="#718096"),
                ft.Container(width=12),
                ft.Text(text, size=14, color="#2D3748"),
            ]),
            padding=ft.Padding.all(12),
            border_radius=8,
            bgcolor="#F7FAFC",
            margin=ft.Margin(bottom=8, left=0, right=0, top=0),
            on_click=lambda _: print(f"Acción: {text}"),
            animate=ft.Animation(150, ft.AnimationCurve.EASE_OUT),
        )
    
    def _build_right_panel(self):
        """Panel derecho con árbol de versiones mejorado"""
        versiones = self.proyecto.get("versiones", [])
        
        if not versiones:
            # Estado vacío con diseño mejorado
            return ft.Container(
                content=ft.Column([
                    # Icono grande con fondo
                    ft.Container(
                        content=ft.Icon(ft.Icons.ACCOUNT_TREE_OUTLINED, size=56, color="#667EEA"),
                        width=120,
                        height=120,
                        border_radius=60,
                        bgcolor="#EDF2F7",
                        alignment=ft.alignment.Alignment(0, 0),
                    ),
                    
                    ft.Container(height=24),
                    
                    ft.Text(
                        "No hay versiones guardadas",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color="#2D3748",
                    ),
                    
                    ft.Container(height=8),
                    
                    ft.Text(
                        "Guarda tu primera versión para comenzar a rastrear cambios",
                        size=14,
                        color="#718096",
                        text_align=ft.TextAlign.CENTER,
                    ),
                    
                    ft.Container(height=24),
                    
                    # Botón para guardar primera versión
                    ft.ElevatedButton(
                        content=ft.Row([
                            ft.Icon(ft.Icons.SAVE_OUTLINED, size=18, color="#FFFFFF"),
                            ft.Container(width=8),
                            ft.Text("Guardar Primera Versión", size=14, weight=ft.FontWeight.W_600, color="#FFFFFF"),
                        ], alignment=ft.MainAxisAlignment.CENTER),
                        on_click=lambda _: self._save_version(),
                        style=ft.ButtonStyle(
                            bgcolor="#667EEA",
                            padding=ft.Padding.symmetric(horizontal=24, vertical=14),
                            shape=ft.RoundedRectangleBorder(radius=10),
                            elevation=0,
                        ),
                    ),
                    
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                expand=True,
                alignment=ft.alignment.Alignment(0, 0),
                bgcolor="#FFFFFF",
            )
        
        # Árbol de versiones con diseño mejorado
        return ft.Container(
            content=ft.Column([
                # Header del panel
                ft.Row([
                    ft.Icon(ft.Icons.ACCOUNT_TREE_OUTLINED, size=20, color="#667EEA"),
                    ft.Container(width=8),
                    ft.Text(
                        "Historial de Versiones",
                        size=18,
                        weight=ft.FontWeight.BOLD,
                        color="#2D3748",
                    ),
                    ft.Container(expand=True),
                    ft.Container(
                        content=ft.Text(
                            f"{len(versiones)} versión{'es' if len(versiones) != 1 else ''}",
                            size=12,
                            color="#667EEA",
                            weight=ft.FontWeight.W_600,
                        ),
                        padding=ft.Padding.symmetric(horizontal=10, vertical=5),
                        border_radius=12,
                        bgcolor="#EDF2F7",
                    ),
                ]),
                
                ft.Container(height=24),
                
                # Lista de versiones en formato árbol
                ft.Column([
                    self._build_version_node(v, i, len(versiones)) 
                    for i, v in enumerate(versiones)
                ], spacing=0),
                
            ], scroll=ft.ScrollMode.AUTO),
            expand=True,
            padding=ft.Padding.all(28),
            bgcolor="#FFFFFF",
        )
    
    def _build_version_node(self, version, index, total):
        """Crea un nodo de versión en el árbol con diseño mejorado"""
        is_last = index == total - 1
        is_first = index == 0
        
        return ft.Container(
            content=ft.Row([
                # Línea vertical y nodo
                ft.Container(
                    content=ft.Column([
                        # Círculo del nodo con gradiente visual
                        ft.Container(
                            content=ft.Container(
                                width=14,
                                height=14,
                                border_radius=7,
                                bgcolor="#667EEA" if is_first else "#FFFFFF",
                                border=ft.Border.all(3, "#667EEA"),
                            ),
                            width=32,
                            height=32,
                            border_radius=16,
                            bgcolor="#EDF2F7",
                            alignment=ft.alignment.Alignment(0, 0),
                        ),
                        # Línea vertical (si no es el último)
                        ft.Container(
                            width=3,
                            height=80 if not is_last else 0,
                            bgcolor="#E2E8F0",
                            border_radius=2,
                        ) if not is_last else ft.Container(),
                    ], spacing=0, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    width=32,
                ),
                
                ft.Container(width=20),
                
                # Card de versión mejorada
                ft.Container(
                    content=ft.Column([
                        # Header de la versión
                        ft.Row([
                            ft.Container(
                                content=ft.Row([
                                    ft.Icon(ft.Icons.BOOKMARK, size=14, color="#667EEA"),
                                    ft.Container(width=6),
                                    ft.Text(
                                        f"v{index + 1}",
                                        size=13,
                                        weight=ft.FontWeight.BOLD,
                                        color="#667EEA",
                                    ),
                                ]),
                                padding=ft.Padding.symmetric(horizontal=10, vertical=5),
                                border_radius=6,
                                bgcolor="#EDF2F7",
                            ),
                            ft.Container(expand=True),
                            ft.Row([
                                ft.Icon(ft.Icons.ACCESS_TIME, size=14, color="#A0AEC0"),
                                ft.Container(width=4),
                                ft.Text(
                                    version.get("fecha", "Hoy"),
                                    size=12,
                                    color="#718096",
                                ),
                            ]),
                        ]),
                        
                        ft.Container(height=12),
                        
                        # Descripción
                        ft.Text(
                            version.get("descripcion", "Sin descripción"),
                            size=14,
                            color="#2D3748",
                            weight=ft.FontWeight.W_500,
                        ),
                        
                        ft.Container(height=8),
                        
                        # Metadata
                        ft.Row([
                            ft.Container(
                                content=ft.Row([
                                    ft.Icon(ft.Icons.INSERT_DRIVE_FILE_OUTLINED, size=12, color="#718096"),
                                    ft.Container(width=4),
                                    ft.Text(
                                        f"{version.get('archivos', 0)} archivos",
                                        size=11,
                                        color="#718096",
                                    ),
                                ]),
                            ),
                            ft.Container(width=12),
                            ft.Container(
                                content=ft.Row([
                                    ft.Icon(ft.Icons.STORAGE_OUTLINED, size=12, color="#718096"),
                                    ft.Container(width=4),
                                    ft.Text(
                                        version.get('tamaño', '0 B'),
                                        size=11,
                                        color="#718096",
                                    ),
                                ]),
                            ),
                        ]),
                        
                        ft.Container(height=14),
                        
                        # Acciones
                        ft.Row([
                            ft.ElevatedButton(
                                content=ft.Row([
                                    ft.Icon(ft.Icons.RESTORE, size=16, color="#FFFFFF"),
                                    ft.Container(width=6),
                                    ft.Text("Restaurar", size=13, color="#FFFFFF", weight=ft.FontWeight.W_600),
                                ], spacing=0),
                                on_click=lambda _, v=version: self._restore_version(v),
                                style=ft.ButtonStyle(
                                    bgcolor="#667EEA",
                                    padding=ft.Padding.symmetric(horizontal=16, vertical=10),
                                    shape=ft.RoundedRectangleBorder(radius=8),
                                    elevation=0,
                                ),
                            ),
                            ft.Container(width=8),
                            ft.OutlinedButton(
                                content=ft.Row([
                                    ft.Icon(ft.Icons.VISIBILITY_OUTLINED, size=16, color="#718096"),
                                    ft.Container(width=6),
                                    ft.Text("Detalles", size=13, color="#718096", weight=ft.FontWeight.W_600),
                                ], spacing=0),
                                on_click=lambda _, v=version: self._view_details(v),
                                style=ft.ButtonStyle(
                                    side=ft.BorderSide(1, "#E2E8F0"),
                                    padding=ft.Padding.symmetric(horizontal=16, vertical=10),
                                    shape=ft.RoundedRectangleBorder(radius=8),
                                ),
                            ),
                            ft.Container(expand=True),
                            ft.IconButton(
                                icon=ft.Icons.MORE_HORIZ,
                                icon_color="#A0AEC0",
                                icon_size=20,
                                tooltip="Más opciones",
                            ),
                        ], spacing=0),
                    ]),
                    padding=ft.Padding.all(20),
                    border_radius=12,
                    bgcolor="#F7FAFC" if not is_first else "#FFFFFF",
                    border=ft.Border.all(2 if is_first else 1, "#667EEA" if is_first else "#E2E8F0"),
                    expand=True,
                    margin=ft.Margin(bottom=20 if not is_last else 0, left=0, right=0, top=0),
                    shadow=ft.BoxShadow(
                        spread_radius=0,
                        blur_radius=8 if is_first else 0,
                        color="#667EEA20" if is_first else "#00000000",
                        offset=ft.Offset(0, 2),
                    ) if is_first else None,
                ),
                
            ], alignment=ft.MainAxisAlignment.START),
        )
    
    def _save_version(self):
        """Guarda una nueva versión con diálogo y loader"""
        # Crear campo de texto para el mensaje
        mensaje_field = ft.TextField(
            hint_text="Ej: Agregadas nuevas funcionalidades",
            multiline=True,
            min_lines=2,
            max_lines=4,
            border_radius=10,
            bgcolor="#F7FAFC",
            border_color="#E2E8F0",
            focused_border_color="#667EEA",
        )
        
        def guardar():
            """Guarda la versión"""
            mensaje = mensaje_field.value or "Sin descripción"
            dialog.open = False
            self.page.update()
            
            # Mostrar loader
            self._show_progress_dialog("Guardando versión...", self._guardar_version_thread, mensaje)
        
        # Crear diálogo
        dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Guardar Nueva Versión", weight=ft.FontWeight.BOLD),
            content=ft.Container(
                content=ft.Column([
                    ft.Text("Describe los cambios de esta versión:", size=14, color="#718096"),
                    ft.Container(height=12),
                    mensaje_field,
                ], tight=True),
                width=450,
            ),
            actions=[
                ft.TextButton("Cancelar", on_click=lambda _: self._close_dialog(dialog)),
                ft.ElevatedButton(
                    "Guardar",
                    on_click=lambda _: guardar(),
                    style=ft.ButtonStyle(
                        bgcolor="#667EEA",
                        color="#FFFFFF",
                    ),
                ),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        
        self.page.overlay.append(dialog)
        dialog.open = True
        self.page.update()
    
    def _guardar_version_thread(self, mensaje):
        """Guarda la versión en un thread separado"""
        try:
            proyecto_actualizado = guardar_version_ui(
                self.proyecto["ruta"],
                mensaje,
                self._update_progress
            )
            
            if proyecto_actualizado:
                # Actualizar proyecto
                proyecto_actualizado["icono"] = self.proyecto.get("icono")
                self.proyecto = proyecto_actualizado
                
                # Refrescar en el padre si existe callback
                if self.on_refresh:
                    self.on_refresh(self.proyecto["ruta"])
                
                # Cerrar loader y reconstruir vista
                self._close_progress_dialog()
                self.page.controls.clear()
                self.page.add(self.build())
                self.page.update()
                
                # Mostrar mensaje de éxito
                self._show_success_snackbar("✓ Versión guardada exitosamente")
            else:
                self._close_progress_dialog()
                self._show_error_snackbar("❌ Error al guardar la versión")
        except Exception as e:
            self._close_progress_dialog()
            self._show_error_snackbar(f"❌ Error: {str(e)}")
    
    def _restore_version(self, version):
        """Restaura una versión con confirmación"""
        numero_version = version.get("numero", 1)
        
        def confirmar():
            """Confirma la restauración"""
            dialog.open = False
            self.page.update()
            
            # Mostrar loader
            self._show_progress_dialog("Restaurando versión...", self._restaurar_version_thread, numero_version)
        
        # Crear diálogo de confirmación
        dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Restaurar Versión", weight=ft.FontWeight.BOLD),
            content=ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.WARNING_AMBER_ROUNDED, size=48, color="#ED8936"),
                    ft.Container(height=16),
                    ft.Text(
                        f"¿Estás seguro de restaurar la versión {numero_version}?",
                        size=16,
                        weight=ft.FontWeight.W_600,
                        color="#2D3748",
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.Container(height=8),
                    ft.Text(
                        "Esto reemplazará todos los archivos actuales con los de esta versión.",
                        size=14,
                        color="#718096",
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.Container(height=12),
                    ft.Container(
                        content=ft.Column([
                            ft.Text(f"📅 {version.get('fecha', '')}", size=13, color="#2D3748"),
                            ft.Text(f"📝 {version.get('descripcion', '')}", size=13, color="#718096"),
                        ]),
                        padding=ft.Padding.all(12),
                        border_radius=8,
                        bgcolor="#F7FAFC",
                    ),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, tight=True),
                width=400,
            ),
            actions=[
                ft.TextButton("Cancelar", on_click=lambda _: self._close_dialog(dialog)),
                ft.ElevatedButton(
                    "Restaurar",
                    on_click=lambda _: confirmar(),
                    style=ft.ButtonStyle(
                        bgcolor="#ED8936",
                        color="#FFFFFF",
                    ),
                ),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        
        self.page.overlay.append(dialog)
        dialog.open = True
        self.page.update()
    
    def _restaurar_version_thread(self, numero_version):
        """Restaura la versión en un thread separado"""
        try:
            proyecto_actualizado = restaurar_version_ui(
                self.proyecto["ruta"],
                numero_version,
                self._update_progress
            )
            
            if proyecto_actualizado:
                # Actualizar proyecto
                proyecto_actualizado["icono"] = self.proyecto.get("icono")
                self.proyecto = proyecto_actualizado
                
                # Refrescar en el padre si existe callback
                if self.on_refresh:
                    self.on_refresh(self.proyecto["ruta"])
                
                # Cerrar loader y reconstruir vista
                self._close_progress_dialog()
                self.page.controls.clear()
                self.page.add(self.build())
                self.page.update()
                
                # Mostrar mensaje de éxito
                self._show_success_snackbar(f"✓ Versión {numero_version} restaurada exitosamente")
            else:
                self._close_progress_dialog()
                self._show_error_snackbar("❌ Error al restaurar la versión")
        except Exception as e:
            self._close_progress_dialog()
            self._show_error_snackbar(f"❌ Error: {str(e)}")
    
    def _view_details(self, version):
        """Ver detalles de una versión"""
        numero_version = version.get("numero", 1)
        
        dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text(f"Versión {numero_version}", weight=ft.FontWeight.BOLD),
            content=ft.Container(
                content=ft.Column([
                    self._build_detail_row("📅 Fecha", version.get("fecha_completa", version.get("fecha", ""))),
                    self._build_detail_row("📝 Descripción", version.get("descripcion", "Sin descripción")),
                    self._build_detail_row("📁 Archivos", str(version.get("archivos", 0))),
                    self._build_detail_row("💾 Tamaño", version.get("tamaño", "0 B")),
                    self._build_detail_row("👤 Autor", version.get("autor", "Usuario")),
                ], tight=True),
                width=400,
            ),
            actions=[
                ft.TextButton("Cerrar", on_click=lambda _: self._close_dialog(dialog)),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        
        self.page.overlay.append(dialog)
        dialog.open = True
        self.page.update()
    
    def _build_detail_row(self, label, value):
        """Crea una fila de detalle"""
        return ft.Container(
            content=ft.Row([
                ft.Text(label, size=14, color="#718096", weight=ft.FontWeight.W_600, width=120),
                ft.Text(value, size=14, color="#2D3748", expand=True),
            ]),
            margin=ft.Margin(bottom=12, left=0, right=0, top=0),
        )
    
    def _show_progress_dialog(self, title, func, *args):
        """Muestra un diálogo de progreso"""
        self.progress_text = ft.Text("Iniciando...", size=14, color="#2D3748")
        self.progress_bar = ft.ProgressBar(width=400, color="#667EEA")
        
        self.progress_dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text(title, weight=ft.FontWeight.BOLD),
            content=ft.Container(
                content=ft.Column([
                    self.progress_text,
                    ft.Container(height=16),
                    self.progress_bar,
                ], tight=True),
                width=400,
                padding=20,
            ),
        )
        
        self.page.overlay.append(self.progress_dialog)
        self.progress_dialog.open = True
        self.page.update()
        
        # Ejecutar función en thread
        thread = threading.Thread(target=func, args=args, daemon=True)
        thread.start()
    
    def _update_progress(self, mensaje):
        """Actualiza el mensaje de progreso"""
        if hasattr(self, 'progress_text'):
            self.progress_text.value = mensaje
            self.page.update()
    
    def _close_progress_dialog(self):
        """Cierra el diálogo de progreso"""
        if hasattr(self, 'progress_dialog'):
            self.progress_dialog.open = False
            self.page.update()
    
    def _close_dialog(self, dialog):
        """Cierra un diálogo"""
        dialog.open = False
        self.page.update()
    
    def _show_success_snackbar(self, mensaje):
        """Muestra un snackbar de éxito"""
        snackbar = ft.SnackBar(
            content=ft.Text(mensaje, color="#FFFFFF"),
            bgcolor="#48BB78",
        )
        self.page.overlay.append(snackbar)
        snackbar.open = True
        self.page.update()
    
    def _show_error_snackbar(self, mensaje):
        """Muestra un snackbar de error"""
        snackbar = ft.SnackBar(
            content=ft.Text(mensaje, color="#FFFFFF"),
            bgcolor="#F56565",
        )
        self.page.overlay.append(snackbar)
        snackbar.open = True
        self.page.update()
