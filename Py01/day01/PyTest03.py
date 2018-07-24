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
