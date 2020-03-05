# enumerate, creating an iterable object that can access index, and values of what you gave in enumerate function
# tuple
print('tuple:')
for index, value in enumerate((1, 2, 3)):
    print(f'index:{index}, value:{value}')
# dictionary
print('\ndictionary:')
for index, value in enumerate({'weapons': 'guns', 'username': 'gamer1'}):
    print(f'index:{index}, value:{value}')
# dictionary, common way:
print('\ndictionary, common way:')
for index, value in {'weapons': 'knife', 'username': 'master2'}.items():
    print(f'index:{index}, value:{value}')
# list
print('\nlist:')
for index, value in enumerate(list(range(0, 3))):
    print(f'index:{index}, value:{value}')
# list, test
print('\nlist, test:')
for index, value in enumerate(list(range(0, 100))):
    if index is 50:
        print(f'{index} index\'s value is {value}')
# set
print('\nset:')
for index, value in enumerate({1, 2, 3, 4, 5}):
    print(f'index:{index}, value:{value}')
