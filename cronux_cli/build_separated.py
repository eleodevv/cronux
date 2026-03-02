#!/usr/bin/env python3
"""
Build System Separado para Cronux-CRX
Genera dos paquetes .deb independientes:
- cronux-crx-cli: Interfaz de línea de comandos
- cronux-crx-gui: Interfaz gráfica
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

class SeparatedBuilder:
    def __init__(self):
        self.project_root = Path(__file__).parent
        self.gui_file = self.project_root / "cronux_gui_v3.py"
        self.assets_dir = self.project_root / "assets"
        self.cli_dir = self.project_root / "cli"
        self.dist_dir = self.project_root / "dist"
        self.build_dir = self.project_root / "build"
        self.version = "0.1.0"
        
    def check_pyinstaller(self):
        """Verifica que PyInstaller esté instalado"""
        try:
            result = subprocess.run(
                ["pyinstaller", "--version"],
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                print(f"✓ PyInstaller instalado: {result.stdout.strip()}")
                return True
            return False
        except FileNotFoundError:
            print("✗ PyInstaller no está instalado")
            print("  Instala con: pip install pyinstaller")
            return False
    
    def build_cli_deb(self):
        """Construye el paquete .deb solo para CLI"""
        print("\n" + "=" * 60)
        print("Building CLI .deb Package")
        print("=" * 60)
        
        # Crear estructura del .deb
        deb_root = self.build_dir / "cli" / f"cronux-crx-cli_{self.version}"
        bin_dir = deb_root / "usr" / "local" / "bin"
        cronux_dir = deb_root / "usr" / "local" / "cronux"
        debian_dir = deb_root / "DEBIAN"
        
        # Crear directorios
        bin_dir.mkdir(parents=True, exist_ok=True)
        cronux_dir.mkdir(parents=True, exist_ok=True)
        debian_dir.mkdir(parents=True, exist_ok=True)
        
        # Copiar archivos CLI a /usr/local/cronux
        for item in self.cli_dir.iterdir():
            if item.is_file():
                shutil.copy(item, cronux_dir / item.name)
            elif item.is_dir() and item.name != "__pycache__":
                shutil.copytree(item, cronux_dir / item.name, dirs_exist_ok=True)
        
        # Copiar script de desinstalación a /usr/local/cronux
        uninstall_script = self.project_root / "uninstall.sh"
        if uninstall_script.exists():
            shutil.copy(uninstall_script, cronux_dir / "uninstall.sh")
            os.chmod(cronux_dir / "uninstall.sh", 0o755)
            print("✓ Script uninstall.sh copiado a /usr/local/cronux")
        
        print("✓ Archivos CLI copiados")
        
        # Crear launcher script en /usr/local/bin
        launcher = bin_dir / "crx"
        launcher_content = """#!/bin/bash
python3 /usr/local/cronux/cronux_cli.py "$@"
"""
        with open(launcher, "w") as f:
            f.write(launcher_content)
        os.chmod(launcher, 0o755)
        print("✓ Launcher 'crx' creado")
        
        # Crear archivo control
        control_content = f"""Package: cronux-crx-cli
Version: {self.version}
Section: utils
Priority: optional
Architecture: all
Depends: python3 (>= 3.6)
Maintainer: Cronux Team <support@cronux.com>
Description: Cronux-CRX CLI - Sistema de Control de Versiones
 Interfaz de línea de comandos para control de versiones local.
 .
 Comandos disponibles:
  - crx crear <nombre>     : Crear nuevo proyecto
  - crx guardar <mensaje>  : Guardar versión
  - crx restaurar <version>: Restaurar versión
  - crx historial          : Ver historial
  - crx info               : Ver información del proyecto
"""
        with open(debian_dir / "control", "w") as f:
            f.write(control_content)
        print("✓ Archivo control creado")
        
        # Crear script postinst
        postinst_content = f"""#!/bin/bash
set -e
echo ""
echo "╔════════════════════════════════════════════════════════╗"
echo "║  Cronux-CRX CLI v{self.version} instalado correctamente  ║"
echo "╚════════════════════════════════════════════════════════╝"
echo ""
echo "Comandos disponibles:"
echo "  crx crear <nombre>      - Crear nuevo proyecto"
echo "  crx guardar <mensaje>   - Guardar versión"
echo "  crx restaurar <version> - Restaurar versión"
echo "  crx historial           - Ver historial"
echo "  crx info                - Ver información"
echo "  crx --help              - Ver ayuda completa"
echo ""
exit 0
"""
        postinst_file = debian_dir / "postinst"
        with open(postinst_file, "w") as f:
            f.write(postinst_content)
        os.chmod(postinst_file, 0o755)
        print("✓ Script postinst creado")
        
        # Construir .deb
        deb_output = self.dist_dir / f"cronux-crx-cli_{self.version}_all.deb"
        self.dist_dir.mkdir(exist_ok=True)
        
        cmd = ["dpkg-deb", "--build", str(deb_root), str(deb_output)]
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("\n" + "=" * 60)
            print("✓ CLI .deb creado exitosamente")
            print("=" * 60)
            print(f"\n📦 Archivo generado:")
            print(f"   {deb_output}")
            print(f"\n💡 Para instalar:")
            print(f"   sudo dpkg -i {deb_output}")
            print(f"\n💡 Para usar:")
            print(f"   crx --help")
            return True
        else:
            print(f"✗ Error al crear CLI .deb: {result.stderr}")
            return False
    
    def build_gui_executable(self):
        """Construye el ejecutable GUI con PyInstaller"""
        print("\n" + "=" * 60)
        print("Building GUI Executable")
        print("=" * 60)
        
        if not self.gui_file.exists():
            print(f"✗ GUI file not found: {self.gui_file}")
            return False
        
        # Usar cronux_cli.png como icono
        icon_file = self.assets_dir / "cronux_cli.png"
        
        # Limpiar build anterior de GUI
        gui_dist = self.dist_dir / "gui"
        if gui_dist.exists():
            shutil.rmtree(gui_dist)
        
        # Crear directorios necesarios para PyInstaller
        gui_work = self.build_dir / "gui_work"
        gui_dist.mkdir(parents=True, exist_ok=True)
        gui_work.mkdir(parents=True, exist_ok=True)
        self.build_dir.mkdir(parents=True, exist_ok=True)
        
        try:
            # Comando PyInstaller
            cmd = [
                "pyinstaller",
                "--name=cronux-crx-gui",
                "--onefile",
                "--windowed",
                f"--add-data={self.assets_dir}:assets",
                f"--add-data={self.cli_dir}:cli",
                f"--distpath={gui_dist}",
                f"--workpath={gui_work}",
                f"--specpath={self.build_dir}",
            ]
            
            # Agregar icono
            if icon_file.exists():
                cmd.append(f"--icon={icon_file}")
                print(f"✓ Usando icono: {icon_file.name}")
            
            cmd.append(str(self.gui_file))
            
            print(f"\nEjecutando PyInstaller...")
            print("Esto puede tardar varios minutos...")
            print("")
            
            result = subprocess.run(
                cmd,
                cwd=str(self.project_root),
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                exe_file = gui_dist / "cronux-crx-gui"
                if exe_file.exists():
                    print("✓ Ejecutable GUI creado")
                    return True
                else:
                    print("✗ Ejecutable no encontrado")
                    return False
            else:
                print(f"✗ Error en PyInstaller:")
                print(result.stderr)
                return False
                
        except Exception as e:
            print(f"✗ Error: {e}")
            return False
    
    def build_gui_deb(self):
        """Construye el paquete .deb para GUI"""
        print("\n" + "=" * 60)
        print("Building GUI .deb Package")
        print("=" * 60)
        
        exe_file = self.dist_dir / "gui" / "cronux-crx-gui"
        if not exe_file.exists():
            print("✗ Ejecutable GUI no encontrado")
            return False
        
        # Crear estructura del .deb
        deb_root = self.build_dir / "gui_deb" / f"cronux-crx-gui_{self.version}"
        bin_dir = deb_root / "usr" / "local" / "bin"
        app_dir = deb_root / "usr" / "share" / "applications"
        icon_dir = deb_root / "usr" / "share" / "icons" / "hicolor" / "256x256" / "apps"
        pixmaps_dir = deb_root / "usr" / "share" / "pixmaps"
        doc_dir = deb_root / "usr" / "share" / "doc" / "cronux-crx-gui"
        debian_dir = deb_root / "DEBIAN"
        
        # Crear directorios
        bin_dir.mkdir(parents=True, exist_ok=True)
        app_dir.mkdir(parents=True, exist_ok=True)
        icon_dir.mkdir(parents=True, exist_ok=True)
        pixmaps_dir.mkdir(parents=True, exist_ok=True)
        doc_dir.mkdir(parents=True, exist_ok=True)
        debian_dir.mkdir(parents=True, exist_ok=True)
        
        # Crear directorio para metadatos AppStream
        metainfo_dir = deb_root / "usr" / "share" / "metainfo"
        metainfo_dir.mkdir(parents=True, exist_ok=True)
        
        # Copiar ejecutable
        shutil.copy(exe_file, bin_dir / "cronux-crx-gui")
        os.chmod(bin_dir / "cronux-crx-gui", 0o755)
        print("✓ Ejecutable copiado")
        
        # Copiar icono cronux_cli.png
        icon_png = self.assets_dir / "cronux_cli.png"
        if icon_png.exists():
            shutil.copy(icon_png, icon_dir / "cronux-crx.png")
            shutil.copy(icon_png, pixmaps_dir / "cronux-crx.png")
            print(f"✓ Icono copiado: {icon_png.name}")
        
        # Copiar imagen de ejemplo para el instalador
        # Los gestores de paquetes buscan screenshots en ubicaciones específicas
        ejemplo_png = self.assets_dir / "ejemplo.png"
        if ejemplo_png.exists():
            # Copiar a doc
            shutil.copy(ejemplo_png, doc_dir / "screenshot.png")
            # También copiar a pixmaps para que sea más accesible
            shutil.copy(ejemplo_png, pixmaps_dir / "cronux-crx-screenshot.png")
            print(f"✓ Imagen de ejemplo copiada")
        
        # Crear archivo copyright (requerido para paquetes Debian)
        copyright_content = """Format: https://www.debian.org/doc/packaging-manuals/copyright-format/1.0/
Upstream-Name: cronux-crx-gui
Source: https://github.com/cronux/cronux-crx

Files: *
Copyright: 2024 Cronux Team
License: MIT
"""
        with open(doc_dir / "copyright", "w") as f:
            f.write(copyright_content)
        print("✓ Archivo copyright creado")
        
        # Crear archivo AppStream metadata para mostrar capturas
        appstream_content = """<?xml version="1.0" encoding="UTF-8"?>
<component type="desktop-application">
  <id>com.cronux.crx</id>
  <metadata_license>MIT</metadata_license>
  <project_license>MIT</project_license>
  <name>Cronux-CRX</name>
  <summary>Sistema de Control de Versiones Local</summary>
  <description>
    <p>
      Cronux-CRX es una interfaz gráfica moderna y minimalista para control de versiones local.
    </p>
    <p>Características principales:</p>
    <ul>
      <li>Gestión visual de proyectos y versiones</li>
      <li>Comparación de versiones</li>
      <li>Restauración de versiones</li>
      <li>Importación y exportación de proyectos</li>
      <li>Interfaz intuitiva y fácil de usar</li>
    </ul>
  </description>
  <launchable type="desktop-id">cronux-crx.desktop</launchable>
  <screenshots>
    <screenshot type="default">
      <image>file:///usr/share/pixmaps/cronux-crx-screenshot.png</image>
      <caption>Interfaz principal de Cronux-CRX</caption>
    </screenshot>
  </screenshots>
  <url type="homepage">https://cronux.com</url>
  <provides>
    <binary>cronux-crx-gui</binary>
  </provides>
  <categories>
    <category>Development</category>
    <category>Utility</category>
  </categories>
  <keywords>
    <keyword>version</keyword>
    <keyword>control</keyword>
    <keyword>git</keyword>
    <keyword>backup</keyword>
  </keywords>
  <releases>
    <release version="{self.version}" date="2024-02-27">
      <description>
        <p>Primera versión estable</p>
      </description>
    </release>
  </releases>
</component>
"""
        with open(metainfo_dir / "com.cronux.crx.appdata.xml", "w") as f:
            f.write(appstream_content)
        print("✓ Archivo AppStream metadata creado")
        
        # Crear archivo .desktop con StartupWMClass
        desktop_content = """[Desktop Entry]
Name=Cronux-CRX
Comment=Sistema de Control de Versiones Local - Interfaz Gráfica
Exec=/usr/local/bin/cronux-crx-gui
Icon=cronux-crx
Terminal=false
Type=Application
Categories=Development;Utility;VersionControl;
Keywords=version;control;git;backup;
StartupWMClass=cronux-crx-gui
StartupNotify=true
"""
        with open(app_dir / "cronux-crx.desktop", "w") as f:
            f.write(desktop_content)
        print("✓ Archivo .desktop creado (con StartupWMClass)")
        
        # Crear archivo control
        control_content = f"""Package: cronux-crx-gui
Version: {self.version}
Section: utils
Priority: optional
Architecture: amd64
Suggests: cronux-crx-cli
Maintainer: Cronux Team <support@cronux.com>
Description: Cronux-CRX GUI - Sistema de Control de Versiones
 Interfaz gráfica para control de versiones local.
 .
 Características:
  - Interfaz gráfica moderna y minimalista
  - Gestión visual de proyectos y versiones
  - Comparación de versiones
  - Restauración de versiones
  - Importación/exportación de proyectos
 .
 Nota: Puede funcionar de forma independiente o junto con cronux-crx-cli
"""
        with open(debian_dir / "control", "w") as f:
            f.write(control_content)
        print("✓ Archivo control creado")
        
        # Crear script postinst
        postinst_content = f"""#!/bin/bash
set -e
echo ""
echo "╔════════════════════════════════════════════════════════╗"
echo "║  Cronux-CRX GUI v{self.version} instalado correctamente  ║"
echo "╚════════════════════════════════════════════════════════╝"
echo ""
echo "Formas de ejecutar:"
echo "  1. Busca 'Cronux-CRX' en el menú de aplicaciones"
echo "  2. Ejecuta: cronux-crx-gui"
echo ""
echo "Sugerencia: Instala también cronux-crx-cli para usar"
echo "            el comando 'crx' desde la terminal"
echo ""
exit 0
"""
        postinst_file = debian_dir / "postinst"
        with open(postinst_file, "w") as f:
            f.write(postinst_content)
        os.chmod(postinst_file, 0o755)
        print("✓ Script postinst creado")
        
        # Construir .deb
        deb_output = self.dist_dir / f"cronux-crx-gui_{self.version}_amd64.deb"
        cmd = ["dpkg-deb", "--build", str(deb_root), str(deb_output)]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print("\n" + "=" * 60)
            print("✓ GUI .deb creado exitosamente")
            print("=" * 60)
            print(f"\n📦 Archivo generado:")
            print(f"   {deb_output}")
            print(f"\n💡 Para instalar:")
            print(f"   sudo dpkg -i {deb_output}")
            print(f"\n💡 Para ejecutar:")
            print(f"   cronux-crx-gui")
            print(f"   (o busca 'Cronux-CRX' en el menú)")
            return True
        else:
            print(f"✗ Error al crear GUI .deb: {result.stderr}")
            return False
    
    def build_all(self):
        """Construye ambos paquetes"""
        print("\n" + "=" * 60)
        print(f"Cronux-CRX v{self.version} - Build Separado")
        print("=" * 60)
        print("\nConstruyendo dos paquetes independientes:")
        print("  1. cronux-crx-cli - Interfaz de línea de comandos")
        print("  2. cronux-crx-gui - Interfaz gráfica")
        print("")
        
        results = {}
        
        # Build CLI
        results['CLI .deb'] = self.build_cli_deb()
        
        # Build GUI
        if self.build_gui_executable():
            results['GUI .deb'] = self.build_gui_deb()
        else:
            results['GUI .deb'] = False
        
        # Resumen
        print("\n" + "=" * 60)
        print("Resumen del Build:")
        print("=" * 60)
        for name, success in results.items():
            status = "✓ SUCCESS" if success else "✗ FAILED"
            print(f"  {name:20} {status}")
        
        print(f"\n📦 Paquetes generados en: {self.dist_dir}")
        print("\nPaquetes:")
        print(f"  • cronux-crx-cli_{self.version}_all.deb")
        print(f"  • cronux-crx-gui_{self.version}_amd64.deb")
        
        print("\nInstalación:")
        print("  # Solo CLI:")
        print(f"  sudo dpkg -i {self.dist_dir}/cronux-crx-cli_{self.version}_all.deb")
        print("")
        print("  # Solo GUI:")
        print(f"  sudo dpkg -i {self.dist_dir}/cronux-crx-gui_{self.version}_amd64.deb")
        print("")
        print("  # Ambos (recomendado):")
        print(f"  sudo dpkg -i {self.dist_dir}/cronux-crx-*.deb")
        
        print("\n" + "=" * 60)

def main():
    builder = SeparatedBuilder()
    
    # Verificar PyInstaller
    if not builder.check_pyinstaller():
        print("\nInstala PyInstaller:")
        print("  pip install pyinstaller")
        sys.exit(1)
    
    # Si se pasa argumento
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        if arg == "cli":
            builder.build_cli_deb()
        elif arg == "gui":
            if builder.build_gui_executable():
                builder.build_gui_deb()
        elif arg == "all":
            builder.build_all()
        else:
            print(f"Argumento desconocido: {arg}")
            print("Uso: python build_separated.py [cli|gui|all]")
            sys.exit(1)
    else:
        # Build ambos por defecto
        builder.build_all()

if __name__ == "__main__":
    main()
