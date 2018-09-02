'''
请用for循环迭代数列 1-100 并打印出7的倍数。
'''
for i in range(1, 101):
    if i % 7 == 0:
        print(i)

'''
zip()函数可以把两个 list 变成一个 list：
>>> zip([10, 20, 30], ['A', 'B', 'C'])
[(10, 'A'), (20, 'B'), (30, 'C')]
在迭代 ['Adam', 'Lisa', 'Bart', 'Paul'] 时，如果我们想打印出名次 - 名字（名次从1开始)，请考虑如何在迭代中打印出来。
提示：考虑使用zip()函数和range()函数
'''
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in zip(range(1, len(L) + 1), L):
    print(index, '-', name)

'''
给定一个dict：
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
请计算所有同学的平均分。
'''
d = {'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74}
sum = 0.0
for score in d.values():
    sum += score
print(sum / len(d))

'''
请根据dict：
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
打印出 name : score，最后再打印出平均分 average : score。
'''
d = {'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74}

sum = 0.0
for k, v in d.items():
    sum = sum + v
    print(k, ':', v)
print('average', ':', sum / len(d))
