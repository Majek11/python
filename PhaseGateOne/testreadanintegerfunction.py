import unittest
import functionreadaninteger

class ReadIntegerFunction(unittest.TestCase):
    
    def test_that_integer_function_exists(self):
        functionreadaninteger.read_integer(1000)
        
    def test_that_all_integers_are_digits(self):
        actual = functionreadaninteger.read_integer(932)
        result = 14
        self.assertEqual(actual, result)
        actual = functionreadaninteger.read_integer(998)
        result = 26
        self.assertEqual(actual,result)
    
    def test_that_all_integers_sum_are_correct(self):
        actual = functionreadaninteger.read_integer(1)
        result = 1
        self.assertEqual(actual, result)
        
    def test_that_integers_are_between_zero_to_hundred(self):
        actual = functionreadaninteger.read_integer('a')
        result = 'invalid data'
        self.assertEqual(actual, result)
        
    def test_that_integers_return_correct_value_with_decimal_value(self):
        actual = functionreadaninteger.read_integer(3.25)
        result = 34.328
        self.assertEqual(actual, actual)
        
        
    
