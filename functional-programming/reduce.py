from functools import reduce


def accumulator(acc, iterable):
    return acc + iterable


def factorial(number, iterable):
    return number * iterable


print(reduce(accumulator, [1, 3, 4, 5], 1))
print(reduce(accumulator, {'name', 'hello'}, 'mars'))
print(reduce(factorial, [1, 2, 3, 4, 5, 6, 7, 8], 1))
