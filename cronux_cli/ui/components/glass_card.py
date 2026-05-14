"""
Tarjeta con efecto glassmorphism
"""
import flet as ft


class GlassCard(ft.Container):
    """Tarjeta con efecto de vidrio (glassmorphism)"""
    
    def __init__(
        self,
        content: ft.Control,
        padding: int = 20,
        border_radius: int = 16,
        blur: int = 10,
        on_click=None,
        width=None,
        height=None,
        bgcolor=None,
    ):
        super().__init__(
            content=content,
            padding=ft.Padding.all(padding),
            border_radius=border_radius,
            width=width,
            height=height,
            bgcolor=bgcolor or ft.Colors.with_opacity(0.7, ft.Colors.WHITE),
            border=ft.Border.all(1, ft.Colors.with_opacity(0.2, ft.Colors.WHITE)),
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=blur,
                color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK),
                offset=ft.Offset(0, 4),
            ),
            on_click=on_click,
            ink=on_click is not None,
            animate=ft.Animation(200, ft.AnimationCurve.EASE_OUT) if on_click else None,
        )


class NeumorphicCard(ft.Container):
    """Tarjeta con efecto neumórfico"""
    
    def __init__(
        self,
        content: ft.Control,
        padding: int = 20,
        border_radius: int = 16,
        on_click=None,
        width=None,
        height=None,
        is_dark: bool = False,
    ):
        # Colores según tema
        if is_dark:
            bg_color = "#1E2433"
            shadow_light = ft.Colors.with_opacity(0.05, ft.Colors.WHITE)
            shadow_dark = ft.Colors.with_opacity(0.5, ft.Colors.BLACK)
        else:
            bg_color = "#F5F7FA"
            shadow_light = ft.Colors.with_opacity(0.8, ft.Colors.WHITE)
            shadow_dark = ft.Colors.with_opacity(0.15, "#A0AEC0")
        
        super().__init__(
            content=content,
            padding=ft.Padding.all(padding),
            border_radius=border_radius,
            width=width,
            height=height,
            bgcolor=bg_color,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=10,
                color=shadow_dark,
                offset=ft.Offset(5, 5),
            ),
            on_click=on_click,
            ink=on_click is not None,
            animate=ft.Animation(200, ft.AnimationCurve.EASE_OUT) if on_click else None,
        )
