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
# 當執行outside_function的時候，只是把inside_function的定義傳回過去
# 像是上面傳給了alpha，然後執行alpha的時候
# 是執行了inside_function的定義
# 只是inside_function這個function含有func << 這個function定義的暫存記憶
# 所以執行inside_function的時候，能執行func
# 而func執行過後，回傳看func() < 回傳什麼
