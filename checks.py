import numpy as np

def check_clipping(signal, threshold=1.0):
    return np.any(np.abs(signal) > threshold)

def rms_level(signal):
    return np.sqrt(np.mean(signal ** 2))
