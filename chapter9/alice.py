# 处理FileNotFoundError 异常
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)

# 分析文本
title = "Alice in Wonderland"
print(title.split())
