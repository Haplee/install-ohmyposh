# Oh My Posh — Instaladores Automatizados 🚀

[![Estado](https://img.shields.io/badge/Estado-Activo-success?style=for-the-badge)](https://github.com/Haplee/install-ohmyposh)
[![Plataformas](https://img.shields.io/badge/Plataformas-Windows%20%7C%20Linux-blue?style=for-the-badge)](#)
[![Sitio Web](https://img.shields.io/badge/Web-GitHub%20Pages-purple?style=for-the-badge&logo=github)](https://Haplee.github.io/install-ohmyposh)

Bienvenido a la solución integral para configurar **Oh My Posh** en tus terminales de manera 100% automática. Olvídate de configuraciones manuales complejas: estos scripts instalan el cliente, descargan la fuente correcta y configuran el perfil de tu terminal en cuestión de segundos.

---

## 📁 Estructura del Proyecto

Para mantener el repositorio limpio y organizado, los componentes están delimitados en sus respectivos directorios:

```text
install-ohmyposh/
├── linux/                      # 🐧 Scripts de instalación para Bash y Zsh
│   └── install_linux.sh        # Script Bash interactivo y seguro
├── windows/                    # 🪟 Instaladores y compiladores para PowerShell
│   ├── install_windows.py      # Lógica del instalador gráfico (Python)
│   └── compilar_windows.bat    # Automatización para crear el .exe
├── docs/                       # 🌐 Código fuente de la Landing Page (GitHub Pages)
│   ├── index.html              
│   └── styles.css              
├── references/                 # 📚 Documentación adicional y archivos originales
└── README.md                   # 📖 Este archivo
```

---

## ✨ Características Principales

* **Instalación de Cero a Cien**: No necesitas tener nada preinstalado más que tu terminal nativa.
* **Fuentes Incluidas**: Gestiona la descarga, instalación y registro de **MesloLGS NF**, la tipografía estándar recomendada para no ver caracteres rotos.
* **Despliegue Multiplataforma**: Scripts nativos que respetan las particularidades del sistema operativo.
* **Interfaz Visual (Windows)**: Un binario ejecutable con interfaz que solicita permisos de administrador automáticamente con UAC.
* **Tema Listo para Producción**: Inyecta el tema `clean-detailed` para empezar a trabajar de inmediato con información rica de git, entornos virtuales, etc.

---

## 🐧 Guía de Instalación en Linux

El script para Linux es compatible con distribuciones basadas en Debian/Ubuntu, Arch, Fedora, etc. Detecta dinámicamente si usas **Bash** o **Zsh** para modificar el archivo de configuración correcto (`~/.bashrc` o `~/.zshrc`).

### Pasos

1. Clona el repositorio e ingresa a la carpeta:
   ```bash
   git clone https://github.com/Haplee/install-ohmyposh.git
   cd install-ohmyposh/linux
   ```
2. Otorga permisos de ejecución al script:
   ```bash
   chmod +x install_linux.sh
   ```
3. Lánzalo y sigue el proceso:
   ```bash
   ./install_linux.sh
   ```
4. Recarga tu terminal para aplicar la nueva interfaz:
   ```bash
   source ~/.bashrc  # Cambia a ~/.zshrc si es tu caso
   ```

---

## 🪟 Guía de Instalación en Windows

Para Windows, el enfoque óptimo es generar un único archivo ejecutable (`.exe`) que puedas distribuir o ejecutar con doble clic.

### Requisitos Previos para compilar
- Tener instalado **Python 3**.
- (El script batch se encargará de instalar `pyinstaller` automáticamente).

### Pasos

1. Abre tu terminal y navega a la carpeta de Windows:
   ```powershell
   cd install-ohmyposh\windows
   ```
2. Ejecuta el compilador para empaquetar el script de Python:
   ```cmd
   .\compilar_windows.bat
   ```
3. Esto creará una nueva carpeta llamada `dist/`. Entra y ejecuta con doble clic el archivo **`OhMyPosh_Installer.exe`**.
4. Se abrirá una pequeña ventana visual indicando el progreso y te pedirá permisos de **Administrador**. Acéptalos (es imprescindible para instalar la tipografía en todo el sistema).
5. Tras el mensaje de finalización, **cierra todas tus ventanas de PowerShell** y vuelve a abrir una nueva para ver los cambios.

---

## ⚙️ Personalización Avanzada (Cambiar Diseño)

Si el tema `clean-detailed` no es de tu agrado, Oh My Posh dispone de decenas de temas diferentes. Para cambiarlo:

1. Visita la [galería oficial de temas de Oh My Posh](https://ohmyposh.dev/docs/themes).
2. Elige el nombre de tu tema favorito (p.ej: `aliens`).
3. Edita tu archivo de perfil y cambia la URL.
   * **Linux**: Modifica la última línea de tu `~/.bashrc` (o `~/.zshrc`).
   * **Windows**: Abre tu `$PROFILE` ejecutando `notepad $PROFILE` y edita la línea equivalente.

---

### ©️ Créditos
Desarrollado y mantenido por FranVi. Construido sobre las increíbles herramientas proporcionadas por [Jan De Dobbeleer](https://ohmyposh.dev/).
