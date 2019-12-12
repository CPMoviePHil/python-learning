li1 = ['a', 'b', 'c', 'd', 'e', 'f']

# adding
li1.append('g')
print(li1)
li1.insert(0, "alpha")
print(li1)
li1.extend(['h', 'i'])
print(li1)

li2 = li1
li2[0] = 'beta'
print(li1)
print(li2)

# removing
li1.pop(0)
print(li1)
li1.pop()
print(li1)
print(li2)
li1.remove('a')
print(li1)
print(li2)
k = li2.pop()
print(k)
li1.clear()
print(li1)
print(li2)

