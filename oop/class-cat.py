class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        return f'{self.name} is running'


def oldest(my_dict):
    oldest_age = 0
    for index, value in my_dict.items():
        if value > oldest_age:
            oldest_age = value
    return f'The oldest cat is {oldest_age} years old'


cat1 = Cat('Boss', 4)
cat2 = Cat('Kobe', 45)
cat3 = Cat('Bryant', 23)
my_dict = {
    cat1.name: cat1.age,
    cat2.name: cat2.age,
    cat3.name: cat3.age,
}
print(oldest(my_dict))

