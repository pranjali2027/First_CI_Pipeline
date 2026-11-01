
import importlib

# Import Program 21
module = importlib.import_module("21_largest_word")
largest_word = module.largest_word

# Test 1: Normal sentence
def test_simple_sentence():
    assert largest_word("I love programming") == "programming"

# Test 2: Ignore punctuation
def test_punctuation_is_ignored():
    assert largest_word("Hello, world!") == "Hello"

# Test 3: First word wins in a tie
def test_tie_returns_first_word():
    assert largest_word("cat dog bat") == "cat"

# Test 4: Single word
def test_single_word():
    assert largest_word("Python") == "Python"

# Test 5: Empty sentence
def test_empty_sentence():
    assert largest_word("") == ""