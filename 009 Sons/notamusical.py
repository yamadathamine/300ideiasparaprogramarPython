# encoding: utf-8 
# usando python 3
# Nota musical - Elaborar um programa que lê uma freqüência (em Hertz) e uma duração (em
# milissegundos) e emite um som na freqüência com a duração.

import pyaudio # folder spelt PyAudio
import numpy as np
import os
 
os.system('clear')

print("Este programa toca um som de acordo com a frequencia e tempo escolhido pelo usuário")
freq = int(input("Digite a frequencia: "))
tempo = int(input("Digite o tempo em millissegundos: "))

p = pyaudio.PyAudio()

volume = 0.5     # range [0.0, 1.0]
fs = 44100       # sampling rate, Hz, must be integer
duration = tempo/1000   # in seconds, may be float
f = freq        # sine frequency, Hz, may be float

# generate samples, note conversion to float32 array
samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)

# for paFloat32 sample values must be in range [-1.0, 1.0]
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)

# play. May repeat with different volume values (if done interactively) 
stream.write(volume*samples)

stream.stop_stream()
stream.close()

p.terminate()