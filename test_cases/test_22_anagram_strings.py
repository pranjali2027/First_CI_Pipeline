
import importlib

module = importlib.import_module("22_anagram_strings")
is_anagram = module.is_anagram

# Test 1: Normal anagram
def test_normal_anagram():
    assert is_anagram("listen", "silent") == True

# Test 2: Different uppercase and lowercase
def test_uppercase_lowercase():
    assert is_anagram("Listen", "Silent") == True

# Test 3: Strings containing spaces
def test_strings_with_spaces():
    assert is_anagram("rail safety", "fairy tales") == True

# Test 4: Non-anagram strings
def test_not_anagram():
    assert is_anagram("hello", "world") == False

# Test 5: Empty strings
def test_empty_strings():
    assert is_anagram("", "") == True