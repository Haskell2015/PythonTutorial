# 从一个模块导入一个类,多个类
from chapter8.Car import Car, ElectricCar
# 导入整个模块
# import chapter8.Car
# 从一个模块导入所有类
# from chapter8.Car import *
from chapter8.Dog import Dog

my_dog = Dog("haha", 6)
print("My dog's name is " + my_dog.name.title() + '.')
print("My dog's age is " + str(my_dog.age) + '.')

my_dog.roll_over()
my_dog.sit()

my_car = Car('audi', 'a4', 2016)
print(my_car.get_descriptive_name())
my_car.read_odometer()
# 直接修改属性值
my_car.odometer_reading = 100
my_car.read_odometer()
# 通过函数进行修改属性会
my_car.update_odometer(200)
my_car.read_odometer()

my_elecar = ElectricCar('tesla', 'a9', 2018)
print(my_elecar.get_descriptive_name())
