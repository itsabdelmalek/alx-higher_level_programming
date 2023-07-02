#!/usr/bin/python3

"""
This module defines a function that prints a text with 2 new lines
"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Remove leading and trailing whitespaces from the text
    text = text.strip()

    # Define the characters that will trigger the indentation
    indent_chars = ['.', '?', ':']

    # Initialize the result string
    result = ""

    # Iterate over each character in the text
    for char in text:
        # Append the character to the result string
        result += char

        # Check if the character is in the indent_chars list
        if char in indent_chars:
            # Add two new lines after the indent character
            result += "\n\n"

    # Print the formatted text
    print(result, end="")
