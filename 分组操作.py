import pandas as pd
import numpy as np
years = range(1880, 2011)

pieces = []
columns = ['name', 'sex', 'births']

for year in years:
    path = 'names/yob%d.txt' % year
    frame = pd.read_csv(path, names=columns)

    frame['year'] = year
    pieces.append(frame)


names = pd.concat(pieces, ignore_index=True)


def add_prop(group):
    births = group.births.astype(float)
    group['prop'] = births / births.sum()
    return group


names = names.groupby(['year', 'sex']).apply(add_prop)



def get_top1000(group):
    return group.sort_index(by='births', ascending=True)[:2]


grouped = names.groupby(['year', 'sex'])
top1000 = grouped.apply(get_top1000)
print(top1000)
print(list(grouped))
