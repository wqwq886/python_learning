# Python中用[]表示list列表，用 , 隔開其中的元素
# 用print直接打印列表，會把[]和其中所有内容顯示，很難看

name_myfamily=['weiqi','wangyelei','weilan']
print(name_myfamily)

# 用list[序號]可提取list中的元素
# 其元素可用其對應類型的所有方法
print(name_myfamily[0])
print(name_myfamily[0].title())

# 修改list中的元素

name_myfamily[0]="魏琪"
print(name_myfamily[0])

# 在list尾部增加元素 list.append(元素)

name_myfamily.append("金毛")
print(name_myfamily)

# 在list中任意位置增加元素 list.insert(int,元素)

name_myfamily.insert(0,'姚慧英')
print(name_myfamily)

# 刪除list中的元素
# del list[int] 根據元素位置刪除
# list.remove() 根據元素值刪除，只刪除找到的第一個元素

del name_myfamily[0]
name_myfamily.remove('金毛')
print(name_myfamily)

# 想刪除list中元素 還想使用該元素用 list.pop()
# 默認刪除最後一個，加數字刪除位置元素
name_youeryuan=name_myfamily.pop()
print(name_myfamily)
print(name_youeryuan)

