import multiprocessing
import threading
import queue
from modelo.audio_analyzer import AudioAnalyzer

class AudioController:
    def __init__(self):
        self.analyzer = None
        self.results_queue = multiprocessing.Queue()
        self.results = {}

    def load_audio(self, file_path):
        """ Carga el archivo de audio para su análisis. """
        self.analyzer = AudioAnalyzer(file_path)

    def analyze_audio(self, update_ui_callback):
        """ Inicia el análisis de audio en paralelo. """
        if not self.analyzer:
            return

        self.results["duration"] = self.analyzer.get_duration()
        self.results["peak_volume"] = self.analyzer.get_peak_volume()
        self.results["silence_ratio"] = self.analyzer.get_silence_ratio()

        # Procesos paralelos
        fft_process = multiprocessing.Process(target=self.analyzer.calculate_fft, args=(self.results_queue,))
        bpm_process = multiprocessing.Process(target=self.analyzer.calculate_bpm, args=(self.results_queue,))
        rms_process = multiprocessing.Process(target=self.analyzer.calculate_rms, args=(self.results_queue,))

        fft_process.start()
        bpm_process.start()
        rms_process.start()

        # Hilo para actualizar la interfaz sin bloquear la app
        threading.Thread(target=self._update_results, args=(update_ui_callback,), daemon=True).start()

    def _update_results(self, update_ui_callback):
        """ Recoge los resultados en segundo plano y actualiza la UI. """
        active_processes = 3
        while active_processes > 0:
            try:
                key, value = self.results_queue.get(timeout=1)
                self.results[key] = value
                update_ui_callback(self.results)
            except queue.Empty:
                pass
            active_processes -= 1
