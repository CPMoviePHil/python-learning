from time import time


def print_func_name(fn):
    def wrapper_1():
        print(f'Function Executing right now: {fn.__name__}')
        fn()
    return wrapper_1


def time_measure(fn):
    def wrapper_2():
        t1 = time()
        fn()
        t2 = time()
        print(f'{fn.__name__} take {t2-t1} seconds to perform')
    return wrapper_2


@time_measure
@print_func_name
def useless_func():
    print('i\'m kinda useless...')
    for value in range(1000000):
        pass


useless_func()
# useless_func = time_measure(print_func_name(useless_func))
# useless_func會先吃到print_func_name此decorator等定義
# 然後才吃到time_measure等decorator的定義
