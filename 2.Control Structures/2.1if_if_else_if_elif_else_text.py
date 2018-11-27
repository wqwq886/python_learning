# 注意冒號

cars=['audi','bmw','subaru','toyouta']

for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())

# 比較方法  ==,>=,<=,!=   與and 或or 是否包含在列表 in 不包含在列表中 not in
# if-elif-else 只能執行一個代碼塊，不滿足全部條件最後執行else后代碼，可省略掉else 達成不滿足條件什麽也不執行。

age=12

if age<=4:
    print('免費')
elif age<18:
    print('五元')
else:
    print('十元')

caidan=['mushrooms','extra cheese']
if 'mushrooms' in caidan: #字符串類型必須加''
    print("\n上蘑菇")
