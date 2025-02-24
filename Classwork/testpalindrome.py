import unittest
import palindrome

class TestPalindrome(unittest.TestCase):
    
    def test_that_the_palindrome_function_exists(self):
        palindrome.get_number_palindrome(true)
        
    def test_that_the_palindrome_values_are_valid(self):
        actual = palindrome.get_number_palindrome(true)
        result = true
        self.assertEqual(actual, result)
    
    def test_that_the_palindrome_values_are_not_negative(self):
        actual = palindrome.get_number_palindrome(true)
        result = 'invalid input'
        self.assertEqual(actual, result)
       


if __name__ == '__main__:
    unittest.main()
