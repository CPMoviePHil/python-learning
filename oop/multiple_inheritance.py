class User:
    # def __init__(self, name, mail):
    #     self.name = name
    #     self.mail = mail

    def get_mail(self):
        return self.mail

    def get_name(self):
        return self.name


class Wizard(User):
    def __init__(self, life, power, name, mail):
        # super().__init__(name, mail)
        self.life = life
        self.power = power
        self.name = name
        self.mail = mail

    def get_life(self):
        return self.life

    def attack(self):
        self._calculate_power('attack')
        print(f'{self.name} is attacking right now, power left : {self.power}')

    def _calculate_power(self, action):
        if action == 'attack':
            self.power -= 1


class Archer(User):
    def __init__(self, life, arrows, name, mail):
        # super().__init__(name, mail)
        self.life = life
        self.arrows = arrows
        self.name = name
        self.mail = mail

    def attack(self):
        self._calculate_arrows('attack')
        print(f'{self.name} is now shooting arrows! arrows-left : {self.arrows}')

    def run(self):
        self._calculate_life('run')
        print(f'{self.name} is running fast! life-left : {self.life}')

    def _calculate_arrows(self, action):
        if action == 'attack':
            self.arrows -= 1

    def _calculate_life(self, action):
        if action == 'run':
            self.life -= 1


class UltimateWizard(Wizard, Archer):
    def __init__(self, life, power, arrows, name, mail):
        Wizard.__init__(self, life, power, name, mail)
        Archer.__init__(self, life, arrows, name, mail)


player1 = UltimateWizard(1000, 300, 50, 'Michael Jackson', 'MichaelJackson@gmail.com')
player1.attack()
player1.run()
# wizard1 = Wizard(50, 100, 'Jordon', 'Jordon@Jordon.nba.com')
# wizard1.attack()
# archer1 = Archer(50, 200, 'Robin Hood', 'robinhood@gmail.com')
# archer1.run()
# archer1.attack()
