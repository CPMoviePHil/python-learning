# 為什麼python需要oop這種概念?
# 我猜有兩個原因
# 1. 原因1，程式越變越大，為了配合各種整合開發，所以才會在Python中套用這種開發藍圖
# 2. 原因2，就跟現實的世界一樣，用藍圖－實作藍圖後的物件來代表事物，讓程式語言更接近人類所使用的工具
# 什麼是class
# 1. 代表一種事情、物質的藍圖，像是事情的特徵、能做到事情，再被編譯時會被寫進記憶體
# 為什麼class可以建立object
# 1. 因為物件(現實的事物)，需經過一定的規劃，才能製造出來吧?
# 什麼又是object
# 1. 當藍圖畫好後，描述好後，要真的使用的時候，不能拿藍圖來用，而是要拿以藍圖做的東西來使用，那就是物件，依藍圖所製造出的事或物
# 為什麼建立程式的世界需要object
# 就跟程式需要class的原因接近，只是object是接近人類使用的工具，一個只是藍圖
# class要怎麼建立object
# 1. 透過實作類別，那就是執行類別的建構子。而建構子所產生的例子(回傳的東西)，就是物件


class FirstClass:
    pass


first_created_object = FirstClass()
print(type('FirstClass()'))
print(type(FirstClass))  # 因為所有類別都會繼承type類別
print(type(first_created_object))
