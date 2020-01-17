# Python 循环语句

# Python 提供了 for 循环和 while 循环（在 Python 中没有 do..while 循环）
# ---------1 while示例
count = 0
while (count < 9):
    print('The count is:', count)
    count = count + 1

print("Good bye!")

# while 语句时还有另外两个重要的命令 continue，break 来跳过循环，
# continue 用于跳过该次循环，break 则是用于退出循环，此外"判断条件"还可以是个常值，表示循环必定成立
i = 1
while i < 10:
    i += 1
    if i % 2 > 0:  # 非双数时跳过输出
        continue
    print(i)    # 输出双数2、4、6、8、10


i = 1
while 1:  # 循环条件为1必定成立
    print(i)    # 输出1~10
    i += 1
    if i > 10:  # 当i大于10时跳出循环
        break

# 在 python 中，while … else 在循环条件为 false 时执行 else 语句块：
count = 0
while count < 5:
   print(count," is  less than 5")
   count = count + 1
else:
   print(count, " is not less than 5")

   # 简单语句组
   # while (flag): print( 'Given flag is really true!')

