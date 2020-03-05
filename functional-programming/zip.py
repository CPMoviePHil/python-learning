
# zipper together
# 把不同的iterables結合成一個tuple

list1 = [1, 2, 3, 4]
list2 = [1, 3, 4, 5]
list3 = ['a', 4, 'd', 'e']

print(list(zip(list1, list2, list3)))

# 以下是測試zip的code
list4 = [2, 3, 4]
list5 = [4, 5, 6, 7, 8]
print(list(zip(list4, list5)))
# 多出來的元素會不忽略，不會放到zip的object裡面

dict1 = {
    'name': 'phil',
    'weapon': 'knives',
    'sex': 'female',
}
tuple1 = (1, 3, 4)
set1 = {1, 2, 3, 'a', 4, 5}
print(list(zip(list4, dict1.values())))
print(list(zip(dict1, tuple1)))
print(list(zip(tuple1, set1)))
