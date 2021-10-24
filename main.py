
from kivymd.uix.label import MDLabel
from kivy.clock import Clock
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.uix.image import Image
from kivymd.app import MDApp
from kivy.core.window import Window
from time import ctime
import pywhatkit
import webbrowser
import wikipedia
import pyjokes
from voice import *
from responces import *

# Set the app size
Window.size = (300, 500)


class Command(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_name = "Rubik-Regular.ttf"
    font_size = 17

class TimeData(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_name = "Rubik-Regular.ttf"
    font_size = 12

class Response(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_name = "Rubik-Regular.ttf"
    font_size = 17

class ResponseImage(Image):
    source = StringProperty()
    size_hint_x = NumericProperty()

class ChatBot(MDApp):

    def change_screen(self, name):
        screen_manager.current = name

    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("Main.kv"))
        screen_manager.add_widget(Builder.load_file("convo.kv"))
        screen_manager.add_widget(Builder.load_file("userg.kv"))
        return screen_manager


    def response(self, *args):
        global size, halign
        response = ""
        response2 = ""
        timedata = ""
        timedata2 = ""
        source = ""

        if 'search' in voice_data:
            timedata = ctime()
            search = record_audio('What do you want me to search for ?')
            inn = wikipedia.summary(search, 2)
            response = inn
            aya_voice(inn)
            url = 'https://google.com/search?q=' + search
            webbrowser.get().open(url)
            aya_voice("Here is the additional information about " + search)

        elif 'who is' in voice_data:
            person = voice_data.replace('who is', '')
            response = "knowing " + person + " is not may thing pwede kang magtanong kay google or kung pwede mong sabihin ang search " + person + " para personal ko siyang masearch "
            timedata = ctime()
            aya_voice("knowing " + person + "is not my thing you can ask google for that but if you insist i can search it but you need to say, search " + person + "so that i can personaly search for it ")

        elif 'logo' in voice_data:
            screen_manager.get_screen("convo").chat_list.add_widget(TimeData(text=ctime(), size_hint_x=.77))
            screen_manager.get_screen('convo').chat_list.add_widget(ResponseImage(source="img/logo.png", size_hint_x=.77))
            response2 = "This is my logo"
            timedata2 = ctime()
            aya_voice("This is my logo")

        elif 'why' in voice_data:
            thing = voice_data.replace('why', '')
            info = wikipedia.summary(thing, 2)
            timedata = ctime()
            response = info
            aya_voice(info)

        for speak in greetings:
            if speak in voice_data:
                timedata = ctime()
                response2 = "Hello"
                aya_voice("Hello")

                if len(voice_data) < 6:
                    size = .22
                    halign = "center"

                elif len(voice_data) < 11:
                    size = .32
                    halign = "center"

                elif len(voice_data) < 16:
                    size = .45
                    halign = "center"

                elif len(voice_data) < 21:
                    size = .58
                    halign = "center"

                elif len(voice_data) < 26:
                    size = .71
                    halign = "center"

                else:
                    size = .77
                    halign = "left"

        for speak in name:
            if speak in voice_data:
                timedata = ctime()
                response = "I am AYA Your Menstruational Companion"
                aya_voice("I am AYA Your Menstruational Companion")

        for speak in nicknames:
            if speak in voice_data:
                timedata = ctime()
                response = "Just call me AYA"
                aya_voice("Just call me AYA")

        for speak in days:
            if speak in voice_data:
                timedata = ctime()
                response2 = "Good Day"
                aya_voice("Good Day")

        for speak in complain:
            if speak in voice_data:
                timedata = ctime()
                response2 = "I am here, You can talk to me"
                aya_voice("I am here, You can talk to me")

        for speak in create_note:
            if speak in voice_data:
                timedata = ctime()
                response = "What do you want me to write into your note"
                aya_voice("What do you want me to write into your note")

                done = False

                while not done:
                    try:
                        with sr.Microphone() as mic:
                            r = sr.Recognizer()

                            r.energy_threshold = 10000
                            r.adjust_for_ambient_noise(mic, 1.2)
                            audio = r.listen(mic)
                            note = r.recognize_google(audio)
                            note = note.lower()
                            timedata = ctime()
                            aya_voice('Choose a file name!')
                            response2 = 'Choose a file name!'

                            r.energy_threshold = 10000
                            r.adjust_for_ambient_noise(mic, 1.2)
                            audio = r.listen(mic)

                            filename = r.recognize_google(audio)
                            filename = filename.lower()

                        with open(f"{filename}.text", 'w') as f:
                            f.write(note)
                            done = True
                            timedata = ctime()
                            response2 = f'Choose a file name! I successfully created the note {filename}'
                            aya_voice(f'I successfully created the note {filename}')

                    except sr.UnknownValueError:
                        response = 'I did not understand you! Please try again!'
                        aya_voice('I did not understand you! Please try again!')

        for speak in bye:
            if speak in voice_data:
                timedata = ctime()
                response = "Thank you and have a good day"
                aya_voice("Thank you and have a good day")

        for speak in song:
            if speak in voice_data:
                songs = record_audio("What do you want me to play?")
                timedata = ctime()
                response2 = "What do you want me to play?"
                timedata2 = ctime()
                response = "This is what i found " + songs + " in youtube"
                aya_voice('This is what i found ' + songs + ' in youtube')
                pywhatkit.playonyt(songs)

        for speak in pains:
            if speak in voice_data:
                response = "Period really do hurts. here are some of the remedies to relieve your pain. " \
                            "If you feel that you can put hot compress in your lower abdomen. oh! also you can put a pillow under you " \
                            "butt to lessen the pain. it is to much ?? you can handle it, i can play a music for you"
                timedata = ctime()
                aya_voice("Period really do hurts. here are some of the remedies to relieve your pain. "
                          "If you feel that you can put hot compress in your lower abdomen. oh! also you can put a pillow under you."
                          "butt to lessen the pain. it is to much ?? you can handle it, i can play a music for you")

        for speak in joke:
            if speak in voice_data:
                response = pyjokes.get_joke()
                timedata = ctime()
                aya_voice(pyjokes.get_joke())


        for speak in complain1:
            if speak in voice_data:
                response = "You look beautiful. All women and girls in all shape, color and size are beautiful"
                timedata = ctime()
                aya_voice("You look beautiful. All women and girls in all shape, color and size are beautiful")

        for speak in time:
            if speak in voice_data:
                response = "hey the current time is :" + ctime()
                timedata = ctime()
                aya_voice("hey the current time is :" + ctime())

        for speak in eat:
            if speak in voice_data:
                response = "But eating is important. Here some of links where you can order your food"
                timedata = ctime()
                aya_voice('But eating is important. Here some of links where you can order your food')

        for speak in friend:
            if speak in voice_data:
                response = "I am here to talk to you if you need a friend"
                aya_voice('I am here to talk to you if you need a friend')

        for speak in entertainment_bf:
            if speak in voice_data:
                response = "I don't have because you are my priority."
                timedata = ctime()
                aya_voice("I don't have because you are my priority")

            if speak in voice_data:
                response = "I don't have because you are my priority."
                timedata = ctime()
                aya_voice("I don't have because you are my priority")

        for speak in entertainment_old:
            if speak in voice_data:
                response = "Old enough to hang out with you and talk about menstruation"
                timedata = ctime()
                aya_voice("Old enough to hang out with you and talk about menstruation")

        for speak in entertainment_smart:
            if speak in voice_data:
                response = "I'm not smart, but i can help you to ease your pain in having menstration"
                timedata = ctime()
                aya_voice("I'm not smart, but i can help you to ease your pain in having menstration")

        for speak in entertainment_ass:
            if speak in voice_data:
                response = "Im not good at answering Assignments but if you say! Aya can you search for me i will gladly search it in google"
                timedata = ctime()
                aya_voice("Im not good at answering Assignments but if you say! Aya can you search for me i will gladly search it in google")

        for speak in entertainment_dance:
            if speak in voice_data:
                response = "I am actually good at twerking"
                aya_voice("I am actually good at twerking")
                timedata = ctime()
                pywhatkit.playonyt("Twerk")

        for speak in entertainment_sing:
            if speak in voice_data:
                response = "no i'm not good at singing"
                timedata = ctime()
                aya_voice("no i'm not good at singing")

        for speak in can:
            if speak in voice_data:
                response = "I can search and give information about menstruation, play a music, " \
                             "create a note for you, and be your companion, that tell you a joke "
                timedata = ctime()
                aya_voice("i can search and give information about menstruation, play a music, "
                          "create a note for you, and be your companion, that tell you a joke ")

        for speak in i_do_know:
            if speak in voice_data:
                response = "Do you want me to talk to you, or do you prefer listening to music, watching movie, " \
                             "reading books, playing games or do you want to sleep?"
                timedata = ctime()
                aya_voice("Do you want me to talk to you, or do you prefer listening to music, watching movie,"
                          "reading books, playing games or do you want to sleep?")

        for speak in companion:
            if speak in voice_data:
                response = "Then i'll be your companion, i tell you a joke " + pyjokes.get_joke()
                timedata = ctime()
                aya_voice("then i'll be your companion, i tell you a joke" + pyjokes.get_joke())

        for speak in talk_to:
            if speak in voice_data:
                response = "Okey, what do you want to talk about?"
                timedata = ctime()
                aya_voice(' Okey, what do you want to talk about?')

        for speak in mens:
            if speak in voice_data:
                timedata = ctime()
                response = "Are you alright? Tell me what I can do for you today"
                aya_voice("Are you alright? Tell me what I can do for you today")

        for speak in complain2:
            if speak in voice_data:
                response = "I know. Tell me more about it"
                timedata = ctime()
                aya_voice('I know. Tell me more about it')

        for speak in questions:
            if speak in voice_data:
                sp = speak
                inn = wikipedia.summary(sp, 2)
                response = inn
                timedata = ctime()
                aya_voice(inn)

        for speak in complain3:
            if speak in voice_data:
                response = "why whats the matter?"
                timedata = ctime()
                aya_voice("why whats the matter?")

        screen_manager.get_screen("convo").chat_list.add_widget(TimeData(text=timedata, size_hint_x=.77))
        screen_manager.get_screen("convo").chat_list.add_widget(TimeData(text=timedata2, size_hint_x=.77))
        screen_manager.get_screen("convo").chat_list.add_widget(Response(text=response, size_hint_x=.77))
        screen_manager.get_screen("convo").chat_list.add_widget(Response(text=response2, size_hint_x=size, halign=halign))

    def send(self):
        global size, halign, voice_data, spacee
        voice_data = record_audio()
        if voice_data:
            voice_data = voice_data.lower()
            if len(voice_data) < 6:
                size = .22
                halign = "center"
                timedata = ctime()

            elif len(voice_data) < 11:
                size = .32
                halign = "center"
                timedata = ctime()

            elif len(voice_data) < 16:
                size = .45
                halign = "center"
                timedata = ctime()

            elif len(voice_data) < 21:
                size = .58
                halign = "center"
                timedata = ctime()

            elif len(voice_data) < 26:
                size = .71
                halign = "center"
                timedata = ctime()

            else:
                size = .77
                halign = "left"
                timedata = ctime()

            screen_manager.get_screen("convo").chat_list.add_widget(TimeData(text=timedata, size_hint_x=.77))
            screen_manager.get_screen("convo").chat_list.add_widget(Command(text=voice_data, size_hint_x=size, halign=halign))
            Clock.schedule_once(self.response, 1)

if __name__ == '__main__':
    ChatBot().run()
