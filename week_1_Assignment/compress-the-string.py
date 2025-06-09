"""compress-the-string: Compresses a string by counting consecutive characters, often using itertools.groupby()."""

from itertools import groupby

def compress_string(input_string):
    """
    Compress the string by counting consecutive characters.
    Example: 'aaabb' -> ('a', 3) ('b',2)
              '1222311' -> ('1',1) ('2',3) ('3',1) ('1',2) """
  
    # calculate consecutive characters
    compressed = [(len(list(group)), char) for char, group in groupby(input_string)]

    # print compressed string
    for count, character in compressed:
        print(f"({character}, {count})", end=' ')
    
# Take user input
string = input("Enter String to commpress: ")
compress_string(string)
