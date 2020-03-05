
# filter這個函式跟map一樣都是內建的，都是接收一個iterables(可以用loop操作的資料)
# 然後針對每一個iterable做個別處理，接者return回去

# map是每處理一個iterable，就會回傳一個東西給新的object

# 而filter則每處理一個iterable，然後判斷回傳值是true/false，
# 假如是true就原封不動的傳回該iterable到新的object
# 假如是false就不會回傳該iterable到新的object


def only_even(iterable):
    return iterable % 2 == 0


def multiply_by_2(iterable):
    return 2


list1 = [1, 2, 3, 4, 5]
new_list1 = map(multiply_by_2, list1)
print(new_list1)
print(list(new_list1))

new_list2 = filter(only_even, list1)
print(new_list2)
print(list(new_list2))
