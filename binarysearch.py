"""
Implementing binary search
A complexity of O(log2n)
Binary search works by at every jump leaving you with a decision: go right or go left
"""

numbers = [1, 3, 4, 5, 7, 9, 13, 14, 22, 34, 38,
           44, 53, 54, 56, 59, 90, 95, 717, 6756, 918845]

final = len(numbers)
init = 0
middle = final // 2

query = 56
jumps = 0

if query in numbers:
    while numbers[middle] != query:
        if query > numbers[middle]:
            init = middle
            middle = (final + init) // 2
            jumps += 1
        elif query < numbers[middle]:
            final = middle
            middle = (final + init) // 2
            jumps += 1

    print(f'It took us {jumps} jumps')
    print(f'{numbers[middle]} was found at index {middle}')
else:
    print(f'{query} not in list')
