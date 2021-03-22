class Converter():

    def __init__(self, arabic_number):
        self._arabic_number = arabic_number
        self._decimal_digits = []

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
            self._first_number = self._decimal_digits[0]
            self.final_number = self.make_first_symbol(self._first_number)

        elif self._lenght_of_number == 2:
            self._first_number = self._decimal_digits[1]
            self._second_number = self._decimal_digits[0]
            self.final_number = self.make_second_symbol(self._second_number) + self.make_first_symbol(self._first_number)

        elif self._lenght_of_number == 3:
            self._first_number = self._decimal_digits[2]
            self._second_number = self._decimal_digits[1]
            self._third_number = self._decimal_digits[0]
            self.final_number = (
                self.make_third_symbol(self._third_number) 
                + self.make_second_symbol(self._second_number) 
                + self.make_first_symbol(self._first_number)
            )
             
        elif self._lenght_of_number == 4:
            self._first_number = self._decimal_digits[3]
            self._second_number = self._decimal_digits[2]
            self._third_number = self._decimal_digits[1]
            self._forth_number = self._decimal_digits[0]
            self.final_number = (
                self.make_forth_symbol(self._forth_number) 
                + self.make_third_symbol(self._third_number) 
                + self.make_second_symbol(self._second_number) 
                + self.make_first_symbol(self._first_number)
            )

        return self.final_number

    def make_first_symbol(self, first_number):
        self._first_number = first_number
        
        if self._first_number < 4:
            self.last_symbol = 'I' * self._first_number
        elif self._first_number == 4:
            self.last_symbol = 'IV'
        elif self._first_number in range(5, 9):
            self.last_symbol = 'V' + 'I' * (self._first_number - 5)
        elif self._first_number == 9:
            self.last_symbol = 'IX'

        return self.last_symbol

    def make_second_symbol(self, second_number):
        self._second_number = second_number
    
        if self._second_number < 4:
            self.before_last_symbol = 'X' * self._second_number
        elif self._second_number == 4:
            self.before_last_symbol = 'XL'
        elif self._second_number in range(5, 9):
            self.before_last_symbol = 'L' + 'X' * (self._second_number - 5)
        elif self._second_number == 9:
            self.before_last_symbol = 'XC'

        return self.before_last_symbol

    def make_third_symbol(self, third_number):
        self._third_number = third_number

        if self._third_number < 4:
            self.third_from_end_symbol = 'C' * self._third_number
        elif self._third_number == 4:
            self.third_from_end_symbol = 'CD'
        elif self._third_number in range(5, 9):
            self.third_from_end_symbol = 'D' + 'C' * (self._third_number - 5)
        elif self._third_number == 9:
            self.third_from_end_symbol = 'CM'

        return self.third_from_end_symbol

    def make_forth_symbol(self, forth_number):
        self._forth_number = forth_number

        if self._forth_number < 4:
            self.fourth_from_end_symbol = 'M' * self._forth_number
        else:
            raise ValueError("\n\t\tI am very sorry, but roman numbers goes only till 3999")

        return self.fourth_from_end_symbol

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
        self.final_number = program.combine_roman_symbols_to_make_a_number()
        
    def __str__(self):
        return f'Roman number from {self._input_number} is: ' + self.final_number


if __name__ == "__main__":
    input_number = input('Please write a number: ')
    program = RunConverter(input_number)
    print(program)
