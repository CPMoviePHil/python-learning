# list comprehension


def create_number_list(start, end):
    new_list = list()
    while start < end + 1:
        new_list.append(start)
        start += 1
    return new_list


list1 = [num for num in range(1, 26)]
list2 = create_number_list(1, 25)
print(list1)
print(list2)

# list1和list2生成的list是一樣的，不過list1比較簡潔

list3 = [char for char in 'python hell yeah']
print(list3)
list4 = [num**2 for num in range(1, 30)]
print(list4)
list5 = [num**num for num in range(1, 10) if num % 2 != 0]
print(list5)

