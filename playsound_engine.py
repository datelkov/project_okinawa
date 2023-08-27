import soundfile as sf
import pyaudio
import numpy as np


def play_audio(file_path):
    chunk_size = 1024

    data,samplerate=sf.read(file_path)
    p = pyaudio.PyAudio()
    #print(samplerate)
    #print(data.shape[1])
    stream = p.open(format=pyaudio.paFloat32,
                    channels=data.shape[1],
                    rate=samplerate,
                    output=True,
                    frames_per_buffer=chunk_size)

    index = 0
    while index < len(data):
        chunk = data[index:index + chunk_size]
        stream.write(chunk.astype(np.float32).tobytes())
        index += chunk_size
    
    stream.stop_stream()
    stream.close()

    p.terminate()
    

if __name__=="__main__":
    audio_file_path = 'test.mp3'
    play_audio(audio_file_path)