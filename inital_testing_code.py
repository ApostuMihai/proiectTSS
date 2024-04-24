import unittest
from unittest.mock import patch
import io
from mutationtest import StringChecker  # Adjust based on your module name

class TestStringChecker(unittest.TestCase):
    # Functional tests for palindrome and isogram checks
    def test_is_palindrome(self):
        self.assertTrue(StringChecker.is_palindrome("radar"))
        self.assertTrue(StringChecker.is_palindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(StringChecker.is_palindrome("hello"))
        self.assertFalse(StringChecker.is_palindrome("world"))

    def test_is_isogram(self):
        self.assertTrue(StringChecker.is_isogram("isogram"))
        self.assertTrue(StringChecker.is_isogram("lumberjack"))
        self.assertFalse(StringChecker.is_isogram("elephant"))
        self.assertFalse(StringChecker.is_isogram("balloon"))

    # Structural tests covering different branches and conditions
    def test_palindrome_branch(self):
        with patch('builtins.input', side_effect=["1", "radar"]), patch('sys.stdout', new=io.StringIO()) as fake_out:
            StringChecker.main()
            output = fake_out.getvalue().strip()
            self.assertIn("Is 'radar' a palindrome? Yes", output)

    def test_isogram_branch(self):
        with patch('builtins.input', side_effect=["2", "isogram"]), patch('sys.stdout', new=io.StringIO()) as fake_out:
            StringChecker.main()
            output = fake_out.getvalue().strip()
            self.assertIn("Is 'isogram' an isogram? Yes", output)

    def test_invalid_input(self):
        with patch('builtins.input', side_effect=["3", "1", "Madam"]), patch('sys.stdout', new=io.StringIO()) as fake_out:
            StringChecker.main()
            output = fake_out.getvalue().strip()
            self.assertIn("Please enter either 1 or 2.", output)
            self.assertIn("Is 'Madam' a palindrome? Yes", output)

    def test_empty_string_palindrome(self):
        with patch('builtins.input', side_effect=["1", ""]), patch('sys.stdout', new=io.StringIO()) as fake_out:
            StringChecker.main()
            output = fake_out.getvalue().strip()
            self.assertIn("Is '' a palindrome? Yes", output)

if __name__ == "__main__":
    unittest.main()
