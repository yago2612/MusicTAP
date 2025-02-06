import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class AudioApp:
    def __init__(self, root):
        self.controller = AudioController()

        self.root = root
        self.root.title("Timer Time - Análisis de Audio")
        self.root.geometry("760x480")
        
        # Creando el canvas para personalizar la interfaz
        self.canvas = tk.Canvas(root, width=760, height=480)
        self.canvas.pack()

        # Fondo de la ventana (puedes cambiar esta imagen por cualquier archivo)
        self.canvas.create_rectangle(0, 0, 500, 400, fill="#E0F7FA")  # Fondo azul claro
        self.canvas.create_text(250, 50, text="Seleccione un archivo de audio", font=("Helvetica", 16, "bold"), fill="black")
        
        # Crear un botón cargador con imágenes o personalizado
        self.load_button = tk.Button(root, text="Cargar Audio", command=self.load_audio, font=("Helvetica", 12), bg="#4CAF50", fg="white", relief="solid")
        self.canvas.create_window(250, 150, window=self.load_button)

        # Crear un botón para analizar
        self.analyze_button = tk.Button(root, text="Analizar Audio", command=self.analyze_audio, font=("Helvetica", 12), bg="#FFC107", fg="black", relief="solid")
        self.canvas.create_window(250, 200, window=self.analyze_button)

        # Etiqueta para mostrar resultados
        self.result_label = tk.Label(root, text="Resultados:", font=("Helvetica", 14), fg="black")
        self.canvas.create_window(250, 250, window=self.result_label)

        # Caja de texto para resultados
        self.results_text = tk.Text(root, height=10, width=40, font=("Helvetica", 12))
        self.canvas.create_window(250, 300, window=self.results_text)

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

class AudioController:
    def load_audio(self, file_path):
        # Aquí debes añadir la lógica para cargar el audio
        print(f"Audio cargado desde {file_path}")

    def analyze_audio(self, callback):
        # Aquí añades el código de análisis y llamas al callback con los resultados
        results = {
            "Duración": "3 min 45 seg",
            "Volumen Pico": "0.96",
            "Frecuencia Dominante": "92 Hz",
            "BPM": "108",
        }
        callback(results)

# Configuración y ejecución de la ventana
if __name__ == "__main__":
    root = tk.Tk()
    app = AudioApp(root)
    root.mainloop()
