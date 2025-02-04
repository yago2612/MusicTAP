from modelo.temporizador import Temporizador
from tkinter import filedialog

class Controlador:
    def __init__(self, vista):
        self.vista = vista
        self.vista.asignar_controlador(self)
        self.sonido = "assets/alarma.mp3"  # Sonido por defecto
        self.temporizador = Temporizador(5, self.sonido, self.vista.actualizar_tiempo)  # 10 seg para pruebas

    def iniciar_temporizador(self):
        print("Botón Iniciar presionado")
        self.temporizador.iniciar()
        print("Temporizador iniciado")

    def seleccionar_sonido(self):
        archivo = filedialog.askopenfilename(filetypes=[("Archivos de audio", "*.mp3 *.wav")])
        if archivo:
            self.sonido = archivo
            self.temporizador.sonido = archivo
            print(f"Sonido seleccionado: {archivo}")