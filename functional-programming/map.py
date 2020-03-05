
# 專門處理能被迴圈跑的資料型別的內建function

list1 = [1, 2, 3, 4]
# object
dict1 = {
    'name': 1,
    'weapon': 2,
}
# the array can't change
tuple1 = (1, 2, 3, 4, 5)
# ex. tuple[0] = x

# unsorted object, more like collection, every item in it must be distinct
set1 = {1, 2, 3, 4, 4}


def multiply_by_2(iterable):
    return iterable * 2


print(list(map(multiply_by_2, list1)))
print(list(map(multiply_by_2, dict1)))
print(tuple(map(multiply_by_2, tuple1)))
print(set(map(multiply_by_2, set1)))
