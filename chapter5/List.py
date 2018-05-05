# python中的列表对应Java中的数组，字典对应的是集合（Map）
# 是结构相同的组成的一个整体
# 获取--R
alien_0 = {'color': 'Green', 'point': 5}
print(alien_0['color'])
print(alien_0['point'])

# 添加--C
alien_0['x_position'] = 100
alien_0['y_position'] = 200
print(alien_0)

# 修改--U
alien_0['color'] = 'Red'
print(alien_0)

# 删除--D
del alien_0['y_position']
print(alien_0)

# 遍历字典
students = {'Tom': 'Java', 'Lily': 'C++', 'John': 'Kotlin', 'Jack': 'Swift'}
for name, language in students.items():
    print(name + ' like ' + language)

# 只获取key或者value
print('只获取key')
for name in students.keys():
    print(name)

print('只获取value')
for language in students.values():
    print(language)

# 类似的，内部是无序的，现在要求按特定的顺序返回
print('按字母顺序返回key或者value')
for name in sorted(students.values()):
    print(name)

print('按key的排序返回value')
for name in sorted(students):
    print(name + ' like ' + students[name])

# 嵌套
worker = {'worker1': 'worker1', 'worker2': 'worker2'}
farmer = {'farmer1': 'farmer', 'farmer2': 'farmer2'}
teacher = {'teacher1': 'teacher1', 'teacher2': 'teacher2'}

persons = [worker, farmer, students]
for person in persons:
    print(person)

# 在字典中存储列表
data = {'code': 404, 'result': ['lily', 'tom']}
for name in data['result']:
    print(name.title())

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print('\n' + name + "'s favorite languages are:")
    for language in languages:
        print('\t' + language)

# 字典中存储字典

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for user_name, user_info in users.items():
    print('\nUseName:' + user_name + '\r')
    fullName = user_info['first'] + user_info['last']
    address = user_info['location']
    print('Full Name:' + fullName.title() + '\r\n' + 'Address:' + address)
