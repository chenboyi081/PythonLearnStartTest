# pyhon列表：https://www.runoob.com/python/python-lists.html

# 1.0 访问列表中的值
list1 = ['Google', 'Runoob', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7];

print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])
# 2.0 更新列表
list = ['Google', 'Runoob', 1997, 2000]

print("第三个元素为 : ", list[2])
list[2] = 2001
print("更新后的第三个元素为 : ", list[2])
# 3.0 删除列表元素
list = ['Google', 'Runoob', 1997, 2000]

print("原始列表 : ", list)
del list[2]
print("删除第三个元素 : ", list)
# 4.0 *Python列表脚本操作符
print(len([1, 2, 3]))
print([1, 2, 3] + [4, 5, 6])
print(['Hi!'] * 4)
3 in [1, 2, 3]
for x in [1, 2, 3]: print(x, end=" ")
# 5.0 Python列表截取
L=['Google', 'Runoob', 'Taobao']
L[2]
L[-2]
L[1:]
squares = [1, 4, 9, 16, 25]
squares += [36, 49, 64, 81, 100]
#5.1 嵌套列表
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[0][1])
# 6.0 Python列表函数&方法
# 查看链接
