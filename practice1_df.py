import pandas as pd
import numpy as np

#数値で構成されているSeriesを作成
s = pd.Series([1,3,5,np.nan,6,8])
print(s)


#日付のSeriesを作成
#2019/01/01から6日間
dates1 = pd.date_range('20190101', periods=6)
print(dates1)


#A:数値、B:日付、C:1、D:3、E:test,train、F:fooのデータフレーム
df = pd.DataFrame({'A':1.,
                    'B':pd.Timestamp('20130102'),
                    'C':pd.Series(1,index=list(range(4)), dtype='float32'),
                    'D':np.array([3]*4, dtype='int32'),
                    'E':pd.Categorical(["test", "train", "test", "train"]),
                    'F':'foo'})
print(df)

#各列の型の確認
print("type of df:")
print(df.dtypes)


#行列をデータフレームに変換
matrix = np.random.randn(6,4) #6行4列
df2 = pd.DataFrame(matrix, columns=list('ABCD')) #内容:matrix、列名：columns
print(df2)

#先頭の抽出
#先頭3行
print(df2.head(3))
#行数を省略すると先頭5行の抽出
print(df2.head())

#末尾の抽出
#末尾2行を抽出
print(df2.tail(2))
#行数を省略すると末尾5行の抽出
print(df2.tail())

#基本統計量を算出
#count:件数、mean:平均値、std:標準偏差
print(df2.describe())


#ディクショナリからデータフレーム作成
a_values = [1,2,3,4,5]
b_values = np.random.rand(5)
c_values = ["apple", "banana", "strawberry", "peach", "orange"]
my_dict = {"A":a_values, "B":b_values,"C":c_values}
my_df = pd.DataFrame.from_dict(my_dict)
print(my_df)

#列名columnと行列indexと値valueのみを表示
dates2 = pd.date_range('20190101', periods=6)
df3 = pd.DataFrame(np.random.randn(6,4), index=dates2, columns=list('ABCD'))
print(df3)
print("columns of df3:")
print(df3.columns)
print("index of df3:")
print(df3.index)
print("values of df3:")
print(df3.values)
