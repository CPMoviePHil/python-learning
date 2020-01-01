class Automobile:
    def __init__(self, brand, name):
        self.car_brand = brand
        self.car_name = name

    # you can access this method but doesn't have to instantiate the class
    @classmethod
    def run(cls, speed):
        if speed > 0:
            return f'car is running'
        # cls means the Automobile class
        # but you can not access the attributes of Automobile, because when
        # you use class method, you don't run __init__ method

    @classmethod
    def re_init(cls):
        return cls('tesla', 'handsome-1')

    @staticmethod
    def speed_account(num1, num2):
        # just like class method, but doesn't have the cls can use
        return num1 + num2


print(Automobile.run(20))
car1 = Automobile.re_init()
print(car1.car_brand)
print(Automobile.speed_account(10, 50))
print(car1.speed_account(10, 20))