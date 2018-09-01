'''
请定义一个 greet() 函数，它包含一个默认参数，
如果没有传入，打印 'Hello, world.'，如果传入，打印 'Hello, xxx.'
'''


def greet(str="world"):
    print("Hello, %s." % str)


greet()
greet("python")


# 请编写接受可变参数的 average() 函数。
def average(*args):
    if len(args) == 0:
        return 0
    sum = 0.0
    for num in args:
        sum += num
    return sum / len(args)


print(average())
print(average(1, 2))
print(average(1, 2, 2, 3, 4))

'''
range()函数可以创建一个数列：
>>> range(1, 101)
[1, 2, 3, ..., 100]
请利用切片，取出：
1. 前10个数；
2. 3的倍数；
3. 不大于50的5的倍数。
'''
L = range(1, 101)
# L[0:len(L):1] 注意：list从下标0开始，len(L)代表list长度，最后的1代表间隔，默认是1
print(L[:10])
print(L[2::3])
print(L[4:50:5])

print("----------------------------")
'''
利用倒序切片对 1 - 100 的数列取出：
* 最后10个数；
* 最后10个5的倍数。
'''
L = range(1, 101)
print(L[-10:])
print(L[-46::5])

'''
字符串有个方法 upper() 可以把字符变成大写字母：
>>> 'abc'.upper()
'ABC'
但它会把所有字母都变成大写。请设计一个函数，它接受一个字符串，
然后返回一个仅首字母变成大写的字符串。
提示：利用切片操作简化字符串操作。
'''


def firstCharUpper(s):
    return s[:1].upper() + s[1:]


print(firstCharUpper('hello'))
print(firstCharUpper('sunday'))
print(firstCharUpper('september'))
