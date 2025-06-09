""" word-order: Counts and displays the number of occurrences of each word while preserving their input order."""

def word_order():
    """
    Count and display word occurrences in order of appearance.
    Does NOT use built-in functions like dict.get() or collections.
    """
    num_words = int(input("Enter number of words: "))
    
    unique_words = []   # List to maintain the order
    word_counts = []    # Parallel list to hold corresponding counts

    for _ in range(num_words):
        word = input().strip()
        
        # Check if the word already exists
        found = False
        for i in range(len(unique_words)):
            if unique_words[i] == word:
                word_counts[i] += 1
                found = True
                break
        
        # If word is not found, add to the list
        if not found:
            unique_words.append(word)
            word_counts.append(1)

    # Output results
    print(len(unique_words))
    for count in word_counts:
        print(count, end=" ")


word_order()

# Example usage:
# Input:
# 4
# apple
# banana
# apple
# orange
#
# Output:
# 3
# 2 1 1
