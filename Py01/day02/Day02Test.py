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
str2 = "I am a student. I am 15 years old."
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
# split,startswith,endswith
print(str2.split(" "))
print(str2.startswith("I"))
print(str2.endswith("old"))
# lower,upper
print(str2.lower())
print(str2.upper())
# center(Int),ljust(Int),rjust(Int) 在某个宽度居中，靠左，靠右
print(str2.center(50))
print(str2.ljust(50))
print(str2.rjust(50))
# strip,lstrip,rstrip 去掉两侧，左侧，右侧的空格
str3 = "     hello world      "
print(str3.strip())
print(str3.lstrip())
print(str3.rstrip())
# partition,rpartition 以传入的内容分三段
print(str2.partition("am"))
print(str2.rpartition("am"))

# isslpha,isdigit，isalnum 是字母，是数字,既有数字又有字母
# num = input("请输入一个字符：")
# if num.isalpha():
#     print("输入的是字母")
# elif num.isdigit():
#     print("输入的是数字")
# elif num.isalnum():
#     print("输入的既有数字又有字母")

# a.join(b), 以a为分割，连接b
a = " "
b = ["hello","world","hello"]
print(a.join(b))
# 如果有空格和换行符同时存在，又需要切割，可直接用split()，它会对空白字符进行切割
# 这个有些版本可以实现，有些不能
str4 = "sad hfk lsd/thg ksl /t fhl gks /t hfd/tkgh lsk /tfghlksgl"
print(str4.split())