# 字符串切片 [起始位置：终止位置；步长]
str = "abcdefABCDEF"
print(str[2:5])
# 获取正数第二个到倒数第二个，包含头不包含尾，所以是-1，-1代表倒数第一位
print(str[2:-1])
# 从第三个取到最后一位，注意此时冒号后面没有数值，也不是0
print(str[3:])
# 从第二个取到倒数第二个，隔两个取一个,注意后面的3，代表每次加的步长，默认为1
print(str[2:-1:3])
# 逆序
print(str[-1:0:-1])  # 无法取到第一位
print(str[-1::-1])  # 这样是完整的逆序

# 字符串的方法
str2 = "I am a student.I am 15 years old."
# find类似于Java中的indexOf
print(str2.find("am"))
# rfind从右往左查找
print(str2.rfind("am"))
# index和find方法类似，只是find找不到返回-1，index会抛出异常ValueError: substring not found
print(str2.find("am1"))
# print(str2.index("am1"))
# count返回次数
print(str2.count("am"))
print(str2.count("am1"))
# replace替换后原来的值不会变
print(str2.replace("am", "is"))
print(str2)
