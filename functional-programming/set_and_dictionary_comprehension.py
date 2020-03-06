# set comprehension
set1 = {char for char in 'Michael Jackson'}
set2 = {num for num in range(1, 20)}
set3 = {num**num for num in range(1, 10) if num % 3 != 0}
print(set1)
print(set2)
print(set3)

# dictionary comprehension
dic1 = {
    'a': 'Alphabet',
    'name': 'Jordon',
    'b': 1,
    'c': 103,
    'd': 'test@test.com.tw',
    'e': 20,
}
dict2 = {k: v*2 for k, v in dic1.items()}
print(dict2)
dict3 = {k: k*2 for k in range(1, 5)}
print(dict3)
print(dict3[1])

