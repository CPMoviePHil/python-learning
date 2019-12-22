import math
i = 0
for item in range(10, 0, -1):
    i += 1
    if i % 2 == 1:
        print(' ' * math.ceil(item / 2) + f'{"*" * i}')
for item in range(10, 0, -10):
    print(' ' * math.floor(item / 2.5) + '*' * math.floor(item / 3))
    print(' ' * math.floor(item / 2.5) + '*' * math.floor(item / 3))