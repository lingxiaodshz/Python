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
