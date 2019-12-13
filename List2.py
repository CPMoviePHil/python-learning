basket = ['a', 'c', 'd', '0', 'e', 'e']
print(basket.count('e'))
print(0 in basket)

print(basket.append('c'))
print(basket.extend(['c', 'd', 'e']))
print(basket.insert(1, 'alpha'))
print(basket.index('d', 0, 10))


print(basket)
new_basket = basket[:]
basket.sort()
basket.reverse()
new_basket[0] = 'beta'
print(f'new:{new_basket}')
print(f'old:{basket}')