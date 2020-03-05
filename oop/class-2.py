# 為什麼一個class要這樣定義?
# A1:為什麼要先寫出建構子呢?
# A2: 為什麼要在建構的時候就要放參數了呢?
# Q for A1 and A2: 也可以不依定要在建構的時候就丟參數進去，這只是方便以後創建的物件使用
# 像是player1.attack = attack，把global環境下的func指派給player1的attribute
# 而在class中的self指的就是物件藍圖本身，所以在實作物件的時候，藍圖中所寫的self會指向建構時所回傳的物件


class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def running(self):
        print(f'{self.name} is running right now')


def attack():
    print('attack')


player1 = PlayerCharacter('PHIL', 20)
player2 = PlayerCharacter('Mandy', 26)
player1.running()
print(player2.name)
player2.__init__('Jordan', 49)
print(f'player2.name:{player2.name}')
player3 = player2.__init__('John', 10)
# print(f'player3.name:{player3.name}')
print(f'player1.name:{player1.name}')
player1.attack = attack
player1.attack()
