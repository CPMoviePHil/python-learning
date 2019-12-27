def check_driver_age(user_age=0):
    user_age = input("What is your age?: ")
    user_age = int(user_age)
    if user_age > 18:
        return 'Powering On. Enjoy the ride!'
    elif user_age == 18:
        return "Congratulations on your first year of driving. Enjoy the ride!"
    elif 0 < user_age < 18:
        return "Sorry, you are too young to drive this car. Powering off"


print(check_driver_age())