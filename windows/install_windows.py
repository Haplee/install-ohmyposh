import os
import sys
import ctypes
import urllib.request
import subprocess
import tkinter as tk
from tkinter import messagebox
import winreg
import shutil

# Constante para ocultar la ventana de consola en subprocess (sólo Windows)
CREATE_NO_WINDOW = 0x08000000

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    # Relanza el script pero como Administrador y muestra la ventana de UAC
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

class InstallerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Instalador Oh My Posh - FranVi")
        self.root.geometry("450x220")
        self.root.resizable(False, False)
        
        # Etiqueta de estado
        self.label = tk.Label(root, text="Iniciando instalación...", font=("Segoe UI", 11, "bold"))
        self.label.pack(pady=10)
        
        # Cuadro de texto para progreso
        self.progress_text = tk.Text(root, height=7, width=50, state=tk.DISABLED, font=("Consolas", 9), bg="#f4f4f4")
        self.progress_text.pack(pady=5, padx=10)
        
        # Procesar instalación después de que se cargue la GUI
        self.root.after(500, self.install_process)

    def log(self, message):
        self.label.config(text=message)
        self.progress_text.config(state=tk.NORMAL)
        self.progress_text.insert(tk.END, f"[>] {message}\n")
        self.progress_text.see(tk.END)
        self.progress_text.config(state=tk.DISABLED)
        self.root.update()

    def is_installed(self):
        try:
            # Comprueba si oh-my-posh es un comando reconocido en powershell
            result = subprocess.run(
                ["powershell", "-Command", "Get-Command oh-my-posh -ErrorAction SilentlyContinue"],
                capture_output=True, text=True, creationflags=CREATE_NO_WINDOW
            )
            return "oh-my-posh" in result.stdout.lower()
        except:
            return False

    def install_process(self):
        try:
            # 1. Instalar Oh My Posh
            if not self.is_installed():
                self.log("Instalando Oh My Posh mediante winget...")
                subprocess.run([
                    "winget", "install", "JanDeDobbeleer.OhMyPosh", 
                    "--accept-source-agreements", "--accept-package-agreements"
                ], check=True, creationflags=CREATE_NO_WINDOW)
            else:
                self.log("Oh My Posh ya está instalado. Omitiendo la descarga del CLI.")

            # 2. Descargar e Instalar Fuentes
            self.log("Preparando la instalación de fuentes...")
            self.install_fonts()

            # 3. Configurar PowerShell
            self.log("Configurando el perfil de PowerShell...")
            self.configure_profile()

            self.log("¡Instalación completada!")
            messagebox.showinfo(
                "Instalación Exitosa", 
                "Oh My Posh se ha instalado y configurado correctamente con el tema clean-detailed y la fuente Meslo.\n\n"
                "Importante: Por favor, reinicia tu terminal (cierra todas las ventanas de PowerShell y vuelve a abrirlas) para aplicar los cambios."
            )
            self.root.destroy()

        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error de instalación", f"Ocurrió un error al ejecutar un comando:\n{str(e)}")
            self.root.destroy()
        except Exception as e:
            messagebox.showerror("Error inesperado", f"Detalle:\n{str(e)}")
            self.root.destroy()

    def install_fonts(self):
        # Enlaces directos a los 4 estilos de la fuente MesloLGS NF
        fonts = {
            "MesloLGS NF Regular.ttf": "https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Regular.ttf",
            "MesloLGS NF Bold.ttf": "https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Bold.ttf",
            "MesloLGS NF Italic.ttf": "https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Italic.ttf",
            "MesloLGS NF Bold Italic.ttf": "https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Bold%20Italic.ttf"
        }
        
        fonts_dir = os.path.join(os.environ['WINDIR'], 'Fonts')
        
        for font_name, url in fonts.items():
            font_path = os.path.join(fonts_dir, font_name)
            
            # Si no está en el directorio Fonts de Windows, descargar e instalar
            if not os.path.exists(font_path):
                self.log(f"Descargando fuente: {font_name}...")
                temp_path = os.path.join(os.environ['TEMP'], font_name)
                
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req) as response, open(temp_path, 'wb') as out_file:
                    shutil.copyfileobj(response, out_file)
                
                self.log(f"Instalando fuente: {font_name} en el sistema...")
                shutil.copy(temp_path, font_path)
                
                # Registrar la fuente en el Registro de Windows
                try:
                    registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts", 0, winreg.KEY_SET_VALUE)
                    # El nombre en el registro suele requerir el sufijo "(TrueType)"
                    winreg.SetValueEx(registry_key, font_name.replace(".ttf", "") + " (TrueType)", 0, winreg.REG_SZ, font_name)
                    winreg.CloseKey(registry_key)
                except Exception as e:
                    self.log(f"Advertencia al registrar {font_name}: {e}")
                    
                # Cleanup temporal
                if os.path.exists(temp_path):
                    os.remove(temp_path)
            else:
                self.log(f"La fuente {font_name} ya está instalada.")

    def configure_profile(self):
        # Un script en cadena de PowerShell para verificar y modificar $PROFILE
        ps_command = r'''
        # Resolver ruta del perfil
        $ProfilePath = $PROFILE.CurrentUserCurrentHost
        if ([string]::IsNullOrEmpty($ProfilePath)) {
            $ProfilePath = "$HOME\Documents\PowerShell\Microsoft.PowerShell_profile.ps1"
        }
        
        $ProfileDir = Split-Path -Parent $ProfilePath
        
        # Crear directorios si no existen
        if (-not (Test-Path $ProfileDir)) {
            New-Item -ItemType Directory -Path $ProfileDir -Force | Out-Null
        }
        
        # Crear archivo profile si no existe
        if (-not (Test-Path $ProfilePath)) {
            New-Item -ItemType File -Path $ProfilePath -Force | Out-Null
        }
        
        $InitString = "oh-my-posh init pwsh --config 'https://raw.githubusercontent.com/JanDeDobbeleer/oh-my-posh/main/themes/clean-detailed.omp.json' | Invoke-Expression"
        
        $ProfileContent = Get-Content $ProfilePath -ErrorAction SilentlyContinue
        
        # Escribir solo si la cadena de oh-my-posh no está presente aún
        if ($ProfileContent -match "oh-my-posh init") {
            # Si hay algo de oh-my-posh, podemos reemplazarlo o dejarlo,
            # pero asumiremos aquí que si ya está el invoke, no añadimos otro.
            Write-Output "El perfil ya tiene configuración de Oh My Posh."
        } else {
            Add-Content -Path $ProfilePath -Value "`n# Configuración de Oh My Posh"
            Add-Content -Path $ProfilePath -Value $InitString
        }
        '''
        
        subprocess.run(["powershell", "-NoProfile", "-Command", ps_command], check=True, capture_output=True, creationflags=CREATE_NO_WINDOW)


if __name__ == "__main__":
    # Asegurarnos de que tenemos permisos de administrador primero (escalada de UAC)
    if not is_admin():
        # Llama a UAC, luego continuará la ejecución de este script con permisos y matará el proceso actual sin administrador
        run_as_admin()
        sys.exit()

    # Si llega aquí, significa que ya tiene permisos de administrador. 
    # Procedemos con la interfaz.
    root = tk.Tk()
    app = InstallerGUI(root)
    # Centrar la ventana
    root.eval('tk::PlaceWindow . center')
    # Evitar abrir consola no deseada si se ejecuta directamente con Python, 
    # se prefiere la ejecución del .exe generado con '--windowed'
    root.mainloop()
