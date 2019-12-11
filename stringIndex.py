# string[start:stop:stepover]
# start是字串index初始的位置，後面沒有其他參數的話就是index，stop是字串的index最終位置，只不過只會取到stop index的前一個字串元素
indexString = '0123456789'
print(indexString[4])       # 4
print(indexString[8:])
print(indexString[0:5])     # 012345
print(indexString[-1])      # 9
print(indexString[-3:10])   # 789
print(indexString[:-7])
# 負數的話就會從尾部開始算index
# string後面的參數都一定是從字串前面算到尾部的，所以stop的起始位置就對不行大於start的起始位置
