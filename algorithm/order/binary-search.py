
# list再進行二元搜尋前，一定要先sort過，不然的還不如用linear search

li = [1, 2, 3, 4, 7, 11, 12, 24, 34]
li2 = [3]
tar = 3


def binary_search(list1, target):
    list1_len = len(list1)
    while True:
        if list1[list1_len // 2] == target:
            return list1_len // 2 + 1
        elif list1[list1_len // 2] > target:
            print(list1[:list1_len//2:])
            binary_search(list1[:list1_len//2:], list1_len//2)
        else:
            print(list1[list1_len//2::])
            binary_search(list1[list1_len//2::], list1_len//2)


li.sort()
print(binary_search(li2, tar))

