class PlayerCharacter:
    def __init__(self, param1, param2):
        self.age = param1
        self.sex = param2

    def get_bio(self):
        return f'age:{self.age}, sex:{self.sex}'


player1 = PlayerCharacter(17, 'male')
print(player1)
print(player1.age)
print(player1.sex)
print(player1.get_bio())