# encoding: utf-8 
# usando python 3
# Afinação - Alberto toca violão e é programador. 
# Precisando afinar o violão e sem diapasão por perto, 
# resolveu fazer um programa para ajudá-lo. 
# O que ele queria era a nota Lá soando sem parar até que ele conseguisse afinar a 
# respectiva corda do violão; as demais cordas ele poderia afinar com base na primeira. 
# Escreva um programa que faz soar no alto-falante do computador a nota Lá (440 Hz) 
# e só para quando for pressionada alguma tecla.

import numpy as np
import simpleaudio as sa

frequency = 440  # Our played note will be 440 Hz
fs = 44100  # 44100 samples per second
seconds = 3  # Note duration of 3 seconds

# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
t = np.linspace(0, seconds, seconds * fs, False)

# Generate a 440 Hz sine wave
note = np.sin(frequency * t * 2 * np.pi)

# Ensure that highest value is in 16-bit range
audio = note * (2**15 - 1) / np.max(np.abs(note))
# Convert to 16-bit data
audio = audio.astype(np.int16)

# Start playback
play_obj = sa.play_buffer(audio, 1, 2, fs)

# Wait for playback to finish before exiting
play_obj.wait_done()