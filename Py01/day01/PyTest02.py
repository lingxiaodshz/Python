# 条件判断和循环

score = 75
if score >= 60:
    print('passed')

score = 55
if score >= 60:
    print('passed')
else:
    print('failed')

score = 85
if score >= 90:
    print('excellent')
elif score >= 80:
    print('good')
elif score >= 60:
    print('passed')
else:
    print('failed')

L = [75, 92, 59, 68]
sum = 0.0
for score in L:
    sum += score
print(sum / 4)

# 利用while循环计算100以内奇数的和。
sum = 0
x = 1
while x < 100:
    sum += x
    x += 2
print(sum)

# 利用 while True 无限循环配合 break 语句，计算 1 + 2 + 4 + 8 + 16 + ... 的前20项的和。
sum = 0
x = 1
n = 1
while True:
    sum += x
    x *= 2
    n += 1
    if n > 20:
        break
print(sum)

# 对已有的计算 0 - 100 的while循环进行改造，通过增加 continue 语句，使得只计算奇数的和：
sum = 0
x = 0
while True:
    x = x + 1
    if x > 100:
        break
    if x % 2 == 0:
        continue
    sum += x
print(sum)

# 对100以内的两位数，请使用一个两重循环打印出所有十位数数字比个位数数字小的数，例如，23（2 < 3）。
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    for y in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        if x < y:
            print(x * 10 + y, end=' ')
