people = pd.DataFrame(np.random.randn(5, 5),
                      columns=['a', 'b', 'c', 'd', 'e'],
                      index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis']
                      )
print(people)
# people.ix[2:5, ['b', 'c']] = np.nan
# print(people)
mapping = {'a': 'red', 'b': 'red', 'c': 'blue',
           'd': 'blue', 'e': 'red', 'f': 'orange'}
# print(type(mapping))
by_column = people.groupby(mapping, axis=1)
print(list(by_column))
print(by_column.sum())
