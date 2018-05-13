# input当做字符串来处理

message = input("Tell me something , I will repeat it to U \n")
print(message)

name = input("Please input your name:\n")
print("Hello " + name + " !")

# 编写清晰的程序--必要的换行处理
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name + "!")

# int来处理字符串当做数值

age = input("How old are U ?")
# 这里是字符串
print(age)
# print(age > 10)
# 这才是数字
print(int(age))

height = input("How tall are you, in inches? ")
height = int(height)
if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
