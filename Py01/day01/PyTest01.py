# -*- coding: utf-8 -*-
# 注意 2.7版本需要在中文前面加u
str = '''静夜思

床前明月光，
疑是地上霜。
举头望明月，
低头思故乡。'''
print(str)

# Python把0、空字符串''和None看成 False，其他数值和非空字符串都看成 True
a = 'python'
print('hello,', a or 'world')
b = ''
print('hello,', b or 'world')

# 倒序
L = [95.5, 85, 59]
print(L[-1])
print(L[-2])
print(L[-3])

List = ['Adam', 'Lisa', 'Bart']
print(List)
# 插入到最后
# List.append('Paul')
# 插入到位置2，'Lisa'后面
List.insert(2, 'Paul')
print(List)
# 删除最后一位
# List.pop()
# 删除位置1
List.pop(1)
print(List)

# tuple是另一种有序的列表，中文翻译为“ 元组 ”。
# tuple 和 list 非常类似，但是，tuple一旦创建完毕，就不能修改了。
# tuple用小括号表示
t = ('Adam', 'Lisa', 'Bart')
print(t)

# ta = (1)
# print(ta)
# ()既可以表示tuple，又可以作为括号表示运算时的优先级，
# 结果 (1) 被Python解释器计算出结果 1，导致我们得到的不是tuple，而是整数 1。
# 因为用()定义单元素的tuple有歧义，所以 Python 规定，
# 单元素 tuple 要多加一个逗号“,”，这样就避免了歧义
# ta('Adam',)
ta = (1,)
print(ta)

# 注意tuple里的list是可变的
tb = ('a', 'b', ['c', 'd'])
la = tb[2]
la[0] = 'x'
print(tb)
