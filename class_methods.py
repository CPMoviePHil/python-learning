class PlayerCharacter:
    # class object attributes
    membership = True

    def __init__(self, name):
        self.name = name

    def get_membership(self):
        return self.membership

    @classmethod
    def get_greeting(cls, greeting):
        return greeting

    @classmethod
    def re_init(cls, name2):
        return cls(name2)


print(f'PlayerCharacter\'s membership: {PlayerCharacter.membership}')
print(PlayerCharacter.get_greeting('hello'))
# pre init attributes and functions of class


obj1 = PlayerCharacter.re_init('phil')
# print(obj1)
print(f'obj1\'s name is {obj1.name}')
