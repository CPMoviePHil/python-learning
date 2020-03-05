username = input('enter username:')
password = input('enter password:')
counter = len(password)
show_password = '*' * counter
print(f'{username}, your password {show_password} is {counter} letters long')
