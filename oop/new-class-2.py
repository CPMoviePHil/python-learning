class PlayerCharacter:
    # Class Object Attribute
    membership = True

    def __init__(self, name, sex, age):
        # class attributes
        self.name = name
        self.sex = sex
        self.age = age

    def change_age(self, new_age):
        self.age = new_age

    def add_weapon(self, weapon):
        self.weapon = weapon

    def change_membership(self):
        self.membership = False

    def get_membership(self):
        return self.membership

    def get_self(self):
        return self.__getattribute__('weapon')


player1 = PlayerCharacter('phil', 'male', 16)
player2 = PlayerCharacter('Jordon', 'female', 27)

# print(f'player1\'s weapon is {player1.weapon}')
player1.add_weapon('claymore')
print(f'player\'s weapon is {player1.weapon}')

''' 必須執行add_weapon()後，才會在player1裡面加入weapon屬性'''

player1.change_membership()
print(f'player1\'s membership is {player1.membership}')
print(f'player1\'s self is {player1.get_self()}')
