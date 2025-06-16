"""exceptions : implementing exception handling"""

def safe_division(a: int, b: int) -> str:
    try:
        return str(a // b)
    except ZeroDivisionError as e:
        return f"Error Code: {e}"
    except ValueError as e:
        return f"Error Code: {e}"

# Input
t = int(input())
for _ in range(t):
    try:
        a, b = map(int, input().split())
    except ValueError as e:
        print(f"Error Code: {e}")
    else:
        print(safe_division(a, b))
