import numpy as np
import librosa
from scipy.fftpack import fft
import multiprocessing

class AudioAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data, self.sr = librosa.load(file_path, sr=None)  # Cargar audio
        self.results = {}

    def get_duration(self):
        """ Retorna la duración total del audio en segundos. """
        return librosa.get_duration(y=self.data, sr=self.sr)

    def get_peak_volume(self):
        """ Retorna el pico de volumen máximo del audio. """
        return np.max(np.abs(self.data))

    def get_silence_ratio(self, threshold=0.01):
        """ Retorna la proporción de silencio en el audio. """
        return np.sum(np.abs(self.data) < threshold) / len(self.data)

    def calculate_fft(self, queue):
        """ Calcula la frecuencia dominante usando FFT y la envía a la cola. """
        N = len(self.data)
        fft_values = np.abs(fft(self.data))[:N // 2]
        freqs = np.fft.fftfreq(N, 1 / self.sr)[:N // 2]
        dominant_freq = freqs[np.argmax(fft_values)]
        queue.put(("dominant_freq", dominant_freq))

    def calculate_bpm(self, queue):
        """ Calcula los BPM (tempo) y los envía a la cola. """
        onset_env = librosa.onset.onset_strength(y=self.data, sr=self.sr)
        tempo, _ = librosa.beat.beat_track(onset_envelope=onset_env, sr=self.sr)
        queue.put(("bpm", tempo))

    def calculate_rms(self, queue):
        """ Calcula la energía RMS y la envía a la cola. """
        rms_energy = np.sqrt(np.mean(self.data ** 2))
        queue.put(("rms_energy", rms_energy))
