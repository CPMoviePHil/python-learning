# dictionary
my_dictionary = {
    'a': 1,
    'b': 2,
    'c': 3,
    123: 'abc',
    True: '2020',
}
my_list = [
    {
        'film-name': 'minority report',
        'film-type': 'sci-fi',
        'film-hour': '2HR',
    },
    {
        'film-name': 'dark city',
        'film-release-year': [
            '1996',
            '1998',
        ],
    }
]
another_list = list(range(1, 100))
print('a' in my_dictionary)
print(my_dictionary['a'])
print(my_list[1]['film-release-year'][0])
print(another_list)