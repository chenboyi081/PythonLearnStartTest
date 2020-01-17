#-------1 Python算术运算符
a = 21
b = 10
c = 0

c = a + b
print("1 - c 的值为：", c)


c = a - b
print("2 - c 的值为：", c)


c = a * b
print("3 - c 的值为：", c)


c = a / b
print("4 - c 的值为：", c)


c = a % b
print("5 - c 的值为：", c)


# 修改变量 a 、b 、c
a = 2
b = 3
c = a ** b  	#幂 - 返回x的y次幂
print("6 - c 的值为：", c)


a = 9
b = 4
c = a // b      #取整除 - 返回商的整数部分（向下取整）
print("7 - c 的值为：", c)


#----------2 Python比较运算符
# 不做介绍
#python3不支持<>，只支持!=

#----------3 Python赋值运算符
# 不做介绍

#----------4 Python位运算符
# 不做介绍

#----------5 Python逻辑运算符
# and or not
# 不做介绍


#----------6 Python成员运算符
#in not in
# 不做介绍

#----------7 Python身份运算符
# 身份运算符用于比较两个对象的存储单元
# is is 是判断两个标识符是不是引用自一个对象
# is not is not 是判断两个标识符是不是引用自不同对象
# is 与 == 区别：
#
# is 用于判断两个变量引用对象是否为同一个(同一块内存空间)， == 用于判断引用变量的值是否相等。

a = 20
b = 20

if (a is b):
    print("1 - a 和 b 有相同的标识")

else:
    print("1 - a 和 b 没有相同的标识")


if (a is not b):
    print("2 - a 和 b 没有相同的标识")

else:
    print("2 - a 和 b 有相同的标识")


# 修改变量 b 的值
b = 30
if (a is b):
    print("3 - a 和 b 有相同的标识")

else:
    print("3 - a 和 b 没有相同的标识")


if (a is not b):
    print("4 - a 和 b 没有相同的标识")

else:
    print("4 - a 和 b 有相同的标识")



# ----------8 Python运算符优先级
# 不做介绍