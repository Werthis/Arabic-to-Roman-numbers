import unittest
from arabic_to_roman_numberals_converter import Converter

class TestMethods(unittest.TestCase):

    def setUp(self):
        self.number = 89
        self.program = Converter(self.number)

    def test_make_list_method(self):
        self.assertEqual(self.program.split_number_and_put_into_list(), [8, 9])

    def test_combine_symbols(self):
        self.program.split_number_and_put_into_list()
        self.assertEqual(self.program.combine_roman_symbols_to_make_a_number(), 'LXXXIX')


class TestNumbers(unittest.TestCase):

    def test_first_ten(self):
        ten = Converter(3)
        ten.split_number_and_put_into_list()
        self.assertEqual(ten.combine_roman_symbols_to_make_a_number(), 'III')
        ten = Converter(4)
        ten.split_number_and_put_into_list()
        self.assertEqual(ten.combine_roman_symbols_to_make_a_number(), 'IV')
        ten = Converter(6)
        ten.split_number_and_put_into_list()
        self.assertEqual(ten.combine_roman_symbols_to_make_a_number(), 'VI')
        ten = Converter(8)
        ten.split_number_and_put_into_list()
        self.assertEqual(ten.combine_roman_symbols_to_make_a_number(), 'VIII')

    def test_till_thousnad(self):
        hundred = Converter(100)
        hundred.split_number_and_put_into_list()
        self.assertEqual(hundred.combine_roman_symbols_to_make_a_number(), 'C')
        hundred = Converter(500)
        hundred.split_number_and_put_into_list()
        self.assertEqual(hundred.combine_roman_symbols_to_make_a_number(), 'D')
        hundred = Converter(210)
        hundred.split_number_and_put_into_list()
        self.assertEqual(hundred.combine_roman_symbols_to_make_a_number(), 'CCX')
        hundred = Converter(8)
        hundred.split_number_and_put_into_list()
        self.assertEqual(hundred.combine_roman_symbols_to_make_a_number(), 'VIII')
        hundred = Converter(2)
        hundred.split_number_and_put_into_list()
        self.assertEqual(hundred.combine_roman_symbols_to_make_a_number(), 'II')
        hundred = Converter(16)
        hundred.split_number_and_put_into_list()
        self.assertEqual(hundred.combine_roman_symbols_to_make_a_number(), 'XVI')
        hundred = Converter(7)
        hundred.split_number_and_put_into_list()
        self.assertEqual(hundred.combine_roman_symbols_to_make_a_number(), 'VII')
        hundred = Converter(499)
        hundred.split_number_and_put_into_list()
        self.assertEqual(hundred.combine_roman_symbols_to_make_a_number(), 'CDXCIX')

    def test_till_four_thousand(self):
        thousand = Converter(1000)
        thousand.split_number_and_put_into_list()
        self.assertEqual(thousand.combine_roman_symbols_to_make_a_number(), 'M')
        thousand = Converter(2000)
        thousand.split_number_and_put_into_list()
        self.assertEqual(thousand.combine_roman_symbols_to_make_a_number(), 'MM')
        thousand = Converter(3333)
        thousand.split_number_and_put_into_list()
        self.assertEqual(thousand.combine_roman_symbols_to_make_a_number(), 'MMMCCCXXXIII')
        thousand = Converter(1111)
        thousand.split_number_and_put_into_list()
        self.assertEqual(thousand.combine_roman_symbols_to_make_a_number(), 'MCXI')
        thousand = Converter(0)
        thousand.split_number_and_put_into_list()
        self.assertEqual(thousand.combine_roman_symbols_to_make_a_number(), '')
        thousand = Converter(1500)
        thousand.split_number_and_put_into_list()
        self.assertEqual(thousand.combine_roman_symbols_to_make_a_number(), 'MD')
        thousand = Converter(3999)
        thousand.split_number_and_put_into_list()
        self.assertEqual(thousand.combine_roman_symbols_to_make_a_number(), 'MMMCMXCIX')
        thousand = Converter(101)
        thousand.split_number_and_put_into_list()
        self.assertEqual(thousand.combine_roman_symbols_to_make_a_number(), 'CI')


    # def test_error(self):
    #     error = Converter(4000)
    #     with self.assertRaises(drzewa.WorngNodeClassError):
    #         self.root.add_children(FakeNode(), FakeNode())

        
        
    #     self.assertRaises("\n\t\tI am very sorry, but roman numbers goes only till 3999", error.check_if_in_range())
    #     (error.combine_roman_symbols_to_make_a_number(), ValueError("\n\t\tI am very sorry, but roman numbers goes only till 3999"))




if __name__ == "__main__":
    unittest.main()
