# Configuración de Oh My Posh — FranVi

## Sistema
- **OS:** Ubuntu (usuario: `franvi`, equipo: `FranVi-Victus`)
- **Shell:** Bash
- **Oh My Posh versión:** 29.7.1

---

## Instalación
Instalado mediante el script oficial:
```bash
curl -s https://ohmyposh.dev/install.sh | bash -s
```
Binario ubicado en: `~/.local/bin/oh-my-posh` 

---

## Configuración en ~/.bashrc
Añadir al final del archivo `/home/franvi/.bashrc`:

```bash
export PATH="$PATH:$HOME/.local/bin"
eval "$(oh-my-posh init bash --config 'https://raw.githubusercontent.com/JanDeDobbeleer/oh-my-posh/main/themes/clean-detailed.omp.json')"
```

Para recargar:
```bash
source ~/.bashrc
```

---

## Tema activo
**clean-detailed**
- URL: `https://raw.githubusercontent.com/JanDeDobbeleer/oh-my-posh/main/themes/clean-detailed.omp.json`
- Muestra: directorio actual, rama Git, timestamp y tiempo de ejecución en dos líneas.

Otros temas probados:
- `wholespace`

Explorar más temas: https://ohmyposh.dev/docs/themes

---

## Fuente
- **Fuente instalada:** MesloLGS NF (Nerd Font)
- Instalada con: `oh-my-posh font install meslo`
- Configurada en **GNOME Terminal** → Preferencias → Perfil "Sin nombre" → Tipografía personalizada → **MesloLGS NF**

Para instalar otras fuentes:
```bash
oh-my-posh font install          # lista interactiva
oh-my-posh font install firacode # ejemplo
```

---

## Cambiar de tema
Editar `~/.bashrc` y cambiar la URL del tema en la línea `eval`:
```bash
eval "$(oh-my-posh init bash --config 'URL_DEL_TEMA')"
```
Luego: `source ~/.bashrc`

---

## Notas adicionales
- El usuario `root` tiene la shell configurada en `/bin/bash` (corregido durante la instalación).
- zsh fue eliminado del sistema (`sudo apt remove --purge zsh`).