#Python 条件语句

# if 判断条件：
#     执行语句……
# else：
#     执行语句……

flag = False
name = 'luren'
if name == 'python':         # 判断变量是否为 python
    flag = True              # 条件成立时设置标志为真
    print('welcome boss')      # 并输出欢迎信息
else:
    print(name)                # 条件不成立时输出变量名称


num = 5
if num == 3:            # 判断num的值
    print('boss')
elif num == 2:
    print('user')
elif num == 1:
    print('worker')
elif num < 0:           # 值小于零时输出
    print('error')
else:
    print('roadman')      # 条件均不成立时输出

# 由于 python 并不支持 switch 语句，所以多个条件判断，只能用 elif 来实现，如果判断需要多个条件需同时判断时，
# 可以使用 or （或），表示两个条件有一个成立时判断条件成功；使用 and （与）时，表示只有两个条件同时成立的情况下，
# 判断条件才成功。

# 简单的语句组
# 你也可以在同一行的位置上使用if条件判断语句
var = 100

if (var == 100): print("变量 var 的值为100")


print("Good bye!")
