class User:
    weapon = 'Claymore'

    @staticmethod
    def login():
        print('user login successfully')

    @staticmethod
    def logout():
        print('logout!!')

    def get_weapon(self):
        print(f'weapon is {self.weapon}')

    def change_weapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        print('wtf')

    def get_self(self):
        self.attack()
        print(f'User\'s self: {self.weapon}')
        return self


class Wizard(User):
    weapon = 'Fire'

    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Wizard {self.name} is attacking with power of {self.power}')

    def change_weapon(self, weapon):
        User.change_weapon(self, weapon)
        print('changing weapon!!')

    def test_func(self):
        print(f'Wizard\'s self:{self.weapon}')
        # 當使用父類別or其他類別的function的時候，一定要丟self進去的原因是因為要只派一個object給父類別/其他類別的function
        # 為什麼呢? 假如你仔細看，class裡面的function會存在是為了對class裡面方法和屬性作操作玩弄，所以都一定定義一個function的時候都會指派self給它使用
        # 讓function能access到屬性或者方法。
        # 所以當執行其他類別的function的時候，取得屬性、方法都是指派的object裡面的。
        # 像是User.get_self() << 當呼叫的時候並不知道要操作的物件是什麼
        # 只寫User.get_self()就有點像正常呼叫function而已，所以為了讓function正常運作，所以還要丟物件給他
        # 那為什麼同個類別中的Function呼叫的時候不用丟self(物件)給該呼叫呢?
        # 那是因為呼叫前面一定要先加上self的關係，已經知道是哪個object
        return User.get_self(self)


wizard1 = Wizard('Johnny', 50)
# print(wizard1.weapon)
# wizard1.change_weapon('Knife')
# print(wizard1.weapon)
wizard1.test_func()

# archer1 = Archer('Archer')
# for char in [wizard1, archer1]:
#     char.change_weapon('Crab')
# class Archer(User):
#     def __init__(self, name):
#         self.name = name
#
#     def change_weapon(self, weapon):
#         self.weapon = 'Hands'
#         print(self.weapon)
