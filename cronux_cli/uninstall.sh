#!/bin/bash
# CRONUX-CRX CLI Uninstaller for Linux/macOS

set -e

INSTALL_DIR="/usr/local/cronux"
BIN_DIR="/usr/local/bin"

echo ""
echo "  Desinstalando CRONUX-CRX CLI..."

if [ -L "$BIN_DIR/cronux" ]; then
    sudo rm -f "$BIN_DIR/cronux"
fi

if [ -d "$INSTALL_DIR" ]; then
    sudo rm -rf "$INSTALL_DIR"
fi

echo "  ✓ CRONUX-CRX CLI desinstalado correctamente"
echo ""
