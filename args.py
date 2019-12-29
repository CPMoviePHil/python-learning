def super_func(*args):
    print(f'args:{args}')
    print(*args)


def super_func_2(first_param, *args):
    print(f'args:{args}')
    print(f'first param:{first_param}')


def super_func_3(first_param, *args, **kwargs):
    print(f'kwargs:{kwargs}')
    print(f'args:{args}')
    print(f'first param:{first_param}')


super_func('a', 'c', '1', 2, 3)
super_func_2('abc', '1', 14, 2, 4)
super_func_3('abcd', 'e', '1', f=20, abc=50)