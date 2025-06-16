"""alphabet-rangoli : pattern printing with the help of alphabets"""

def print_rangoli(size):
    import string
    letters = string.ascii_lowercase

    lines = []

    # Build the pattern line by line
    for i in range(size):
        left = letters[size-1:i:-1]  # Left part
        middle = letters[i:size]     # Middle to right
        full_line = '-'.join(left + middle)
        # Center align the line with width = 4*size - 3
        lines.append(full_line.center(4*size - 3, '-'))

    # Print top + bottom
    for line in lines[::-1] + lines[1:]:
        print(line)

# Input from user
n = int(input())
print_rangoli(n)
