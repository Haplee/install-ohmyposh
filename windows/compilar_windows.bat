@echo off
echo ====================================================
echo   Compilador de instalador de Oh My Posh a EXE
echo ====================================================
echo.

echo Comprobando instalacion de Python e instalando PyInstaller si es necesario...
python -m pip install pypiwin32
python -m pip install pyinstaller

echo.
echo Compilando el script install_windows.py a un .exe standalone...
echo (Esto puede tardar unos segundos)

pyinstaller --noconfirm --onefile --windowed --uac-admin --name "OhMyPosh_Installer" "install_windows.py"

echo.
echo ====================================================
if exist "dist\OhMyPosh_Installer.exe" (
    echo [EXITO] Compilacion finalizada correctamente.
    echo         Encontraras el instalador en:
    echo         %~dp0dist\OhMyPosh_Installer.exe
) else (
    echo [ERROR] Ocurrio un problema durante la compilacion.
)
echo ====================================================
pause
