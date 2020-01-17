# ----------1 Python Number 类型转换
# int(x [,base ])         将x转换为一个整数
# long(x [,base ])        将x转换为一个长整数
# float(x )               将x转换到一个浮点数
# complex(real [,imag ])  创建一个复数
# str(x )                 将对象 x 转换为字符串
# repr(x )                将对象 x 转换为表达式字符串
# eval(str )              用来计算在字符串中的有效Python表达式,并返回一个对象
# tuple(s )               将序列 s 转换为一个元组
# list(s )                将序列 s 转换为一个列表
# chr(x )                 将一个整数转换为一个字符
# unichr(x )              将一个整数转换为Unicode字符
# ord(x )                 将一个字符转换为它的整数值
# hex(x )                 将一个整数转换为一个十六进制字符串
# oct(x )                 将一个整数转换为一个八进制字符串

#---------2 Python math 模块、cmath 模块
# Python 中数学运算常用的函数基本都在 math 模块、cmath 模块中。
#
# Python math 模块提供了许多对浮点数的数学运算函数。
#
# Python cmath 模块包含了一些用于复数运算的函数。
#
# cmath 模块的函数跟 math 模块函数基本一致，区别是 cmath 模块运算的是复数，math 模块运算的是数学运算。
#
# 要使用 math 或 cmath 函数必须先导入：import math
# 查看 math 查看包中的内容:
import math
print(dir(math))
print(math.sin(1))

#--------3 Python数学函数
print(abs(-10))
print(math.ceil(4.1))
print(math.floor(4.9))
print(max(80,100,1000))
#round 函数python2与python3不同，python3不是四舍五入
print(round(100.000056, 3))
print(round(80.23456, 2))
print(round(2.355, 2))

# Python随机数函数
# 随机数可以用于数学，游戏，安全等领域中，还经常被嵌入到算法中，用以提高算法效率，并提高程序的安全性。
import random
print(random.choice(range(10)))
# start -- 指定范围内的开始值，包含在范围内。
# stop -- 指定范围内的结束值，不包含在范围内。
# step -- 指定递增基数。
print(random.randrange(100,1000,2))
print(random.random())

list = [20, 16, 10, 5]
random.shuffle(list)
print("随机排序列表 : ",  list)     #shuffle() 方法将序列的所有元素随机排序。


#--------4  Python三角函数
#跳过

# Python数学常量
# pi
# e