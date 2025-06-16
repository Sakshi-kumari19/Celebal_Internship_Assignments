"""collections-counter : calculate the total earned amount"""

from collections import Counter

def calculate_total_revenue(shoe_sizes: list[int], customer_orders: list[tuple[int, int]]) -> int:
    """
    Calculates total revenue from selling shoes to customers with available sizes.
    """
    stock = Counter(shoe_sizes)
    total_income = 0

    for size, price in customer_orders:
        if stock[size] > 0:
            total_income += price
            stock[size] -= 1

    return total_income

# Input
_ = int(input())
shoe_inventory = list(map(int, input().split()))
num_customers = int(input())
orders = [tuple(map(int, input().split())) for _ in range(num_customers)]

print(calculate_total_revenue(shoe_inventory, orders))
