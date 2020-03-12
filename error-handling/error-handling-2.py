def sum(num1, num2):
    try:
        return num1 + num2
    except ValueError:
        print(f'error : {ValueError}')
    except NameError:
        print(f'error : Can\'t find the definition of the value')
    except TypeError:
        print(f'error : Please enter 2 same type objects')
    except EOFError:
        print(f'error : {EOFError}')


print(sum(1, '456123'))


def divided(num1, num2):
    try:
        return num1 / num2
    except ValueError as err:
        print(f'{err}')
    except (ZeroDivisionError, TypeError) as err:
        print(f'{err}')


print(divided(1, 0))

