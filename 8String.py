# Python 字符串
var1 = 'Hello World!'
var2 = "Python Runoob"

print("var1[0]: ", var1[0])
print("var2[1:5]: ", var2[1:5])

#--------2 Python 字符串连接
var1 = 'Hello World!'

print("输出 :- ", var1[:6] + 'Runoob!')

#--------3 Python 转义字符
# 在需要在字符中使用特殊字符时，python 用反斜杠 \ 转义字符。
# \(在行尾时)	续行符
# \\	反斜杠符号
# \'	单引号
# \"	双引号
# \a	响铃
# \b	退格(Backspace)
# \e	转义
# \000	空
# \n	换行
# \v	纵向制表符
# \t	横向制表符
# \r	回车
# \f	换页
#其他查阅：https://www.runoob.com/python/python-strings.html


#--------4 Python字符串运算符
a = "Hello"
b = "Python"

print("a + b 输出结果：", a + b)

print("a * 2 输出结果：", a * 2)

print("a[1] 输出结果：", a[1])

print("a[1:4] 输出结果：", a[1:4])

if ("H" in a):
    print("H 在变量 a 中")

else:
    print("H 不在变量 a 中")


if ("M" not in a):
    print("M 不在变量 a 中")
else:
    print("M 在变量 a 中")

print(r'\n')
print(R'\n')


#--------5 Python 字符串格式化
print("My name is %s and weight is %d kg!" % ('Zara', 21) )
# python 字符串格式化符号:
# % c:格式化字符及其ASCII码
# % s:格式化字符串
# % d:格式化整数
# % u:格式化无符号整型
# % o:格式化无符号八进制数
# % x:格式化无符号十六进制数
# % X:格式化无符号十六进制数（大写）
# % f:格式化浮点数字，可指定小数点后的精度
# % e:用科学计数法格式化浮点数
# % E:作用同 %e，用科学计数法格式化浮点数
# %g:%f和%e的简写
# %G:%F 和 %E 的简写
# %p:用十六进制数格式化变量的地址

#--------5 Python format 格式化函数(支持python2.6以上)
print("{} {}".format("hello", "world"))   # 不设置指定位置，按默认顺序)
print("{0} {1}".format("hello", "world"))   # 设置指定位置
print("{1} {0} {1}".format("hello", "world"))  # 设置指定位置
print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))
# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))
# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的

# 也可以向 str.format() 传入对象：
class AssignValue(object):
    def __init__(self, value):
        self.value = value
my_value = AssignValue(6)
print('value 为: {0.value}'.format(my_value))  # "0" 是可选的
# 数字格式化：	格式具体看：https://www.runoob.com/python/att-string-format.html
print("{:.2f}".format(3.1415926));