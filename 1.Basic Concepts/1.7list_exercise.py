my_destination=['lijiang','gugong','gulangyu','Maldives','Mount Fuji']

print(my_destination) #原有順序
print(sorted(my_destination)) #字母順序且不保存
print(my_destination) #測試原順序
print(sorted(my_destination,reverse=True)) #反字母順序且不保存
print(my_destination) #測試原順序

print("分割\n一下")

my_destination.reverse()
print(my_destination)

my_destination.reverse()
print(my_destination)

my_destination.sort()
print(my_destination)

my_destination.sort()

print(my_destination)

finished_destination=my_destination.pop(2)
print(finished_destination)
