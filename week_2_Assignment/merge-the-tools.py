"""merge-the-tools : Split a string into equal parts of length and Convert each parts by removing any subsequent occurrences of non-distinct"""

def merge_tools(string: str, k: int):
    """
    Splits the string into substrings of size k and removes duplicate characters in each substring.
    """
    for i in range(0, len(string), k):
        segment = string[i:i + k]
        unique = ""
        for char in segment:
            if char not in unique:
                unique += char
        print(unique)

# Input
input_string = input()
k = int(input())
merge_tools(input_string, k)
