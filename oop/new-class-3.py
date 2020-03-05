class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Jordon', 12)
cat2 = Cat('Kobe', 2)
cat3 = Cat('Donald', 1)


# 2 Create a function that finds the oldest cat
def find_oldest_age(ages):
    ages.sort()
    return ages[-1]


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(find_oldest_age([cat1.age, cat2.age, cat3.age]))
