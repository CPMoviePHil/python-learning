def duplicate_item(my_list):
    temp_list = []
    for value in my_list:
        if my_list.count(value) > 1 and value not in temp_list:
            temp_list.append(value)
    return temp_list


some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n', 'b']
print(duplicate_item(some_list))

