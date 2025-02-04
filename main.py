
import tkinter as tk
from vista.audio_app import AudioApp

if __name__ == "__main__":
    root = tk.Tk()
    app = AudioApp(root)
    root.mainloop()

"""
 5. Cómo Hacerlo Portable
Para distribuir la aplicación como un ejecutable en Windows:

Instala PyInstaller:

sh
Copiar
Editar
pip install pyinstaller
Genera el ejecutable:

sh
Copiar
Editar
pyinstaller --onefile --windowed --add-data "assets/alarma.mp3;assets/" main.py
--onefile: Genera un solo archivo ejecutable.
--windowed: Evita que aparezca la consola de terminal.
--add-data: Incluye archivos adicionales como el sonido de la alarma.
El ejecutable estará en dist/main.exe. Puedes renombrarlo a TimerTime.exe y enviarlo.
"""