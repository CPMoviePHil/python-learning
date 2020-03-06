# Higher order function, two rules:
# 1. function take another function as the parameter
# 2. function return another function


def outside_function(func):
    def inside_function():
        print('mars!!')
        return func()
    return inside_function


def test_1():
    print('My name is test-1')


alpha = outside_function(test_1)
# print(alpha)
# print(test_1)
alpha()


@outside_function
def test_2():
    print('hello wtf?')
    return 'wtf'


print(test_2())
# decorator做的事情22-24行，跟16-19行做的事情一樣
# 只是為了讓人更容易閱讀程式才用Decorator包著
