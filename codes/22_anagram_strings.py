
"""Program 22: Check whether two strings are anagrams."""

def is_anagram(first, second):
    """Return True if both strings are anagrams."""
    first = first.replace(" ", "").lower()
    second = second.replace(" ", "").lower()

    return sorted(first) == sorted(second)

if __name__ == "__main__":
    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")

    if is_anagram(str1, str2):
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")