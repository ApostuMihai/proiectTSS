import unittest
from unittest.mock import patch
from io import StringIO
from string_manipulator import StringChecker

class TestStringChecker(unittest.TestCase):
    def setUp(self):
        self.checker = StringChecker()

#teste acoperire cod
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=["3","1", "racecar"])
    def test_main_palindrome(self, mock_input, mock_stdout):
        self.checker.main()
        self.assertIn("Is 'racecar' a palindrome? Yes", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=["da","2","L","Lumberjacks"])
    def test_main_fail2(self, mock_input, mock_stdout):
        self.checker.main()
        self.assertIn("Is 'lumberjacks' an isogram? Yes", mock_stdout.getvalue())

#testare functionala

    def test_string_cleaner(self):
        self.assertEqual(self.checker.clean_string("Good morning!! How are you?"), "goodmorninghowareyou")
        self.assertEqual(self.checker.clean_string("HELLO WORLD"), "helloworld")
        self.assertEqual(self.checker.clean_string("!@#$%^&*()_+="), "")
        self.assertEqual(self.checker.clean_string("hello"), "hello")
        self.assertEqual(self.checker.clean_string(""), "")

    def test_is_palindrome(self):
        self.assertTrue(self.checker.is_palindrome("radar"))
        self.assertTrue(self.checker.is_palindrome("We panic in a pew"))
        self.assertTrue(self.checker.is_palindrome("123!21"))
        self.assertTrue(self.checker.is_palindrome(""))
        self.assertFalse(self.checker.is_palindrome("radars"))

    def test_is_isogram(self):
        self.assertTrue(self.checker.is_isogram("isogram"))
        self.assertTrue(self.checker.is_isogram("!a!"))
        self.assertFalse(self.checker.is_isogram("123!21"))
        self.assertTrue(self.checker.is_isogram(""))


    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=["1","a","a!!", "aa"])
    def test_boundary_values(self, mock_input, mock_stdout):
        self.checker.main()
        self.assertIn("The string must be at least 2 characters long. Please try again.", mock_stdout.getvalue())
        self.assertIn("Is 'aa' a palindrome? Yes", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=["3","2", "12345"])
    def test_equivalence_partitions(self, mock_input, mock_stdout):
        self.checker.main()
        self.assertIn("Please enter either 1 or 2.", mock_stdout.getvalue())
        self.assertIn("Is '12345' an isogram? Yes", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=["da","2", "Hello",])
    def test_category_partition(self, mock_input, mock_stdout):
        self.checker.main()
        self.assertIn("Invalid input. Please enter a number.", mock_stdout.getvalue())
        self.assertIn("Is 'hello' an isogram? No", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=["1", "a", "racecar"])
    def test_input_less_than_two_chars(self, mock_input, mock_stdout):
        self.checker.main()
        output = mock_stdout.getvalue()
        self.assertIn("The string must be at least 2 characters long. Please try again.", output)
        self.assertIn("Is 'racecar' a palindrome? Yes", output)

if __name__ == '__main__':
    unittest.main()
