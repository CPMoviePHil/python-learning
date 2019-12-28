def find_duplicate(my_list):
    temp_dict = {}
    duplicated_list = []
    for index, value in enumerate(my_list):
        if value in temp_dict.keys() and temp_dict[value] != 'added':
            temp_dict[value] = True
        else:
            temp_dict[value] = False
        if temp_dict[value]:
            duplicated_list.append(value)
            temp_dict[value] = 'added'
    return duplicated_list


some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n', 'b']
print(find_duplicate(some_list))