
import pandas as pd
import numpy as np
df = pd.DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'], 'key2': ['one', 'two', 'one', 'two', 'one'], 'data1': np.random.randn(5), 'data2': np.random.randn(5)})
# print(df)
#
# grouped = df['data1'].groupby(df['key1'])
# print(grouped.mean())
#
# means = df['data1'].groupby([df['key2'], df['key1']]).mean()
# print(means)
# print(means.unstack())
#
# states = np.array(['Ohio', 'California', 'California', 'Ohio', 'Ohio'])
# years = np.array([2005, 2005, 2006, 2005, 2006])
# means = df['data1'].groupby([states, years]).mean()
# print(means.unstack())
# print(df.groupby('key1').mean())
# print(df.groupby(['key1', 'key2']).size().unstack())
# for name, group in df.groupby('key1'):
#     print(name)
#     print(group)

# for (k1, k2), group in df.groupby(['key1', 'key2']):
#     print(k1, k2)
#     print(group)
pieces = dict(list(df.groupby('key1')))
for keys, values in pieces.items():
    print(keys)
    print(values)
