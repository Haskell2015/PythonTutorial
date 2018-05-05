cars = ['audi', 'bmw', "subaru", 'toyota']

# if-elif-else--进入一个后不会再进另一个
for car in cars:
    if car == 'bmw':
        print(car.upper())
    elif car == 'audi':
        print(car + ' is my car')
    else:
        print(car.title())

# python是区分大小写的
print(cars[-1] == 'bmw')
# lower()和upper()是不会改变原值的
print(cars[0].upper() == 'AUDI')

# 判断不相等
print(cars[-2].title() != 'subaru')

# 多条件检查（与或）--and&or
print((cars[0] == 'audi') and (cars[-1] == 'toyota'))
print((cars[0] == 'audi') or (cars[-1] == 'subaru'))

# 检测特定值是否在列表中
print('audi' in cars)
print('bmw' not in cars)

# 确定列表是否为空
teachers = []
if teachers:
    print("Have teachers")
else:
    print('Empty Array!')

# 练习
names = ['admin', 'lily', 'lucy', 'tom']
if names:
    for name in names:
        if name == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print('hello ' + name + ',thank you logging in again')
else:
    print('No names')
