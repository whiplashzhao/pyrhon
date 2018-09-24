from pylab import *
import pandas as pd
import numpy as np
# df = pd.DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'], 'key2': ['one', 'two', 'one', 'two', 'one'], 'data1': np.random.randn(5), 'data2': np.random.randn(5)})
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
#
# for (k1, k2), group in df.groupby(['key1', 'key2']):
#     print(k1, k2)
#     print(group)
# pieces = dict(list(df.groupby('key1')))
# for keys, values in pieces.items():
#     print(keys)
#     print(values)
# print(df.dtypes)
# print(df)
# grouped = df.groupby(df.dtypes, axis=1)  # in which axis=0 along the rows (namely, index in pandas), and axis=1 along the columns
# print(list(grouped))
# print(df)
# print(list(df.groupby('key1')[['data1']]))
# print(list(df.groupby('key1')[[]]))
# print('end')
# print(list(df.groupby('key1')['data1'].mean()))
# print(df.groupby(['key1', 'key2'])[['data1']].mean())
# people = pd.DataFrame(np.random.randn(5, 5),
#                       columns=['a', 'b', 'c', 'd', 'e'],
#                       index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis']
#                       )
# print(people)
# people.ix[2:5, ['b', 'c']] = np.nan
# print(people)
# mapping = {'a': 'red', 'b': 'red', 'c': 'blue',
#            'd': 'blue', 'e': 'red', 'f': 'orange'}
# print(type(mapping))

# by_column = people.groupby(mapping, axis=1)
# print(list(by_column))
# print(by_column.sum())
# map_series = pd.Series(mapping)
# print(map_series)
# print(type(map_series))
# print('end')
# print(list(people.groupby(map_series, axis=1)))
# print(people.groupby(map_series, axis=1).count())
# print(people.count())
# print(people.groupby(len).sum())
# key_list = ['one', 'one', 'one', 'two', 'two']
# print(people.groupby([key_list, len]).min())
# columns = pd.MultiIndex.from_arrays([['US', 'US', 'US', 'JP', 'JP'],
#                                     [1, 3, 5, 1, 3]], names=['cty', 'tenor'])
# # print(columns)
# hier_df = pd.DataFrame(np.random.randn(4, 5), columns=columns)
# hier_df.ix[2:3, 2:3] = np.nan
# print(hier_df)
# print(list(hier_df.groupby(level='cty', axis=1)))
# print(hier_df.groupby(level='cty', axis=1).count())
# names1880 = pd.read_csv('names/yob1880.txt', names=['name', 'sex', 'births'])
# print(names1880)
# print(list(names1880.groupby('sex')))
# print(names1880.groupby('sex').births.sum())
years = range(1880, 2011)

pieces = []
columns = ['name', 'sex', 'births']

for year in years:
    path = 'names/yob%d.txt' % year
    frame = pd.read_csv(path, names=columns)

    frame['year'] = year
    pieces.append(frame)

# print(pieces)
names = pd.concat(pieces, ignore_index=True)
# print(names)
#
# total_births = names.pivot_table('births', index='year', columns='sex', aggfunc=sum)
# print(total_births.head())
#
# print(names.head())


def add_prop(group):
    births = group.births.astype(float)
    group['prop'] = births / births.sum()
    return group


names = names.groupby(['year', 'sex']).apply(add_prop)
# names = add_prop(names)
# print(names.births.sum())
# print(list(names.groupby(['year', 'sex'])))
# print(np.allclose(names.prop.sum(), 1))
# print(np.allclose(names.groupby(['year', 'sex']).prop.sum(), 1))
#
#
# def get_top1000(group):
#     return group.sort_index(by='births', ascending=True)[:2]
#
#
# grouped = names.groupby(['year', 'sex'])
# top1000 = grouped.apply(get_top1000)
# print(top1000)
# print(list(grouped))

# num_check = names[names.year == 1881]
# print(num_check)

pieces = []
for year, group in names.groupby(['year', 'sex']):
    pieces.append(group.sort_index(by='births', ascending=False)[:1000])
top1000 = pd.concat(pieces, ignore_index=True)
# print(top1000)


boys = top1000[top1000.sex == 'M']
girls = top1000[top1000.sex == 'F']
# y_check = top1000[top1000.year == 1999]
# print(y_check)

# total_births = top1000.pivot_table('births', index='year', columns='name', aggfunc=sum)
# print(total_births)

# subset = total_births[['John', 'Harry', 'Mary', 'Marilyn']]
# subset.plot(subplots=True, figsize=(12, 10), grid=False, title="Number of births per year")
# show()

table = top1000.pivot_table('prop', index='year', columns='sex', aggfunc=sum)
# print(table)
# table.plot(title='Sum of table1000.prop by year and sex', yticks=np.linspace(0, 1.2, 13), xticks=range(1880, 2020, 10))
# show()
# print('nearly end')
df = boys[boys.year == 2010]
# print(df)

prop_cumsum = df.sort_index(by='prop', ascending=False).prop.cumsum()
# print(prop_cumsum)
print(prop_cumsum.searchsorted(0.5)+1)
df = boys[boys.year == 1900]
in1990 = df.sort_index(by='prop', ascending=False).prop.cumsum()
print(in1990.searchsorted(0.5)+1)


def get_quantile_count(group, q=0.5):
    group = group.sort_index(by='prop', ascending=False)
    return group.prop.cumsum().searchsorted(q)[0]+1
#注意！！！这里和书本不一样，上面看到python3的searchsorted()返回的是ndarray类型
#需要先取[0]元素，才能获得想要的数据，如果不作该处理，绘图会报错


diversity = top1000.groupby(['year', 'sex']).apply(get_quantile_count)
# print(diversity)
diversity = diversity.unstack('sex')

print(diversity)
diversity.plot(title="Number of popular names in top 50%")
# diversity.plot(title="Number of popular names in top 50")
show()
