while True:
    try:
        response = input('enter a number!:')
        print(10 / int(response))
        raise Exception('hello world!')
        # raise ValueError('wtf? you enter the value can\'t convert to the integer!')
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

# 因為在try的block不管程式錯誤為何or根本沒錯都會執行到關鍵字raise
# 有raise關鍵字的話，就一定會把程式停下來，然後丟出錯誤
# 所以else的block才執行不到(要try都沒問題的話，else才會執行)。
# 而raise丟出的錯誤訊息可以自己製作，像是用Exception class or 已經定義好的錯誤，(不過能輸入自己想要的錯誤)
