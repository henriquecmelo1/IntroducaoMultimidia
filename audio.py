import pygame, random
import pyaudio
import numpy as np
import scipy.fftpack
import time

WIDTH = 1200
HEIGHT = 600
SPEED = 10
GAME_SPEED = 10
GROUND_WIDTH = 2 * WIDTH
GROUND_HEIGHT = 30

def get_microphone_frequency():
    CHUNK = 1024  # Number of audio frames per buffer
    RATE = 44100  # Sampling rate (samples per second)

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True, frames_per_buffer=CHUNK)

    while True:
        data = stream.read(CHUNK)
        audio_array = np.frombuffer(data, dtype=np.int16)
        frequencies = scipy.fftpack.fftfreq(len(audio_array))
        freq_amplitudes = scipy.fftpack.fft(audio_array)
        dominant_frequency = abs(frequencies[np.argmax(np.abs(freq_amplitudes))])
        return dominant_frequency
        time.sleep(1)
    stream.stop_stream()
    stream.close()
    p.terminate()
