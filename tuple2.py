my_tuple = (1, 2, 3, 4, 'a', 6)
print(f'type(my_tuple):{type(my_tuple)}')
new_tuple = my_tuple[1:2]
new_tuple2 = my_tuple[1:5]
print(f'type(new_tuple):{new_tuple}, {type(new_tuple)}')
print(f'type(new_tuple2:{new_tuple2}, {type(new_tuple2)}')
x, y, z, *others = (1, 2, 3, 4, 5, 6)
print(f'type(x), type(y), type(z): {type(x)}, {type(y), type(z)}')
print(f'type(others):{type(others)}')

print(f'my_tuple.index(\'a\'):{my_tuple.index("a")}')
print(f'my_tuple.count(\'a\'):{my_tuple.count("a")}')
print(f'len(my_tuple):{len(my_tuple)}')

