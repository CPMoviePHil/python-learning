def highest_even(my_list):
    highest = my_list[0]
    counter = 1
    while counter < len(my_list):
        if my_list[counter] % 2 is 0 and highest < my_list[counter]:
            highest = my_list[counter]
        counter += 1
    return highest


list_1 = [1, 20, 3, 4, 7, 9]
print(highest_even(list_1))
