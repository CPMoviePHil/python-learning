# two rules

# not to affect outside scope of the function
# whenever put the things into the function, always get the same results
# ex: 1 => function A => 2
# ex: 2 => function A => 4
# the point of pure function is to separate the data and the function
# making the code clean, and easier to maintain


def list_multiply_by_2(li):
    for index, value in enumerate(li):
        li[index] = value * 2
    return li


list1 = [1, 2, 3]
list2 = [2, 4, 6]
print(list_multiply_by_2(list1))
print(list_multiply_by_2(list2))
