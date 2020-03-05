
def multiply_by_2(iterable):
    return iterable * 2


list1 = [
    [1, 2, 3],
    [4, 5, 6],
]
for value in list1:
    print(list(map(multiply_by_2, value)))

