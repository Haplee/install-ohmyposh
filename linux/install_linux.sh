#!/bin/bash

# Salir si hay algún error
set -e

# Colores para los mensajes
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

print_info() { echo -e "${BLUE}[INFO]${NC} $1"; }
print_success() { echo -e "${GREEN}[EXITO]${NC} $1"; }
print_warning() { echo -e "${YELLOW}[AVISO]${NC} $1"; }
print_error() { echo -e "${RED}[ERROR]${NC} $1"; }

# 1. Detectar el shell en uso
USER_SHELL=$(basename "$SHELL")
if [ "$USER_SHELL" = "bash" ]; then
    RC_FILE="$HOME/.bashrc"
    INIT_CMD="oh-my-posh init bash --config 'https://raw.githubusercontent.com/JanDeDobbeleer/oh-my-posh/main/themes/clean-detailed.omp.json'"
elif [ "$USER_SHELL" = "zsh" ]; then
    RC_FILE="$HOME/.zshrc"
    INIT_CMD="oh-my-posh init zsh --config 'https://raw.githubusercontent.com/JanDeDobbeleer/oh-my-posh/main/themes/clean-detailed.omp.json'"
else
    print_error "Shell no soportado: $USER_SHELL. Este script solo soporta bash o zsh."
    exit 1
fi

print_info "Shell detectado: $USER_SHELL. Archivo de configuración: $RC_FILE"

# 2. Comprobar si ya está instalado
if command -v oh-my-posh &> /dev/null || [ -f "$HOME/.local/bin/oh-my-posh" ]; then
    print_warning "Oh My Posh ya está instalado."
else
    # Instalar Oh My Posh
    print_info "Instalando Oh My Posh..."
    if ! curl -s https://ohmyposh.dev/install.sh | bash -s; then
        print_error "Error al descargar o ejecutar el script de instalación."
        exit 1
    fi
    print_success "Oh My Posh instalado correctamente en ~/.local/bin."
fi

# Añadir al PATH en la sesión actual para usarlo inmediatamente
export PATH=$PATH:$HOME/.local/bin

# 3. Instalación de la fuente
print_info "Instalando la fuente Meslo Nerd Font..."
if oh-my-posh font install meslo; then
    print_success "Fuente instalada correctamente."
else
    print_error "Ocurrió un error al instalar la fuente."
fi

# 4. Configurar el archivo rc (.bashrc o .zshrc)
print_info "Configurando $RC_FILE..."

# Crear o verificar que el archivo existe
if [ ! -f "$RC_FILE" ]; then
    touch "$RC_FILE"
fi

# Añadir al PATH si no está
if ! grep -q 'export PATH="$PATH:$HOME/.local/bin"' "$RC_FILE"; then
    echo -e '\n# Configuración de PATH para Oh My Posh' >> "$RC_FILE"
    echo 'export PATH="$PATH:$HOME/.local/bin"' >> "$RC_FILE"
fi

# Añadir la inicialización de oh-my-posh si no está
if ! grep -q "oh-my-posh init $USER_SHELL" "$RC_FILE"; then
    echo -e '\n# Inicializar Oh My Posh' >> "$RC_FILE"
    echo "eval \"\$($INIT_CMD)\"" >> "$RC_FILE"
    print_success "Oh My Posh añadido a $RC_FILE."
else
    print_warning "Oh My Posh ya estaba configurado en $RC_FILE."
fi

print_success "¡Instalación completada correctamente!"
print_info "Por favor, para aplicar los cambios en la terminal actual, ejecuta:"
print_info "source $RC_FILE"
print_info "(O simplemente abre una nueva pestaña/ventana de tu terminal bash/zsh)"
