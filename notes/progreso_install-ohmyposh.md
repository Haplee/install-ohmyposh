# Registro de Progreso — install-ohmyposh

## [2026-03-08] — Primera versión (Scripts, GUI y Landing Page)

- **Qué se hizo**: 
  - Archivo `linux/install_linux.sh` para instalación en bash/zsh.
  - Archivo `windows/install_windows.py` y `windows/compilar_windows.bat` (GUI de Tkinter con autogestión de UAC y Winget).
  - Landing page con "glassmorphism" en `docs/index.html` y `docs/styles.css`.
  - Archivo `README.md` reescrito con árbol de directorios y badges dinámicos.
  - Cambio de alias en repositorio a `Haplee`.
- **Por qué se hizo**: Para proveer una automatización completa tipo "todo en uno" requerida.
- **Estado actual del proyecto**: Listo para pruebas. Linux validado como sintaxis correcta; Windows requiere validación manual de ejecución debido al uso de librerías nativas `winreg` y `ctypes`.
