name_myfamily=['weiqi','jinmao','yezhi','zai']
# list.sort()对列表永久性排序（开头字母顺序）
# list.sort(reverse=Ture)開頭字母反向排序。
name_myfamily.sort()
print(name_myfamily)
name_myfamily.sort(reverse=True)
print(name_myfamily)

# sorted(listname) 对列表暂时排序 函數操作
# list.reverse 反向排列列表(不是字母順序)
# len.(list) 確定列表長度
# list[-1] 為檢索列表最後一個元素

abc=["wow","lol","sc2","steam"]
print(sorted(abc))
print(abc)

abc.reverse()
print(abc)
print(len(abc))
print(abc[-1])