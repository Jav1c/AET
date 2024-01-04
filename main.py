from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.config import Config

Config.set('graphics', 'Resizable', '0')
Config.set('graphics', 'width', '412')
Config.set('graphics', 'height', '732')

class Prototype(FloatLayout):
    pass

class QuizApp(App):
    def build(self):
        return Prototype()

QuizApp().run()