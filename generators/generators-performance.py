from time import time


def performance(fn):
    def inside_func(*args, **kwargs):
        t1 = time()
        fn(*args, **kwargs)
        t2 = time()
        print(f'{fn} take {t2-t1} s\n')
    return inside_func


@performance
def not_generators(num):
    for i in list(range(num)):
        i * 1


@performance
def is_generators(num):
    for i in range(num):
        i * 1


times = 10000000
not_generators(times)
is_generators(times)
