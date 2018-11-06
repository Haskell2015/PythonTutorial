# 读文件
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    # print(contents)
    # print(contents.rstrip())
    
    # 分行打印--这里可以看到空行
    # for line in file_object:
    #     print(line)
    # 去空行
    # print(line.rstrip())
    
    # 一次读出所有行
    # lines = file_object.readlines()
    # for line in lines:
    #     print(line.rstrip())

# 其他位置
with open('../pi.txt') as file_obj:
    contents2 = file_obj.read()
    print(">>>" + contents2)
    # 去除开头和结尾的空格
    print('>>>' + contents2.strip())
    
    print('1415' in contents2)
