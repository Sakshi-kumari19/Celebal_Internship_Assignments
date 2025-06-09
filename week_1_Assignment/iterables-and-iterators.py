""" iterables-and-iterators: Works with iterators and combinations to solve problems involving sequences and probabilities."""

from itertools import combinations

def probability_of_a(n, letters, k):
    """
    Calculate probability of getting at least one 'a' in k-combinations of the input letters.
    """
    total_combinations = list(combinations(letters, k))
    favorable_combinations = [combo for combo in total_combinations if 'a' in combo]
    probability = len(favorable_combinations) / len(total_combinations)
    print(f"{probability:.4f}")

# Example usage
n = 4
letters = ['a', 'a', 'c', 'd']
k = 2
probability_of_a(n, letters, k)
