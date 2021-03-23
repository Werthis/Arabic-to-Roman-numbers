class Converter():

    def __init__(self, arabic_number):
        self._arabic_number = arabic_number
        self._decimal_digits = []
        self.I_symbol = 'I'
        self.V_symbol = 'V'
        self.X_symbol = 'X'
        self.L_symbol = 'L'
        self.C_symbol = 'C'
        self.D_symbol = 'D'
        self.M_symbol = 'M'

    def split_number_and_put_into_list(self):
        self._text = str(self._arabic_number)
        self._lenght_of_number = len(self._text)
        for i in range(self._lenght_of_number):
            x = int(self._text[i])
            self._decimal_digits.append(x)

        return self._decimal_digits

    def check_if_in_range(self):
        if self._lenght_of_number > 4:
            raise ValueError("\n\t\tI am very sorry, but roman numbers goes only till 3999")

    def combine_roman_symbols_to_make_a_number(self):
        if self._lenght_of_number == 1:
            first_number = self._decimal_digits[0]
            roman_number = self.make_all(first_number, self.I_symbol, self.V_symbol, self.X_symbol)

        elif self._lenght_of_number == 2:
            first_number = self._decimal_digits[1]
            second_number = self._decimal_digits[0]
            roman_number = (
                self.make_all(second_number, self.X_symbol, self.L_symbol, self.C_symbol) 
                + self.make_all(first_number, self.I_symbol, self.V_symbol, self.X_symbol)
            )
        elif self._lenght_of_number == 3:
            first_number = self._decimal_digits[2]
            second_number = self._decimal_digits[1]
            third_number = self._decimal_digits[0]
            roman_number = (
                self.make_all(third_number, self.C_symbol, self.D_symbol, self.M_symbol) 
                + self.make_all(second_number, self.X_symbol, self.L_symbol, self.C_symbol) 
                + self.make_all(first_number, self.I_symbol, self.V_symbol, self.X_symbol)
            )
             
        elif self._lenght_of_number == 4:
            first_number = self._decimal_digits[3]
            second_number = self._decimal_digits[2]
            third_number = self._decimal_digits[1]
            forth_number = self._decimal_digits[0]
            roman_number = (
                self.make_forth_symbol(forth_number) 
                + self.make_all(third_number, self.C_symbol, self.D_symbol, self.M_symbol) 
                + self.make_all(second_number, self.X_symbol, self.L_symbol, self.C_symbol) 
                + self.make_all(first_number, self.I_symbol, self.V_symbol, self.X_symbol)
            )

        return roman_number

    def make_all(self, number, first_symbol, second_symbol, third_symbol):      
        if number < 4:
            return first_symbol * number
        elif number == 4:
            return first_symbol + second_symbol
        elif number in range(5, 9):
            return second_symbol + first_symbol * (number - 5)
        elif number == 9:
            return first_symbol + third_symbol

    def make_forth_symbol(self, number):
        if number < 4:
            return self.M_symbol * number
        else:
            raise ValueError("\n\t\tI am very sorry, but roman numbers goes only till 3999")

    def input_send_to_gui(self, gui_input):
        self._arabic_number = gui_input
        self.split_number_and_put_into_list()
        self.check_if_in_range()
        message_to_gui = self.combine_roman_symbols_to_make_a_number()
        self._decimal_digits = []
        return message_to_gui


class RunConverter():

    def __init__(self, input_number):
        self._input_number = input_number
        program = Converter(self._input_number)
        program.split_number_and_put_into_list()
        program.check_if_in_range()
        self.roman_number = program.combine_roman_symbols_to_make_a_number()
        
    def __str__(self):
        return f'Roman number from {self._input_number} is: ' + self.roman_number


if __name__ == "__main__":
    input_number = input('Please write a number: ')
    program = RunConverter(input_number)
    print(program)
