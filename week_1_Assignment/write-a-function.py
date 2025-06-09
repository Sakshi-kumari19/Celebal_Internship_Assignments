""" write-a-function: Teaches how to define reusable blocks of code using the def keyword. """


def is_leap(year):
    """
    Check if a given year is a leap year.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Taking user input
year = int(input())
print(is_leap(2024))
