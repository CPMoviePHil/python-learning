while True:
    try:
        response = input('enter a number!:')
        print(10 / int(response))
    except TypeError as err:
        print(f'error(different type object can\'t add up): {err}')
    except ValueError as err:
        print(f'error(can\'t convert the input to the number): {err}')
    except (ZeroDivisionError, EOFError, NameError) as err:
        print(f'error:{err}')
    else:
        print('finally successfully executed!')
        break
    finally:
        print('above codes have been executed finish!, and this will run every try-except block code executing.')

