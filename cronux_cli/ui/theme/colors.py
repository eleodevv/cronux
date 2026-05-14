"""
Cronux UI v2 - Sistema de colores moderno
Diseño: Glassmorphism + Gradientes
"""

class AppColors:
    """Colores principales de la aplicación"""
    
    # Modo Claro
    class Light:
        # Fondos con gradientes
        BG_PRIMARY = "#FFFFFF"
        BG_SECONDARY = "#F5F7FA"
        BG_CARD = "#FFFFFF"
        BG_HOVER = "#F0F2F5"
        
        # Gradientes
        GRADIENT_PRIMARY = ["#667EEA", "#764BA2"]  # Púrpura
        GRADIENT_SECONDARY = ["#F093FB", "#F5576C"]  # Rosa
        GRADIENT_SUCCESS = ["#4FACFE", "#00F2FE"]  # Azul
        GRADIENT_DANGER = ["#FA709A", "#FEE140"]  # Naranja-Rosa
        
        # Textos
        TEXT_PRIMARY = "#1A202C"
        TEXT_SECONDARY = "#718096"
        TEXT_MUTED = "#A0AEC0"
        TEXT_WHITE = "#FFFFFF"
        
        # Bordes
        BORDER_DEFAULT = "#E2E8F0"
        BORDER_LIGHT = "#EDF2F7"
        
        # Acentos sólidos
        ACCENT_PRIMARY = "#667EEA"
        ACCENT_SECONDARY = "#764BA2"
        ACCENT_SUCCESS = "#48BB78"
        ACCENT_DANGER = "#F56565"
        ACCENT_WARNING = "#ED8936"
        ACCENT_INFO = "#4299E1"
        
        # Sombras
        SHADOW_SM = "0 2px 4px rgba(0,0,0,0.06)"
        SHADOW_MD = "0 4px 6px rgba(0,0,0,0.07)"
        SHADOW_LG = "0 10px 15px rgba(0,0,0,0.1)"
        SHADOW_XL = "0 20px 25px rgba(0,0,0,0.15)"
    
    # Modo Oscuro
    class Dark:
        # Fondos oscuros
        BG_PRIMARY = "#0F1419"
        BG_SECONDARY = "#1A1F2E"
        BG_CARD = "#1E2433"
        BG_HOVER = "#252B3B"
        
        # Gradientes (más vibrantes en oscuro)
        GRADIENT_PRIMARY = ["#667EEA", "#764BA2"]
        GRADIENT_SECONDARY = ["#F093FB", "#F5576C"]
        GRADIENT_SUCCESS = ["#4FACFE", "#00F2FE"]
        GRADIENT_DANGER = ["#FA709A", "#FEE140"]
        
        # Textos
        TEXT_PRIMARY = "#F7FAFC"
        TEXT_SECONDARY = "#CBD5E0"
        TEXT_MUTED = "#718096"
        TEXT_WHITE = "#FFFFFF"
        
        # Bordes
        BORDER_DEFAULT = "#2D3748"
        BORDER_LIGHT = "#252B3B"
        
        # Acentos sólidos
        ACCENT_PRIMARY = "#7C3AED"
        ACCENT_SECONDARY = "#8B5CF6"
        ACCENT_SUCCESS = "#48BB78"
        ACCENT_DANGER = "#F56565"
        ACCENT_WARNING = "#ED8936"
        ACCENT_INFO = "#4299E1"
        
        # Sombras (más sutiles en oscuro)
        SHADOW_SM = "0 2px 4px rgba(0,0,0,0.3)"
        SHADOW_MD = "0 4px 6px rgba(0,0,0,0.4)"
        SHADOW_LG = "0 10px 15px rgba(0,0,0,0.5)"
        SHADOW_XL = "0 20px 25px rgba(0,0,0,0.6)"


class ThemeManager:
    """Gestor de temas"""
    
    def __init__(self):
        self.is_dark = False
    
    def get_colors(self):
        """Retorna los colores según el tema actual"""
        return AppColors.Dark if self.is_dark else AppColors.Light
    
    def toggle(self):
        """Alterna entre modo claro y oscuro"""
        self.is_dark = not self.is_dark
        return self.is_dark
