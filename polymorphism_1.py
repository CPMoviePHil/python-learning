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


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Wizard {self.name} is attacking with power of {self.power}')

    def change_weapon(self, weapon):
        User.change_weapon(self, weapon)
        print('changing weapon!!')


class Archer(User):
    def __init__(self, name):
        self.name = name

    def change_weapon(self, weapon):
        self.weapon = 'Hands'
        print(self.weapon)


wizard1 = Wizard('Johnny', 50)
# print(wizard1.weapon)
# wizard1.change_weapon('Knife')
# print(wizard1.weapon)

archer1 = Archer('Archer')
for char in [wizard1, archer1]:
    char.change_weapon('Crab')