import tkinter as tk
from tkinter import filedialog

class Vista:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer Time")
        self.root.geometry("760x480")
        self.root.overrideredirect(True)
        
        self.label = tk.Label(root, text="Temporizador de 1 minuto", font=("Arial", 12))
        self.label.pack(pady=10)

        self.tiempo_label = tk.Label(root, text="00:00", font=("Arial", 20))
        self.tiempo_label.pack(pady=10)

        self.boton_iniciar = tk.Button(root, text="Iniciar", font=("Arial", 12), command=None)
        self.boton_iniciar.pack(pady=10)

        self.boton_seleccionar_sonido = tk.Button(root, text="Seleccionar Sonido", font=("Arial", 10), command=None)
        self.boton_seleccionar_sonido.pack(pady=10)

    def asignar_controlador(self, controlador):
        self.boton_iniciar.config(command=controlador.iniciar_temporizador)
        self.boton_seleccionar_sonido.config(command=controlador.seleccionar_sonido)

    def actualizar_tiempo(self, segundos_restantes):
        minutos = segundos_restantes // 60
        segundos = segundos_restantes % 60
        self.tiempo_label.config(text=f"{minutos:02}:{segundos:02}")
        self.root.update()  # Refresca la interfaz