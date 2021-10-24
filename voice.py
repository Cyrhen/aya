import speech_recognition as sr
from kivymd.toast import toast
import playsound
import os
import random
from gtts import gTTS

r = sr.Recognizer()

def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            aya_voice(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            print('You: ' + voice_data)

        except Exception:
            aya_voice('Oops something went Wrong.')
            toast(text='Oops something went Wrong', background=[255/255, 138/255, 170/255, 1], duration=1)

        return voice_data

def aya_voice(audio_string):

    tts = gTTS(text=audio_string)
    r = random.randint(1, 1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print('Aya: ' + audio_string)
    os.remove(audio_file)
