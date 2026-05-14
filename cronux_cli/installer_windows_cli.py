#!/usr/bin/env python3
"""
CRONUX-CRX CLI Installer for Windows
Simple installer/uninstaller with the new brand design
"""

import flet as ft
import os
import sys
import shutil
import subprocess
from pathlib import Path

# ── Brand colors ──────────────────────────────────────────
BRAND   = "#667EEA"
DARK    = "#1A202C"
GRAY    = "#718096"
LIGHT   = "#F7FAFC"
BORDER  = "#E2E8F0"
SUCCESS = "#48BB78"
DANGER  = "#F56565"
WHITE   = "#FFFFFF"

# ── Install config ────────────────────────────────────────
INSTALL_DIR  = Path(os.environ.get("LOCALAPPDATA", "C:/Users/Public")) / "cronux-crx"
SCRIPTS_DIR  = INSTALL_DIR / "cli"
PYTHON_SCRIPT = SCRIPTS_DIR / "cronux_cli.py"
BAT_FILE     = INSTALL_DIR / "cronux.bat"
PATH_KEY     = r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment"

def is_installed():
    return INSTALL_DIR.exists() and BAT_FILE.exists()

def get_source_dir():
    """Obtiene el directorio fuente del CLI"""
    if getattr(sys, 'frozen', False):
        return Path(sys._MEIPASS) / "cli"
    return Path(__file__).parent / "cli"

def install():
    """Instala el CLI de CRONUX-CRX"""
    try:
        # Crear directorio de instalación
        INSTALL_DIR.mkdir(parents=True, exist_ok=True)
        SCRIPTS_DIR.mkdir(parents=True, exist_ok=True)

        # Copiar archivos del CLI
        src = get_source_dir()
        if src.exists():
            for f in src.glob("*.py"):
                shutil.copy2(f, SCRIPTS_DIR / f.name)

        # Crear cronux.bat
        bat_content = f'@echo off\npython "{PYTHON_SCRIPT}" %*\n'
        BAT_FILE.write_text(bat_content)

        # Agregar al PATH del sistema (requiere admin)
        try:
            import winreg
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, PATH_KEY, 0, winreg.KEY_ALL_ACCESS)
            current, _ = winreg.QueryValueEx(key, "Path")
            install_str = str(INSTALL_DIR)
            if install_str not in current:
                winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, current + ";" + install_str)
            winreg.CloseKey(key)
        except Exception:
            # Si no hay permisos de admin, agregar al PATH del usuario
            try:
                import winreg
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment", 0, winreg.KEY_ALL_ACCESS)
                try:
                    current, _ = winreg.QueryValueEx(key, "Path")
                except FileNotFoundError:
                    current = ""
                install_str = str(INSTALL_DIR)
                if install_str not in current:
                    new_path = (current + ";" + install_str).lstrip(";")
                    winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, new_path)
                winreg.CloseKey(key)
            except Exception:
                pass

        return True, None
    except Exception as e:
        return False, str(e)

def uninstall():
    """Desinstala el CLI de CRONUX-CRX"""
    try:
        if INSTALL_DIR.exists():
            shutil.rmtree(INSTALL_DIR)

        # Remover del PATH
        try:
            import winreg
            for hive in [winreg.HKEY_LOCAL_MACHINE, winreg.HKEY_CURRENT_USER]:
                subkey = PATH_KEY if hive == winreg.HKEY_LOCAL_MACHINE else "Environment"
                try:
                    key = winreg.OpenKey(hive, subkey, 0, winreg.KEY_ALL_ACCESS)
                    current, _ = winreg.QueryValueEx(key, "Path")
                    install_str = str(INSTALL_DIR)
                    new_path = ";".join(p for p in current.split(";") if p and p != install_str)
                    winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, new_path)
                    winreg.CloseKey(key)
                except Exception:
                    pass
        except Exception:
            pass

        return True, None
    except Exception as e:
        return False, str(e)


# ── UI ────────────────────────────────────────────────────
def main(page: ft.Page):
    page.title = "CRONUX-CRX CLI Installer"
    page.window.width  = 520
    page.window.height = 620
    page.window.resizable = False
    page.bgcolor = WHITE
    page.padding = 0

    installed = is_installed()

    # ── Estado ──────────────────────────────────────────
    status_text  = ft.Text("", size=13, color=GRAY, text_align=ft.TextAlign.CENTER)
    progress_bar = ft.ProgressBar(width=400, color=BRAND, bgcolor=BORDER, visible=False)
    action_btn   = ft.Ref[ft.Button]()

    def set_status(msg, color=GRAY):
        status_text.value = msg
        status_text.color = color
        page.update()

    def set_loading(loading):
        progress_bar.visible = loading
        action_btn.current.disabled = loading
        page.update()

    def on_action(e):
        set_loading(True)

        if not is_installed():
            set_status("Instalando CRONUX-CRX CLI...", BRAND)
            ok, err = install()
            if ok:
                set_status("✓ Instalado correctamente. Reinicia la terminal.", SUCCESS)
                action_btn.current.content = ft.Text("Desinstalar", color=WHITE)
                action_btn.current.bgcolor = DANGER
                installed_badge.value = "Instalado"
                installed_badge.color = SUCCESS
                page.update()
            else:
                set_status(f"✗ Error: {err}", DANGER)
        else:
            set_status("Desinstalando CRONUX-CRX CLI...", DANGER)
            ok, err = uninstall()
            if ok:
                set_status("✓ Desinstalado correctamente.", SUCCESS)
                action_btn.current.content = ft.Text("Instalar", color=WHITE)
                action_btn.current.bgcolor = BRAND
                installed_badge.value = "No instalado"
                installed_badge.color = GRAY
                page.update()
            else:
                set_status(f"✗ Error: {err}", DANGER)

        set_loading(False)

    # ── Badge de estado ──────────────────────────────────
    installed_badge = ft.Text(
        "Instalado" if installed else "No instalado",
        size=13,
        color=SUCCESS if installed else GRAY,
        weight=ft.FontWeight.W_600,
    )

    # ── Logo CLI (hexágono actualizado) ──────────────────
    logo_path = Path(__file__).parent / "assets" / "hexagon_logo_256.png"
    logo = None
    if logo_path.exists():
        logo = ft.Image(src=str(logo_path), width=120, height=120)
    
    if not logo:
        # Fallback: hexágono con diseño actualizado
        logo = ft.Container(
            content=ft.Stack([
                # Fondo azul/morado redondeado
                ft.Container(
                    width=120, height=120,
                    border_radius=28,
                    bgcolor=BRAND,
                ),
                # Hexágono blanco centrado
                ft.Container(
                    content=ft.Icon(ft.icons.HEXAGON, size=60, color=WHITE),
                    width=120, height=120,
                    alignment=ft.alignment.center,
                ),
            ]),
            width=120,
            height=120,
        )

    # ── Comandos de ejemplo ──────────────────────────────
    def cmd_row(cmd, desc):
        return ft.Container(
            content=ft.Row([
                ft.Container(
                    content=ft.Text(cmd, size=12, color=BRAND,
                                    font_family="monospace", weight=ft.FontWeight.BOLD),
                    bgcolor="#EEF2FF", border_radius=6,
                    padding=ft.Padding.symmetric(horizontal=10, vertical=4),
                ),
                ft.Container(width=12),
                ft.Text(desc, size=12, color=GRAY),
            ]),
            margin=ft.Margin(bottom=6, left=0, right=0, top=0),
        )

    # ── Layout principal ─────────────────────────────────
    page.add(
        ft.Container(
            content=ft.Column([
                ft.Container(height=40),

                # Logo
                ft.Row([logo], alignment=ft.MainAxisAlignment.CENTER),

                ft.Container(height=20),

                # Título
                ft.Text("CRONUX-CRX CLI", size=28, weight=ft.FontWeight.BOLD,
                        color=DARK, text_align=ft.TextAlign.CENTER),
                ft.Text("Control de Versiones v0.2.0", size=14, color=GRAY,
                        text_align=ft.TextAlign.CENTER),

                ft.Container(height=8),

                # Badge estado
                ft.Row([
                    ft.Container(
                        content=ft.Row([
                            ft.Icon(
                                ft.Icons.CHECK_CIRCLE_ROUNDED if installed else ft.Icons.CIRCLE_OUTLINED,
                                size=14,
                                color=SUCCESS if installed else GRAY,
                            ),
                            ft.Container(width=6),
                            installed_badge,
                        ]),
                        padding=ft.Padding.symmetric(horizontal=14, vertical=6),
                        border_radius=20,
                        bgcolor="#F0FFF4" if installed else LIGHT,
                        border=ft.Border.all(1, "#C6F6D5" if installed else BORDER),
                    )
                ], alignment=ft.MainAxisAlignment.CENTER),

                ft.Container(height=28),

                # Comandos disponibles
                ft.Container(
                    content=ft.Column([
                        ft.Text("Comandos disponibles", size=13, color=GRAY,
                                weight=ft.FontWeight.W_600),
                        ft.Container(height=10),
                        cmd_row("cronux crear", "Crear nuevo proyecto"),
                        cmd_row("cronux guardar", "Guardar versión"),
                        cmd_row("cronux historial", "Ver historial"),
                        cmd_row("cronux restaurar", "Restaurar versión"),
                    ]),
                    padding=ft.Padding.all(20),
                    border_radius=12,
                    bgcolor=LIGHT,
                    border=ft.Border.all(1, BORDER),
                    width=400,
                ),

                ft.Container(height=28),

                # Progress bar
                progress_bar,

                # Status
                status_text,

                ft.Container(height=12),

                # Botón principal
                ft.Button(
                    ref=action_btn,
                    content=ft.Text("Desinstalar" if installed else "Instalar", color=WHITE),
                    on_click=on_action,
                    width=400,
                    style=ft.ButtonStyle(
                        bgcolor=DANGER if installed else BRAND,
                        padding=ft.Padding.symmetric(horizontal=32, vertical=16),
                        shape=ft.RoundedRectangleBorder(radius=12),
                    ),
                ),

                ft.Container(height=16),

                # Nota
                ft.Text(
                    "Requiere Python 3.8+ instalado en el sistema",
                    size=11, color=GRAY, text_align=ft.TextAlign.CENTER,
                ),

            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=0),
            expand=True,
            padding=ft.Padding.symmetric(horizontal=60, vertical=0),
        )
    )


if __name__ == "__main__":
    ft.app(target=main)
