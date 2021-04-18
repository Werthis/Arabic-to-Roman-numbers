import tkinter as tk
import arabic_to_roman_numberals_converter as trans

class GuiTrans():

    def __init__(self, backend):
        self._backend = backend

        self.window = tk.Tk()
        self.window.title('Arabic to Roman number conversion')
        self.window.geometry("300x200")

        self.number = tk.StringVar()
        self.text = tk.StringVar()

        introduction_label = tk.Label(self.window, text = 'Arabic to Roman number converter', font=('calibre', 12))

        arabic_label = tk.Label(self.window, text = 'enter Arabic number:', font=('calibre', 10))

        input_area = tk.Entry(self.window, textvariable = self.number, font=('calibre',10,'normal'))

        conversion_button = tk.Button(self.window, text='Convert', font=('calibre', 10), command = self.conversion)
    
        roman_label = tk.Label(self.window, text = 'This is your roman number:', font=('calibre', 10))

        blanc_label = tk.Label(self.window, text = '')

        roman_number_converted = tk.Label(self.window, textvariable=self.text)

        introduction_label.pack(fill=tk.BOTH)
        arabic_label.pack(fill=tk.BOTH)
        input_area.pack(fill=tk.BOTH)
        conversion_button.pack(fill=tk.BOTH)
        roman_label.pack(fill=tk.BOTH)
        blanc_label.pack(fill=tk.BOTH)
        roman_number_converted.pack(fill=tk.BOTH)


    def get_number_from_user(self):
        self.arabic_number = str(0)
        self.arabic_number = self.number.get()
        return self.arabic_number

    def conversion(self):
        self.text.set('')
        self.get_number_from_user()
        roman_number = self._backend.gui_cumunication(self.arabic_number)
        self.arabic_number = 0
        self.text.set(roman_number)
        self.number.set('')

    def start(self):
        self.window.mainloop()

if __name__ == "__main__":
    number = ''                            
    program = trans.Converter(number)
    app = GuiTrans(program)
    app.start()
