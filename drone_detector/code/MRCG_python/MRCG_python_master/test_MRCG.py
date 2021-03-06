import numpy as np
import mrcg.MRCG as mrcg
import scipy.io.wavfile
import os
import librosa
import wave
import time

wav_dir = '/home/stealthdrone/Desktop/code/MRCG_python/MRCG_python_master/example/SNR103F3MIC021002_ch01.wav'
audio, sr = librosa.load(wav_dir, sr=16000)
# sr,audio = scipy.io.wavfile.read(wav_dir)
print('success to load sample wav-file')
s = time.clock()
samp_mrcg = mrcg.mrcg_extract(audio,sr)
e = time.clock()
print('success to extract features')
print(e-s)
