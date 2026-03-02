@echo off
REM Cronux-CRX Uninstaller v0.1.0 Beta
REM Desinstala completamente Cronux-CRX del sistema Windows

setlocal enabledelayedexpansion

echo ========================================
echo   Cronux-CRX Uninstaller v0.1.0 Beta
echo ========================================
echo.

REM Verificar permisos de administrador
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo [ERROR] Este script requiere permisos de administrador
    echo Por favor, ejecuta como administrador
    echo.
    pause
    exit /b 1
)

echo [INFO] Permisos de administrador verificados
echo.

REM Confirmar desinstalacion
echo [ADVERTENCIA] Estas a punto de desinstalar Cronux-CRX
echo.
echo Esto eliminara:
echo   * El comando 'crx' del sistema
echo   * Todos los archivos de Cronux-CRX
echo   * Configuracion del PATH
echo.
echo [NOTA] Tus proyectos y versiones guardadas NO seran eliminados
echo.
set /p confirm="Escribe 'SI' para continuar: "

if /i not "%confirm%"=="SI" (
    echo [INFO] Desinstalacion cancelada
    pause
    exit /b 0
)

echo.
echo [INFO] Iniciando desinstalacion...
echo.

REM Ubicaciones de instalacion
set "INSTALL_DIRS[0]=%ProgramFiles%\Cronux-CRX"
set "INSTALL_DIRS[1]=%ProgramFiles(x86)%\Cronux-CRX"
set "INSTALL_DIRS[2]=%LOCALAPPDATA%\Cronux-CRX"
set "INSTALL_DIRS[3]=%LOCALAPPDATA%\cronux"
set "INSTALL_DIRS[4]=%APPDATA%\Cronux-CRX"

REM Archivos ejecutables
set "EXE_FILES[0]=%SystemRoot%\System32\crx.exe"
set "EXE_FILES[1]=%SystemRoot%\System32\crx.bat"
set "EXE_FILES[2]=%LOCALAPPDATA%\cronux\bin\crx.exe"
set "EXE_FILES[3]=%LOCALAPPDATA%\cronux\bin\crx.bat"

REM Eliminar directorios
echo [INFO] Eliminando directorios de instalacion...
for /l %%i in (0,1,4) do (
    if exist "!INSTALL_DIRS[%%i]!" (
        echo [INFO] Eliminando: !INSTALL_DIRS[%%i]!
        rmdir /s /q "!INSTALL_DIRS[%%i]!" 2>nul
        if exist "!INSTALL_DIRS[%%i]!" (
            echo [WARNING] No se pudo eliminar completamente: !INSTALL_DIRS[%%i]!
        ) else (
            echo [SUCCESS] Eliminado: !INSTALL_DIRS[%%i]!
        )
    )
)

REM Eliminar ejecutables
echo.
echo [INFO] Eliminando ejecutables...
for /l %%i in (0,1,3) do (
    if exist "!EXE_FILES[%%i]!" (
        echo [INFO] Eliminando: !EXE_FILES[%%i]!
        del /f /q "!EXE_FILES[%%i]!" 2>nul
        if exist "!EXE_FILES[%%i]!" (
            echo [WARNING] No se pudo eliminar: !EXE_FILES[%%i]!
        ) else (
            echo [SUCCESS] Eliminado: !EXE_FILES[%%i]!
        )
    )
)

REM Limpiar PATH del usuario
echo.
echo [INFO] Limpiando PATH del usuario...

REM Obtener PATH actual
for /f "tokens=2*" %%a in ('reg query "HKCU\Environment" /v PATH 2^>nul') do set "USER_PATH=%%b"

REM Eliminar entradas de Cronux del PATH
set "NEW_PATH=!USER_PATH!"
set "NEW_PATH=!NEW_PATH:;%ProgramFiles%\Cronux-CRX=!"
set "NEW_PATH=!NEW_PATH:;%LOCALAPPDATA%\cronux\bin=!"
set "NEW_PATH=!NEW_PATH:%ProgramFiles%\Cronux-CRX;=!"
set "NEW_PATH=!NEW_PATH:%LOCALAPPDATA%\cronux\bin;=!"

REM Actualizar PATH si cambio
if not "!USER_PATH!"=="!NEW_PATH!" (
    reg add "HKCU\Environment" /v PATH /t REG_EXPAND_SZ /d "!NEW_PATH!" /f >nul 2>&1
    if !errorLevel! equ 0 (
        echo [SUCCESS] PATH del usuario actualizado
    ) else (
        echo [WARNING] No se pudo actualizar el PATH automaticamente
    )
) else (
    echo [INFO] No se encontraron entradas de Cronux en el PATH
)

REM Limpiar PATH del sistema (requiere admin)
echo.
echo [INFO] Limpiando PATH del sistema...

for /f "tokens=2*" %%a in ('reg query "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v PATH 2^>nul') do set "SYSTEM_PATH=%%b"

set "NEW_SYSTEM_PATH=!SYSTEM_PATH!"
set "NEW_SYSTEM_PATH=!NEW_SYSTEM_PATH:;%ProgramFiles%\Cronux-CRX=!"
set "NEW_SYSTEM_PATH=!NEW_SYSTEM_PATH:%ProgramFiles%\Cronux-CRX;=!"

if not "!SYSTEM_PATH!"=="!NEW_SYSTEM_PATH!" (
    reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v PATH /t REG_EXPAND_SZ /d "!NEW_SYSTEM_PATH!" /f >nul 2>&1
    if !errorLevel! equ 0 (
        echo [SUCCESS] PATH del sistema actualizado
    ) else (
        echo [WARNING] No se pudo actualizar el PATH del sistema
    )
) else (
    echo [INFO] No se encontraron entradas de Cronux en el PATH del sistema
)

REM Eliminar entradas del registro
echo.
echo [INFO] Limpiando registro de Windows...

reg delete "HKCU\Software\Cronux-CRX" /f >nul 2>&1
reg delete "HKLM\Software\Cronux-CRX" /f >nul 2>&1
reg delete "HKLM\Software\Microsoft\Windows\CurrentVersion\Uninstall\Cronux-CRX" /f >nul 2>&1

echo [SUCCESS] Registro limpiado

REM Verificar desinstalacion
echo.
echo [INFO] Verificando desinstalacion...

where crx >nul 2>&1
if %errorLevel% equ 0 (
    echo [WARNING] El comando 'crx' todavia esta disponible
    echo [WARNING] Puede que necesites reiniciar tu terminal o computadora
) else (
    echo [SUCCESS] El comando 'crx' fue eliminado correctamente
)

REM Resumen
echo.
echo ========================================
echo   Desinstalacion Completada
echo ========================================
echo.
echo [SUCCESS] Cronux-CRX ha sido desinstalado del sistema
echo.
echo Notas importantes:
echo   * Tus proyectos con carpetas .cronux NO fueron eliminados
echo   * Puedes eliminarlos manualmente si lo deseas
echo   * Reinicia tu terminal o computadora para aplicar cambios
echo.
echo Nos extranaras? :^(
echo Reinstala cuando quieras desde: https://cronux.dev
echo.

pause