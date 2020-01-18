# Python 字典(Dictionary)：https://www.runoob.com/python3/python3-dictionary.html
# 字典是另一种可变容器模型，且可存储任意类型对象。
#
# 字典的每个键值 key=>value 对用冒号 : 分割，每个键值对之间用逗号 , 分割，整个字典包括在花括号 {} 中 ,格式如下所示

dict1 = { 'abc': 456 }
dict2 = { 'abc': 123, 98.6: 37 }

# 1.0 访问字典里的值
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])

# 2.0 修改字典
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

dict['Age'] = 8  # 更新 Age
dict['School'] = "菜鸟教程"  # 添加信息

print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])

# 3.0 删除字典元素
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

del dict['Name']  # 删除键 'Name'
dict.clear()  # 清空字典
del dict  # 删除字典

# 3.1 字典键的特性
# 不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
dict = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}

print("dict['Name']: ", dict['Name'])
# 键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行
dict = {['Name']: 'Runoob', 'Age': 7}

#print("dict['Name']: ", dict['Name'])   #报错

# 4.0 字典内置函数&方法
#查看链接

