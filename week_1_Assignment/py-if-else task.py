""" py-if-else task: Uses conditional statements (if-elif-else) to make decisions based on input values. """

def classify_file_size(file_size):
    """
    Scenario : Classify a file based on its size in MB.

    Parameters:
    - file_size: int, file size in megabytes (MB)

    Returns:
    - A string indicating the size category
    """
    if file_size < 100:
        return "Small File"
    elif 100 <= file_size <= 500:
        return "Medium File"
    elif 501 <= file_size <= 1000:
        return "Large File"
    else:
        return "Very Large File"

# Taking user input
file_name = input("Enter the file name: ")
file_size = int(input("Enter file size in MB: "))

# Get classification label
label = classify_file_size(file_size)

# Display the result
print(f"File: {file_name} | Size: {file_size} MB -> Category: {label}")
