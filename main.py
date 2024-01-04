from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.config import Config

Config.set('graphics', 'Resizable', '0')
Config.set('graphics', 'width', '412')
Config.set('graphics', 'height', '732')


class Q1(Screen):
    pass

class Q2(Screen):
    pass

class Q3(Screen):
    pass

class Q4(Screen):
    pass

class Q5(Screen):
    pass

class Q6(Screen):
    pass

class Q7(Screen):
    pass

class Q8(Screen):
    pass

class Q9(Screen):
    pass

class Q10(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('Quiz.kv')

class QuizApp(App):
    def build(self):
        return kv

QuizApp().run()