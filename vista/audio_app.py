import tkinter as tk
from tkinter import filedialog
from controlador.audio_controller import AudioController

class AudioApp:
    def __init__(self, root):
        self.controller = AudioController()

        self.root = root
        self.root.title("Timer Time - Análisis de Audio")
        self.root.geometry("500x300")

        self.label = tk.Label(root, text="Seleccione un archivo de audio:")
        self.label.pack()

        self.load_button = tk.Button(root, text="Cargar Audio", command=self.load_audio)
        self.load_button.pack()

        self.analyze_button = tk.Button(root, text="Analizar Audio", command=self.analyze_audio)
        self.analyze_button.pack()

        self.result_label = tk.Label(root, text="Resultados:")
        self.result_label.pack()

        self.results_text = tk.Text(root, height=10, width=50)
        self.results_text.pack()

    def load_audio(self):
        """ Abre un diálogo para seleccionar un archivo de audio. """
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav *.mp3")])
        if file_path:
            self.controller.load_audio(file_path)

    def analyze_audio(self):
        """ Inicia el análisis de audio. """
        self.results_text.delete("1.0", tk.END)
        self.controller.analyze_audio(self.update_results)

    def update_results(self, results):
        """ Muestra los resultados del análisis en la interfaz. """
        self.results_text.delete("1.0", tk.END)
        for key, value in results.items():
            self.results_text.insert(tk.END, f"{key}: {value}\n")
