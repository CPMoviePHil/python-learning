from functools import reduce
# anonymous function, only used once.
# and once function execution finished, python will abandon the function not to take memory and resource.
# lambda param1, param2... : return param1 + param2

list1 = [1, 2, 3, 4]
print(list(map(lambda iterable: iterable * 2, list1)))  # list1中的每個項目*2
print(list(filter(lambda iterable: iterable % 2 != 0, list1)))  # 挑出偶數
print(reduce(lambda acc, iterable: acc + iterable, list1, 10))  # 10 + list1所有項目的總和
