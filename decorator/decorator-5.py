
def print_func_name(fn):
    def wrapper():
        print(f'{fn.__name__} function want\'s to shout!')
        fn()
    return wrapper


def dog():
    pass


@print_func_name
def cat():
    pass


print_func_name(dog)()
# 解析
# dog = print_function_name(dog)
# dog => def wrapper
# 執行dog()

cat()
