# CRONUX-CRX CLI Uninstaller for Windows
# Usage: irm https://raw.githubusercontent.com/eleodevv/CRONUX-CRX/main/cronux_cli/uninstall.ps1 | iex

$ErrorActionPreference = "Stop"

$INSTALL_DIR = "$env:ProgramFiles\Cronux-CRX"

# Colors
function Write-Color {
    param([string]$Text, [string]$Color = "White")
    Write-Host $Text -ForegroundColor $Color
}

Write-Host ""
Write-Color "CRONUX-CRX CLI - Desinstalador" "Cyan"
Write-Host ""

# Verificar permisos de administrador
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if (-not $isAdmin) {
    Write-Color "✗ Este script requiere permisos de administrador" "Red"
    Write-Color "  Ejecuta PowerShell como Administrador y vuelve a intentar" "Yellow"
    exit 1
}

# Verificar si está instalado
if (-not (Test-Path $INSTALL_DIR)) {
    Write-Color "✗ CRONUX-CRX CLI no está instalado" "Yellow"
    exit 0
}

Write-Color "  → Eliminando archivos..." "Gray"
Remove-Item -Path $INSTALL_DIR -Recurse -Force -ErrorAction SilentlyContinue

# Remover del PATH
Write-Color "  → Removiendo del PATH..." "Gray"
$currentPath = [Environment]::GetEnvironmentVariable("Path", "Machine")
if ($currentPath -like "*$INSTALL_DIR*") {
    $newPath = ($currentPath -split ';' | Where-Object { $_ -ne $INSTALL_DIR }) -join ';'
    [Environment]::SetEnvironmentVariable("Path", $newPath, "Machine")
    Write-Color "  ✓ Removido del PATH" "Green"
}

Write-Host ""
Write-Color "✓ CRONUX-CRX CLI desinstalado correctamente" "Green"
Write-Host ""
