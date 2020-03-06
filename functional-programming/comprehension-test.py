list1 = ['a', 'b', 'n', 'c', 'a', 'n', 'b']
new_list1 = list(set([value for index, value in enumerate(list1) if list1.count(value) > 1]))
print(new_list1)

