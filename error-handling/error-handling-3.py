
def my_decorator(fn):
    def wrapper(*args, **kwargs):
        print(f'{fn.__name__} is executing!')
        return fn(*args, **kwargs)
    return wrapper


def second_decorator(fn):
    def wrapper_2(*args, **kwargs):
        print(f'{fn.__name__} is executing!!')
        return fn(*args, **kwargs)
    return wrapper_2


@second_decorator
@my_decorator
def divided(num1, num2):
    try:
        print(num1 / num2)
    except (ZeroDivisionError, TypeError, ValueError) as err:
        print(f'{err}')
    else:
        print('successfully executed!')


divided(1, 20)
# divided = second_decorator(my_decorator(divided))
# divided()
# printing order
# 1. second decorator
# 2. my_decorator
# 3. divided

