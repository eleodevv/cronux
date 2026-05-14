"""
Botón con gradiente - Componente reutilizable
"""
import flet as ft


class GradientButton(ft.Container):
    """Botón moderno con gradiente"""
    
    def __init__(
        self,
        text: str,
        on_click,
        gradient_colors: list,
        icon: str = None,
        width: int = None,
        height: int = 48,
        disabled: bool = False,
    ):
        self.text = text
        self.icon = icon
        self.disabled = disabled
        
        # Contenido del botón
        content_items = []
        if icon:
            content_items.append(ft.Icon(icon, size=20, color=ft.Colors.WHITE))
            content_items.append(ft.Container(width=8))
        content_items.append(
            ft.Text(
                text,
                size=15,
                weight=ft.FontWeight.W_600,
                color=ft.Colors.WHITE,
            )
        )
        
        super().__init__(
            content=ft.Row(
                content_items,
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=0,
            ),
            gradient=ft.LinearGradient(
                begin=ft.alignment.Alignment(-1, 0),
                end=ft.alignment.Alignment(1, 0),
                colors=gradient_colors if not disabled else ["#A0AEC0", "#718096"],
            ),
            width=width,
            height=height,
            border_radius=12,
            padding=ft.Padding.symmetric(horizontal=24, vertical=0),
            on_click=on_click if not disabled else None,
            ink=not disabled,
            animate=ft.Animation(200, ft.AnimationCurve.EASE_OUT),
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=20,
                color=ft.Colors.with_opacity(0.3, gradient_colors[0]) if not disabled else ft.Colors.TRANSPARENT,
                offset=ft.Offset(0, 4),
            ),
        )
