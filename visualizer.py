import sounddevice as sd
import numpy as np

def print_sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*9
    if volume_norm < 3:
        volume_norm = 0
    print ((int(volume_norm)) * "|" * 2)
with sd.Stream(callback=print_sound):
    sd.sleep(1000000000)
