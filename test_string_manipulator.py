import pytest
from string_manipulator import StringManipulator

@pytest.fixture
def manipulator():
    return StringManipulator()

def test_reverse(manipulator):
    assert manipulator.reverse("abc") == "cba"
    assert manipulator.reverse("") == ""

def test_capitalize(manipulator):
    assert manipulator.capitalize("hello world") == "Hello World"
    assert manipulator.capitalize("good morning") == "Good Morning"

def test_is_palindrome(manipulator):
    assert manipulator.is_palindrome("A man a plan a canal Panama") == True
    assert manipulator.is_palindrome("hello") == False

def test_trim(manipulator):
    assert manipulator.trim("   hello   ") == "hello"
    assert manipulator.trim("\n\t hi \t") == "hi"

def test_contains(manipulator):
    assert manipulator.contains("hello world", "world") == True
    assert manipulator.contains("hello world", "bye") == False

def test_word_count(manipulator):
    assert manipulator.word_count("hello world") == 2
    assert manipulator.word_count("") == 0
    assert manipulator.word_count("   ") == 0

def test_reverse_words(manipulator):
    assert manipulator.reverse_words("hello world") == "world hello"
    assert manipulator.reverse_words("one") == "one"
    assert manipulator.reverse_words("") == ""
