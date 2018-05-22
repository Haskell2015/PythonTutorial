# 传递任意数量的实参--类比JDK1.5引入的不定参数
# 空元组--toppings


def make_pizza(*toppings):
    """打印Pizza"""
    print(toppings)
    for topping in toppings:
        print('--' + topping)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# 结合使用位置实参和任意数量实参
# 如果要让函数接受不同类型的实参， 必须在函数定义中将接纳任意数量实参的形参放在最后。

def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# 使用任意数量的关键字实参
# **info--空字典
def build_profile(first, last, **info):
    """创建一个字典来保存客户信息"""
    profile = {'first_name': first, 'last_name': last}
    for key, value in info.items():
        profile[key] = value
    
    return profile


user_profile = build_profile('albert', 'einstein',
                             location='princeton', field='physics')

print(user_profile)
