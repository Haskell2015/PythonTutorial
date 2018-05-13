num = 0
while num <= 5:
    print(num)
    num += 1
# 让用户决定什么时候结束程序的运行
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
