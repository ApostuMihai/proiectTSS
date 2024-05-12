import pytest
from string_manipulator import StringChecker  # replace 'your_module' with the actual module name

def setup_function():
    global checker
    checker = StringChecker()

def test_clean_string():
    assert checker.clean_string("Hello, World!") == "helloworld"

def test_is_palindrome():
    assert checker.is_palindrome("A man, a plan, a canal: Panama")
    assert not checker.is_palindrome("Hello, World!")

def test_is_isogram():
    assert checker.is_isogram("Subdermatoglyphic")
    assert not checker.is_isogram("Hello, World!")