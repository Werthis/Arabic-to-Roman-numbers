import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty, ObjectProperty

import arabic_to_roman_numberals_converter as trans


class RomanGrid(Widget):
    arabic_number = ObjectProperty(None)
    roman_number = StringProperty()

    def __init__(self, **kwargs):
        super(RomanGrid, self).__init__(**kwargs)
        self.roman_number = 'Here comes your number!'

    def change_text(self):
        new_number = self.arabic_number.text
        self.roman_number = str(new_number)
        self.arabic_number.text = ''

    def get_number_from_user(self):
        self.number_to_convert = self.arabic_number.text
        self.number_to_convert = str(self.number_to_convert)
        self.roman_number.set(self.number_to_convert)
        print('Arabic number is:', self.number_to_convert)
        self.arabic_number.text = ''
        return self.number_to_convert

    def request(self):
        self.get_number_from_user()
        roman_number = self._backend

class RomanApp(App):
    def build(self):
        return RomanGrid()

    def start_app(self):
        RomanApp().run()                


if __name__ == '__main__':
    number = ''
    program = trans.Converter(number)
    ## Tu pisz dalej
    app = RomanApp()
    app.start_app()
