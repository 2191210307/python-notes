import numpy as np
import pandas as pd

s = pd.Series([1, 3, 5, np.nan, 6, 8])
dates = pd.date_range('20130101', periods=6)
df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})
print(df2)
print(df2.dtypes)
print(df2.head())
print(df2.tail(3))
print(df2.index)
print(df2.columns)
print(df2.to_numpy())
print(df2.describe())
print(df2.T)
print(df2.sort_index(axis=1, ascending=False))
print(df2.sort_values(by='B'))
print(df2['A'])
print(df2[0:3])
#print(df2.loc[dates[0]])
print(df2.columns)
print(df2.columns)