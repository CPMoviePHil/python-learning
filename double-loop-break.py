def two_sum():
    for index, value in enumerate(range(0, 3)):
        print(f'index:{index}')
        for index_2, value_2 in enumerate(range(0, 4)):
            print(f'index_2:{index_2}')
            if (value + value_2) is 3:
                print([value, value_2])
                break


two_sum()
# break只會跳脫一層的重複迴圈，上面的程式測試後的結果
