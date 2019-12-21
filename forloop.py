# iterable collections in python
# data type: string
# data collection: dictionary, list, tuple(immutable list), set(unordered object, and unique values)
gamer1 = {
    'user_id': 'gamer1',
    'age': 18,
    'is_skilled': False,
}
# dictionary
for item in gamer1:
    print(item)
for item in gamer1.items():
    print(item)
for keys, values in gamer1.items():
    print(f'{keys}:{values}')
for key in gamer1.keys():
    print(f'keys:{key}')
for value in gamer1.values():
    print(f'values:{value}')

# number(integer), data type is not a collection of something, not like string
# for item in 50:
#     print(item)

# string, following piece of block will split the string into single character, because this is how string
# will store in memory. a ordered sequence of places in memory to point to identifier my_string
# but why not data type, integer
# because integer only has one place spot in memory, is not a collection of places
my_string = 'hello, have a great day'
for char in my_string:
    print(char)
