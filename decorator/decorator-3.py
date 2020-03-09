from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'this function take {t1-t2} s')
        return result
    return wrapper


@performance
def in_the_loop():
    for i in range(100000000):
        pass


# in_the_loop = performance(in_the_loop)
in_the_loop()
