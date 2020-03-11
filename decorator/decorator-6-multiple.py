from time import time


def print_func_name(fn):
    def wrapper_1():
        print(f'Function Executing right now: {fn.__name__}')
        fn()
    return wrapper_1


def time_measure(fn):
    def wrapper_2():
        print(f'{fn.__name__} is executing!!')
        fn()
        # t1 = time()
        # fn()
        # t2 = time()
        # print(f'{fn.__name__} take {t2-t1} seconds to perform')
    return wrapper_2


@time_measure
@print_func_name
def useless_func():
    print('i\'m kinda useless...')
    for value in range(1000000):
        pass


useless_func()
# useless_func = time_measure(print_func_name(useless_func))
# useless()
# 執行useless()就是執行time_measure() -> wrapper2()
# wrapper2() 裡面fn()會print_func_name當參數執行
# print_func_name() -> wrapper1()
# wrapper1()會執行fn()也就是useless_func
# 所以print的順序會是
# wrapper1 is executing!(因為wrapper2的fn是吃到print_func_name也就是wrapper1)
# Function Executing right now: useless_func(因為wrapper1的fn吃到的是useless_func)
# 然後最後print i'm kinda useless