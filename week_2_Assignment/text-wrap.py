"""text-wrap : Task to wrap the string into a paragraph of given width ."""

import textwrap

def wrap_text(string: str, width: int) -> str:
    """
    Wraps the string to the given width using the textwrap module.
    """
    return textwrap.fill(string, width)

# Input
input_string = input()
max_width = int(input())
print(wrap_text(input_string, max_width))
