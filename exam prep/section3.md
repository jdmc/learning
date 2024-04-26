[Back2Overview](https://github.com/jdmc/learning/blob/master/exam.md)  
# PCAP Exam Prep: Section 3: Strings (score + weight =18%  8 items)

## Machine Representation of Characters:

- Characters are the basic building blocks of text.
- Computers store characters using encoding standards, which define how each character is represented as a sequence of bits (0s and 1s).
- ASCII (American Standard Code for Information Interchange): A common early encoding that represents basic English characters (letters, numbers, punctuation) - using 7 bits per character.
- Unicode: A universal character encoding standard that can represent a much wider range of characters, including those from almost all writing systems. Each - character in Unicode has a unique code point, an integer value that identifies it.
- UTF-8 (Unicode Transformation Format - 8): A popular encoding for Unicode that represents characters using a variable number of bytes (1 to 4) depending on - the code point. This makes it efficient for storing text in most languages.
- Escape sequences: Special backslash (\) notations used to represent non-printable characters or special characters within strings (e.g., \n for newline, \" - for double quote).

## Operating on Strings:

- ord(char): Converts a character to its corresponding Unicode code point (integer).
- chr(code_point): Converts a Unicode code point (integer) to its corresponding character.
- Indexing and Slicing: Accessing characters or substrings using zero-based indexing (string[index]) and slicing (string[start:end:step]). Strings are - immutable (unchangeable) after creation.
- Iterating: Looping through characters of a string using a for loop.
- Concatenation (+): Joining strings to create a new string.
- Multiplication (*): Repeating a string a specified number of times.
- Comparison (==, !=): Comparing strings for equality or inequality (compares characters one-by-one).
- in and not in: Check if a substring is present (or not) within a string.

## Built-in String Methods:

- .isxxx() methods: Check various string properties (e.g., .isalnum(): checks alphanumeric characters, .isupper(): checks uppercase).
- .join(iterable): Joins elements of an iterable (like a list) using the separator string between them.
- .split(sep=None, maxsplit=-1): Splits a string into a list of substrings based on the delimiter (sep) and maximum number of splits (maxsplit).
- .sort(): Sorts characters of the string in-place (modifies the original string).
- sorted(string): Returns a new list containing the sorted characters of the string (doesn't modify the original).
- .index(substring, start=0, end=len(string)): Finds the index of the first occurrence of a substring within the given search range.
- .find(substring, start=0, end=len(string)): Similar to .index(), but returns -1 if the substring is not found.
- .rfind(substring, start=0, end=len(string)): Finds the index of the last occurrence of a substring within the given search range.