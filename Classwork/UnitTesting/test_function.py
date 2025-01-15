import unittest
import functionpractice

class TestCubeFunction(unittest.TestCase):
    
    def test_that_cube_function_exists(self):
        functionpractice.get_cube(3)
        
    def test_that_cube_function_return_correct_value(self):
        actual = functionpractice.get_cube(3)
        result = 27
        self.assertEqual(actual, result)
        actual = functionpractice.get_cube(5)
        result = 125
        self.assertEqual(actual,result)
    
    def test_that_cube_function_return_negative_value_with_negative_parameter(self):
        actual = functionpractice.get_cube(-3)
        result = -27
        self.assertEqual(actual, result)
        
    def test_that_cube_function_return_invalid_data_with_invalid_input(self):
        actual = functionpractice.get_cube('a')
        result = 'invalid data'
        self.assertEqual(actual, result)
        
    def test_that_cube_function_return_correct_value_with_decimal_value(self):
        actual = functionpractice.get_cube(3.25)
        result = 34.328
        self.assertEqual(actual, actual)
        

class TestDollarAmount(unittest.TestCase):

    def test_that_takes_dollar_exchange_rate(self):
        functionpractice.get_dollar(1550)
    
    def test_that_takes_dollar_amount_as_input(self):
        actual = functionpractice.get_dollar(1000)
        result = 1550000
        self.assertEqual(actual, actual)
        
    def test_that_takes_negative_dollar_ammount(self):
        actual = functionpractice.get_dollar(-1000)
        result = -1550000
        self.assertEqual(actual, actual)
        
    def test_that_takes_dollar_invalid_data(self):
        actual = functionpractice.get_dollar('a')
        result = 'Not a number'
        self.assertEqual(actual, result)
        
    def test_that_takes_dollar_value_with_decimal(self):
        actual = functionpractice.get_dollar(13.99)
        result = 21684.5
        self.assertEqual(actual, actual)
        
    
