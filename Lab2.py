#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from math import pi as PI
from scipy import signal
import IPython.display as ipd


# <b>Zadanie 2.1.a)<b>

# In[103]:


y = [0]*41
y[0] = 1
y[40] = 1

plt.figure(figsize= (12,4), dpi= 100)
plt.title("Impuls oraz impuls przesunięty o N = 40 próbek")
plt.xlabel("Wartość Próbki")
plt.ylabel("Nr Próbki")
plt.stem(range(41), y)
plt.savefig("Zadanie_2_1\\a.png")


# <b>Zadanie 2.1.b)<b>

# In[102]:


a = np.arange(0, 36.2, 0.2)
y1 = np.cos(a)
y2 = signal.sawtooth(a)
y3 = signal.square(a)

fig, plots = plt.subplots(3, 1, figsize= (12,8), dpi= 100)

for plot in plots:
    plot.set_yticks(np.arange(-1, 1.1, 0.5))
    plot.set_xticks(np.arange(0, 40, 4))
    plot.grid(True)
    plot.set_ylim(-1.1, 1.1)
    plot.set_xlim(a[0], a[-1])

plots[0].set_title("Cosinus")
plots[0].plot(a, y1)

plots[1].set_title("Piłokształtny")
plots[1].plot(a, y2)

plots[2].set_title("Prostokątny")
plots[2].plot(a, y3)

plt.subplots_adjust(hspace=1)

plt.savefig("Zadanie_2_1\\b.png")


# <b>Zadanie 2.1.c)<b>

# In[101]:


x = np.arange(0, 200)
y = np.random.normal(0, np.sqrt(0.5), 200)

plt.figure(figsize=(12,8), dpi= 100)
plt.title("Szum Gaussowski")
plt.xlabel("Numer Próbki")
plt.ylabel("Wartość Chwilowa")
plt.plot(x, y)
plt.savefig("Zadanie_2_1\\c.png")


# <b>Zadanie 2.2<b>

# In[115]:


def PlotSignal(plot, A, f, phi, fs, justReturnY=False):
    Ts = 1/fs
    x = np.arange(0, 0.003 + Ts, Ts)
    y = A * np.sin((phi + x * 2 * PI)*f)
    if justReturnY:
        return y
    plot.set_title(f"A: {A},   f: {f/1000}kHz,   phi: {phi}rad,   fs: {fs/1000}kHz")
    plot.plot(x, y)

fig, plots = plt.subplots(3, 1, figsize= (12,8), dpi= 100)

maxA = 1

for plot in plots:
    plot.set_yticks(np.arange(-maxA, maxA + .1, 1))
    plot.set_xticks(np.arange(0, 0.003 + .0005, 0.0005))
    plot.grid(True)
    plot.set_ylim(-maxA - .1, maxA + .1)
    plot.set_xlim(0, 0.003)

PlotSignal(plots[0], 1, 1000, 0, 80000)
PlotSignal(plots[1], 1, 1000, 0.5, 80000)
PlotSignal(plots[2], 1, 1000, 1, 80000)

plt.subplots_adjust(hspace=1)

plt.savefig("Zadanie_2_2\\phi.png")

ipd.Audio(PlotSignal(plots[0], 1, 1000, 0, 80000, True), rate=44100)

# <b>Zadanie 2.3<b>

# In[119]:


def PlotSignal(plot, A, f, phi, fs, justReturnY=False):
    Ts = 1/fs
    x = np.arange(0, 0.007 + Ts, Ts)
    y = A * np.sin((phi + x * 2 * PI)*f)
    if justReturnY:
        return y
    plot.set_title(f"A: {A},   f: {f/1000}kHz,   phi: {phi}rad,   fs: {fs/1000}kHz")
    plot.plot(x, y, 'D-')

fig, plots = plt.subplots(3, 1, figsize= (12,8), dpi= 100)

maxA = 1

for plot in plots:
    plot.set_yticks(np.arange(-maxA, maxA + .1, 1))
    plot.set_xticks(np.arange(0, 0.007 + .0005, 0.0005))
    plot.grid(True)
    plot.set_ylim(-maxA - .1, maxA + .1)
    plot.set_xlim(0, 0.007)

PlotSignal(plots[0], 1, 1000, 0, 8000)
PlotSignal(plots[1], 1, 1000, 0, 2000)
PlotSignal(plots[2], 1, 1000, 0, 1100)

plt.subplots_adjust(hspace=1)

plt.savefig("Zadanie_2_3\\fs.png")


# <b>Zadanie 2.4<b>

# In[81]:


import wave

SNR = 3

data = wave.open("Zadanie_2_4\\Nagranie.wav")
framerate = data.getframerate()*2
recording = np.frombuffer(data.readframes(-1), dtype = "int16") /2000

recording_reversed = np.flip(recording)

x = np.arange(0, recording.size/framerate, 1/framerate)

noise = np.random.normal(0, 1, recording.size)

# Powinno się to zrobić za pomocą formuły na decybele i jak ktoś zechciałby to zrobić to byłoby miło gdyby zrobił pull request
mixed = recording + noise/(5*SNR)


fig, plots = plt.subplots(4, 1, figsize= (8,8), dpi= 100)

for plot in plots:
    plot.set_xticks(np.arange(0, x[-1], 1))
    plot.grid(True)
    plot.set_xlim(0, x[-1])

plots[0].set_title("Mowa")
plots[0].set_xlabel("Czas [s]")
plots[0].plot(x, recording, color="orange")

plots[1].set_title("Mowa - odwrócona")
plots[1].set_xlabel("Czas [s]")
plots[1].plot(x, recording_reversed, color="orange")

plots[2].set_title("Szum")
plots[2].set_xlabel("Czas [s]")
plots[2].plot(x, noise, color="orange")

plots[3].set_title(f"Mowa + szum, SNR: {SNR}dB")
plots[3].set_xlabel("Czas [s]")
plots[3].plot(x, mixed, color="orange")


plt.subplots_adjust(hspace=1)
plt.savefig("Zadanie_2_4\\plots.png")
ipd.Audio(mixed, rate=framerate)


# <b>Zadanie 2.5<b>

# In[27]:


from math import sin


def generate_sound(frequency, lenght = 0.5, samplerate = 44100):
    sound = []
    i = 0
    while i < int(lenght * samplerate):
        sound.append(sin(i*2*PI*frequency/samplerate))
        i += 1
    for a in range(500):
        sound.append(sin(i*2*PI*frequency/samplerate) * (500 - a)/500)
        i += 1
    return sound

#Wzięte z internetu:
Notes = {
    ' ': 0.0,
    'C': 261.6,
    'D': 293.7,
    'E': 329.6,
    'F': 349.2,
    'G': 392.0,
    'A': 440.0,
    'B': 493.9,
}

def play_notes(notesToPlay, samplerate=44100):
    melody = []
    notesToPlay = list(notesToPlay)
    for note in notesToPlay:
        melody.extend(generate_sound(Notes.get(note[0], 0.0), note[1]))
    return melody



catSong = [
    ['G', 0.4],
    ['E', 0.4],
    ['E', 0.4],
    ['F', 0.4],
    ['D', 0.4],
    ['D', 0.4],
    ['C', 0.2],
    ['E', 0.2],
    ['G', 0.8],
    [' ', 0.4],
    ['G', 0.4],
    ['E', 0.4],
    ['E', 0.4],
    ['F', 0.4],
    ['D', 0.4],
    ['D', 0.4],
    ['C', 0.2],
    ['E', 0.2],
    ['C', 0.8],
]

melody = play_notes(catSong)
ipd.Audio(melody, rate=44100)


# In[ ]:




