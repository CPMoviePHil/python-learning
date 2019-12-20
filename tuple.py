# immutable lists
my_tuple = (1, 3, 4, 5)
new_tuple2 = my_tuple
print(f'my tuple: {my_tuple}')
print(f'my tuple[0]: {my_tuple[0]}')

user = dict(age='20', name='godzilla')
print(f'user.items()，放著tuple的型態的list: {user.items()}')
user2 = {
    (1, 2): '1, 2的tuple',
    (3, 4, 5): '3, 4, 5的tuple',
}
# 因為tuple是immutable的list，所以能當作dictionary的keys(property)
print(f'user2[(1,2)]:{user2[(1,2)]}')
print(f'user2.keys():{user2.keys()}')
print(f'user.keys():{user.keys()}')
print(f'my_tuple[1::]:{my_tuple[1::]}')
print(f'my_tuple[1:2]:{my_tuple[1:2]}')

