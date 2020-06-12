# encoding: utf-8 
# usando python 3
# Parabéns - Faça um programa que emite as seis primeiras notas do "Parabéns prá você". 
# Tente as seguintes notas (freqüência em Hz/duração em milissegundos): 
# [440,200], [440,200], [500,800], [440,400], [600,400], [560,800],

import numpy as np
import simpleaudio as sa


frequency = 294  # Our played note will be 440 Hz
fs = 44100  # 44100 samples per second
seconds = 1  # Note duration of 3 seconds

# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
t = np.linspace(0, seconds, seconds * fs, False)
note = np.sin(frequency * t * 2 * np.pi)
audio = note * (2**15 - 1) / np.max(np.abs(note))
audio = audio.astype(np.int16)
play_obj = sa.play_buffer(audio, 1, 2, fs)
input('')
play_obj.stop()

play_obj = sa.play_buffer(audio, 1, 2, fs)
input('')
play_obj.stop()

frequency = 330  # Our played note will be 440 Hz
fs = 44100  # 44100 samples per second
seconds = 1  # Note duration of 3 seconds

# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
t = np.linspace(0, seconds, seconds * fs, False)
note = np.sin(frequency * t * 2 * np.pi)
audio = note * (2**15 - 1) / np.max(np.abs(note))
audio = audio.astype(np.int16)
play_obj3 = sa.play_buffer(audio, 1, 2, fs)
input('')
play_obj3.stop()


frequency = 294  # Our played note will be 440 Hz
fs = 44100  # 44100 samples per second
seconds = 1  # Note duration of 3 seconds

# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
t = np.linspace(0, seconds, seconds * fs, False)
note = np.sin(frequency * t * 2 * np.pi)
audio = note * (2**15 - 1) / np.max(np.abs(note))
audio = audio.astype(np.int16)
play_obj4 = sa.play_buffer(audio, 1, 2, fs)
input('')
play_obj4.stop()


frequency = 392  # Our played note will be 440 Hz
fs = 44100  # 44100 samples per second
seconds = 1  # Note duration of 3 seconds

# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
t = np.linspace(0, seconds, seconds * fs, False)
note = np.sin(frequency * t * 2 * np.pi)
audio = note * (2**15 - 1) / np.max(np.abs(note))
audio = audio.astype(np.int16)
play_obj5 = sa.play_buffer(audio, 1, 2, fs)
input('')
play_obj5.stop()


frequency = 360  # Our played note will be 440 Hz
fs = 44100  # 44100 samples per second
seconds = 1  # Note duration of 3 seconds

# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
t = np.linspace(0, seconds, seconds * fs, False)
note = np.sin(frequency * t * 2 * np.pi)
audio = note * (2**15 - 1) / np.max(np.abs(note))
audio = audio.astype(np.int16)
play_obj6 = sa.play_buffer(audio, 1, 2, fs)
input('')
play_obj6.stop()
