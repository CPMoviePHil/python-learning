class CommonAction:
    @staticmethod
    def user_login():
        print('successfully login!')

    @staticmethod
    def user_logout():
        print('log out successfully')


class Wizard(CommonAction):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'{self.name} wizard is attacking with power of {self.power}')


class Archer(CommonAction):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        self._calculate_num_arrows()
        print(f'{self.name} archer is attacking! arrows left {self.num_arrows}')

    def _calculate_num_arrows(self):
        self.num_arrows -= 1


archer1 = Archer('Legalos', 300)
archer1.user_login()
archer1.attack()
archer1.attack()
archer1.user_login()
