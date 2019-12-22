my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0
for item in my_list:
    if isinstance(item, int):
        total += item

print(total)