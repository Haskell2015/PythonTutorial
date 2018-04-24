# 列表的一些其他操作
magicians = ['alice', 'david', 'carolina']

# 遍历列表（缩进是属于循环体；反之，则不是--注意缩进即可）
for magician in magicians:
    print(magician)
    print("Hello\n")

print("thx everyone")

# 创建数值列表
# range(x,y)左闭右开=[x,y)
for value in range(1, 5):
    print(value)

numbers = list(range(2, 8))
print(numbers)

numbers = list(range(1, 7, 2))
print(numbers)

squares = []
for value in range(1, 11):
    # **2表示平方，这个临时变量也是可以省略的
    square = value ** 2
    squares.append(square)

print(squares)

# 获取列表中的最值等
digits = list(range(1, 10))
print("最小值：" + str(min(digits)))
print("最大值：" + str(max(digits)))
print("总数量：" + str(sum(digits)))

# 列表解析

squares = [value ** 2 for value in range(1, 5)]
print(squares)

# 判断是否在列表中
print(3 in squares)

# 4.4 使用列表的一部分
players = ['charles', 'martina', 'michael', 'florence', 'eli']
# 同样是左闭右开区间
print(players[1:3])
# 不指定起始则从头开始
print(players[:2])
# 同样的末尾不指定则到最后，这里需要注意的是如果起始位置越界了不会报错，只是会返回空的列表
print(players[4:])
# 还记得之前使用-1来获取最后的一个数吗?
print(players[-1:])

# 遍历切片
for player in players[1:3]:
    print(player)

# 复制切片
persons = players[:]
print(persons)
print(persons[0:3])

persons = players[1:3]
persons.append('Toms')
print(persons)

# 4.5元组
# 元组不能修改里面的值！
dimensions = (100, 200)
print("第一个：" + str(dimensions[0]))
print("第二个：" + str(dimensions[1]))

# 遍历元组
for dimension in dimensions:
    print(dimension)

# 改变元组--直接修改元组的变量
print(dimensions)
dimensions = (200, 400)
print(dimensions)

# 4.6设置代码格式： Python Enhancement Proposal， PEP
# PEP 8建议每级缩进都使用四个空格
# PEP 8还建议注释的行长都不超过72字符
# 要将程序的不同部分分开， 可使用空行
