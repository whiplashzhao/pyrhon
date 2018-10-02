import pandas as pd



unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('ml-1m/users.dat', sep='::', header=None, names=unames, engine='python')

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('ml-1m/ratings.dat', sep='::', header=None, names=rnames, engine='python')

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('ml-1m/movies.dat', sep='::', header=None, names=mnames, engine='python')
'''
sep : str, default ‘,’
指定分隔符。如果不指定参数，则会尝试使用逗号分隔。分隔符长于一个字符并且不是‘\s+’,
将使用python的语法分析器。并且忽略数据中的逗号。正则表达式例子：'\r\t'

header : int or list of ints, default ‘infer’指定行数用来作为列名，数据开始行数。

names : array-like, default None
用于结果的列名列表，如果数据文件中没有列标题行，就需要执行header=None。
engine解析器引擎使用。C引擎速度更快，而python引擎目前更加完善。除去警告
'''
# print(users[:5])
# print(ratings[:5])

data = pd.merge(pd.merge(movies, ratings), users)
# print(data.loc[0])                                 # ix[0]已经deprecated弃用
# print(data[: 10])

mean_ratings = data.pivot_table('rating', index='title', columns='gender', aggfunc='mean')
# print(mean_ratings[:5])

ratings_by_title = data.groupby('title').size()
# print(ratings_by_title[:10])
# print(ratings_by_title)

active_title = ratings_by_title.index[ratings_by_title >= 250]
# print(active_title)

mean_ratings = mean_ratings.loc[active_title]
# 对F列进行降序
# top_female_rating = mean_rating.sort_values(by='F', ascending=False)
# print(top_female_rating[:10])

# mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
# sorted_by_diff = mean_ratings.sort_values(by='diff', ascending=True)
# print(sorted_by_diff[::-1][:15])

ratings_std_by_title = data.groupby('title')['rating'].std()
ratings_std_by_title = ratings_std_by_title.loc[active_title]

# print(ratings_std_by_title)
print(ratings_std_by_title.sort_values(ascending=False)[:10])
