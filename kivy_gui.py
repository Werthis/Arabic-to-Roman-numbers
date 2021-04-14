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

    def __init__(self, backend, *args, **kwargs):
        super(RomanGrid, self).__init__(*args, **kwargs)
        self._backend = backend
        self.roman_number = 'Here comes your number!'

    def get_number_from_user(self):
        self.number_to_convert = self.arabic_number.text
        return self.number_to_convert
    
    def request(self):
        self.get_number_from_user()
        number_to_convert = self._backend.gui_cumunication(self.number_to_convert)
        self.roman_number = str(number_to_convert)

class RomanApp(App):

    def __init__(self, backend):
        super(RomanApp, self).__init__()
        self._backend = backend

    def build(self):
        return RomanGrid(self._backend)

    def start_app(self):
        RomanApp(self._backend).run()                


if __name__ == '__main__':
    number = ''
    program = trans.Converter(number)
    ## Tu pisz dalej
    app = RomanApp(program)
    app.start_app()
