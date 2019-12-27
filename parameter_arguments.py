

# 一般參數的function定義
# name, greeting 定義參數
def greeting(name, the_greeting):
    print(f'name: {name}')
    print(f'greeting: Hello, {name}, {the_greeting}')


# default parameters function
def default_party(time='6:30', place='Center Park'):
    print(f'We will hold a party in {place} and begin with the time {time}')


# 一般arguments的的呼叫，被稱作positional arguments，因為只要呼叫時，帶入function的變數position不對的話，執行所定義的function值就會顛倒
greeting('Johnson', 'you are so big')
greeting('WTH?', 'Brandon')

# keyword arguments
greeting(name='Donald', the_greeting='You are gonna fall')

# default parameters function
default_party('10:30', 'John\'s apartment')
default_party()
