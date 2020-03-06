list1 = [2, 3, 5]
# square all the item
print(list(map(lambda iterable: iterable * iterable, list1)))

tuple1 = [(0, 2), (4, 3), (9, 9), (10, -1)]
# sorted by second item
tuple1.sort(key=lambda iterable: iterable[1])
print(tuple1)
