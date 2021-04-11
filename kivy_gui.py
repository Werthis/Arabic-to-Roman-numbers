import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty

import arabic_to_roman_numberals_converter as trans


class RomanGrid(Widget):
    arabic_number = ObjectProperty(None)
    roman_number = ObjectProperty(None)

    def __init__(self, backend):
        self._backend = backend

    def get_number_from_user(self):
        self.number_to_convert = self.arabic_number.text
        print('Arabic number is:', self.number_to_convert)
        self.arabic_number.text = ''
        return self.number_to_convert

    def request(self):
        self.get_number_from_user()
        roman_number = self._backend

class RomanApp(App):
    def build(self):
        return RomanGrid()


if __name__ == '__main__':
    number = ''
    program = trans.Converter(number)
    ## Tu pisz dalej
    RomanApp().run()