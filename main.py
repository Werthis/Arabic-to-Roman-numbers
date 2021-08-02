import arabic_to_roman_numberals_converter as trans
import kivy_gui as kivy


if __name__ == '__main__':
    number = ''
    backend = trans.Converter(number)
    app = kivy.RomanApp(backend)
    app.start_app()
