"""py-set-discard-remove-pop : task based on discard(),remove() & pop()"""

def execute_set_operations(initial_set: set[int], commands: list[str]) -> int:
    """
    Executes given commands on the set.
    """
    for command in commands:
        parts = command.split()
        action = parts[0]

        if action == "pop":
            initial_set.pop()
        elif action == "remove":
            initial_set.remove(int(parts[1]))
        elif action == "discard":
            initial_set.discard(int(parts[1]))

    return sum(initial_set)

# Input
n = int(input())
numbers = set(map(int, input().split()))
num_operations = int(input())
operations = [input() for _ in range(num_operations)]

print(execute_set_operations(numbers, operations))
