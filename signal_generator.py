import numpy as np

def generate_sine(freq=5, fs=100, duration=1.0):
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    return np.sin(2 * np.pi * freq * t)

def generate_square(freq=5, fs=100, duration=1.0):
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    return np.sign(np.sin(2 * np.pi * freq * t))

def generate_noise(fs=100, duration=1.0):
    return np.random.randn(int(fs * duration))
