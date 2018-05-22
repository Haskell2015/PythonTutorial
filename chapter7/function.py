# 函数
def greet_user():
    # 文档字符串 （ docstring） 的注释， 描述了函数是做什么的。 文档字符串用三引号括
    # 起， Python使用它们来生成有关程序中函数的文档
    """显示简单的问候语"""
    print("Hello Python")


greet_user()


# 带形参的函数
def say_hello_2_someone(user_name):
    """传入名字"""
    print('Hello ' + user_name)


say_hello_2_someone("John")


# 最简单的关联方式是基于实参的顺序。 这种关联方式被称为位置实参
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('hamster', 'harry')
# 可以多次调用
describe_pet('dog', 'willie')

# 关键字实参 --是传递给函数的名称—值对
print("关键字实参")
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')


# 编写函数时， 可给每个形参指定默认值
# 使用默认值时， 在形参列表中必须先列出没有默认值的形参， 再列出有默认值的实参。 这让Python依然能够正确地解读位置实参。
def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet(pet_name='willie')
