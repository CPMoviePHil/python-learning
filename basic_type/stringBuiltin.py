quote = 'HEllo Earthers. I\'m from the Mars. To Prepare to conquer you all.'
print(quote.replace('to', '2'))
print(quote.upper())
print(quote[0:len(quote)])
print(len(quote))
# 為什麼string.replace不會影響到quote在記憶體儲存的值呢?
# 我們只是藉由quote去產生另一個字串，並沒有給該值指派給quote或其他變數
# 字串在python是沒辦法突變的，意思是說quote會存著"HEllo Earthers...."的值是因為在python把該字串以單字元分解成好幾個
# 然後每個字元在記憶體都有一個空間位置儲存，單要使用該字串的時候就會去記憶體裡面找字串有的位置
# 而就因此因素，python的string是沒辦法突變的，不行從拿單一字元在記憶體的位置去改變該值，除非創造一個新值重新指派給字串變數，不然值都沒辦法改變
