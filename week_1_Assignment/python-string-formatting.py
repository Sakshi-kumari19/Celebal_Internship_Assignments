""" python-string-formatting: Demonstrates ways to format and align strings and numbers for clean output."""
def format_numbers(limit):
    """
    Prints numbers from 1 to 'limit' in:
    - Decimal
    - Octal
    - Hexadecimal (uppercase)
    - Binary

    Output is aligned based on the widest binary number.
    """

    # Calculate the width needed for alignment based on binary format of the limit
    binary_of_limit = bin(limit)        
    width = len(binary_of_limit) - 2   

    # Loop through numbers from 1 to limit
    for number in range(1, limit + 1):
        # Decimal format
        decimal_value = str(number)

        # Octal format (removing '0o' prefix)
        octal_value = oct(number)      
        octal_value = octal_value[2:]  

        # Hexadecimal format (remove '0x' and convert to uppercase)
        hex_value = hex(number)         
        hex_value = hex_value[2:].upper()

        # Binary format (remove '0b')
        binary_value = bin(number)      
        binary_value = binary_value[2:]

        # Print all values with proper alignment
        print(decimal_value.rjust(width),
              octal_value.rjust(width),
              hex_value.rjust(width),
              binary_value.rjust(width))


format_numbers(17)
