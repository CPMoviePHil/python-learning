def func_1():
    # a = 'abc'
    return a

def func_2():
    a = 'func2'
    return func_1()

def closure():
    a = 'closure'
    def inside_func():
        return a
    return inside_func

a = 'global'
print(func_2()) # print global
print(closure()()) # print closure