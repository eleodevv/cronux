#!/bin/bash
# Cronux-CRX Uninstaller v0.1.0 Beta

echo "Cronux-CRX Uninstaller"
echo ""
echo "Esto eliminará:"
echo "  - El comando 'crx' del sistema"
echo "  - Todos los archivos de Cronux-CRX"
echo ""
echo "Nota: Tus proyectos NO serán eliminados"
echo ""
read -p "Continuar? (si/no): " confirm

if [ "$confirm" != "si" ]; then
    echo "Desinstalación cancelada"
    exit 0
fi

echo ""
echo "Desinstalando Cronux-CRX..."

# Eliminar archivos
sudo rm -rf /usr/local/cronux
sudo rm -f /usr/local/bin/crx

# Eliminar recibo del paquete
sudo pkgutil --forget com.cronux.crx 2>/dev/null || true

# Verificar
echo ""
if command -v crx &> /dev/null; then
    echo "El comando 'crx' aún está disponible"
    echo "Reinicia tu terminal para aplicar cambios"
else
    echo "Cronux-CRX desinstalado correctamente"
fi

echo ""
echo "Tus proyectos con carpetas .cronux NO fueron eliminados"
echo "Reinicia tu terminal para aplicar cambios"
echo ""