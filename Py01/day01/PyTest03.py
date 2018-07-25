# Dict和Set类型

# 新来的Paul同学成绩是 75 分，请编写一个dict，把Paul同学的成绩也加进去。
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59,
    'Paul': 75
}

print('Adam:', d['Adam'])
print('Lisa:', d.get('Lisa'))
print('Bart:', d['Bart'])

# dict的第一个特点是查找速度快，无论dict有10个元素还是10万个元素，查找速度都一样。
# 而list的查找速度随着元素增加而逐渐下降。
# dict的第二个特点就是存储的key-value序对是没有顺序的！这和list不一样
# dict的第三个特点是作为 key 的元素必须不可变
# Python的基本类型如字符串、整数、浮点数都是不可变的，都可以作为 key。

# 请用 for 循环遍历如下的dict，打印出 name: score 来。
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
for k in d:
    print(k, ':', d[k])

# set的内部结构和dict很像，唯一区别是不存储value，因此，判断一个元素是否在set中速度很快。
# set存储的元素和dict的key类似，必须是不变对象，因此，任何可变对象是不能放入set中的。
# set存储的元素也是没有顺序的。

months = set(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
x1 = 'Feb'
x2 = 'Sun'

if x1 in months:
    print('x1: ok')
else:
    print('x1: error')

if x2 in months:
    print('x2: ok')
else:
    print('x2: error')

# 请用 for 循环遍历如下的set，打印出 name: score 来。
s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
for x in s:
    print(x[0], ':', x[1])

# 针对下面的set，给定一个list，对list中的每一个元素，
# 如果在set中，就将其删除，如果不在set中，就添加进去。
# s = set(['Adam', 'Lisa', 'Paul'])
# L = ['Adam', 'Lisa', 'Bart', 'Paul']
s = set(['Adam', 'Lisa', 'Paul'])
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for x in L:
    l = len(s)
    s.add(x)
    if l == len(s):
        s.remove(x)
print(s)
