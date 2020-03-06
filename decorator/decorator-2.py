# Higher order function, two rules:
# 1. function take another function as the parameter
# 2. function return another function

# 以下註解請參考decorator-1.py
# decorator做的事情22-24行，跟16-19行做的事情一樣
# 只是為了讓人更容易閱讀程式才用Decorator包著
# 當執行outside_function的時候，只是把inside_function的定義傳回過去
# 像是上面傳給了alpha，然後執行alpha的時候
# 是執行了inside_function的定義
# 只是inside_function這個function含有func << 這個function定義的暫存記憶
# 所以執行inside_function的時候，能執行func
# 而func執行過後，回傳看func() < 回傳什麼


def outside_function(func):
    def inside_function(x):
        print('mars!!')
        return func(x)

    return inside_function


# 當用decorator裝飾test_2的時候，
# python應該已經執行了 test_2 = outside_function(test_2)這樣的動作


@outside_function
def test_2(greeting):
    print(greeting)
    return 'wtf'


# 所以下面這行的執行，是在執行inside_function
print(test_2('xxx'))  # <<我丟變數給test_2，所以inside_function也要定義參數才不會錯誤


# 以上假如要多增加一個參數，就連decorator也要改就太麻煩了，所以有另外一種變化方式

def outside_function_2(func):
    def inside_function(*args, **kwargs):
        return func(*args, **kwargs)
    return inside_function


@outside_function_2
def test_many_arguments_func(name, greeting, age, sex):
    print(f'name:{name}, greeting:{greeting}, age:{age}, sex:{sex}')


print(test_many_arguments_func)
test_many_arguments_func('phil', 'go fuck myself?', 23, 'male')

# 那以上既然test_many_arguments_func已經用了outside_function2裝飾過後
# 所以執行test_many_arguments_func已經是inside_function了，為什麼需要傳參數給test_..呢??
# 因為這樣才能傳給inside_function裡面執行func的那行阿
# 我猜test_...應該還是有以前身test_...的定義的記憶，在使用裝飾器的時候傳給了func這個參數吧?
