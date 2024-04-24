import unittest
from unittest.mock import patch
import io
from mutationtest import StringChecker  # Adjust based on your module name


class TestStringChecker(unittest.TestCase):
    # Combined tests for clean_string, is_palindrome, and is_isogram
    def test_cleaned_input(self):
        self.assertEqual(StringChecker.clean_string("A man, a plan, a canal: Panama"), "amanaplanacanalpanama")
        # More tests for clean_string...

    def test_is_palindrome(self):
        # Combined palindrome tests...
        for palindrome in ["radar", "A man, a plan, a canal: Panama", "", " "]:
            with self.subTest(palindrome=palindrome):
                self.assertTrue(StringChecker.is_palindrome(palindrome))

        for non_palindrome in ["hello", "world", "ab"]:
            with self.subTest(non_palindrome=non_palindrome):
                self.assertFalse(StringChecker.is_palindrome(non_palindrome))

    def test_is_isogram(self):
        # Combined isogram tests...
        for isogram in ["isogram", "lumberjack"]:
            with self.subTest(isogram=isogram):
                self.assertTrue(StringChecker.is_isogram(isogram))

        for non_isogram in ["elephant", "balloon"]:
            with self.subTest(non_isogram=non_isogram):
                self.assertFalse(StringChecker.is_isogram(non_isogram))

    # Structural tests covering different branches and conditions
    def test_palindrome_branch(self):
        with patch('builtins.input', side_effect=["1", "radar"]), patch('sys.stdout', new=io.StringIO()) as fake_out:
            StringChecker.main()
            output = fake_out.getvalue().strip()
            self.assertIn("Is 'radar' a palindrome? Yes", output)

    def test_isogram_branch_for_correct_choice(self):
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
