""" python-tuples: Introduces immutable sequences and their use in operations like hashing."""

def hash_tuple():
    """
    Create a tuple from user input and print its hash.
    """
    number_count = int(input("Enter number of elements: "))
    numbers = tuple(map(int, input("Enter numbers separated by space: ").split()))
    print("Hash of the tuple:", hash(numbers))

hash_tuple()
