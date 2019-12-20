# set 集合
my_set1 = {1, 2, 3, 4, 5, 2, 5, 5, 6}
print(f'my_set1: {my_set1}')
print('因為set再被執行的時候，不會存放在記憶體相鄰的位置，造成set沒有order、排列的順序，所以也沒辦法用index的方法access set中的item')
print(f'my_set1[1]:{my_set1}')
my_tuple = ('a', 'b', 'd', 'a', '1')
my_list = [1, 2, 3, 4]
my_dict = {
    'a': '1',
    'b': 'weapons',
    'name': 'user',
    'a': 'wtf',
}
# print(f'list(my_tuple): {list(my_tuple)}')

# set是沒有順序的dict(object)
print(f'set(my_tuple): {set(my_tuple)})')
# print(f'dict(my_tuple: {dict(my_tuple)}')
print(f'set(my_dict): {set(my_dict)}')
print(f'tuple(my_dict): {tuple(my_dict)}')
