from _collections_abc import Iterator, Iterable


class MyIterator:
    def __iter__(self):
        pass

    def __next__(self):
        pass



my_list = [1, 2, 3]
my_dict = {
    'a': 20,
    'b': 10,
    'c': 1,
}
my_tuple = (1, 2, 3, 4)
my_set = {1, 2, 3, 4, 5}
print(f'my_list, iterable: {isinstance(my_list, Iterable)}, iterator:{isinstance(my_list, Iterator)}')
print(f'my_dict, iterable: {isinstance(my_dict, Iterable)} iterator:{isinstance(my_dict, Iterator)}')
print(f'my_tuple, iterable:{isinstance(my_tuple, Iterable)}, iterator:{isinstance(my_tuple, Iterator)}')
print(f'my_set, iterable: {isinstance(my_set, Iterable)}, iterator:{isinstance(my_set, Iterator)}')
# 是否是Iterable要看該物件是否有__iter__和__getitem__等方法，有此方法的話就能用loop迴圈跑過該物件內涵的項目
print(f'my_list, __iter__:{hasattr(my_list,"__iter__")}, __getitem__:{hasattr(my_list, "__getitem__")}')
# 而Iterator則是要有__iter__和__next__此兩個方法才能被稱作Iterator
my_iterator = MyIterator()
print(f'my_iterator, iterable: {isinstance(my_iterator, Iterable)}, iterator:{isinstance(my_iterator, Iterator)}')
