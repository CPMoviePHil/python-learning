import datetime

birth_year = input('what year were you born: ')
current_year = datetime.datetime.now().year
print(current_year)
age = int(current_year) - int(birth_year)
print(f'your current age is {age}')