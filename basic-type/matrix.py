# 2D-list
matrix = [[1, 2, 345, 1], ['a', 'c', 'd'], ['python', 'java', 'javascript']]
print(matrix[1][0])
print(matrix[0:3:1][1])
print(matrix[-3:3:2][1][0])    # python
# matrix[0:3:1]會產品新的一組list儲存在記憶體，[1, 2, 345, 1], ['a', 'c', 'd'], ['python', 'java', 'javascript']
# 所以matrix[0:3:1][1]會取得['a','b','c']
# 記得，使用list[start:stop:stepover]會在記憶體生成一個新的list
