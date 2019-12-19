user = {
    'name': 'Suzuki',
    'age': 20,
    'occupation': 'professional baseball player',
    'sex': 'male',
    'species': 'man',
}

# 測試在物件user中keys
print('age' in user)
print(user.get('country'))
print('name' in user.keys())

# 測試物件user中的values
print(20 in user.values())

# 更新物件user
user.update({'age': 48})
print(user['age'])
user.update({'country': 'japan'})
print(user)

# 對user中的key和value操作
print(user.items())
print('age' in user.items())
print(user.pop('name'))
print(user)
print(user.popitem())
print(user)