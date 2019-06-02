import numpy as np

array = np.array([[[1, 2, 3],
                   [2, 5, 8]]], dtype=int)

# 基本属性
print("======================================")
print(array.ndim)  # 维数
print(array.shape)  # 行列
print(array.size)  # 元素个数

# 创建矩阵
print("======================================")
zeroArray = np.zeros((3, 4))  # 生成3行4列的零矩阵
print(zeroArray)
oneArray = np.ones((3, 4))  # 生成3行4列的单位矩阵
print(oneArray)
emptyArray = np.empty((2, 3))  # 每个元素几乎为零
print(emptyArray)
rangeArray = np.arange(12).reshape((3, 4))  # 按顺序取0-12，并reshape为3行4列的矩阵
print(rangeArray)
rangeArray2 = np.arange(14, 2, -1).reshape((6, 2))
print(rangeArray2)

# 基础运算
print("======================================")
a = np.array([[10, 20],
              [1, 0, ]])
b = np.arange(4).reshape((2, 2))
c = a * b  # 对应位置逐个相乘
c_dot = np.dot(a, b)  # 矩阵相乘
print(c)
print(c_dot)

a = np.random.random((2, 4))
print(a)
print(np.sum(a))
print(np.max(a, axis=1))  # 按行求最大值
print(np.min(a, axis=0))  # 按列求最小值

print("======================================")
a = np.arange(14, 2, -1).reshape((3, 4))
print(a)
print(np.clip(a, 5, 9))  # 大于9的全设为9，小于5的设为5
print(np.mean(a, axis=0))  # 对于列进行计算平均值
print(np.mean(a, axis=1))  # 对于行进行计算平均值

# numpy索引
a = np.arange(12)
print('a', a)
print(a[3])
b = a.reshape((3, 4))
print(b)
print(b[2][1])  # 第2行，第1列(索引从0开始)
print(b[:2])  # 第二列所有元素
# 注意看逗号的位置，逗号用来区分行列，冒号代表全部或者从哪个位置到哪个位置
print(b[0, :])  # 第0行，所有元素
print(b[0:2, 1])  # 第1列0-2行的元素，注意0:2不包含第2个位置
print(b[0, 1:3])
print(b[0, 1:])

# for循环
a = np.arange(3, 15).reshape(3, 4)
print(a)
print("row:")
for row in a:
    print(row)

print("column:")
for column in a.T:
    print(column)

print("flat:")
print(a.flatten())
for item in a.flat:
    print(item)

# numpy array合并
a = np.array([1, 1, 1])
b = np.array([2, 2, 2])

c = np.vstack((a, b))
d = np.hstack((a, b))
print(c.shape, d.shape)
print(c)
print(d)

print(a[np.newaxis, :])
print(a[:, np.newaxis])
d = np.concatenate((a, b, b, a), 0)
print(d)

# array分割
a = np.arange(12).reshape((3, 4))
print(a)

print(np.split(a, 2, axis=1))  # 纵向平均分割为2个array
print(np.split(a, 3, axis=0))  # 横向平均分割为3个array
print(np.array_split(a, 3, axis=1))  # 纵向不等分割3个array

# numpy copy & deep copy
a = np.arange(4)
print(a)
b = a
c = a
d = a
a[0] = 11
print(a)
# a,b,c,d相互关联
print(b is a)
d[1:3] = [22, 33]
print(c)

# 不互相关联
b = a.copy()  # deep copy
a[3] = 15
print(a is b)
