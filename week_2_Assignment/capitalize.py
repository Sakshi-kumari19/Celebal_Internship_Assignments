"""capitalize : Task to make the first letter of every words as capital"""

def solve(s):
    # Split the string into words (including spaces)
    words = s.split(' ')
    
    # Capitalize each word and store in a new list
    result = []
    for word in words:
        result.append(word.capitalize())
    
    # Join the capitalized words back into a string
    return ' '.join(result)

# Input from user
s = input()
print(solve(s))
