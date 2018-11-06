# 存储数据--写json

import json

numbers = [2, 3, 5, 7, 11, 13]
file_name = "number.txt"
with open(file_name, 'w') as file_object:
    json.dump(numbers, file_object)
