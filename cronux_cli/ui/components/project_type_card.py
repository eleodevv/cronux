"""
Tarjeta de tipo de proyecto con animación
"""
import flet as ft


class ProjectTypeCard(ft.Container):
    """Tarjeta animada para seleccionar tipo de proyecto"""
    
    def __init__(
        self,
        nombre: str,
        icono_path: str,
        descripcion: str,
        is_selected: bool,
        on_click,
        gradient_colors: list,
        is_dark: bool = False,
    ):
        self.nombre = nombre
        self.is_selected = is_selected
        self.gradient_colors = gradient_colors
        
        # Usar un icono de Flet como fallback si no se carga el SVG
        icon_map = {
            "nodeblanco": ft.Icons.JAVASCRIPT,
            "pythonblanco": ft.Icons.CODE,
            "javablanco": ft.Icons.COFFEE,
            "jsblanco": ft.Icons.WEB,
            "kotlinblanco": ft.Icons.ANDROID,
            "c#blanco": ft.Icons.DESKTOP_WINDOWS,
            "goblanco": ft.Icons.SPEED,
            "wordblanco": ft.Icons.DESCRIPTION,
        }
        
        # Intentar determinar el icono
        icon_key = icono_path.split("/")[-1].replace(".svg", "")
        fallback_icon = icon_map.get(icon_key, ft.Icons.FOLDER)
        
        # Contenido
        content = ft.Column(
            [
                # Icono con fondo circular
                ft.Container(
                    content=ft.Icon(
                        fallback_icon,
                        size=40,
                        color=ft.Colors.WHITE if is_selected else (
                            gradient_colors[0] if not is_selected else ft.Colors.WHITE
                        ),
                    ),
                    width=80,
                    height=80,
                    border_radius=40,
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.Alignment(-1, -1),
                        end=ft.alignment.Alignment(1, 1),
                        colors=gradient_colors if is_selected else [
                            ft.Colors.with_opacity(0.1, gradient_colors[0]),
                            ft.Colors.with_opacity(0.1, gradient_colors[1]),
                        ],
                    ),
                    alignment=ft.alignment.Alignment(0, 0),
                    shadow=ft.BoxShadow(
                        spread_radius=0,
                        blur_radius=20,
                        color=ft.Colors.with_opacity(0.3, gradient_colors[0]) if is_selected else ft.Colors.TRANSPARENT,
                        offset=ft.Offset(0, 4),
                    ) if is_selected else None,
                ),
                ft.Container(height=16),
                # Nombre
                ft.Text(
                    nombre,
                    size=16,
                    weight=ft.FontWeight.W_700,
                    color=gradient_colors[0] if is_selected else ("#1A202C" if not is_dark else "#F7FAFC"),
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Container(height=4),
                # Descripción
                ft.Text(
                    descripcion,
                    size=12,
                    color="#718096",
                    text_align=ft.TextAlign.CENTER,
                    max_lines=2,
                    overflow=ft.TextOverflow.ELLIPSIS,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0,
        )
        
        # Fondo según selección
        if is_selected:
            bgcolor = ft.Colors.with_opacity(0.05, gradient_colors[0])
            border_color = gradient_colors[0]
            border_width = 2
        else:
            bgcolor = "#FFFFFF" if not is_dark else "#1E2433"
            border_color = "#E2E8F0" if not is_dark else "#2D3748"
            border_width = 1
        
        super().__init__(
            content=content,
            padding=ft.Padding.all(20),
            border_radius=20,
            bgcolor=bgcolor,
            border=ft.Border.all(border_width, border_color),
            on_click=on_click,
            ink=True,
            animate=ft.Animation(300, ft.AnimationCurve.EASE_OUT),
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=20,
                color=ft.Colors.with_opacity(0.1, gradient_colors[0]) if is_selected else ft.Colors.with_opacity(0.05, ft.Colors.BLACK),
                offset=ft.Offset(0, 4),
            ),
        )
