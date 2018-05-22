# 函数返回值
# 返回简单值
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)


# 让实参变成可选的---中间使用''默认实现
def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)


# 返回字典
def build_person(first_name, last_name):
    """返回一个字典， 其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    return person


musician = build_person('jimi', 'hendrix')
print(musician)


# 结合使用函数和while 循环

def greet(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name.title()


while True:
    print("\n Please tell your name:")
    fir_name = input("Input your first name:")
    las_name = input("Input your last name:")
    greetStr = greet(fir_name, las_name)
    print("Hello," + greetStr)
