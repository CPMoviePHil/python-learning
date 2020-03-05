# my_set1 = {1, 'a', True, {'a': 'alpha', 'weapons': 'guns'}, (1, 3), ['a', 'b', 'c']}
print('immutable的資料結構或者資料不能放到set(集合)裡面當作資料喔!，上面那行執行會有錯誤')
my_set1 = {1, 'a', True, (1, 3)}
print(f'my_set1: {my_set1}')
# 在記憶體創造另一系列的新值(另一個集合)，指向new_set1
# 所以你對my_set1什麼樣的操作，都不會影響到new_set1
# 因為兩個集合是指向不同的記憶體空間
# 由於集合並沒有依順序存放在記憶體，它們沒有Index可以用，所以操作值就變成能分辨他們的辦法惹
new_set1 = my_set1.copy()
my_set1.clear()
print(f'my_set1: {my_set1}')
print(f'new_set1: {new_set1}')
