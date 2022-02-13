# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 18:15:23 2022

@author: JonLD
"""
from pydub import AudioSegment
from pydub.playback import play
import numpy as np
import matplotlib.pyplot as plt

def plot_sample(Sample, Name):
    plt.plot(Sample)
    plt.xlabel("Sample Index")
    plt.ylabel("Amplitude")
    plt.title(f"Audio Waveform of {Name}")
    plt.show()



class pydub_audio:
    def __init__(self, filename, export_filename):
        self.filename = filename
        self.export_filename = export_filename
        self.audio_segment = self.get_audiosegment()
        self.audio_array = self.to_raw_audio()
        
        
    def get_audiosegment(self):
        sound = AudioSegment.from_file(self.filename, format="wav")
        return sound
        
    
    def to_raw_audio(self):
        sound = self.audio_segment
        samples = sound.get_array_of_samples()
        samples = np.array(samples)
        samples = samples.reshape(sound.channels, -1, order='F'); samples.shape # (<probably 2>, <len(song) in samples>)
        self.audio_array = samples
        return samples
    
    
    def audiosegment_from_array(self):
        return self.audio_segment._spawn(self.audio_segment)
    
    def export_audio(self):
        self.audio_segment.export(self.export_filename, format="wav")
        print(f'Successfully exported: {self.export_filename}')

        
        
        
        
        
        
        
    