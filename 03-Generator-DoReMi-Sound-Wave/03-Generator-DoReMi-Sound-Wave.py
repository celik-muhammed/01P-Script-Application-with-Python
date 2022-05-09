# HapyBirthday-DoReMi
# step-1 Define Python Library
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scitools.sound

# step-2 Define Function for Generate Note
# Generate Note Tones
def noteGenerator(frequency=440, length=0.2, amplitude=1, sample_rate=44100):
    '''
    # Signal Formula -data- f(t) = A*sin(2*π*f*t+ϕ) or f(t) = A*sin(ω*t+ϕ)
    # signal basic settings - sound may vary by device type
    base_tone_freq = 440    # hertz (Hz) - 0.44kHz (Sound Frequency(Hz)) - Note A4(La4)
    base_duration = .2      # (Basic Duration Unit in Seconds) or length = 0.2
    sampleRate = 44100      # Samples Per Second Hz - 44.1kHz (Sample Rate)
    samples = base_duration*sampleRate  #
    
    # Produces a t second Audio-File
    t = np.linspace(0, time, time*sampleRate)  # timepoints
    A = np.iinfo(np.int16).max  # Volume (Amplitude) - the volume measure (max is 32768) or the Peak Value
    '''
    timepoints = np.linspace(0, length, int(length*sample_rate))
    data = amplitude*np.sin(2*np.pi*frequency*timepoints)  # A*sin(2*π*f*t)
    return data

# step-3 Define Suitable Note Letter and Frequency for Process
df = pd.read_csv('ScaleFreqs.csv', decimal =',')
print(df)

# step-4 Define Samle Composition Sheet
composition_letters = """
G3-0.4 G3-0.4 A3-0.8 G3-0.8 C4-0.7 B3-1.5 
G3-0.4 G3-0.4 A3-0.8 G3-0.8 D4-0.7 C4-1.4 
G3-0.4 G3-0.4 G4-0.7 E4-0.7 C4-0.8 D4-0.8 E4-0.8
F4-0.4 F4-0.4 E4-0.8 C4-0.8 D4-0.8 C4-1.6 
"""  # Happy Birthday to You - DoReMi-CDE

# step-5 Generate all tone from defined Composition
comp_letters_list = composition_letters.split()
tones = []
for letter in comp_letters_list:
    note, duration = letter.split('-')
    if note.title() in df['notes'].values:
        s = noteGenerator(df.loc[df['notes']==note.upper()]['frequency'].values[0], float(duration))
        tones.append(s)
    elif note.title() in df['notesDO'].values:
        s = noteGenerator(df.loc[df['notesDO']==note.upper()]['frequency'].values[0], float(duration))
        tones.append(s)
    else:
        print('Someting is wrong! Check and Try Again.')
        pass

# step-6 Make Note Data into a Single Array 
tones_wave = (np.concatenate(tones)*(np.iinfo(np.int16).max))  # Amplitude run 1 time

# step-7 Make Single Array into Double for Stereo Sound
# A 2D array where the left and right tones are contained in their respective rows
tones_wave_stereo = np.vstack((tones_wave, tones_wave))

# step-8 Make double array available for registration
# Reshape 2D array so that the left and right tones are contained in their respective columns
tones_wave_stereo = tones_wave_stereo.transpose()

# step-9 Save to Local Folder
scitools.sound.write(data=tones_wave_stereo, filename="HapyBirthday-DoReMi-MuCe.wav", sample_rate=44100)

# tones_wave_stereo features
print(len(tones_wave_stereo))
print(np.max(tones_wave_stereo))
print(np.min(tones_wave_stereo))

plt.plot(tones_wave_stereo[0:int(815845/440)])
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.show()