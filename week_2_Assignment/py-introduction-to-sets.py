"""py-introduction-to-sets: Calculate the avarges of items present inside a python set"""

def average_unique_heights(heights: list[int]) -> float:
    """
    Calculates the average of unique heights from a list.
    """
    unique_heights = set(heights)
    return sum(unique_heights) / len(unique_heights)

# Input
n = int(input())
height_list = list(map(int, input().split()))
print(average_unique_heights(height_list))
