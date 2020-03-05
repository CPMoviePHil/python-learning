print('while-block code:')
i = 0
while i <= 40:
    print(i)
    i += 10
else:
    print(f'i is {i} now, done with this while-block')

# another writing
print('\nanother while-block code:')
i = 0
while i < 40:
    print(i)
    i += 10
    if i is 40:
        break

# but if there is 'break' statement in your while block code, it won't execute what's in else statement
print('\nanother while-else-block statement:')
i = 0
while i < 40:
    print(i)
    i += 10
    if i is 40:
        break
else:
    # won't execute following code, because there is break in the while block
    # and it make sense, cause keyword break, will escape the whole while-else block code
    print(f'value of i is {i} right now, done with while-block code')
