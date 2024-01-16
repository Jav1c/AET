from kivy.app import App
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.config import Config
from kivy.clock import Clock
import time

Config.set('graphics', 'Resizable', '0')
Config.set('graphics', 'width', '412')
Config.set('graphics', 'height', '732')

class HomePage(Screen):
    pass

class Q1(Screen):
    index = 1
    correct_answer = NumericProperty(0)  # Index of the correct answer

class Q2(Screen):
    index = 2
    correct_answer = NumericProperty(2)

class Q3(Screen):
    index = 3
    correct_answer = NumericProperty(2)

class Q4(Screen):
    index = 4
    correct_answer = NumericProperty(3)  # Index of the correct answer

class Q5(Screen):
    index = 5
    correct_answer = NumericProperty(0)

class Q6(Screen):
    index = 6
    correct_answer = NumericProperty(0)

class Q7(Screen):
    index = 7
    correct_answer = NumericProperty(3)  # Index of the correct answer

class Q8(Screen):
    index = 8
    correct_answer = NumericProperty(0)

class Q9(Screen):
    index = 9
    correct_answer = NumericProperty(3)

class Q10(Screen):
    index = 10
    correct_answer = NumericProperty(0)

class ScoreScreen(Screen):
    pass

class InstructionPage(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('Quiz.kv')

class QuizApp(App):
    score = NumericProperty(0)
    start_time = 0

    def build(self):
        return kv

    def on_start(self):
        self.start_time = time.time()

    def check_answer(self, question_screen, selected_option):
        feedback_label = question_screen.ids.feedback_label
        score_label = question_screen.ids.score_label

        if self.start_time == 0:
            # Start the timer when answering the first question
            self.start_time = time.time()

        if question_screen.correct_answer == selected_option:
            feedback_label.text = "Correct answer!"
            self.score += 1
        else:
            feedback_label.text = "Incorrect answer!"

        score_label.text = f"Score: {self.score}"

        next_question_index = question_screen.index + 1
        if next_question_index <= 10:
            next_question_screen = app.root.get_screen(f'Q{next_question_index}')
            next_question_screen.ids.score_label.text = f"Score: {self.score}"
            app.root.current = f'Q{next_question_index}'
        else:
            elapsed_time = int(time.time() - self.start_time)
            app.root.current = 'ScoreScreen'
            final_score_label = app.root.get_screen('ScoreScreen').ids.final_score
            timer_label = app.root.get_screen('ScoreScreen').ids.timer_label
            final_score_label.text = f" {self.score}"
            timer_label.text = f"Time: {elapsed_time // 60} min {elapsed_time % 60} sec"
            self.score = 0  # Reset the score for a new quiz

if __name__ == '__main__':
    app = QuizApp()
    app.run()
