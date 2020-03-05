
my_set = {1, 2, 3, 4, 5}
own_set = {4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}

# 測試集合的內建的方法
print(f'my_set.difference(your_set): {my_set.difference(your_set)}')
# {1, 2, 3} 因為從my_set的觀點，跟your_set做比較，發現{1, 2, 3}的不一樣，{4, 5}是相同的，比較完後，把結果回傳

my_set.difference_update(your_set)
print(f'my_set.difference_update(your_set): {my_set}')
# 跟difference很像的method，不過會再做一個步驟，把my_set這個集合不一樣的地方留下來，更改my_set集合

my_set.discard(3)
print(f'在執行過my_set.discard(3)後的my_set: {my_set}')
print(f'own_set.intersection(my_set): {own_set.intersection(my_set)}')
# 不是false喔，而是一個空集合，{} or set()。我猜因為intersection就一定是要丟出一個set的method吧
print(f'own_set.intersection(your_set): {own_set.intersection(your_set)}')
# {4, 5}
own_set.intersection_update(your_set)
print(f'在經過intersection_update()後的own_set: {own_set}')
print(f'在經過intersection_update()後的your_set: {your_set}')
# 因為own_set本身此集合就完全在your_set此集合裡面，intersection_update也只能更新有交集的地方吧?

own_set2 = own_set.copy()
own_set2.add(20)
print(f'own_set2: {own_set2}')
own_set2.intersection_update(your_set)
print(f'在經過intersection_update()後的own_set2: {own_set2}')

# union、issubset、issuperset、isdisjoint、and、or
print(f'my_set.isdisjoint(your_set): {my_set.isdisjoint(your_set)}')
# 回傳true喔，因為本身沒有交流到，是disjoint
print(f'own_set.isdisjoint(your_set): {own_set.isdisjoint(your_set)}')
# 回傳false，因為交集到了
print(own_set.issubset(your_set))
# 回傳true，因為own_set完完全全包在your_set裡面
print(your_set.issubset(own_set))
# 回傳false，因為兩個集合沒有交流

print(f'own_set.issubset(your_set): {own_set.issubset(your_set)}')
print(f'your_set.issuperset(own_set): {your_set.issuperset(own_set)}')
print(f'your_set.issuperset(own_set): {your_set.issuperset(own_set)}')

# union
own_set2.union(your_set)
print(own_set2)

# or and
# my_set和your_set的union
print(f'my_set | your_set: {my_set | your_set}')
# my_set的intersection
print(f'set交集的縮寫: {own_set & your_set}')
