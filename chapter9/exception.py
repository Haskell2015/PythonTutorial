# 异常处理

try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# 依赖于try 代码块成功执行的代码都应放到else代码块中
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        pass
        print("You can't divide by 0!")
    else:
        print(answer)
