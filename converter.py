import pretty_midi as pmd
import librosa
import numpy as np

def create_sine(f, duration, amp=1, fs=44100):
    return amp * np.sin(2 * np.pi * f * np.arange(0, duration, 1/fs))

def pitch_to_f(pitch_num):
    return 440 * pow(2, (pitch_num - 69)/12.0)

def draw_triangle(pitch, duration, n=10, fs=44100):
    f = pitch_to_f(pitch)
    sgn = 1
    wave = 0 * np.arange(0, duration, 1/fs)
    for i in range(1, 2 * n, 2):
        sgn *= -1
        wave += create_sine(f * i, duration, sgn*amp/(i*i))

def draw_pulse(pitch, duration, amp=1, n=10, fs=44100):
    f = pitch_to_f(pitch)
    wave = 0 * np.arange(0, duration, 1/fs)
    for i in range(1, 2 * n, 2):
        wave += create_sine(f * i, duration, amp / i)
    return wave

def draw_pulse2(pitch, duration, amp=1, n=10, fs=44100):
    f = pitch_to_f(pitch)
    sgn = 1
    wave = 0 * np.arange(0, duration, 1/fs)
    for i in range(1, 2 * n, 2):
        wave += create_sine(f * i, duration, amp / i)
    return wave

def draw_noise(pitch, duration):
    f = pitch_to_f(pitch)
    wave = 0 * np.arange(0, duration, 1/fs)
