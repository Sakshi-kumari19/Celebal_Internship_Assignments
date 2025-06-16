"""py-set-discard-remove-pop : task based on discard(),remove() & pop()"""

n = int(input())
numbers = sorted(set(map(int, input().split())))

N = int(input())
for _ in range(N):
    cmd = input().split()
    operation = cmd[0]
    
    if operation == "pop":
        if numbers:
            numbers.pop(0)  # Remove from beginning
    elif operation == "remove":
        try:
            numbers.remove(int(cmd[1]))
        except ValueError:
            pass
    elif operation == "discard":
        if int(cmd[1]) in numbers:
            numbers.remove(int(cmd[1]))

print(sum(numbers))
num_operations = int(input())
operations = [input() for _ in range(num_operations)]

print(execute_set_operations(numbers, operations))
