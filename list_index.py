amazon_cart = [
    'books',
    'apples',
    'guitars',
    'second-hand cars',
]
# 就跟變數-字串python處理的方式一樣，前面是指到記憶體的位置，後面字串的個別字元會個別儲存在記憶體
# 所以以這個例子來說，books、apples...等等會分別儲存在記憶體的某些位置，而amazon_cart這個變數會指向這些記憶體位置

print(amazon_cart[0])
print(amazon_cart[1:3])
print(amazon_cart[-3:-1])
print(amazon_cart[1::2])

# 以上面註解的話，我把amazon_cart分配給另一個變數，此變數就只是單純指向同樣的記憶體位置
new_cart = amazon_cart
new_cart[0] = 'waters'

print(new_cart[0])
print(amazon_cart[0])

# 以上輸出結果會是同樣的
# 假如意圖再指派給new_cart的時候希望不要指到同個記憶體位置的話，就必須重新依據amazon_cart再創一個新的list

# list[start:stop:stepover]
# start的初始值是0
# stop的初始值應該就是len(list)
# stepover初始值應該就是1

new_cart_2 = amazon_cart[::]

# 創造一個新的list(在記憶體再開一個空間儲存)，然後new_cart_2會指向該新位置
new_cart_2[0] = 'Cells'
print(amazon_cart[0])
print(new_cart_2[0])
