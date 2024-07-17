import pyaudio
import wave
numbers = [r"C:\Users\jijoe.joseph\scale\numbers\0.wav", r"C:\Users\jijoe.joseph\scale\numbers\1.wav", r"C:\Users\jijoe.joseph\scale\numbers\2.wav", r"C:\Users\jijoe.joseph\scale\numbers\3.wav", r"C:\Users\jijoe.joseph\scale\numbers\4.wav", r"C:\Users\jijoe.joseph\scale\numbers\5.wav", r"C:\Users\jijoe.joseph\scale\numbers\6.wav", r"C:\Users\jijoe.joseph\scale\numbers\7.wav", r"C:\Users\jijoe.joseph\scale\numbers\8.wav", r"C:\Users\jijoe.joseph\scale\numbers\9.wav"]
stop_audio = False

def play_audio(audio_file):
    audio_file = audio_file
    global stop_audio
    chunk = 1024

    wf = wave.open(audio_file, 'rb')

    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(chunk)
    while data and not stop_audio:
        stream.write(data)
        data = wf.readframes(chunk)
    stream.stop_stream()
    stream.close()

    p.terminate()
def say_num(num):
    num = str(num)
    lis = []
    for digit in num:
        if digit == '.':
            play_audio(r"C:\Users\jijoe.joseph\scale\numbers\point.wav")
        else:
            play_audio(numbers[int(digit)])
