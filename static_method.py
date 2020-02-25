class PlayerCharacter:
    # class object attributes
    membership = True

    def __init__(self, name):
        self.name = name

    @classmethod
    def alternative_init(cls, name, age):
        temp_c = cls(name)
        temp_c.age = age
        return temp_c

    @staticmethod
    def number_plus(number1, number2):
        return number1 + number2


print(f'static method: {PlayerCharacter.number_plus(1, 2)}')
player1 = PlayerCharacter('Phil')
print(f'player1\'s name: {player1.name}')
player1.alternative_init('Jordon', 23)
print(f're init player1: player1\'s name, {player1.name}, player1\'s age, {player1}')
