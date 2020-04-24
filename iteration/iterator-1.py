
my_list = [1, 2, 3, 4]
print(my_list.__iter__())
t = iter([1, 2, 3, 4])
next(t)
next(t)
next(t)
next(t)
print(next(t))
