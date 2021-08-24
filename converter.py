import librosa
import soundfile as sf
import numpy as np
from scipy import signal

def create_sine(f, duration, amp=1, fs=44100):
    return amp * np.sin(2 * np.pi * f * np.arange(0, duration, 1/fs))

def pitch_to_f(pitch_num):
    return 440*pow(2, (pitch_num - 69)/12.0)

def draw_triangle(pitch, duration, amp=1, n=10, fs=44100):
    f = pitch_to_f(pitch)
    sgn = 1
    wave = 0 * np.arange(0, duration, 1/fs)
    for i in range(1, 2 * n, 2):
        sgn *= -1
        wave += create_sine(f * i, duration, sgn*amp/(i*i))
    return wave

def draw_pulse(pitch, duration, amp=1, n=10, fs=44100):
    f = pitch_to_f(pitch)
    '''
    wave = 0 * np.arange(0, duration, 1/fs)
    for i in range(1, 2 * n, 2):
        wave += create_sine(f * i, duration, amp / i)
    return wave
    '''
    t = np.linspace(0, duration, fs)
    return signal.square(np.pi * f * t)

def draw_pulse2(pitch, duration, amp=1, n=10, fs=44100):
    f = pitch_to_f(pitch)
    t = np.linspace(0, duration, fs)
    return signal.square(np.pi * f * t, duty=1/4)

def draw_noise(pitch, duration, amp=1, fs=44100):
    f = pitch_to_f(pitch)*15
    wave = 0 * np.arange(0, duration, 1/fs)
    print(fs // int(f))
    j = 0
    sig = amp * np.random.rand()
    for i in range(duration * fs):
        if j >= fs/f:
            sig = amp * np.random.rand()
            j -= fs/f
        j += 1
        wave[i] += sig
    return wave

if __name__ == '__main__':
    sr = 44100
    y = draw_triangle(69, 2)
    sf.write('triangle_A4.wav', y, sr)
    y = draw_pulse(69, 2)
    sf.write('pulse_A4.wav', y, sr)
    y = draw_pulse2(69, 2)
    sf.write('pulse2_A4.wav', y, sr)