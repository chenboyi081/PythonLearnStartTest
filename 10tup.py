# Python 元组：https://www.runoob.com/python3/python3-tuple.html
# Python的元组与列表类似，不同之处在于元组的元素不能修改。
#
# 元组使用小括号，列表使用方括号。
#
# 元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"
print(type(tup3))
tup1 = (50)     # 不加逗号，类型为整型
type(tup1)
tup1 = (50,)    # 加上逗号，类型为元组
type(tup1)

# 1.0 访问元组
tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])

# 2.0  修改元组
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
# 以下修改元组元素操作是非法的。
# tup1[0] = 100

# 创建一个新的元组
tup3 = tup1 + tup2
print(tup3)


# 3.0  删除元组
tup = ('Google', 'Runoob', 1997, 2000)

print(tup)
del tup
print("删除后的元组 tup : ")
#print(tup)      #元组被删除后，输出变量会有异常信息

# 4.0  元组运算符
# 同list

# 5.0  元组索引，截取
# 同list

# 7.0  元组内置函数
# 看链接