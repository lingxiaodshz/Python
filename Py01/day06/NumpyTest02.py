import numpy as np

array = np.array([[[1,2,3],
                  [2,5,8]]],dtype=int)

#基本属性
print(array.ndim)#维数
print(array.shape)#行列
print(array.size)#元素个数

#创建矩阵
zeroArray = np.zeros((3,4))#生成3行4列的零矩阵
print(zeroArray)
oneArray = np.ones((3,4))#生成3行4列的单位矩阵
print(oneArray)
emptyArray = np.empty((2,3))#每个元素几乎为零
print(emptyArray)
rangeArray = np.arange(12).reshape((3,4))#按顺序取0-12，并reshape为3行4列的矩阵
print(rangeArray)
rangeArray2 = np.arange(14,2,-1).reshape((6,2))
print(rangeArray2)
