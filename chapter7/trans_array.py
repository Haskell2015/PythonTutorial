# 传递列表

def greet_users(names):
    for name in names:
        print('Hello,' + name)


users = ['Lily', 'Tom', 'Jerry']
greet_users(users)

# 在函数中修改列表
old_data = ["a", 'b', 'c']
new_data = []


def change(values):
    while values:
        new_data.append(values.pop())


change(old_data)

print(new_data)
print(old_data)

# 有时需要禁止函数修改列表--永久性的
old = ['1', '2', '3']
new = []


def stay_same(nums):
    while nums:
        new.append(nums.pop())


stay_same(old[:])

print(new)
print(old)
