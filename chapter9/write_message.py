# 写入文件
file_name = 'programming.txt'
# 默认不传'w'是指只打开文件'r'
# 读取模式（'r'）、写入模式('w'）、附加模式（'a'）或让你能够读取和写入文件的模式（'r+'）
with open(file_name, 'w') as file_object:
    # 写单行
    file_object.write("I like Python.")
    # 在写一行-- 发现挤在一起了
    file_object.write("I like Kotlin.\n")
    # 加换行符即可
    file_object.write("I like Julia.\n")

# 额外添加信息到文本末尾
with open(file_name, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
