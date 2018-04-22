data = [0, 1, 2, 3, 4, 5, 6]

# 修改数据
data[-1] = 10
print(data)

# 增加数据
data[-1] = 6
data.append(7)
print(data)

# 初始化
data2 = []
data2.append(100)
data2.append(101)
print(data2)

# 插入数据
data.insert(0, -1)
print(data)
data.insert(-1, 8)
print(data)

# 删除数据
del data[-2]
print(data)

firstData = data.pop()
print(firstData)
print(data)

# 删除并获取第二个索引的数据
secondData = data.pop(1)
print(secondData)
print(data)

# 使用remove删除制定值
val4 = data[4]
print("我要删除值是" + str(val4) + "的数据")
data.remove(val4)
print(data)

data = [1, 2, 3, 4]
print(data)
print("在中间插入一个100")
length = len(data)
print("列表的长度：" + str(length))
data.insert(int(len(data) / 2), 100)
print(data)

# sort永久排序
newData = ["China", "Japan", "English", "Canada", "France"]
newData.sort()
print(newData)
# 倒序(也是永久)
newData.sort(reverse=True)
print(newData)

# sorted()临时排序
print(sorted(newData))
print(newData)
# reverse()反转输出（永久修改顺序）
print("反转输出")
newData.reverse()
print(newData)

# len()确定长度
print("newData的length:" + str(len(newData)))

# 当且仅当列表为空的时候，通过-1来获取最后的一个元素才会出错
