class PlayerCharacter:
    # class object attribute
    membership = True
    # can access it by self keyword or class name
    # because i guess there were a mechanism that, when creating the instance of the PlayerCharacter
    # there will

    def __init__(self, name, weapon):
        self.player_name = name
        self.player_weapon = weapon
        # class attribute
        # these attributes are only available when you instantiate this class
        # then, these attributes will bound to the class's instance, object
        # why is that?
        # because you can see what we wrote in the __init__ method
        # the self keyword, will point to the object when we run __init__ method

    def set_name(self):
        PlayerCharacter.player_name = 'Try to change something'
        return PlayerCharacter.player_name
        # will get an error
        # because python mechanism?


player1 = PlayerCharacter('JOHN', 'knife')
print(player1.set_name())
