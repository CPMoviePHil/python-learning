class SuperList(list):
    def __str__(self):
        return 'Super List!'

    def __len__(self):
        return 1000


super_list1 = SuperList()
print(f'len(super_list1) : {len(super_list1)}')
print(f'super_list1.__len__ : {super_list1.__len__()}')

test_lists = [1, 2, 3, 4]
print(f'len(test_lists) : {len(test_lists)}')

print('因為繼承了list，多了append功能')
super_list1.append(1)
print(f'super_list1[0] : {super_list1[0]}')
