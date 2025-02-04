import time
import threading
import pygame

class Temporizador:
    def __init__(self, duracion, sonido, actualizar_ui):
        self.duracion = duracion  # Duración en segundos
        self.sonido = sonido  # Ruta del sonido de la alarma
        self.actualizar_ui = actualizar_ui
        self.en_ejecucion = False
        self.hilo = None

    def iniciar(self):
        if not self.en_ejecucion:
            print(f"Temporizador iniciando: {self.duracion} segundos")
            self.en_ejecucion = True
            self.hilo = threading.Thread(target=self._contar)
            self.hilo.start()

    def _contar(self):
        for i in range(self.duracion, 0, -1):
            self.actualizar_ui(i)  # Actualiza la UI en cada segundo
            print(f"Tiempo restante: {i} segundos")
            time.sleep(1)
        self.actualizar_ui(0)
        self.reproducir_sonido()
        print("Temporizador finalizado")
        self.en_ejecucion = False

    def reproducir_sonido(self):
        print(f"Reproduciendo sonido: {self.sonido}")
        pygame.mixer.init()
        pygame.mixer.music.load(self.sonido)
        pygame.mixer.music.play()