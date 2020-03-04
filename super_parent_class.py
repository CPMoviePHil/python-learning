
class Register:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def register_succeed(self):
        self.get_name()
        print(f'registered successfully, self:{self}')


class User(Register):
    def __init__(self, name, occupation, email, password):
        super().__init__(email, password)
        self.name = name
        self.occupation = occupation

    def register_succeed(self):
        super().register_succeed()
        print(f'hello user, self:{self}')

    def get_name(self):
        print(f'{self.email}\'s name is {self.name}')


# 藉由父類別的__init__，把email和password指派給User的物件
# 使用super的話，只是借用父類別(Register)的function，操作的物件還是User的
user1 = User('Phil', 'Archer', 'Phil@gmail.com', 'password')
user1.register_succeed()