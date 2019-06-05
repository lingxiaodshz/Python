import pandas as pd
import numpy as np

"""
---------------------------------------------------------
pandas基本介绍
---------------------------------------------------------
"""
# 可以显示索引的列表
s = pd.Series([1, 2, 6, np.nan, 55, 1])
print(s)
print("---------------------------------------")

# 从20190605开始的6天时间数据
dates = pd.date_range('20190605', periods=6)
print(pd.Series(dates))
print("---------------------------------------")

# dataframe相当于一个matrix矩阵，也就是numpy里面的二维矩阵。
# 行索引为dates，列索引为中括号内所述内
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=["a", "b", 'c', 'd'])
print(df)
df1 = pd.DataFrame(np.arange(12).reshape((3, 4)))
print(df1)
df2 = pd.DataFrame({'A': 1,
                    'B': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'C': pd.Timestamp('20180102'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(['test', 'train', 'test', 'train']),
                    'F': 'foo'})
print(df2)
print(df2.dtypes)  # 输出类型
print(df2.index)  # 索引
print(df2.columns)  # 列名
print(df2.values)  # df2内的所有元素，按二维矩阵展示
print(df2.describe())  # 描述
print(df2.T)  # 矩阵转置
print(df2.sort_index(axis=1, ascending=False))  # 按列排序，降序
print(df2.sort_values(by="E"))  # 按E列中的值排序
